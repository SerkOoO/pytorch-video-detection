import cv2
import torch
import torchvision.transforms as transforms
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import torchvision.models as models
import torch.nn as nn
from pathlib import Path

async def predict_video(video_path:str) -> str:

    model = models.resnet18(pretrained=True)
    num_classes = 11
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    model_path = Path(__file__).parent.parent / "model" / "resnet_cpu.pth"
    state_dict = torch.load(model_path)
    model.load_state_dict(state_dict)
    model.eval()


    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    #video_path = Path(__file__).parent.parent / "test-video" / "v_shooting_02_01.mpg"
    cap = cv2.VideoCapture(video_path)

    if torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")
    model.to(device)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_index = 0

    model.eval()

    plt.ion() 
    fig, ax = plt.subplots()

    predict = None

    with torch.no_grad():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Prédire 1 frame par seconde
            if frame_index % int(fps) == 0:
                img_input = transform(frame).unsqueeze(0).to(device)
                output = model(img_input)
                _, predicted = torch.max(output, 1)
                class_names = ['basketball', 'biking', 'diving', 'golf_swing','horse_riding','soccer_juggling','swing','tennis_swing','trampoline_jumping','volleyball_spiking','walking'] 
                predicted_label = class_names[predicted.item()]
                predict = predicted_label


                # Convertir BGR → RGB pour affichage matplotlib
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                ax.clear()
                ax.imshow(frame_rgb)
                ax.set_title(f"Prédiction : {predicted_label}")
                ax.axis('off')
                plt.pause(0.1)  # temps d'affichage entre chaque frame

            frame_index += 1

    cap.release()
    plt.ioff()
    plt.show()
    return predict


'use client';

import React, { useState } from 'react';
import styles from './page.module.css';

export default function Home() {
  const [video, setVideo] = useState(null);
  const [prediction, setPrediction] = useState(null);


  const handleUpload = async () => {
    if (!video) return;

    const formData = new FormData();
    formData.append("file", video);

    try {
      const res = await fetch("http://localhost:8000/upload-video/", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        throw new Error("HTTP error: " + res.status);
      }

      const json = await res.json();
      alert("Upload réussi : " + json);
    } catch (err) {
      console.error("Erreur upload :", err);
    }

    const predict = await fetch("http://localhost:8000/send-data", {
      method: "POST",
    });

    const predictionResponse = await predict.json();
    setPrediction(predictionResponse.response);
    alert("Prédiction  : " + predictionResponse.response);


  };

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <input type="file" accept="video/*" onChange={e => setVideo(e.target.files?.[0] || null)} />
        <button onClick={handleUpload}>Envoyer</button>
        {prediction && <div>Prédiction : {prediction}</div>}

      </main>
    </div>
  );
}


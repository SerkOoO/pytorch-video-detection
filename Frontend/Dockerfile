FROM node:23.11.0 AS builder

WORKDIR /app

# Installer les dépendances
COPY package*.json ./
RUN npm install

# Copier le code source
COPY . .

# Build Next.js (production)
RUN npm run build

# ---
# Étape de production
FROM node:23.11.0

WORKDIR /app

# Copier seulement ce qui est nécessaire
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules

# Tu peux aussi copier le reste du code source si `pages/` ou `app/` est nécessaire pour `next start`
COPY --from=builder /app ./

EXPOSE 3000

CMD ["npm", "start"]

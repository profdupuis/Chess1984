FROM python:3.11-slim

# Mise à jour et installation des dépendances nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    cmake \
    make \
    g++ \
 && rm -rf /var/lib/apt/lists/*

# Cloner et compiler Stockfish
RUN git clone https://github.com/official-stockfish/Stockfish.git /stockfish
WORKDIR /stockfish/src
RUN make build ARCH=x86-64

# Revenir au dossier principal
WORKDIR /app

# Copier les fichiers de l'app Flask
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Rendre Stockfish exécutable visible dans l'app
ENV STOCKFISH_EXEC=/stockfish/src/stockfish

# Commande de démarrage
CMD ["gunicorn", "app:app"]

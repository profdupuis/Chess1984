# Utiliser une image Python de base
FROM python:3.11-slim

# Installer curl pour récupérer Stockfish
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean

# Créer un dossier pour l'app
WORKDIR /app

# Copier les fichiers
COPY . /app

# Télécharger Stockfish (AVX2)
RUN mkdir -p stockfish && \
    curl -L -o stockfish/stockfish https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish-ubuntu-x86-64-avx2 && \
    chmod +x stockfish/stockfish

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Rendre exécutable gunicorn
RUN pip install gunicorn

# Lancer l'app Flask avec gunicorn
CMD ["gunicorn", "app:app"]
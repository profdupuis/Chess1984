#!/bin/bash

# Télécharger Stockfish Linux compatible Render (x86-64-modern)
mkdir -p stockfish
curl -L -o stockfish/stockfish https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish-linux-x86-64-modern
chmod +x stockfish/stockfish

# Lancer l'app Flask
gunicorn app:app

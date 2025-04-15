#!/bin/bash

# Télécharger Stockfish statique compatible Render
mkdir -p stockfish
curl -L -o stockfish/stockfish https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish-ubuntu-x86-64
chmod +x stockfish/stockfish

# Lancer l'app Flask
gunicorn app:app

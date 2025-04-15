#!/bin/bash

# Télécharger Stockfish (AVX2 version Linux)
mkdir -p stockfish
curl -L -o stockfish/stockfish https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish-ubuntu-x86-64-avx2
chmod +x stockfish/stockfish

# Lancer l'app Flask
gunicorn app:app
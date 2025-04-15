#!/bin/bash

# Installer stockfish depuis les dépôts
apt-get update && apt-get install -y stockfish

# Lancer l'app Flask
gunicorn app:app

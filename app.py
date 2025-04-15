from flask import Flask, render_template, request
from stockfish import Stockfish
import os

app = Flask(__name__)

# Chemin vers le binaire Stockfish, défini dans le Dockerfile via ENV
stockfish_path = os.getenv("STOCKFISH_EXEC", "stockfish")
stockfish = Stockfish(path=stockfish_path)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    move = request.form["move"]
    if move in stockfish.get_legal_moves():
        stockfish.make_moves_from_current_position([move])
        response = f"IA joue : {stockfish.get_best_move()}"
    else:
        response = "Coup invalide."
    return render_template("index.html", response=response)

# 🚀 Lancement de l'app Flask (Render détecte ce port automatiquement)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

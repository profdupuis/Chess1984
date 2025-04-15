import os
from flask import Flask, render_template, request, jsonify
from stockfish import Stockfish
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

stockfish = Stockfish(path="stockfish/stockfish.exe")
stockfish.set_skill_level(10)

history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    user_move = data.get("move", "").strip()

    legal_moves = [m['Move'] for m in stockfish.get_top_moves(30)]
    if user_move not in legal_moves:
        history.append(f"> {user_move}")
        history.append("HUMAN: INVALID MOVE")
        return jsonify({"history": history[-20:]})

    stockfish.make_moves_from_current_position([user_move])
    history.append(f"> {user_move}")
    history.append(f"HUMAN: {user_move}")
    comment_human = get_comment(stockfish.get_fen_position(), user_move, "humain")
    history.append(f"COACH: {comment_human}")

    engine_move = stockfish.get_best_move()
    stockfish.make_moves_from_current_position([engine_move])
    history.append(f"COMPUTER: {engine_move}")
    comment_cpu = get_comment(stockfish.get_fen_position(), engine_move, "ordinateur")
    history.append(f"COACH: {comment_cpu}")

    return jsonify({"history": history[-20:]})

def get_comment(fen, move, source):
    if source == "ordinateur":
        prompt = f"Stockfish a joue {move} dans la position suivante : {fen}. Commente ce coup et conseille un coup pour le joueur humain."
    else:
        prompt = f"Le joueur a joue {move} dans la position suivante : {fen}. Commente ce coup avec franchise et stratégie."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Tu es un coach d'échecs honnête et stratégique."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=80
        )
        return response.choices[0].message.content.strip()
    except:
        return "(commentaire non disponible)"

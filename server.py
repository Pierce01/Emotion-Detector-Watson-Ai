"""This module runs a Flask server that uses the emotion_detector function."""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(
    __name__,
    static_url_path="/static",
    static_folder="static",
    template_folder="templates",
)

@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Detect the emotions in the provided text."""
    text_to_analyze = request.args.get("textToAnalyze")
    emotion = emotion_detector(text_to_analyze)
    if emotion["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return jsonify(emotion)

if __name__ == "__main__":
    app.run(debug=True)

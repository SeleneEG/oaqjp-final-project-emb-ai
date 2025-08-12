"""Flask app for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__, template_folder="templates", static_folder="static")


def format_score(value):
    """Format number to 8 decimals."""
    return f"{value:.8f}"


@app.route("/", methods=["GET"])
def home():
    """Render index page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Process text and return formatted result."""
    text = (request.args.get("textToAnalyze") or "").strip()
    result = emotion_detector(text)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        "For the given statement, the system response is "
        f"'anger': {format_score(result['anger'])}, "
        f"'disgust': {format_score(result['disgust'])}, "
        f"'fear': {format_score(result['fear'])}, "
        f"'joy': {format_score(result['joy'])}, "
        f"and 'sadness': {format_score(result['sadness'])}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

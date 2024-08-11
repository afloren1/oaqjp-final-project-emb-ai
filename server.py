"""
This module sets up a Flask web application to detect emotions.
It handles the routes to analyze the emotions in a given text and render the index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detection():
    """Analyzes the emotions from the provided text and returns the dominant emotion. """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection(text_to_analyze)
    emotions_only = {k: v for k, v in response.items() if k != 'dominant_emotion' and v is not None}
    if not emotions_only:
        return "Invalid text! Please try again!"
    dominant_emotion = max(emotions_only, key=emotions_only.get)
    emotions_str = ', '.join(f"'{k}': {v}" for k, v in emotions_only.items())
    return (
        f"For the given statement, the system response is {emotions_str}." 
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detection") 

@app.route("/emotionDetector")
def sent_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection(text_to_analyze)
    emotions_only = {k: v for k, v in response.items() if k != 'dominant_emotion' and v is not None}
    if not emotions_only: 
       return "Invalid text! Please try again!" 
    else:        
       dominant_emotion = max(emotions_only, key=emotions_only.get)
       emotions_str = ', '.join(f"'{k}': {v}" for k, v in emotions_only.items())
       return "For the given statement, the system response is {}. The dominant emotion is <b>{}</b>".format(
    emotions_str, dominant_emotion
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
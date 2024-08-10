from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detection
app = Flask("Emotion Detection") 

@app.route("/emotionDetector") 

def sent_detection(): 
   # Retrieve the text to analyze from the request arguments 
   text_to_analyze = request.args.get('textToAnalyze')  
   response = emotion_detection(text_to_analyze)
   emotion_data = response['emotionPredictions'][0]['emotion']
   anger_score = emotion_data['anger']
   disgust_score = emotion_data['disgust']
   fear_score = emotion_data['fear']
   joy_score = emotion_data['joy']
   sadness_score = emotion_data['sadness']
   dominant_emotion = max(emotion_data, key=emotion_data.get)
   formatted_response = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        } 
   return "For the given statement, the system response is{}. The dominant emotion is {}".format(formatted_response, dominant_emotion) 

@app.route("/") 
def render_index_page():
   return render_template('index.html')

if __name__ == "__main__": 
   app.run(host="0.0.0.0", port=5000) 
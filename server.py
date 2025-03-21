"""
Emotion Detection Analyzer Flask Application.
This application analyzes emotions in a given text using the emotion_detector module.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Analyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotion of the provided text.

    Returns:
        str: A formatted string with emotion scores and the dominant emotion.
             If the text is invalid, returns an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Analyze the emotion of the text
    response = emotion_detector(text_to_analyze)

    # Check if the response is valid
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    # Format the response
    return (
        f"For the given statement, the system response is "
        f"anger: {response['anger']}, "
        f"disgust: {response['disgust']}, "
        f"fear: {response['fear']}, "
        f"joy: {response['joy']}, "
        f"and sadness: {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index page of the Emotion Detection Analyzer.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
    
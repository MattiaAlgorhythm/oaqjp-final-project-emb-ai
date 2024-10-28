"""Server file for emotion detection web application"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Route for emotion detection. Accepts JSON input with a 'statement' key
    and returns emotion analysis or error message for invalid input.
    """
    data = request.get_json()
    statement = data.get("statement", "") if data else ""

    # Call the emotion_detector function
    result = emotion_detector(statement)

    # Check if the dominant_emotion is None, indicating an invalid or blank input
    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Format the output according to the requirements
    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"response": response_text})

@app.route("/")
def index():
    """Render the main index page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

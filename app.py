from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import re
import string
import nltk
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')  # In case Render requires it

app = Flask(__name__, static_folder="static")

# Load trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    words = nltk.word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    cleaned_text = clean_text(message)
    transformed_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(transformed_text)[0]
    result = "Spam" if prediction == 1 else "Ham"
    return jsonify({'prediction': result})

# Run the Flask app
import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render requires PORT from environment
    app.run(host="0.0.0.0", port=port, debug=False)


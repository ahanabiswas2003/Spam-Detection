# Spam Detection Project

## Project Overview
This is a Spam Detection system built using Flask and machine learning techniques. The model is trained to classify messages as spam or ham (not spam) using NLP techniques and scikit-learn. The web application is built with Flask, and the project has been deployed for free using Render.

## Features
- **Text Classification**: Detects whether a given text message is spam or ham.
- **Machine Learning Model**: Uses a trained model with scikit-learn.
- **Web Interface**: Built with Flask to allow users to input text and get predictions.
- **Deployment**: Hosted freely on Render for easy accessibility.

## Project Structure
```
Spam_Detection/
│-- .vscode/              # VS Code settings
│-- static/               # Contains CSS styles
│   ├── styles.css
│-- templates/            # Contains HTML templates
│   ├── index.html
│-- venv/                 # Virtual environment (not included in repo)
│-- .gitattributes        # Git attributes
│-- .gitignore            # Git ignore file
│-- app.py                # Main Flask application
│-- model.pkl             # Trained machine learning model
│-- README.md             # Project documentation
│-- requirements.txt      # Dependencies for the project
│-- vectorizer.pkl        # Vectorizer for text preprocessing
```

## Installation & Setup
### Prerequisites
Ensure you have Python installed (preferably Python 3.9+).

### Steps to Set Up Locally
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Spam_Detection
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open the browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## Deployment on Render
This project is deployed for free using [Render](https://render.com/). Follow these steps to deploy your own version:
1. Create an account on Render.
2. Create a new **Web Service**.
3. Connect your GitHub repository.
4. Set the build command:
   ```bash
   pip install -r requirements.txt
   ```
5. Set the start command:
   ```bash
   gunicorn app:app
   ```
6. Deploy and access the provided URL.

## Usage
- Enter a text message in the web interface.
- Click the "Predict" button.
- The system will classify the message as **Spam** or **Ham**.

## Dependencies
The required dependencies are listed in `requirements.txt`, including:
- Flask
- scikit-learn
- nltk
- numpy
- pandas
- xgboost

## Author
Developed by Ahana Biswas

---
This README provides complete details on the project, installation, and deployment. Let me know if you need modifications!


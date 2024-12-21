from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os
from utils.logger import get_logger

app = Flask(__name__)
logger = get_logger(__name__)

# Load your model (you can put this in a function to avoid loading it on each request)
model_file = 'C:/Users/kabee/OneDrive/Desktop/DS PROJ4/CineRateAI/artifacts/best_model.pkl'
model = joblib.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data
        movie_title = request.form['movie_title']
        movie_info = request.form['movie_info']
        critics_consensus = request.form['critics_consensus']
        rating = request.form['rating']
        genre = request.form['genre']
        directors = request.form['directors']
        writers = request.form['writers']
        cast = request.form['cast']
        in_theaters_date = request.form['in_theaters_date']
        on_streaming_date = request.form['on_streaming_date']
        runtime_in_minutes = request.form['runtime_in_minutes']
        studio_name = request.form['studio_name']
        tomatometer_status = request.form['tomatometer_status']
        tomatometer_rating = request.form['tomatometer_rating']
        tomatometer_count = request.form['tomatometer_count']

        # Create DataFrame from input values
        input_data = pd.DataFrame({
            'movie_title': [movie_title],
            'movie_info': [movie_info],
            'critics_consensus': [critics_consensus],
            'rating': [rating],
            'genre': [genre],
            'directors': [directors],
            'writers': [writers],
            'cast': [cast],
            'in_theaters_date': [in_theaters_date],
            'on_streaming_date': [on_streaming_date],
            'runtime_in_minutes': [runtime_in_minutes],
            'studio_name': [studio_name],
            'tomatometer_status': [tomatometer_status],
            'tomatometer_rating': [tomatometer_rating],
            'tomatometer_count': [tomatometer_count]
        })

        # Preprocess input data (similar to your prediction function)
        text_columns = ['movie_info', 'movie_title', 'cast']
        input_data = input_data.drop(columns=[col for col in text_columns if col in input_data.columns], errors='ignore')

        columns_to_encode = ['rating', 'tomatometer_status']
        for col in columns_to_encode:
            if col in input_data.columns:
                input_data = pd.get_dummies(input_data, columns=[col], drop_first=True)

        input_data = input_data.select_dtypes(include=['number'])
        if 'audience_rating' in input_data.columns:
            input_data = input_data.drop(columns=['audience_rating'])

        # Make predictions
        predictions = model.predict(input_data)
        predicted_rating = predictions[0]

        return render_template('index.html', prediction=predicted_rating)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

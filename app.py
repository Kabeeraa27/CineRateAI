from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os
from utils.logger import get_logger

app = Flask(__name__)
logger = get_logger(__name__)

# Load your model
model_file = 'C:/Users/kabee/OneDrive/Desktop/DS PROJ4/CineRateAI/artifacts/best_model.pkl'
model = joblib.load(model_file)

# Manually define the columns the model was trained with
# Ensure that the order matches the training data
model_columns = [
    'movie_title', 'movie_info', 'critics_consensus', 'rating', 'genre', 
    'directors', 'writers', 'cast', 'in_theaters_date', 'on_streaming_date', 
    'runtime_in_minutes', 'studio_name', 'tomatometer_status', 
    'tomatometer_rating', 'tomatometer_count'
]

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

        # Convert empty or non-numeric values to default values for numeric fields
        def safe_convert(value, default=0):
            try:
                return float(value) if value != '' else default
            except ValueError:
                return default

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
            'runtime_in_minutes': [safe_convert(runtime_in_minutes)],  # Convert runtime to float
            'studio_name': [studio_name],
            'tomatometer_status': [tomatometer_status],
            'tomatometer_rating': [safe_convert(tomatometer_rating)],  # Convert tomatometer rating to float
            'tomatometer_count': [safe_convert(tomatometer_count)]  # Convert tomatometer count to float
        })

        # Preprocess input data (similar to your prediction function)
        text_columns = ['movie_info', 'movie_title', 'cast']
        input_data = input_data.drop(columns=[col for col in text_columns if col in input_data.columns], errors='ignore')

        # Encode categorical columns
        columns_to_encode = ['rating', 'tomatometer_status']
        for col in columns_to_encode:
            if col in input_data.columns:
                input_data = pd.get_dummies(input_data, columns=[col], drop_first=True)

        # Ensure all model columns are in the input data
        for col in model_columns:
            if col not in input_data.columns:
                input_data[col] = 0  # Fill missing columns with default values (0)

        # Align columns to match the model columns order
        input_data = input_data[model_columns]

        # Make predictions
        predictions = model.predict(input_data)
        predicted_rating = predictions[0]

        return render_template('index.html', prediction=predicted_rating)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

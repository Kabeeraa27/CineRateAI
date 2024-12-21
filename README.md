# CineRateAI

This project aims to predict movie ratings using a RandomForestRegressor model. The project includes data preprocessing steps such as target encoding and one-hot encoding with additive smoothing on several features. The model achieves a high accuracy of **99.7%**.

## Steps to Run the Project

### 1. **Clone the Repository**

Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/movie-rating-prediction.git
cd movie-rating-prediction
```

### 2. **Set Up the Environment**

Create a Python virtual environment to manage the dependencies.

```bash
python -m venv movie-env
```

Activate the virtual environment:

- On Windows:

    ```bash
    movie-env\Scriptsctivate
    ```

- On macOS/Linux:

    ```bash
    source movie-env/bin/activate
    ```

### 3. **Install Dependencies**

Install the required dependencies using `pip`.

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include all necessary libraries like `pandas`, `scikit-learn`, `flask`, etc.

### 4. **Prepare the Dataset**

Ensure that you have the dataset (e.g., `movies.csv`) in the `data/` directory. You can modify the path or name in the script if necessary.

### 5. **Run the Application**

First, run the following command to generate the pickle files:

```bash
python main.py
```

Run the Flask application to start the web app and model prediction service.

```bash
python app.py
```

This will start a local development server at `http://127.0.0.1:5000/`.

### 6. **Access the Model Predictions**

- Open a browser and go to `http://127.0.0.1:5000/`.
- Input the relevant movie details (e.g., movie title, rating, cast, etc.).
- The model will predict the movie rating and display it on the page.

### 7. **Evaluate the Model**

To evaluate the model, use the following metrics:

- **R² Score (Coefficient of Determination)**: Measures how well the model explains the variance in the target variable.

    ```python
    from sklearn.metrics import r2_score

    y_pred = best_model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print(f'R² of the best model: {r2:.2f}')
    ```

- **Mean Absolute Error (MAE)**: Measures the average absolute difference between predicted and actual values.

    ```python
    from sklearn.metrics import mean_absolute_error

    mae = mean_absolute_error(y_test, y_pred)
    print(f'Mean Absolute Error: {mae}')
    ```

- **Mean Squared Error (MSE)**: Measures the average of the squared differences between predicted and actual values.

    ```python
    from sklearn.metrics import mean_squared_error

    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    ```

### 8. **Suppressing Warnings**

If you encounter warnings related to `joblib` or `loky` (e.g., about physical cores not being found), you can suppress them by setting the environment variable `LOKY_MAX_CPU_COUNT`.

```bash
set LOKY_MAX_CPU_COUNT=4  # Adjust based on your system
```

### 9. **Contributing**

Feel free to contribute to this project by opening issues or submitting pull requests. Make sure to follow the guidelines for adding new features or bug fixes.

### 10. **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

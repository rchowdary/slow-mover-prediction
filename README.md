# Slow Mover Prediction App

This project is a Streamlit application that predicts whether an item is a slow mover based on user inputs. It utilizes a pre-trained machine learning model to make predictions.

## Project Structure

```
slow-mover-prediction
├── src
│   ├── app.py               # Main entry point for the Streamlit application
│   ├── model_prediction.py   # Logic for loading the model and making predictions
│   └── utils
│       └── helper.py        # Utility functions for data processing
├── models
│   └── slow_mover_model.pkl  # Pre-trained model for predictions
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd slow-mover-prediction
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:

```
streamlit run src/app.py
```

This will start the Streamlit server and open the application in your default web browser.

## Usage

- Enter the required parameters in the input fields.
- Click on the "Predict" button to see the prediction results.

## License

This project is licensed under the MIT License.

## To use this:

Open a command prompt in the project directory
Run the script: setup_env.bat
Once complete, you can start the Streamlit app with:
venv\Scripts\activate
streamlit run src\app.py

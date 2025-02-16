import os
import pandas as pd
import joblib

def predict_slow_mover(item, cqyt, uom, tqty, twght, lot1, lot2, lot3):
    """Predicts if an item is a slow mover based on input features."""
    try:
        # Load model inside function to avoid import-time errors
        model_file_path = os.path.join(os.path.dirname(__file__), '../models/slow_mover_model.pkl')
        
        if not os.path.exists(model_file_path):
            print(f"Error: Model file not found at {model_file_path}")
            return None
            
        pipeline = joblib.load(model_file_path)
        
        new_data = pd.DataFrame({
            'ITEM': [item],
            'CQTY': [cqyt],
            'UOM': [uom],
            'TQTY': [tqty],
            'TWGHT': [twght],
            'LOT1': [lot1],
            'LOT2': [lot2],
            'LOT3': [lot3]
        })

        prediction = pipeline.predict(new_data)[0]
        return prediction
    except Exception as e:
        print(f"An error occurred during prediction: {e}")
        return None

# Example usage
if __name__ == "__main__":
    item_input = input("Enter item code: ")
    cqty_input = float(input("Enter CQTY: "))
    uom_input = input("Enter UOM: ")
    tqty_input = float(input("Enter TQTY: "))
    twght_input = float(input("Enter TWGHT: "))
    lot1_input = input("Enter LOT1: ")
    lot2_input = input("Enter LOT2: ")
    lot3_input = input("Enter LOT3: ")


    prediction = predict_slow_mover(item_input, cqty_input, uom_input,
                                     tqty_input, twght_input,
                                     lot1_input, lot2_input, lot3_input)

    if prediction is not None:
        if prediction == 1:
            print("The item is predicted to be a slow mover.")
        else:
            print("The item is predicted to NOT be a slow mover.")
from typing import Tuple
from sklearn.base import BaseEstimator

# Score Function
def score(text: str,
          model: BaseEstimator,
          threshold: float = 0.5) -> Tuple[bool, float]:
    '''
    Function to score a trained model on a given text

    Args:
        text (str): The text to score
        model (BaseEstimator): Trained sklearn model
        threshold (float): Decision threshold

    Returns:
        tuple[bool,float]: prediction (True/False), propensity score
    '''

    # ---------------- Input validation -------------------

    if not isinstance(text, str):
        raise ValueError("Text must be a string")

    if not isinstance(model, BaseEstimator):
        raise ValueError("Model must be an instance of sklearn BaseEstimator")

    if not (0 <= threshold <= 1):
        raise ValueError("Threshold must be between 0 and 1")

    
    # ------------- Prediction ---------------ss
    propensity = model.predict_proba([text])[0][1] # Get probability
    prediction = bool(propensity > threshold) # Applying threshold

    return prediction, float(propensity)

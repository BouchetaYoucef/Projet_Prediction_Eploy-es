import pytest
import pandas as pd
from app import load_model, return_prediction

def test_load_model():
    # Test if load_model() loads the model used in this application
    test_model = load_model()
    assert test_model != None

def test_prediction_range():
    # Test if load_model() returns the right classes (0 or 1)
    test_data = pd.DataFrame([[0,2013,2,1,28,0,0,3]], 
                               columns=['Education', 'JoiningYear', 'City',
                                        'PaymentTier', 'Age', 'Gender',
                                        'EverBenched', 'ExperienceInCurrentDomain'])
    test_model = load_model()
    test_prediction = test_model.predict(test_data)
    assert test_prediction == 0 or test_prediction == 1

def test_return_prediction():
    # Test if return_prediction() returns the right response.
    test_data = pd.DataFrame([[0,2013,2,1,28,0,0,3]], 
                               columns=['Education', 'JoiningYear', 'City',
                                        'PaymentTier', 'Age', 'Gender',
                                        'EverBenched', 'ExperienceInCurrentDomain'])
    test_model = load_model()
    test_result = return_prediction(test_data)
    assert test_result == "This employee will probably LEAVE your company" or test_result == "This employee will probably STAY in your company"
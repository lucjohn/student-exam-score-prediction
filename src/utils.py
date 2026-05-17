import os 
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj: 
            dill.dump(obj, file_obj)


    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(X_training_set, Y_Training_set, X_test_set, Y_test_set, models, params):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i] 
            para = params[list(models.keys())[i]]
            model.fit(X_training_set, Y_Training_set)

            gs = GridSearchCV(model, para, cv=3) 
            gs.fit(X_training_set, Y_Training_set)
            
            Y_training_prediction = model.predict(X_training_set)
            Y_test_prediction = model.predict(X_test_set)

            training_accuracy = r2_score(Y_Training_set, Y_training_prediction)
            test_accuracy = r2_score(Y_test_set, Y_test_prediction)
            report[list(models.keys())[i]] = {'training_accuracy': training_accuracy, 'test_accuracy': test_accuracy}
        return report
    except Exception as e:
        raise CustomException(e, sys)
    

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)

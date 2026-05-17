import os
import sys
from dataclasses import dataclass   

from catboost import CatBoostRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_array, test_array, preprocessor_path):
        try:
            logging.info("Split training and testing input data")
            X_train, y_train = train_array[:, :-1], train_array[:, -1]
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            models = {
                "random_forest": RandomForestRegressor(),
                "decision_tree": DecisionTreeRegressor(),
                "gradient_boosting": GradientBoostingRegressor(),
                "linear_regression": LinearRegression(),
                "knn": KNeighborsRegressor(),
                "catboost": CatBoostRegressor(verbose=False),
                "adaboost": AdaBoostRegressor(),
                "xgboost": XGBRegressor()
            }

            model_report = dict(evaluate_model(X_training_set = X_train, Y_Training_set = y_train, X_test_set = X_test, Y_test_set = y_test, models = models))

            print(model_report)
            best_model_name = max(model_report, key=lambda x: model_report[x]['test_accuracy'])
            best_model_score = model_report[best_model_name]['test_accuracy']

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No good model found", sys)
            
            logging.info("Best found model using training and testing data")

            save_object(self.model_trainer_config.trained_model_file_path, best_model)

            predicted=best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square

        except Exception as e:
            logging.error("Error occurred during model training: %s", str(e))
            raise CustomException(e, sys)
        

            

            

        


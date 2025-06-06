import os 
import sys

import numpy
import pandas as pd
import dill

from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
  try:
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok= True)

    with open(file_path, 'wb') as file_obj:
      dill.dump(obj, file_obj)
  except Exception as e:
    raise CustomException(e,sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for model_name, model in models.items():
            model_params = params.get(model_name, {})  # get hyperparameters
            grid = GridSearchCV(model, model_params, cv=3, scoring='r2', verbose=0, n_jobs=-1)
            grid.fit(X_train, y_train)

            best_model = grid.best_estimator_

            y_test_pred = best_model.predict(X_test)
            test_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
    
    
def load_object(file_path):
       try:
          with open(file_path, 'rb') as file_obj:
             return dill.load(file_obj)
       except Exception as e:
          raise CustomException(e,sys)
          
        
        
      

  
  

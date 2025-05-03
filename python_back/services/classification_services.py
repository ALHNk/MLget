from models import knn_model as model_knn
from models import xgboost_model as model_xgb
import pandas as pd
import os
from dataset_manage.laptops_manage import stop_words, punctuation_marks, preprocesses



def predict(query, model, dataset):
    query = preprocesses(query, stopwords=stop_words, punctuation_marks=punctuation_marks)
    if model == "knn":
        print("service: hello")        
        # query = " ".join(query)
        return model_knn.predict(query)
    elif model == "xgb":
        return model_xgb.predict(query, dataset)
    else:
        return "Model Not Found"
    
def train(model, dataset):
    try:
        base_path = os.path.dirname(__file__)
        file_path_1 = os.path.join(base_path, '..', 'dataset_manage', 'datasets', f'train_data_{dataset}.csv')
        file_path_2 = os.path.join(base_path, '..', 'dataset_manage', 'datasets', f'test_data_{dataset}.csv')
        train = pd.read_csv(file_path_1, sep = ",")
        test = pd.read_csv(file_path_2, sep = ",")
        X = train["text"]
        y = train["rating"]
        X = pd.Series(X).astype(str)
        X_test = test["text"]
        y_test = test["rating"]
        X_test = pd.Series(X_test).astype(str)
    except Exception as e:
        return f"Failed to read csv {e}" 
    if dataset == 'laptops':
        n = 600
    
    try: 
        if model == "knn":                  
            return model_knn.train(X, y)
        elif model == "xgb":
            print("xgboost training choosed")
            return model_xgb.train(X_train=X, y_train=y, X_test = X_test, y_test=y_test, n=n, dataset=dataset)
    except Exception as e:
        return str (e)       
    else:
        return "model Not Found"
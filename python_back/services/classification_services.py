from models import knn_model as model_knn
import pandas as pd
import os
from dataset_manage.laptops_manage import stop_words, punctuation_marks, preprocesses



def predict(query, model):
    if model == "knn":
        print("service: hello")
        query = preprocesses(query, stopwords=stop_words, punctuation_marks=punctuation_marks)
        # query = " ".join(query)
        return model_knn.predict(query)
    else:
        return "Model Not Found"
    
def train(model):
    if model == "knn":
        try:
            base_path = os.path.dirname(__file__)
            file_path_1 = os.path.join(base_path, '..', 'dataset_manage', 'datasets', 'train_data_laptops.csv')
            # file_path_2 = os.path.join(base_path, '..', 'dataset_manage', 'datasets', 'test_data_laptops.csv')
            train = pd.read_csv(file_path_1, sep = ",")
            # test = pd.read_csv(file_path_2, sep = ",")
            X = train["text"]
            y = train["rating"]
            X = pd.Series(X).astype(str)
            # X_test = test["text"]
            # y_test = test["rating"]
            # X_test = pd.Series(X_test).astype(str)
            return model_knn.train(X, y)
        except Exception as e:
            return "Failed to read csv"        
    else:
        return "model Not Found"
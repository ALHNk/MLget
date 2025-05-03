from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import accuracy_score
import joblib as jl
import os
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import LabelEncoder


base_path = os.path.dirname(__file__)

def predict(input, dataset):
    try:
        file_path = os.path.join(base_path, 'training_fits', f'xgb_{dataset}.pkl')
        print(file_path)
        model = jl.load(file_path)
        y = model.predict([" ".join(input)])
        return str(y)
    except Exception as e:
        return str(e)

def train(X_train, y_train, n, X_test, y_test, dataset):
    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(y_train)  
    y_test_encoded = label_encoder.fit_transform(y_test)  

    try:
        if n < 1000:
            classifier = XGBClassifier(n_estimators = 30,
                                       max_depth = 3,
                                       learning_rate = 0.3,
                                       subsample = 0.7,
                                       colsample_bytree = 0.7)
        elif n <= 5000 and n >= 1000:
            classifier = XGBClassifier(n_estimators = 70,
                                       max_depth = 4,
                                       learning_rate = 0.1,
                                       subsample = 0.8,
                                       colsample_bytree = 0.8)
        else:
            classifier = XGBClassifier(n_estimators = 120,
                                       max_depth = 5,
                                       learning_rate = 0.05,
                                       subsample = 0.9,
                                       colsample_bytree = 0.9)
        model = Pipeline([('vect', CountVectorizer()),
                          ('tfidf', TfidfTransformer()),
                        #   ('toarray', FunctionTransformer(lambda x: x.toarray(), validate=False)),
                          ('clf', classifier)])
        print("XGB MODEL STARTED")
        
        if n > 5000:
            model.fit(X_train, y_train_encoded, 
                      eval_set=[(X_test, y_test_encoded)], 
                      early_stopping_rounds=10, 
                      verbose=False)
        else :
            model.fit(X_train, y_train_encoded)
        
        file_path = os.path.join(base_path, 'training_fits', f'xgb_{dataset}.pkl')
        jl.dump(model, file_path)
        return "Model trained successfully!"

    except Exception as e:
        return str(e)
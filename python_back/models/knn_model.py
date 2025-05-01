from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import accuracy_score
import joblib as jl
import os

base_path = os.path.dirname(__file__)



def predict(input):
    try:
        print(f"model: {input}")
        file_path = os.path.join(base_path, 'training_fits', 'knn_laptops.pkl')
        model = jl.load(file_path)
        y = model.predict([" ".join(input)])
        print(y)
        return str(y)
    except Exception as e:
        return str(e)

def train(X_train, y_train):
    try:
        model = Pipeline ([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', KNeighborsClassifier(n_neighbors=5)),
        ])
        
        model.fit(X_train, y_train)
        file_path = os.path.join(base_path, 'training_fits', 'knn_laptops.pkl')

        jl.dump(model, file_path)

        

        # y_pred = model.predict(X_test)
        # accuracy = accuracy_score(y_pred, y_test)
        # return str(accuracy)
        return "Model trained successfully!"
    except Exception as e:
        return str(e)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

model = Pipeline ([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', KNeighborsClassifier(n_neighbors=10)),
])

def predict(input):
    try:
        print(f"model: {input}")
        y = model.predict([" ".join(input)])
        print(y)
        return str(y)
    except Exception as e:
        return str(e)

def train(X_train, y_train):
    try:
        model.fit(X_train, y_train)
        return "Model trained successfully"
    except Exception as e:
        return str(e)
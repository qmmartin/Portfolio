import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('spam.csv', encoding='latin1', names=['label', 'text'])
data.fillna('', inplace=True)

X = data['text']
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train Neural Network
clf = MLPClassifier(hidden_layer_sizes=(50, 50), max_iter=1000)
clf.fit(X_train_counts, y_train)

data_shuffled = data.sample(frac=1, random_state=42)

X = data_shuffled['text']
y = data_shuffled['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

clf = MLPClassifier(hidden_layer_sizes=(50, 50), max_iter=1000)
clf.fit(X_train_counts, y_train)

y_pred = clf.predict(X_test_counts)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy on shuffled test data: {:.2f}%".format(accuracy * 100))

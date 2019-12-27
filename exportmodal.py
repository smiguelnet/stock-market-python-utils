from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

data = datasets.load_iris()

dt = DecisionTreeClassifier()

dt.fit(data.data, data.target)

joblib.dump(dt, 'my_decision_tree.txt')

print(dt)
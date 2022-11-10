
import pandas
import matplotlib.pyplot as plt
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import metrics

# https://scikit-learn.org/stable/datasets.html
# https://pt.wikipedia.org/wiki/Conjunto_de_dados_flor_Iris
ds = sklearn.datasets.load_iris()
df = pandas.DataFrame(data=ds['data'], columns=ds['feature_names'])

print(df.head())
print(df.corr())
print(df.describe())

X = ds.data
y = ds.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=1, splitter='best', min_samples_split=2)
clf.fit(X_train, y_train)

tree.plot_tree(clf)
plt.show()

y_pred = clf.predict(X_test)

print(metrics.accuracy_score(y_test, y_pred))
print(metrics.precision_score(y_test, y_pred, average='weighted'))

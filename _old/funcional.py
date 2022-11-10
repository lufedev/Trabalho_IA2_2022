
import pandas as pd
from regex import P
from sklearn.tree import export_graphviz
from six import StringIO 
from IPython.display import Image  
import pydotplus
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import metrics
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
#matplotlib inline

# https://scikit-learn.org/stable/datasets.html
# https://pt.wikipedia.org/wiki/Conjunto_de_dados_flor_Iris
df = pd.read_csv('small_grocery.csv',)

print(df.head())
print(df.corr())
print(df.describe())


feature_cols = ['Gram_Prot','Gram_Fat', 'Gram_Carb']

X = df[feature_cols] # Features
y = df['Calories']# Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier(criterion="entropy", max_depth=11)
clf = clf.fit(X_train,y_train)

y_pred = clf.predict(X_train)
print(X_train)
print("Accuracy_train:",metrics.accuracy_score(y_train, y_pred))



y_pred = clf.predict(X_test)
print(X_test)
print("Accuracy_test:",metrics.accuracy_score(y_test, y_pred))


dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('food_project.png')
Image(graph.create_png())

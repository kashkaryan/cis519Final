# -*- coding: utf-8 -*-
"""CIS519_Final_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ahjBIE22vLkyoNZbELeF8cqxBe4un9tP
"""

from google.colab import drive
drive.mount('/content/drive')

"""Download https://docs.google.com/spreadsheets/d/1T8-opFnR1pVZaRGmJ6ovCrbb8hTQavk7Ui2yBTULJ38/edit?usp=sharing and set the name to cis519finaldataset."""

import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

df = pd.read_csv("/content/drive/MyDrive/cis519finaldataset - Sheet3.csv")
nX = df["Headers"]
ny = df["Labels"]
headers = []
labels = []
for i in nX:
  headers.append(i)

for i in ny:
  labels.append(i)

X = np.array(headers)
y = np.array(labels)

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
df.groupby('Labels').Headers.count().plot.bar(ylim=0)
plt.show()

from sklearn.feature_selection import chi2
import numpy as np

category_id_df = df[['Headers', 'Labels']].drop_duplicates().sort_values('Labels')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['Labels', 'Headers']].values)
df.head()

# N = 2
# for Product, category_id in sorted(id_to_category.items()):
#   features_chi2 = chi2(features, labels == category_id)
#   indices = np.argsort(features_chi2[0])
#   feature_names = np.array(tfidf.get_feature_names())[indices]
#   unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
#   bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
#   print("# '{}':".format(Product))
#   print("  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-N:])))
#   print("  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-N:])))

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(df.Headers).toarray()
labels = df.Labels

from sklearn.feature_selection import chi2
import numpy as np
N = 2
for Product, category_id in sorted(category_to_id.items()):
  features_chi2 = chi2(features, labels == category_id)
  indices = np.argsort(features_chi2[0])
  feature_names = np.array(tfidf.get_feature_names())[indices]
  unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
  bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
  print("# '{}':".format(Product))
  print("  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-N:])))
  print("  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-N:])))

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
models = [
    RandomForestClassifier(n_estimators=200, random_state=0),
    LinearSVC(),
    MultinomialNB(),
    LogisticRegression(random_state=0),
    SVC(C=1.0, kernel='linear', degree=3, gamma='auto'),
]
CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = []
for model in models:
  model_name = model.__class__.__name__
  accuracies = cross_val_score(model, features, labels, scoring='accuracy', cv=CV)
  for fold_idx, accuracy in enumerate(accuracies):
    entries.append((model_name, fold_idx, accuracy))
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])
import seaborn as sns
sns.boxplot(x='model_name', y='accuracy', data=cv_df)
sns.stripplot(x='model_name', y='accuracy', data=cv_df, 
              size=8, jitter=True, edgecolor="gray", linewidth=2)
plt.show()

cv_df.groupby('model_name').accuracy.mean()

X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, df.index, test_size=0.05, random_state=42)
model = LogisticRegression(random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, df.index, test_size=0.05, random_state=42)
tree = RandomForestClassifier(n_estimators=200, random_state=0)
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.svm import SVC
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, df.index, test_size=0.05, random_state=42)
svclassifier = SVC(C=0.9, kernel='linear', gamma='scale')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

"""#Naive Bayes Multinomial """

from sklearn.feature_extraction.text import CountVectorizer

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=42)

vect = CountVectorizer()
vect.fit(X_train)
X_train_dtm = vect.transform(X_train)
X_train_dtm = vect.fit_transform(X_train)

X_test_dtm = vect.transform(X_test)
X_test_dtm

# Commented out IPython magic to ensure Python compatibility.
from sklearn.naive_bayes import MultinomialNB

nb = MultinomialNB(alpha=0.9)
# nb = AdaBoostClassifier(n_estimators=50, base_estimator=nb,learning_rate=1)
# %time nb.fit(X_train_dtm, y_train)

from sklearn import metrics
y_pred_class = nb.predict(X_test_dtm)
l = metrics.accuracy_score(y_test, y_pred_class)
s = metrics.f1_score(y_test, y_pred_class, average='weighted')
print("Accuracy Score is " + str(l))
print("F1 Score is " + str(s))
print(confusion_matrix(y_test, y_pred_class))
print(classification_report(y_test, y_pred_class))
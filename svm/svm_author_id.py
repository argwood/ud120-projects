#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
clf = SVC(kernel="rbf", C=10000)
#features_train = features_train[:int(len(features_train)/100)] # shrink training set to 1% of original size to speed up training
#labels_train = labels_train[:int(len(labels_train)/100)]
t0=time()
clf.fit(features_train, labels_train)
print('Training time: ', round(time()-t0,3))
t1=time()
pred = clf.predict(features_test)
print('Prediction time: ', round(time()-t1,3))

acc = accuracy_score(pred, labels_test)
print("SVM Accuracy: ", acc)
print("Prediction for element 10: ", pred[10])
print("Prediction for element 26: ", pred[26])
print("Prediction for element 50: ", pred[50])
chris = 0
for i,p in enumerate(pred):
    if p==1:
        chris+=1
print('There are {} emails belonging to Chris'.format(chris))
#########################################################


##NOTES##
# With full training set, linear kernel: Accuracy = 0.98; Training time = 388.573; Prediction time = 38.034 (much slower than naive bayes)
# With 1% training set, rbf kernel with no param tailoring: Accuracy = 0.61, pretty low
# Using rbf kernel with very large C values gives higher accuracy (C=10,000 -> acc = 0.89)
# With full training set, optimized rbf kernel: Accuracy > 0.99; Training time = 333.70; Prediction time = 57.148

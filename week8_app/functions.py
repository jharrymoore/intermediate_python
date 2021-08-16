from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import datasets
import streamlit as st
from sklearn.model_selection import train_test_split, cross_val_score
from typing import Dict
from sklearn.neighbors import KNeighborsClassifier

def get_dataset_name(dataset_name: str):
    if dataset_name.lower() == 'iris':
        data = datasets.load_iris()
    elif dataset_name.lower() == 'wine':
        data = datasets.load_wine()
    elif dataset_name.lower() == 'breast cancer':
        data = datasets.load_breast_cancer()
    else:
        raise AssertionError('Dataset must be one of the provided options')
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)
    return X_train, X_test, y_train, y_test, data


def add_ui_params(classifier_name):
    params = {}
    if classifier_name.lower() == 'knn':
        K = st.sidebar.slider('K', 1, 15) 
        params['n_neighbors'] = K
    elif classifier_name.lower() == 'svm':
        c = st.sidebar.slider('C', 0.01, 10.0)
        kernel = st.sidebar.selectbox('Kernel', ('linear', 'poly', 'rbf', 'sigmoid', 'precomputed'))
        params['C'] = c
        params['kernel'] = kernel
    elif classifier_name.lower() == 'random forest':
        max_depth = st.sidebar.slider('Max Depth', 2, 15)
        num_trees = st.sidebar.slider('n_estimators', 1, 100)
        params['max_depth'] = max_depth
        params['n_estimators'] = num_trees
    return params

def get_classifier(clf_name: str, params: Dict):
    if clf_name.lower() == 'knn':
        model = KNeighborsClassifier(**params)
    elif clf_name.lower() == 'svm':
        model = SVC(**params)
    elif clf_name.lower() == 'random forest':
        model = RandomForestClassifier(**params)

    return model

def train_model(model, X, y, metric, k_folds):
    results = cross_val_score(model, X, y, scoring=metric, cv=k_folds)
    model = model.fit(X, y)
    return model, results, results.mean(), results.std()

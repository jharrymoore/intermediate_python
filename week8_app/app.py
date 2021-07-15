# taken from github.com/jharrymoore/sklearn_gui
import sklearn
import streamlit as st
import numpy as np
import  matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from functions import get_dataset_name, get_classifier, add_ui_params, train_model



st.title('Machine Learning GUI')

st.write('Example GUI application with a machine learning backend')


dataset_name = st.sidebar.selectbox('Select Dataset',
        ('Wine', 'Breast Cancer', 'Iris'))

st.write(f'Dataset Name: {dataset_name}')

classifier_name = st.sidebar.selectbox('Select Classifier', 
                    ('KNN', 'SVM', 'Random Forest'))



X_train, X_test, y_train, y_test, data = get_dataset_name(dataset_name)


st.write(f'Shape of the dataset is {X_train.shape}')
st.write('Number of classes:', len(np.unique(data.target)))



params = add_ui_params(classifier_name)






model = get_classifier(classifier_name, params)

k_folds = st.sidebar.slider('Cross Validation Folds', 2, 20)
metric = st.sidebar.selectbox('Model performance metric', tuple(sklearn.metrics.SCORERS.keys()), index=11)


fitted_model, accuracy, mean, std = train_model(model, X_train, y_train, metric, k_folds)
y_pred = fitted_model.predict(X_test)
test_set_accuracy = accuracy_score(y_test, y_pred)
st.write('Cross validation Model Accuracy', mean)
st.write('Test set accuracy:', test_set_accuracy)


# plot the principle components

pca = PCA(2)

x_proj = pca.fit_transform(data.data)

x1 = x_proj[:, 0]
x2 = x_proj[:,1]

fig = plt.figure()
plt.scatter(x1, x2, c=data.target, alpha=0.8, cmap='viridis')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.colorbar()

st.pyplot(fig)
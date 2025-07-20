# Credit_Risk_Analysis

## Overview
The purpose of this project was to train a supervised machine learning model to predict whether a loan is considered "low" or "high" risk based on a number of parameters about the loan. As there were an overrepresentation of "low-risk" loans in the data, we tested a number of over and under-sampling methods combined with a logistic regression model. We also trained a couple ensemble models.

## Results

### Logistic Regression models
First, we used logistic regression to model the data. We used three types of sampling methods to correct for the imbalanced representation of target types: Naive Random Oversampling, SMOTE Oversampling, and SMOTEENN. Below are the performace measurements for each model

Naive Random Oversampling
![](/images/naiveover.png)

SMOTE Oversampling
![](/images/smoteover.png)

SMOTEENN
![](/images/smoteencomb.png)

### Ensemble models
We also trained a Balanced Random Forest Classifier and an Easy Ensemble AdaBoost Classifier to see if ensemble models would result in better performance.

Balanced Random Forest Classifier
![](/images/balrf.png)

Easy Ensemble AdaBoost Classifier
![](/images/ada.png)

## Summary
All of our models perfomed reasonably well for predicting low-risk loans. In particular, the Logistic regression model with SMOTEENN resampling, Balanced Random Forest Classifier, and AdaBoost Classifers all resulted in high precicision, recall and F1 scores. Despite correcting for imbalanced sample sizes, our models performed poorly at predicting high-risk loans. While recall for high-risk loans was substantial, precision suffered. Out of all models we trained, I would recommend using a Logistic regression model with SMOTEENN re-sampling to predict loan status as this model resulted in the highest F1 score.
# Neural_Network_Charity_Analysis

## Overview
Alphabet Soup provides grants to non-profit organizations to fund environmental and humanitarian projects. Our task was to build neural network that can predict whether or not an organization's project will be successful if given funding. We used a dataset of past funding recipients to train and test our model.

## Results

### Preprocessing
Our target in the dataset was a binary variable indicating whether a particular project was successful. We dropped columns that served as project identifiers, and retained all other variables as features for our model. Categorial features were binned and encoded. All features were split into training and testing sets and finally standardized.

### Models
Our intial model included two hidden layers with 80 and 30 neurons, respectively. We used relu activation functions for both hidden layers, and a sigmoid activation function for the output layer. This model resulted in an accuracy of 70.6% and a loss of 0.669.

To optimize our model, we used keras-tuner to tune the number of layers, number of neurons in each layer, and activation functions. Out of 235 models evaluated, the best model achieved an accuray of 73.4% and a loss of .554. This model and four layers with 96, 480, 480, and 320 neurons respectively. It used relu activations functions for all layers and a sigmoid activation function for the output layer.

## Summary
In conclusion, we were not able to achieve target accuracy of 75%. Optimization using keras-tuner only resulted in an accuracy increase of ~3%. To achieve better accuracy, We would likely have to reevaluate our preprocessing steps and determine if our input data can be adjusted to be more interpretable (e.g. removing outliers, dropping/retaining columns, binning). We could also let our model train for more epochs. In our opinion, it would be worthwhile to train a supervised machine learning model such as a random forest on this data to see if a similar accuracy can be generated with less time and computer resources.


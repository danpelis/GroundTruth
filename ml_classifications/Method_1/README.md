# Method 1 File Descriptions

`Predictor_Generation.ipynb` is used to generate the predictor matrix. This is a matrix that contains all the rating information for the users contained in the ground truth file that was provided to us for the ML Classifier assignment. We look at the album, artist, and average genre ratings as features here. 

`Method_1_Classifiers.ipynb` takes the predictor matrix and trains several models using the dataset. We look at logistic regression, decision trees, reandom forest, and gradient boosted trees for our models. The resulting weight vectors of each of the models is saved and used in order for us to make recommendation on the test set.

`Weighted_Average.ipynb` is used to generate the reccommendations for the test set by using a given weight vector provided by the different models trained in the previous notebook. The results of this file are used as the submission on Kaggle.

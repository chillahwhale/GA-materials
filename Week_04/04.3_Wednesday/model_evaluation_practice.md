<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Model Evaluation Practice

_Author: Noelle Brown (DEN)_

---

**Instructions:** Answer the following questions regarding model evaluation. Note that for some of the questions, there may be more than one correct answer or it may not even be possible to answer the question without more information - so be sure to justify your choices.  

## Regression

### 1. Define the following regression evaluation techniques:
- **MSE**:
- **RMSE**:
- **MAE**:
- **R2**:
- **Adjusted R2**:

### 2. Home Prices
*You are interested in predicting the sale prices of homes in Denver.*  
- What would a MAE of 18,456 mean?
> Answer here:

- What would a MSE of 23,534 mean?
> Answer here:

- What would a RMSE of 19,425 mean?
> Answer here:

- What would an R2 of 0.46 mean?
> Answer here:

- What would an adjusted R2 of 0.42 mean?
> Answer here:

- Justify whether or not these metrics make sense in this context.
> Answer here:

- In this case, is it better to use MAE, MSE, RMSE, or R2?
> Answer here:

### 3. Football Points
*You are interested in predicting the number of points a football team will get over the season.**
- What would a MAE of 30 mean?
> Answer here:

- What would a MSE of 34 mean?
> Answer here:

- What would a RMSE of 27 mean?
> Answer here:

- What would an R2 of 0.73 mean?
> Answer here:

- Justify whether or not these metrics make sense in this context.
> Answer here:

- In this case, is it better to use MAE, MSE, RMSE, or R2?
> Answer here:

### 4. Customers
*Your boss asks you to predict the number of new customers in various regions. Your boss tells you to make sure that your model does not have any extreme outliers, as this could have negative impacts for where the marketing team decides to spend money.*  
- What would a MAE of 135 mean?
> Answer here:

- What would a RMSE of 187 mean?
> Answer here:

- Justify whether or not these metrics make sense in this context.
> Answer here:

- In this case, is it better to use MAE or RMSE?
> Answer here:

## Classification

### 5. Define the following classification evaluation techniques:
- **Accuracy**:
- **Precision**:
- **Recall**:
- **F1 Score**:
- **Log Loss**:
- **AUC**:

*The following questions are taken from [Damien Martin](https://kiwidamien.github.io/interview-practice-with-precision-and-recall.html).*

### 6. We are trying to build a classifier to identify whether a particular insurance claim is fraudulent. What do recall and precision mean in this context, and which is a better metric for our problem? Why?
> Answer here:

### 7. You are trying to detect whether or not a person has a disease.
- What is the positive class?
> Answer here:  

- What would an accuracy of 93% mean?
> Answer here:

- What would a recall of 80% mean?
> Answer here:  

- What would a precision of 75% mean?
> Answer here:  

- In this case, should you use accuracy, precision, or recall?
> Answer here:  

### 8. Should we approve a loan?
*We are looking to develop a machine learning algorithm to predict whether someone will pay a loan back or not.*  
- What is the positive class?
> Answer here:  

- What would an accuracy of 78% mean?
> Answer here:

- What would a recall of 75% mean?
> Answer here:  

- What would a precision of 85% mean?
> Answer here:  

- In this case, should you use accuracy, precision, or recall?
> Answer here:  

### 9. Should we unlock a phone?
*We are building a facial recognition algorithm to allow people to unlock their phone. If the phone recognizes the person as the authorized user, it will unlock the phone. If it doesn't recognize the user, it will prompt them to try again or try an alternative method (such as a passphrase).*  
- What is the positive class?
> Answer here:

- What would a recall of 80% mean?
> Answer here:

- What would a precision of 70% mean?
> Answer here:

- In this case, should you use precision or recall?
> Answer here:  

### 10. Detect malicious programs
*When running a program for the first time, we are running some information about the program (such as where it was downloaded, size of the executable, etc) through a classifier. If the program is deemed safe, it will run. If it is deemed unsafe, the user will be prompted to confirm that the program is safe before running.*  
- What is the positive class?
> Answer here:

- What does 85% recall mean?
> Answer here:

- What does 75% precision mean?
> Answer here:

- In this case, should you use precision or recall?
> Answer here:  

## Additional Resources
**If you are interested in learning more about evaluation metrics, here are some good resources:**  
- [MAE and RMSE — Which Metric is Better?](https://medium.com/human-in-a-machine-world/mae-and-rmse-which-metric-is-better-e60ac3bde13d)
- [Choosing the Right Metric for Evaluating Machine Learning Models](https://medium.com/usf-msds/choosing-the-right-metric-for-machine-learning-models-part-1-a99d7d7414e4)
- [The 5 Classification Evaluation metrics every Data Scientist must know](https://towardsdatascience.com/the-5-classification-evaluation-metrics-you-must-know-aa97784ff226)
- [Performance Metrics for Classification problems in Machine Learning](https://medium.com/thalus-ai/performance-metrics-for-classification-problems-in-machine-learning-part-i-b085d432082b)

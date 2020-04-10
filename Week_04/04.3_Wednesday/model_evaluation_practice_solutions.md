<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Model Evaluation Practice - Solutions

_Author: Noelle Brown (DEN)_

---

**Instructions:** Answer the following questions regarding model evaluation. Note that for some of the questions, there may be more than one correct answer or it may not even be possible to answer the question without more information - so be sure to justify your choices.  

## Regression

### 1. Define the following regression evaluation techniques:
- **MSE**: The mean of the sum of the squared errors (difference between your predicted value and the actual value)
- **RMSE**: The square root of the MSE
- **MAE**: The mean of the absolute value of errors
- **R2**: The proportion of the variation in y that is explained by x
- **Adjusted R2**: Penalizes the R2 term by accounting for more variables (if the variable improves the model by less than expected by chance)

### 2. Home Prices
*You are interested in predicting the sale prices of homes in Denver.*  
- What would a MAE of 18,456 mean?
> Answer here: On average, you are off on your prediction by $18,456

- What would a MSE of 23,534 mean?
> Answer here: On average, the square of your error is $23,534

- What would a RMSE of 19,425 mean?
> Answer here: The square root of your average squared error is $19,425.

- What would an R2 of 0.46 mean?
> Answer here: 46% of the variation in sale price can be explained by your model.

- What would an adjusted R2 of 0.42 mean?
> Answer here: 42% of the variation in sale price can be explained by your model, penalized for additional variables added to the model.

- Justify whether or not these metrics make sense in this context.
> Answer here: Yes, it makes sense to be off by these amounts when talking about home prices.

- In this case, is it better to use MAE, MSE, RMSE, or R2?
> Answer here: Depends on your goal. I would probably look at a combination of all of them. It is up to you if you are very concerned about outliers or not.

### 3. Football Points
*You are interested in predicting the number of points a football team will get over the season.**
- What would a MAE of 30 mean?
> Answer here: On average, you are off on your predictions by 30 points.

- What would a MSE of 34 mean?
> Answer here: On average, the square of your errors is 34 points.

- What would a RMSE of 27 mean?
> Answer here: The square root of your average squared error is 27 points.

- What would an R2 of 0.73 mean?
> Answer here: 73% of the variation in points can be explained by your model.

- Justify whether or not these metrics make sense in this context.
> Answer here: Yes, it makes sense to be off by this many points over a season.

- In this case, is it better to use MAE, MSE, RMSE, or R2?
> Answer here: Again, depends.

### 4. Customers
*Your boss asks you to predict the number of new customers in various regions. Your boss tells you to make sure that your model does not have any extreme outliers, as this could have negative impacts for where the marketing team decides to spend money.*  
- What would a MAE of 135 mean?
> Answer here: On average, you are off on your predictions by 135 new customers.

- What would a RMSE of 187 mean?
> Answer here: On average, the square root of your squared errors is 187 customers.

- Justify whether or not these metrics make sense in this context.
> Answer here: It makes sense for customer numbers if you can get a lot of new customers. Wouldn't make sense if you don't get that many new customers.

- In this case, is it better to use MAE or RMSE?
> Answer here: RMSE based on what your boss wants.

## Classification

### 5. Define the following classification evaluation techniques:
- **Accuracy**: The percent of correct choices out of the total number of predictions
- **Precision**: Measures what percentage of predicted positives are truly positive
- **Recall**: The percentage of actual positives that was correctly classified
- **F1 Score**: Balance of precision and recall
- **Log Loss**: Penalizes false classifications using the probability that each observation belongs in a specific class (worse score for more incorrect probabilities)
- **AUC**: Area under the ROC curve, indicates how well the classes are separated

*The following questions are taken from [Damien Martin](https://kiwidamien.github.io/interview-practice-with-precision-and-recall.html).*
*ALL SOLUTIONS FOR THIS SECTION ARE FROM THE ABOVE LINK.*

### 6. We are trying to build a classifier to identify whether a particular insurance claim is fraudulent. What do recall and precision mean in this context, and which is a better metric for our problem? Why?
> Answer here: "Precision is the fraction of cases that are fraudulent out of those that our classifier labelled as fraudulent. The problem with a low precision is that our investigators will spend a lot of time investigating claims that are actually legitimate. Recall is the fraction of fraudulent cases our classifier finds. The problem with a low recall is that we would be paying out on a lot of undetected fraudulent claims."

### 7. You are trying to detect whether or not a person has a disease.
- What is the positive class?
> Answer here: The positive class is the presence of the disease.

- What would an accuracy of 93% mean?
> Answer here: An accuracy of 93% means that our classifier correctly identifies the presence of the disease 93% of the time.

- What would a recall of 80% mean?
> Answer here: A recall of 80% would mean that 80% of the positive cases were found by the detector (if you submitted the entire population). Alternatively, a recall of 80% means that there is an 80% chance of someone with the disease setting off the detector. The problem with a low recall score is that we would miss people that were unhealthy. If the recall is 80%, we are would not detect 20% of the sick population.

- What would a precision of 75% mean?
> Answer here: A precision of 75% means 75% of the times the detector went off, they were actually positive cases. The problem with a low precision score is spending time having people undergo further screenings or using medication unnecessarily. In this example, 25% of the people we flagged as being sick would have unnecessary followups.

- In this case, should you use accuracy, precision, or recall?
> Answer here: Recall - this could potentially be more deadly if you are missing positive cases. It is better to follow up on non-sick cases than to miss sick cases.

### 8. Should we approve a loan?
*We are looking to develop a machine learning algorithm to predict whether someone will pay a loan back or not.*  
- What is the positive class?
> Answer here:  The positive class are the borrowers that pay back the loans.

- What would an accuracy of 78% mean?
> Answer here: An accuracy of 78% means that our classifier correctly classifies borrowers 78% of the time.

- What would a recall of 75% mean?
> Answer here: 75% recall means that 75% of the borrowers that would pay back the loan are approved by our system. We miss 25% of people that would have paid us back by rejecting them. In general, the problem with a low recall is that we are rejecting customers who we would have paid us back (and for whom we would have made interest).

- What would a precision of 85% mean?
> Answer here: 85% precision means that of all the loans we approve, 85% pay us back. The remaining 15% of approved loans go into default. The problem with a low precision is that we are approving loans that are defaulting.

- In this case, should you use accuracy, precision, or recall?
> Answer here: In this example we would generally prefer to emphasize precision over recall, as approving a bad loan (and losing the capital investment) is more costly than missing out on the profit we could make from a good loan.  
We have to be a little careful here too, as we are binarizing a continuous variable: there is a difference between someone who defaults after paying 1 year of a 5 year loan, and someone who defaults after paying 4 years of a 5 year loan. A product manager might expect you to look at the expected loss of a customer and threshold on that as a more useful (and nuanced) metric, rather than precision.

### 9. Should we unlock a phone?
*We are building a facial recognition algorithm to allow people to unlock their phone. If the phone recognizes the person as the authorized user, it will unlock the phone. If it doesn't recognize the user, it will prompt them to try again or try an alternative method (such as a passphrase).*  
- What is the positive class?
> Answer here: The positive class is recognizing the user as authorized.

- What would a recall of 80% mean?
> Answer here: 80% recall means 80% of the times the authorized user tries to use this feature, the phone unlocks. The remaining 20% of the time, the authorized user was asked to try again or use a passphase.

- What would a precision of 70% mean?
> Answer here: 70% precision means that out of all the times the phone was unlocked using this feature, it was unlocked by an authorized user 70% of the time. The remaining 30% of the times it was unlocked, it allowed in someone that was not authorized.

- In this case, should you use precision or recall?
> Answer here: Precision is the more important metric here: if precision is low that means this device isn't securing information very well on your phone. If recall is low, it just means the user has to try again (perhaps from a different angle) or resort to using a passphrase. This adds more friction, and users are likely to say the feature isn't worth the effort if recall is very low, but this is better than allowing people that look vaguely similar to unlock your phone (this would be high recall, low precision).
As a product manager, you would also care about how precision and recall are distributed amongst users. There is a huge difference between having a recall of 80% over all attempts, compared to it always working for 80% of the population, and never working for 20% of the population. The reality is unlikely to be this extreme, but there probably is a difference between the recall and precision rates based on gender and ethnicity. For image recognition, you should consider the following:
- Are there biases in the training data set? Often training sets will have some ethnic groups over-represented. Thankfully, this can be addressed by fixing the data set.
- Darker skin tones don't reflect as much light, which gives sensors less signal to work off. This can be overcome by taking images in brighter conditions, but it will mean that many image recognition algorithms will be more responsive to lighter skin tones than darker tones. There isn't a way to fix this (it's physics!) but you can handicap your algorithm to refuse to classify any person if the ambient brightness is too low (even if it is very confident it could identify a light skin toned person). This would mean that users would have a uniform experience, regardless of ethnic group.

### 10. Detect malicious programs
*When running a program for the first time, we are running some information about the program (such as where it was downloaded, size of the executable, etc) through a classifier. If the program is deemed safe, it will run. If it is deemed unsafe, the user will be prompted to confirm that the program is safe before running.*  
- What is the positive class?
> Answer here: The positive class is "this program is not safe to run"

- What does 85% recall mean?
> Answer here: 85% recall means that 85% of unsafe programs are detected, and showed the prompt. The other 15% of malicious programs did not require a prompt.

- What does 75% precision mean?
> Answer here: A precision of 75% means that out of all the programs that set off the prompt, 75% of them were malicious. The other 25% of the times the dialog popped up, it was for programs that were fine.

- In this case, should you use precision or recall?
> Answer here: In this case we would want to prioritize recall. The cost of letting a malicious program run is high, and the cost of incorrectly flagging a program is low - we just need to prompt the user whether or not we are sure. An extreme version of this is to flag every program, which would be a recall of 100% and a low precision; this is one of the few examples where this might be an acceptable tradeoff.

## Additional Resources
**If you are interested in learning more about evaluation metrics, here are some good resources:**  
- [MAE and RMSE — Which Metric is Better?](https://medium.com/human-in-a-machine-world/mae-and-rmse-which-metric-is-better-e60ac3bde13d)
- [Choosing the Right Metric for Evaluating Machine Learning Models](https://medium.com/usf-msds/choosing-the-right-metric-for-machine-learning-models-part-1-a99d7d7414e4)
- [The 5 Classification Evaluation metrics every Data Scientist must know](https://towardsdatascience.com/the-5-classification-evaluation-metrics-you-must-know-aa97784ff226)
- [Performance Metrics for Classification problems in Machine Learning](https://medium.com/thalus-ai/performance-metrics-for-classification-problems-in-machine-learning-part-i-b085d432082b)

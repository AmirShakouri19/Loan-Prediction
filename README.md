# Loan-Prediction

Banks make money by giving loans and charging interests. In the case of loans defaults, however, banks incur loss. So, as much as banks are willing to issue loans
to increase their profit, they need to avoid bad lending. An automated loan process can help to accelerate the process of approval - or rejection - even if it is not completely substituted for the conventional loan approval process. Other benefits includes avoiding decession biases or discrimination.

The aim of this project is to develope an application for automating loan approval process. A supervised machine learning model is developed based on features extracted/engineered from the income/credit history, household situation and education level. The model is finally deployed on AWS EC2.

Prior to developing the model, several exploratory data analyses are performed which can be found in "EDA" notebook, e.g.:

<img src="/Images/Image4.png">  <img src="/Images/Image4.png">

Key characteristics of the data are being skewed and imbalanced. Some feature engineering are done to fix these issues which includes log-transformation and combining the income components, for example:

<img src="/Images/Image1.png">  <img src="/Images/Image2.png">

Finally, the modeling pipeline are built using RandomForest. The model is then tested, optimised using GridSearchCV and deployed by cloudpickling. You can find the modeling part on the "Coding" notebook.

Interested or have questions? Please don't hesitate to comment here or contact me. Also, feel free to fork and contribute to the project...

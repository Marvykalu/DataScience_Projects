# Introduction

Businesses have evolved to the point where facts, metrics and data are used to guide strategic business decisions that align with business goals, objectives, and initiatives. 

This notebook looks at a business problem in a mail-order catalog business. 

#### Description of problem

The company manufactures and sells high-end home goods. Last year, the company sent out its first print catalog, and is preparing to send out this year's catalog in the coming months to their new customers. The company has 250 new customers from their mailing list that they want to send the catalog.

#### Undecided decision

Management want to make a decision based on the `expected profits` from sending a catalog to these customers. They do not want to send the catalog out to these new customers unless the `expected profit contribution` exceeds **10,000** dollars. 

#### Given information

From management we know the

- costs of printing and distributing catalogs (**6.50** per catalog).
- We also know the average gross margin (price - cost) on all products sold through the catalog is 50%.

#### Task
The task is to predict how much money the company can expect to earn from sending out a catalog to their new customers.

## Analysis Steps

`1.` **Data Exploration**: What are the features correlated with average sales amounts, based on the existing customer data?

2) **Build a predictive model**: build a predictive model with the features from step one to predict the average sales amount of the new customers

3) **Estimate the expected revenue**: By multiplying the predicted sales amount with the probability that each new customer will buy our catalog, we can get this expected revenue information these 250 people.

4) **Aggregated revenue**: The aggregated revenue should be multiplied with the average gross margin. 

5) Next, the total costs of catalog for 250 customers should be subtracted.

6) **Decision making process**: Compare total expected net profit with the cut-off (10,000) provided by management. If the total expected profit contribution is larger than the cut-off value, sending this year's catalog to the new customers is recommended.

The task is to predict how much money the company can expect to earn from sending out a catalog to their new customers.

# Summary/Conclusion

- We explored our training dataset  (which has information about existing customers), to find features that would help us predict average sales amount for future customers.

- Then we used the observed features to build a model that would predict average sales amount for future customers.

- In this notebook, we used the predictive model to predict average sales amount for the 250 customers in the mailing list dataset. 

- Then we performed all necessary calculations with this predicted average sales amount:

 - `expected revenue/ per customer = predicted sales * score_yes`

 - `total expected revenue = sum(expected revenue/ per customer) = 47,224.87`
 
 - `expected profit = total expected revenue* average gross margin(0.5) -  cost of sending catalog to 25 customers (6.5*250) = USD 21,987.43
 
Therefore, if the catalog is sent to the 250 customers, the company should expect a profit of USD 21,987.43. Which is higher than the cutoff value of USD 10,000 suggested by the management. 

# Deployment

- BuildingPredictiveModel.ipynb contains the data exploration process and model building.

- PredictiveModelling-MakingDecision.ipynb contains the predictive process on our new customers and calculation of necessary business metrics for determining company's expected profit.

# Acknowledgement

I acknowledge the use of data and business problem description from the GitHub account [here](https://github.com/SooyeonWon/catalog_launch_sales_prediction)
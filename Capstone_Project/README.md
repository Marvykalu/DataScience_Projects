# Introduction

This blog post summarizes my work on the final capstone project for the Udacity Data Scientist nano degree program. 
I analyzed demographic data for customers of a mail-order sales company (Bertelsmann Arvato Analytics) in Germany, comparing it against demographic information for the general population in Germany.
The aim is to find which individuals in the general population are most likely to convert into becoming customers for the company.

## Data
There are four (4) csv files in total:

- Udacity_AZDIAS_052018.csv: Demographics data for the general population of Germany; 891 211 persons (rows) x 366 features (columns).

- Udacity_CUSTOMERS_052018.csv: Demographics data for customers of a mail-order company; 191 652 persons (rows) x 369 features (columns).

- Udacity_MAILOUT_052018_TRAIN.csv: Demographics data for individuals who were targets of a marketing campaign; 42 982 persons (rows) x 367 (columns).

- Udacity_MAILOUT_052018_TEST.csv: Demographics data for individuals who were targets of a marketing campaign; 42 833 persons (rows) x 366 (columns).

Each row of the demographics files represents a single person, but also includes information outside of individuals, including information about their household, building, and neighborhood.

The first two files will be used to figure out how customers ("CUSTOMERS") are similar to or differ from the general population at large ("AZDIAS"). Then result of our analysis will be used to make predictions on the other two files ("MAILOUT"), predicting which recipients are most likely to become a customer for the mail-order company.

In addition to the above data, there are two additional meta-data which helped to understand the data better:

- DIAS Information Levels - Attributes 2017.xlsx: a top-level list of attributes and descriptions, organized by informational category

- DIAS Attributes - Values 2017.xlsx: a detailed mapping of data values for each feature in alphabetical order
# Summary/Conclusion

By using machine learning, we have discussed how to predict  potential customers of a mail-order company based on Germany's general population. 

The dataset provided by Udacity partners at Bertelsmann Arvato Analytics presents a real-life data. We spent more time on getting the data into a form for machine learning applications. 

In the first part, preprocessing of general and customer demographic datasets was made. I created a function that cleans the dirty and untidy data: dealing with and imputing missing values, dropping correlated features, engineering more features, selecting features, and standardization. This part was the most time-consuming part of the project.

We created customer segmentation report for Avarto Financial Solutions in the second part using unsupervised ML models. I reduced the dimension of datasets by using principal component analysis. Then clustering was made by using kmeans from sklearn. Specifically, results from our segmentation report showed that the general population can be divided into 11 clusters.

The highest proportion (overrepresentation) of Arvato customers belong to cluster 3, which is associated with older generations, who are money savers and have strong affinity for online shopping.
These aspects should be taken into consideration in any marketing campaign and the recommendations we can give to the company is to focus on offers and advertising campaigns that aim to save money.

Similarly the underrepresented customer groups were identified by the clusters and belong to cluster 1.
In the last part, a supervised learning model was used to find out potential customers. The best model to predict the response of target customers is XGBoost regressor, then the fine-tuning of parameters was made by random search method. With the imbalanced nature of the train data, AUC -ROC curve was used as evaluation metric to measure the performance of the model.


# Deployment

Arvato_Project_Workbook.ipynb contains the data exploration process and model building.

# Acknowledgement

I acknowledge the use of data and business problem description from Udacity
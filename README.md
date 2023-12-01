# Predicting Drug Ratings Based on Patient Review with Natural Language Processing

### Built With Python 3.11

<!-- ABOUT THE PROJECT -->
### Project Description

Using the Drug Review dataset from the <a href="https://archive.ics.uci.edu/dataset/462/drug+review+dataset+drugs+com">UCI Machine Learning Repository</a>, our application includes an end-to-end statistical analysis alongside model development with multiple algorithms. During development, we used Python 3.11 and a few popular libraries for data manipulation, visualization and model development. The intent of this project is to determine if it is possible to accurately predict a drug’s rating (out of 10) based on the review that a patient left by leveraging natural language processing (NLP) techniques along with supervised classification algorithms. There are two separate approaches for the problem at hand. One approach consists of using all 10 individual ratings (E.g., 0-10). The alternative approach consists of grouping ratings into buckets based on their rating (E.g., 0-2, 3-5, 6-8, 9-10). The reasoning behind the use of supervised learning lies in the fact that the data being used to make predictions is already labeled. The use of NLP stems from the need to convert the patient’s text-based review into a format that the computer can understand. A combination of algorithms and techniques will result in a classification model that accurately predicts a drug’s rating based on a patient’s review. 


<!-- Installation and Running the Project -->
### Installation and Running the Project
1. Clone the repo 
   ```
   gh repo clone arin-deloatch/Predicting-Drug-Ratings-Based-on-Patient-Review
    ```
   
2. Ensure the necessary packages are installed via your package manager (pip, anaconda,etc.) and import the modules into your python/notebook file. 
    ```
   import pandas as pd
   import numpy as np
    import nltk
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
    from sklearn.pipeline import Pipeline
    from sklearn.metrics import classification_report
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.linear_model import SGDClassifier
    from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
    from sklearn.metrics import accuracy_score
     ```
3. If you're using the ucimlrepo library for importing the data, be sure to install and import the dependencies.
  ```
  pip install ucimlrepo
  from ucimlrepo import fetch_ucirepo
 ```

### Data
You can find the data files we used for our project in the "data" folder. Feel free to change parameters and slice up the data any way you'd like to interpret different types of results. It's important to note that the majority of features are categorical and if you'd like a feature breakdown you can visit the <a href="https://archive.ics.uci.edu/dataset/462/drug+review+dataset+drugs+com" target="_blank">UC Irvine Machine Learning Repository</a>

<!-- LICENSE -->
### License

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.

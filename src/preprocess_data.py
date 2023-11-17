# import all modules needed
import pandas as pd
import nltk


# to clean the data
from data_cleaner import DataCleaner

train_cleaner = DataCleaner('drugsComTrain_raw.csv')
train_data = train_cleaner.get_cleaned_data()

test_cleaner = DataCleaner('drugsComTest_raw.csv')
test_data = test_cleaner.get_cleaned_data()

traind = train_data[["rating","review"]].copy()
testd = test_data[["rating","review"]].copy()


# to preprocess the text data
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# preprocess text: convert to lowercase, tokenize, remove punctuation and stopwords
def preprocess_text(text):
	tokens = word_tokenize(text.lower())
	tokens = [word for word in tokens if word.isalpha()]
	tokens = [word for word in tokens if word not in stopwords.words('english')]
	return ' '.join(tokens)
	

traind['cleaned_review'] = traind['review'].apply(preprocess_text)

testd['cleaned_review'] = testd['review'].apply(preprocess_text)


# drop non-processed review column
traind.drop('review', axis=1, inplace=True)
testd.drop('review', axis=1, inplace=True)

# export to csv for use later
traind.to_csv('preprocessedTrain.csv', index=False)
testd.to_csv('preprocessedTest.csv', index=False)


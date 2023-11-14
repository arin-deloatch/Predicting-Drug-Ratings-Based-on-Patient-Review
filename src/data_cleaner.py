import pandas as pd
import numpy as np

class DataCleaner:
	def __init__(self, file_path):
		self.file_path = file_path
		self.data = None
		self._load_and_clean_data()
	
	def _load_and_clean_data(self):
		# import csv data
		imported_data1 = pd.read_csv(self.file_path)
		imported_data1.drop(columns={"date", "usefulCount"}, inplace=True)
		
		# make condition missing/nan for all rows in which variable condition contains 
		# the following unwanted text: "</span> users found this comment helpful."
		temp1 = imported_data1[imported_data1['condition'].str.contains("/span> users found this comment helpful.", na=False)]
		temp1.loc[:, 'condition'] = np.nan
		temp2 = imported_data1[~imported_data1['condition'].str.contains("/span> users found this comment helpful.", na=False)]
		imported_data2 = pd.concat([temp1, temp2], axis=0)
		
		# find all rows with condition variable missing/nan, then fill in from 
		# other rows containing the same drugName
		
		# condition is missing
		data_blank_condition = imported_data2[pd.isna(imported_data2['condition'])]
		
		# condition is not missing
		data_non_blank_condition = imported_data2[~pd.isna(imported_data2['condition'])]
		
		# get a dataset of unique drugName with corresponding condition
		unique_drug_condition = data_non_blank_condition[['drugName', 'condition']].groupby('drugName').first().reset_index()
		unique_drug_condition.rename(columns={"condition":"new_condition"}, inplace=True)
		
		# merge with condition missing dataset to get condition for each drug
		merged_data = pd.merge(data_blank_condition, unique_drug_condition, on='drugName', how='left')
		merged_data['condition'] = merged_data['condition'].fillna(merged_data['new_condition'])
		merged_data.drop(columns='new_condition', inplace=True)
		
		# keep only rows with condition not missing
		imported_data3 = pd.concat([data_non_blank_condition, merged_data], axis=0)
		imported_data3 = imported_data3[~pd.isna(imported_data3['condition'])]
		
		# ensure condition column is string type
		imported_data3.loc[:, 'condition'] = imported_data3['condition'].astype(str)
		
		# sort data by condition then drug so that numeric variables follow this
		imported_data3.sort_values(by=['condition', 'drugName'], inplace=True)
		imported_data3.reset_index(drop=True, inplace=True)
		
		# get a sorted list of unique drug names
		unique_drug = imported_data3['drugName'].unique()
		
		# get a sorted list of unique conditions
		unique_cond = imported_data3['condition'].unique()
		
		# create dictionaries mapping each unique drug name and condition to a unique number
		drug_name_mapping = {drug_name: i for i, drug_name in enumerate(unique_drug)}
		condition_mapping = {condition: i for i, condition in enumerate(unique_cond)}
		
		# map these numbers to drugName and condition columns
		imported_data3['drugName_num'] = imported_data3['drugName'].map(drug_name_mapping)
		imported_data3['condition_num'] = imported_data3['condition'].map(condition_mapping)
		
		# assign to self.data
		self.data = imported_data3.copy()


	def get_cleaned_data(self):
		return self.data

# Usage
#cleaner = DataCleaner('drugsComTrain_raw.csv')
#train_data = cleaner.get_cleaned_data()

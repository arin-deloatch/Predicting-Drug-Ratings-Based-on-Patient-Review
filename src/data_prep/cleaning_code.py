from data_cleaner import DataCleaner

train_cleaner = DataCleaner('drugsComTrain_raw.csv')
train_data = train_cleaner.get_cleaned_data()


test_cleaner = DataCleaner('drugsComTest_raw.csv')
test_data = test_cleaner.get_cleaned_data()


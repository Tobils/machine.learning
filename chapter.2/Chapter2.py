import pandas as pd
import matplotlib.pyplot as plt

class Housing:
    def __init__(self):
        self.housing = self.__load_housing_data()
        print(self.housing.head())
        print(self.housing.info())
        print(self.housing["ocean_proximity"].value_counts())
        print(self.housing.describe())

        self.__show_histogram()


    def __load_housing_data(self):
        csv_path = "./dataset/housing.csv"
        return pd.read_csv(csv_path)

    def __show_histogram(self):
        self.housing.hist(bins=50,figsize=(20,15))
        plt.show()
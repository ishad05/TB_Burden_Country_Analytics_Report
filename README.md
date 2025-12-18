**Global TB Dataset Cleaning and Preprocessing**


This repository contains a python script to clean and preprocess the Tuberculosis Burden dataset by country, making it ready for analysis and visualization. The cleaned dataset can be used for research, analysis, and plotting.

**Dataset**

**Source file:** TB_Burden_Country.csv

**Source:** World Health Organization (WHO) Global Tuberculosis Database

**Contents:** Global tuberculosis (TB) statistics by country, including incidence, prevalence, mortality, and other indicators

**Purpose:** Prepare the dataset for analysis by handling inconsistencies, missing values, and formatting issues

**Features**
> Normalizes column names by removing spaces, parentheses, and special characters
> Handles missing values
> Converts numerical and categorical data into standard formats
> Prepares the dataset for visualization using libraries like matplotlib and seaborn
> Outputs a cleaned CSV named tb_burden_cleaned.csv


**Getting Started**

**Clone the repository**
```
git clone github.com/ishad05/TB_Burden_Country_Analytics_Report
cd TB_Burden_Country_Analytics_Report
```

**Install dependencies**
```
pip install pandas matplotlib seaborn
```

**Run the script**
```
python TB_cleaning.py
```

Output: Cleaned dataset saved as TB_Burden_Country_CLEANED.csv, visualization using matplotlib and seaborn using histogram, lineplot and barplot

**Requirements**

Python 3.7+
pandas
matplotlib
seaborn

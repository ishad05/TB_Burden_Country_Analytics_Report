import pandas as pd                      # data manipulation
import matplotlib.pyplot as plt          # base plotting
import seaborn as sns                    # statistical visualization


# STEP 1: LOAD THE DATASET
df = pd.read_csv("TB_Burden_Country.csv")    # read WHO TB CSV
print(df.columns.tolist())                   # view raw column names

# STEP 2: DATA CLEANING
df.columns = (
    df.columns
    .str.strip()                          # remove extra spaces
    .str.lower()                          # lowercase for consistency
    .str.replace(r"[()]", "", regex=True) # remove brackets
    .str.replace(",", "", regex=False)    # remove commas
    .str.replace("  ", " ")               # fix double spaces
    .str.replace(" ", "_")                # spaces → underscores
    .str.replace("-", "_")                # hyphens → underscores
)

df['year'] = pd.to_numeric(df['year'], errors='coerce')   # force invalid years → NaN

print(df['estimated_incidence_all_forms_per_100_000_population'])  # inspect key metric

df.isnull().sum().sort_values(ascending=False).head(10)       # identify missing data


# STEP 3: SAVE CLEANED DATA
df.to_csv(
    "TB_Burden_Country_CLEANED.csv",
    index=False                           # exclude index column
)

print("Cleaned dataset saved successfully!")


# STEP 4: EXPLORATORY DATA ANALYSIS (EDA)
df.describe()                             # statistical summary
df.info()                                 # data types & nulls

df['estimated_incidence_all_forms_per_100_000_population'].hist()  # distribution


# STEP 5: GROUPED ANALYSIS
df.groupby('region')['estimated_incidence_all_forms_per_100_000_population'].mean() # regional averages

df[df['country_or_territory_name'] == 'India'].plot(x='year',y='estimated_incidence_all_forms_per_100_000_population')                                        
# India trend (quick plot)



# STEP 6: VISUALIZATION (ALL TOGETHER)
india_data = df[df['country_or_territory_name'] == 'India']

fig, axes = plt.subplots(
    3, 1,                   # 3 plots, 1 column
    figsize=(10, 14)        # fits most screens
)

# 1️⃣ Histogram
axes[0].hist(
    df['estimated_incidence_all_forms_per_100_000_population'].dropna()
)
axes[0].set_title("Distribution of TB Incidence")
axes[0].set_xlabel("Incidence per 100,000")
axes[0].set_ylabel("Frequency")

# 2️⃣ India trend
sns.lineplot(
    data=india_data,
    x='year',
    y='estimated_incidence_all_forms_per_100_000_population',
    ax=axes[1]
)
axes[1].set_title("TB Incidence Trend in India")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Incidence per 100,000")

# 3️⃣ Region comparison
region_avg = df.groupby('region')[
    'estimated_incidence_all_forms_per_100_000_population'
].mean().reset_index()

sns.barplot(
    data=region_avg,
    y='region',   # horizontal bars = NO cutoff
    x='estimated_incidence_all_forms_per_100_000_population',
    ax=axes[2]
)
axes[2].set_title("Average TB Incidence by Region")
axes[2].set_xlabel("Incidence per 100,000")
axes[2].set_ylabel("Region")

plt.tight_layout()
plt.show()
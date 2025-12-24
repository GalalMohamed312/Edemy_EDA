
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


uber_df = pd.read_csv('UberDataset.csv')

# data profiling and check  nulls
print("view top 5 rows in table", uber_df.head())
print("Information about columns", uber_df.info())

print("check unique values", uber_df.nunique())
print("Number of nulls before clean", uber_df.isnull().sum())

# Data cleaning and remove nulls
uber_df['PURPOSE'].fillna('Unavailable', inplace=True)
uber_df.dropna(subset=['STOP', 'START', 'CATEGORY', 'END_DATE', 'START_DATE'], inplace=True)

print("Total Number of nulls after clean", uber_df.isnull().sum().sum())

# EDA and visualization
purpose_df = uber_df[uber_df['PURPOSE'] != 'Unavailable'].copy()

# get top 5 purposes by count
top5_purpose = (
    purpose_df['PURPOSE']
        .value_counts()
        .head(5)
        .index
)

plt.figure(figsize=(10, 5))
sns.countplot(
    data=purpose_df,
    x="PURPOSE",
    order=top5_purpose,
    palette="viridis"
)
plt.title("top 5 purposes")
plt.xlabel("Purpose")
plt.ylabel("Total Count")
plt.show()

print("Q1: most common purposes for uber trips?")
print("Most common purposes:", uber_df['PURPOSE'].value_counts())

# convert start and end date to  datetime
uber_df['START_DATE'] = pd.to_datetime(uber_df['START_DATE'])
uber_df['END_DATE'] = pd.to_datetime(uber_df['END_DATE'])

# add hour of day column
uber_df['hour_of_day'] = uber_df['START_DATE'].dt.hour


# divide time of day to segments
def time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'


uber_df['time_of_day'] = uber_df['hour_of_day'].apply(time_of_day)

# ----------------------------
#  mileage trends by purpose and time of day
mileage_trends = uber_df.groupby(['PURPOSE', 'time_of_day'])['MILES'].mean().unstack()
print("Q2:Average trip mileage by purpose and time of day:")
print(mileage_trends)

# Q2 mileage trends by purpose and time of day?
mileage_trends.plot(kind='bar', figsize=(12, 7))
plt.title("Average miles for every purpose and time of day")
plt.ylabel("Average Miles")
plt.xlabel("Purpose")
plt.xticks(rotation=45)
plt.legend(title='Time of Day')
plt.show()

# ----------------------------
# Differences between business and personal miles trips
category_stats = uber_df.groupby('CATEGORY')['MILES'].describe()
print("\n ///////////////////////////////////\n Q3: Trip length statistics by category:")
print(category_stats)

# رسم Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='CATEGORY', y='MILES', data=uber_df, palette="Set2")
plt.title("Differences between business and personal miles trips ")
plt.ylabel("Miles")
plt.show()

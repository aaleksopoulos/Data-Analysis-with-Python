import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex']=='Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df['education']=='Bachelors'])/len(df)*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education'].isin(advanced_education))]
    lower_education = df[~(df['education'].isin(advanced_education))]
    
    
    # percentage with salary >50K
    higher_education_rich = round(len(higher_education[higher_education['salary']=='>50K'])/len(higher_education)*100, 1)
    lower_education_rich = round(len(lower_education[lower_education['salary']=='>50K'])/len(lower_education)*100, 1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df['hours-per-week']==min_work_hours)]

    rich_percentage = round(len(num_min_workers[num_min_workers['salary']=='>50K'])/len(num_min_workers)*100, 1)

    # What country has the highest percentage of people that earn >50K?
    #first we will create a series object calculating the number of people each country of the whole dataframe has
    grouped_countries = df.groupby(['native-country'])['salary'].count()
    #then we will see how many of them are "rich" aka are paid more than 50k
    rich_grouped_countries = df[df['salary']=='>50K'].groupby(['native-country'])['salary'].count().rename('rich_salary')
    
    #we will combine those 2 in 1 dataframe, will calculate the percentages and sort by 
    df2 = pd.concat([grouped_countries, rich_grouped_countries], axis=1)
    df2['percentage'] = df2['rich_salary']/df2['salary']
    df2 = df2.sort_values(by=['percentage'], ascending=False)

    highest_earning_country = df2.iloc[0].name
    
    highest_earning_country_percentage = round(df2.iloc[0].percentage*100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    #first we will create a pandas series object, counting how many people each occupation has and we will sort it
    india_series = df[(df['native-country']=='India') & (df['salary']!='<=50K')].groupby('occupation')['occupation'].count().sort_values(ascending=False)
    
    #the requested value is the first index
    top_IN_occupation = india_series.index[0]


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
import numpy as np
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    demo_dat = pd.read_csv('adult.data.csv')



    


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race=pd.Series(demo_dat['race'].value_counts())

    # What is the average age of men?
    
    mean_men=demo_dat.loc[demo_dat["sex"] == "Male", "age"].mean()
    average_age_men=mean_men.round(1)

    # What is the percentage of people who have a Bachelor's degree?
    

    count_bach=(demo_dat["education"] =="Bachelors").sum()



    ed_nums=(demo_dat["education"]).value_counts().sum()


    percentage_bachelors =round(count_bach/ed_nums*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = ((demo_dat["education"] == "Bachelors") | (demo_dat["education"] == "Masters") | (demo_dat["education"] == "Doctorate")).sum()
    lower_education = (~((demo_dat["education"] == "Bachelors") |(demo_dat["education"] == "Masters") |(demo_dat["education"] == "Doctorate"))).sum()


    


    
    # percentage with salary >50K

    count_advance_50 = (((demo_dat["education"] == "Bachelors") |(demo_dat["education"] == "Masters") |(demo_dat["education"] == "Doctorate"))&(demo_dat["salary"] == ">50K")).sum()
    higher_education_rich =round(count_advance_50/higher_education*100,1)


    count_non_advance_50 = (~((demo_dat["education"] == "Bachelors") |(demo_dat["education"] == "Masters") |(demo_dat["education"] == "Doctorate"))&(demo_dat["salary"] == ">50K")).sum()


    lower_education_rich=round(count_non_advance_50/lower_education*100,1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    

    hours_per_week=demo_dat["hours-per-week"].unique()
    min_work_hours=hours_per_week.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    num_min_workers=(demo_dat["hours-per-week"]==1).sum()


    min_hours_pips_50=((demo_dat["hours-per-week"]==1) & (demo_dat["salary"] == ">50K")).sum()




    rich_percentage=round(min_hours_pips_50/num_min_workers*100,1)
    
    
    

    # What country has the highest percentage of people that earn >50K?
    


    total_per_country = demo_dat.groupby("native-country").size()

    high_earners = (demo_dat[demo_dat["salary"] == ">50K"].groupby("native-country").size())

    percentage = (high_earners / total_per_country) * 100

    top_country = percentage.idxmax()
    top_percentage = percentage.max()

    highest_earning_country = top_country
    highest_earning_country_percentage = top_percentage.round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    


    demo_dat["occupation"] 

    india_50k_filter=((demo_dat["native-country"] == "India") & (demo_dat["salary"] == ">50K"))

    filter_occ_ind=demo_dat.loc[india_50k_filter, "occupation"].value_counts()


    most_common_occ = demo_dat.loc[india_50k_filter, "occupation"].value_counts().idxmax()

    top_IN_occupation = most_common_occ

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race) 
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
        'race_count': race,
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

#Homework 2
import pandas as pd

# Load the StackOverflow dataset
df = pd.read_csv('task\\stackoverflow_qa.csv', parse_dates=['creationdate'])

# 1. Questions created before 2014
before_2014 = df[df['creationdate'] < '2014-01-01']

# 2. Questions with score > 50
score_gt_50 = df[df['score'] > 50]

# 3. Questions with score between 50 and 100
score_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]

# 4. Questions answered by Scott Boston
answered_by_scott = df[df['ans_name'] == 'Scott Boston']

# 5. Questions answered by 5 specific users
users_list = ['Scott Boston', 'unutbu', 'Jon Skeet', 'Mike Pennington', 'DarkAnt']
answered_by_5_users = df[df['ans_name'].isin(users_list)]

# 6. Between Mar 2014 and Oct 2014, answered by Unutbu, score < 5
unutbu_2014 = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'unutbu') &
    (df['score'] < 5)
]

# 7. Score between 5 and 10 OR viewcount > 10,000
score_or_views = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) |
    (df['viewcount'] > 10000)
]

# 8. Questions NOT answered by Scott Boston
not_by_scott = df[df['ans_name'] != 'Scott Boston']

# OPTIONAL: To see all results
print("Before 2014:\n", before_2014)
print("Score > 50:\n", score_gt_50)
print("Score 50-100:\n", score_50_100)
print("Answered by Scott Boston:\n", answered_by_scott)
print("Answered by 5 Users:\n", answered_by_5_users)
print("Unutbu Mar-Oct 2014 Score<5:\n", unutbu_2014)
print("Score 5-10 OR Views>10k:\n", score_or_views)
print("Not by Scott Boston:\n", not_by_scott)


#homework 3
import pandas as pd

# Load the Titanic dataset
titanic_df = pd.read_csv("task\\titanic.csv")

# 1. Female Passengers in Class 1, Ages 20-30
female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]

# 2. Passengers Who Paid > $100
paid_over_100 = titanic_df[titanic_df['Fare'] > 100]

# 3. Survived & Alone
survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]

# 4. Embarked from 'C' & Paid > $50
embarked_c_over_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]

# 5. Had both siblings/spouses AND parents/children aboard
sibsp_and_parch = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]

# 6. Age <= 15 & Did Not Survive
age_15_no_survive = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]

# 7. Known Cabin & Fare > $200
cabin_over_200 = titanic_df[
    titanic_df['Cabin'].notna() &
    (titanic_df['Fare'] > 200)
]

# 8. Odd Passenger IDs
odd_passenger_ids = titanic_df[titanic_df['PassengerId'] % 2 == 1]

# 9. Unique Ticket Numbers
ticket_counts = titanic_df['Ticket'].value_counts()
unique_ticket_df = titanic_df[titanic_df['Ticket'].isin(ticket_counts[ticket_counts == 1].index)]

# 10. 'Miss' in Name & Class 1
miss_class1 = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Sex'] == 'female')
]

# OPTIONAL: Print results
print("Female Class 1 Age 20-30:\n", female_class1_20_30)
print("Paid > 100:\n", paid_over_100)
print("Survived Alone:\n", survived_alone)
print("Embarked C & Paid > 50:\n", embarked_c_over_50)
print("SibSp AND Parch:\n", sibsp_and_parch)
print("Age <= 15 & No Survive:\n", age_15_no_survive)
print("Cabin & Fare > 200:\n", cabin_over_200)
print("Odd Passenger IDs:\n", odd_passenger_ids)
print("Unique Ticket:\n", unique_ticket_df)
print("'Miss' in Name & Class 1:\n", miss_class1)

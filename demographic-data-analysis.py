#!/usr/bin/env python
# coding: utf-8

# In[202]:


import pandas as pd


# In[203]:


# Analyzing the race column


# In[205]:


df = pd.read_csv('adult.data.csv')
df['race'].count()


# In[206]:


df['race'].unique()


# In[207]:


wp = df['race'] == 'White'
print('Number of white people:- ',wp.sum())


# In[212]:


bp = df['race'] == 'Black'
print('Number of black people:- ',bp.sum())


# In[213]:


api = df['race'] == 'Asian-Pac-Islander'
print('Number of Asian-Pac-Islander people:- ',api.sum())


# In[214]:


aie = df['race'] == 'Amer-Indian-Eskimo'
print('Number of Amer-Indian-Eskimo people:- ',aie.sum())


# In[215]:


other = df['race'] == 'Other'
print('Number of other people:- ',other.sum())


# In[216]:


df['race'].value_counts()


# In[217]:


# bar chart for race 


# In[220]:


import matplotlib.pyplot as plt

race = ['White', 'Black', 'Asian-pacific-Islander', 'Amer-Indian-Eskimo', 'Other']
people = [wp.sum(),bp.sum(),api.sum(),aie.sum(),other.sum()]

plt.bar(race,people)
plt.xticks(rotation=35)
plt.xlabel('(Race)')
plt.ylabel('(Number of People)')
plt.title('(Analysis of the race column)')
plt.show()


# In[222]:


# What is the average age of men?


# In[223]:


avg_age = df.loc[df['sex'] =='Male', 'age']
print("The average age of men:- ",avg_age.mean())


# In[224]:


df['age'].mean()


# In[ ]:





# In[229]:


#What is the percentage of people who have a Bachelor's degree?


# In[231]:


bchl = df['education'] == 'Bachelors'
bchl_total = bchl.sum()
bchl_total


# In[232]:


df['education'].value_counts()


# In[233]:


lenght_edu = len(df['education'])


# In[234]:


print("The percentage of people who have a Bachelor's degree:- ",(bchl_total*100)/lenght_edu)


# In[235]:


'HS-grad', '11th', '9th', 'Some-college','Assoc-acdm', 'Assoc-voc', '7th-8th', 'Prof-school','5th-6th', '10th', '1st-4th', 'Preschool', '12th'


# In[239]:


# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?


# In[241]:


df['education'].unique()


# In[245]:


df['salary'].unique()


# In[246]:


df[['education','salary']].head(10)


# In[247]:


filtr = df.loc[(df['education'] == 'Bachelors')|(df['education'] =='Masters')|(df['education'] =='Doctorate') , 'salary'  ] == '>50K'
filtr.count()


# In[248]:


adv = (f"Number of people with advanced education (Bachelors, Masters, or Doctorate) making more than 50K :- {filtr.sum()}")
print(adv)


# In[251]:


total_edu = len(df['education'])
total_edu


# In[252]:


print(f"Percentage of people with advanced education (Bachelors, Masters or Doctorate) make more than 50K :- {((filtr.sum())*100)/filtr.count()}")


# In[255]:


# pie chart


# In[259]:


sorting1 = df.loc[(df['education'] == 'Bachelors'), 'salary'  ] == '>50K'
perc1 = (sorting1.sum()*100)/filtr.count()


# In[261]:


sorting2 = df.loc[(df['education'] == 'Masters'), 'salary'  ] == '>50K'
perc2 = (sorting2.sum()*100)/filtr.count()


# In[262]:


sorting3 = df.loc[(df['education'] == 'Doctorate'), 'salary'  ] == '>50K'
perc3 = (sorting3.sum()*100)/filtr.count()


# In[263]:


perc1,perc2,perc3,perc4


# In[264]:


sort = sorting1.sum()+sorting2.sum()+sorting3.sum()


# In[265]:


others = (filtr.count())-(sort)
perc4 = (others*100)/filtr.count()


# In[268]:


import matplotlib.pyplot as plt
percentage = [perc1,perc2,perc3,perc4]
edu = ["Bachelors","Masters","Doctorate","Others"]
plt.pie(percentage, labels=edu, autopct='%1.1f%%',shadow=True)
plt.title('(Percentage of people with advanced education making >50K')
plt.show()


# In[ ]:





# In[271]:


# What percentage of people without advanced education make more than 50K ?


# In[276]:


len(df['education'])


# In[278]:


grt_50k = df.loc[df['salary'] == '>50K' , 'education']
print("Number of people making more than 50K :- ",len(grt_50k))


# In[279]:


#w_adv = int(grt_50k) - int(adv)
print("People without advanced education making more than 50K :- ",(7841-3486))


# In[ ]:





# In[282]:


# What is the minimum number of hours a person works per week?


# In[285]:


df['hours-per-week'].unique()


# In[287]:


min_hr = df['hours-per-week']
print(f"Minimum number of hours a person works is {min_hr.min()}")
print(f"Maximum number of hours a person works is {min_hr.max()}")


# In[ ]:





# In[292]:


# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?


# In[293]:


hr_50k = df.loc[df['hours-per-week']== min_hr.min() , 'salary'] == '>50K'


# In[294]:


hr_len = len(df['hours-per-week']) 


# In[295]:


perc = ((hr_50k.sum())*100) / hr_len


# In[296]:


print(f"Percentage of people who work the mininmum number of hour per week and have a salary of more than 50k is {perc.round(3)} %")


# In[ ]:





# In[298]:


# What country has the highest percentage of people that earn >50K and what is that percentage?


# In[299]:


df['native-country'].unique()


# In[300]:


df['native-country'].value_counts()


# In[301]:


country_50k = df.loc[df['salary'] == '>50K' , 'native-country']
max_count = country_50k.value_counts()
max_count


# In[304]:


max_count.count()


# In[305]:


max_count.index[0], max_count.tolist()[0]


# In[310]:


print(f"Country that has maximum number of people with salary more than 50k is {max_count.index[0]} with {max_count.max()} people")


# In[314]:


print(f"Country that has maximum number of people with salary more than 50k is {max_count.index[0]} with {max_count.tolist()[0]} people")


# In[315]:


len(country_50k)


# In[316]:


print(f"Country that has the highest percentage of people that earn >50K is {max_count.index[0]} and percentage is {(max_count.max()*100)/len(country_50k)} (for only >50K salary) and {(max_count.max()*100)/len(df['native-country'])} (for both >50k and <=50K)")


# In[ ]:





# In[320]:


# Identify the most popular occupation for those who earn >50K in India.


# In[322]:


df.columns


# In[324]:


df['occupation']


# In[325]:


occ_filtr = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K') , 'occupation']
occ_filtr


# In[326]:


occ_filtr.unique()


# In[327]:


popu_occ = occ_filtr.value_counts()
popu_occ


# In[328]:


print("The most popular occupation in India in which people are making more than 50K is",popu_occ.index[0])


# In[329]:


popu_occ.index[:],popu_occ.tolist()[:]


# In[330]:


import matplotlib.pyplot as plt
professions = (popu_occ.index[:])
values = (popu_occ.tolist()[:])
plt.bar(professions,values,color='green')
plt.xlabel('(Professions)')
plt.xticks(rotation=35)
plt.ylabel('(No. of people making more than 50k)')
plt.title('Most popular profession in India')
plt.show()


# In[331]:


popu_occ.tolist()[:]


# In[ ]:





# In[333]:


print('CONCLUSION:-')

print("-"*100)

# Analyzing the race column
print('1)Number of white people:- ',wp.sum())
print('Number of black people:- ',bp.sum())
print('Number of Asian-Pac-Islander people:- ',api.sum())
print('Number of Amer-Indian-Eskimo people:- ',aie.sum())
print('Number of other people:- ',other.sum())

print("-"*100)

# What is the average age of men
print("2)The average age of men:- ",avg_age.mean())

print("-"*100)

# What is the percentage of people who have a Bachelor's degree?
print("3)The percentage of people who have a Bachelor's degree:- ",((bchl_total*100)/lenght_edu).round(3))

print("-"*100)

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
print(f"4)Percentage of people with advanced education (Bachelors, Masters or Doctorate) make more than 50K :- {((filtr.sum()*100)/(filtr.count())).round(3)}")

print("-"*100)

# What percentage of people without advanced education make more than 50K ?
print("5)People without advanced education making more than 50K :- ",(7841-3486))

print("-"*100)

# What is the minimum and maximum number of hours a person works per week?
print(f"6)Minimum number of hours a person works is {min_hr.min()}")
print(f"Maximum number of hours a person works is {min_hr.max()}")

print("-"*100)

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
print(f"7)Percentage of people who work the mininmum number of hour per week and have a salary of more than 50k is {perc.round(3)} %")

print("-"*100)

# What country has the highest percentage of people that earn >50K and what is that percentage?
print(f"8)Country that has the highest percentage of people that earn >50K is {max_count.index[0]} and percentage is {(max_count.max()*100)/len(country_50k)} (for only >50K salary) and {((max_count.max()*100)/len(df['native-country']))} (for both >50k and <=50K)")

print("-"*100)

# Identify the most popular occupation for those who earn >50K in India.
print("9)The most popular occupation in India in which people are making more than 50K is",popu_occ.index[0])

print("-"*100)


# In[ ]:





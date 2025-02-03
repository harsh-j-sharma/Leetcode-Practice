#2877. create a DataFrame from the list
pd.DataFrame(data=student_data,columns=['student_id','age'])

#2878. Get the size of the DataFrame
list(players.shape)

#2879. Display the first three rows
employees.head(3)

#2880. select the data
students[students['student_id'] == 101].iloc[:,1:]

#2881. Create New column
employees['bonus'] = employee['salary']*2
employees.assign(bonus= lambda x:x['salary']*2)

#2882. Drop duplicates rows
customers.drop_duplicates(subset=['email'],implace=True)

#2883 Drop missing data
customers.dropna(subset=['name'],inplace=True)

#2884. Modify column
employees['salary'] = employees['salary']*2

#2885. rename column
students = students.rename(
  columns={
    'id': 'student_id',
    'first': 'first_name',
    'last': 'last_name',
    'age': 'age_in_years'},inplace=True)
  }
)

#2886. change the data type
students['grade'] = students['grade'].astype(int)

#2887 fill missing data
products['quantity'] = products['quantity'].fillna(0)

#2888. Reshape the data  : concatenate
pd.concat([df1,df2],axis=0)

#2889 Reshape data : Pivot
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(
        index='month',
        columns='city',
        values='temperature'
    )

#2890. Reshape Data: Melt
report.melt(id_vars=['product'],value_vars=['quarter_1','quarter_2','quarter_3','quarter_4']
    ,var_name='quarter',value_name='sales')

##2891 Method chaning
animals[animals['weight'] > 100].sort_values(['weight'],ascending=False)[['name']]




import pandas as pd 


x=pd.read_csv('adult.data.csv')

# def Demographic_Data_Calculator ():

#     v=x['race'].value_counts()


#     s=x[x['sex'] == 'Male']
#     st=s['age'].mean()
#     print(st)

#     l=x[x['education'] == 'Bachelors']
#     vt=x['education']
#     ds=len(l)/len(vt) * 100
#     print(ds)

 
#     Advanced_Edu=len(x[x['education'].isin(['Bachelors','Masters','Doctorate'])])
#     UnAdvanced_Edu=len(x[~x['education'].isin(['Bachelors','Masters','Doctorate'])])
#     Advanced_Edu=Advanced_Edu[type:object]
#     amt=len(Advanced_Edu[Advanced_Edu.salary=='>50K'])
#     unamt=len(UnAdvanced_Edu[UnAdvanced_Edu.salary=='>50K'])
#     cv=round(amt/Advanced_Edu*100,1)
#     cd=round(unamt/UnAdvanced_Edu*100,1)
#     print(cv)
#     print(cd)
#     print(sa)

bc=x['hours-per-week'].min()


#     dsf=

#       
c=x['salary'].unique()
print(bc)




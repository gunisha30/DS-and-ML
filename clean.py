import pandas as pd
import re

df=pd.read_csv("C:/Users/hp1/Documents/sih/datascientist2.csv")
df.drop(columns=['Sponsored'])

#sal=list(df['Salary'])
#x=re.search("^â‚",sal)

def remove_tags(data):
    yr = re.compile('a year$')
    cleantext = re.sub(rup, '', data)
    return cleantext
#df['Salary'] = df['Salary'].apply(lambda x: remove_tags(x) if x!='None' else x)

st=df.iloc[1][3]
#stnew=st.replace('â','')
#print(type(st[0]))

st=re.sub(r'a year$',"",st)
l=st.split('-')
for i in range(0,len(l)):
    l[i]=re.sub("\D", "",l[i])
print(l)
s="-".join(l)
print(s)

import pandas as pd
import numpy as np
#na=['NEW', '-']


missing_val = ["NEW","-","None","Not rated","Opening","opening",np.nan]
df = pd.read_csv("C:/Users/hp1/Documents/regex project/integrated cities/kota1.csv",na_values = missing_val)


#df=pd.read_csv("C:/Users/hp1/Documents/regex project/integrated cities/kota1.csv")
df1=df.copy()

df.columns = map(str.lower , df.columns)
#c=df['rating_type'].value_counts()
#print(c)
#df.info()
#res=df[df['CUSINE TYPE']=='Casual Dining']#'RATING']]
#print(res[0][0])

#print(df['rating_type'].isnull().sum())
df2=df[df['rating']
    

    
#col1=df["RATING"]
#print(df.dtypes)

#removing the rows with cuisine as none
#df.drop(df[df["CUSINE TYPE"]=="none"].index, inplace= True)
#print(df.iloc[[25]])

#calculate mean of column

#x=df["RATING"].mean(skipna='True')

#df.loc[:,(df=="NEW") and (df=="-")]=np.nan 

#df.replace('-','NaN')
#df.replace('CafÃ©','Cafe')
#print(df.iloc[[18][0]])

#df.astype({'RATING':'int64'})
#df['RATING'].astype('float')
#df.to_csv('C:/Users/hp1/Documents/regex project/integrated cities/kotatest.csv')

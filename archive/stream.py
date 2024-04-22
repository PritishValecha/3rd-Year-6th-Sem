import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.write("""
# My first app
Hello *World!*
""")

df = pd.read_csv("covid_vaccine_statewise.csv")
# st.dataframe(df)
# st.line_chart(df, x='State', y='Total Doses Administered')
df1 = pd.read_csv("StatewiseTestingDetails.csv")

shantanu = df
shantanu = shantanu[['Updated On', 'State', 'Total Doses Administered', 'First Dose Administered', 'Second Dose Administered']]
shantanu = shantanu.dropna(subset=['Total Doses Administered','First Dose Administered', 'Second Dose Administered'], axis=0, how='all')
# fig2, q = plt.subplots()
# q.bar(x=shantanu['State'], color)
# q.legend(labels=list(dic1.keys()), loc="lower left", bbox_to_anchor=(1,0))
# st.pyplot(fig)


aditi = df[df['State'] != 'India']
x=aditi.iloc[:,1:5]
x.dropna(how="any")
#Bar Plot
vaccination = x.groupby('State')['Total Doses Administered'].sum().reset_index()
vaccination_sort = vaccination.sort_values(by='Total Doses Administered', ascending=False)

fig1, z = plt.subplots()
# z.figure(figsize=(10, 6))
z.bar(vaccination_sort['State'], vaccination_sort['Total Doses Administered'], color='lightblue')
plt.xlabel('States')
plt.ylabel('Total Doses Administered')
plt.title('Total COVID-19 Vaccination Doses Administered per State')
plt.xticks(rotation=90) 
# plt.tight_layout()
# z.show()
st.pyplot(fig1)



prasad = df[['State', 'Total Doses Administered', 'Male (Doses Administered)', 'Female (Doses Administered)']]
prasad = prasad.dropna(subset=['Total Doses Administered','Male (Doses Administered)', 'Female (Doses Administered)'], axis=0, how='any')
state = prasad['State'].unique()
state = state.tolist()
state.pop(0)
prasad_dic_male ={}
prasad_dic_female ={}
bw = 0.5
bw1 = np.arange(len(state))
bw2 = [x + bw for x in bw1]
for i in state:
    prasad_dic_male[i] = max(prasad[prasad['State']==i]['Male (Doses Administered)'])
    prasad_dic_female[i] = max(prasad[prasad['State']==i]['Female (Doses Administered)'])
fig2, w = plt.subplots()
w.bar(bw1, list(prasad_dic_male.values()), color='b', width=bw, label='Male')
w.bar(bw2, list(prasad_dic_female.values()), color='pink', width=bw, label='Female')
plt.xlabel('States') 
plt.ylabel('Vaccinated') 
plt.xticks([r + bw for r in range(len(state))], state)
plt.xticks(rotation=90)
w.legend()
plt.title('Male-Female Distribution')
st.pyplot(fig2)

data1 = df
data1 = data1.iloc[:,:3]
# data1

data2 = df1
data2 = data2.iloc[:,1:]

data1 = data1.dropna(subset='Total Doses Administered', axis=0)
data2 = data2.dropna(subset=['Negative', 'Positive'], axis=0, how='all')

# st.bar_chart(data1, x='State', y='Total Doses Administered')

states = data1['State'].unique()

dic = {}
for i in states:
    dic[i] = max(data1[data1['State']==i]['Total Doses Administered'])

# print(dic)

states1 = data2['State'].unique()

dic1 = {}
for i in states1:
    dic1[i] = max(data2[data2['State']==i]['TotalSamples'])

# print(dic1)
    
# ind = dic.pop('India')

dic1_keys = list(dic1.keys())
dic1_keys.sort()

sorted_dic = {i: dic[i] for i in dic1_keys}
sorted_dic1 = {i: dic1[i] for i in dic1_keys}

data2 = data2.replace(' ', np.nan)

data2['Positive'] = pd.to_numeric(data2['Positive'])
data2['Negative'] = pd.to_numeric(data2['Negative'])

for i in range(9073):
    if(str(data2.iloc[i,3])=='nan' or (data2.iloc[i,3]==' ')):
        data2.iloc[i,3] = data2.iloc[i,1] - data2.iloc[i,2]
    if((str(data2.iloc[i,2])=='nan') or (data2.iloc[i,2]==' ')):
        data2.iloc[i,2] = data2.iloc[i,1] - data2.iloc[i,3]

# data2

column1 = list(sorted_dic.keys())
column2 = list(sorted_dic.values())
# column3 = list(dic1.keys())
column4 = list(sorted_dic1.values())

fig, x = plt.subplots()
x.pie(x=list(dic1.values()))
x.legend(labels=list(dic1.keys()), loc="lower left", bbox_to_anchor=(1,0))
st.pyplot(fig)
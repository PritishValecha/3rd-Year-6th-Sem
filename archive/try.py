import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Covid Vaccine Status",
    page_icon="💉",
    # layout="wide",
    initial_sidebar_state="expanded"
)

alt.themes.enable("dark")

df = pd.read_csv("covid_vaccine_statewise.csv")
prasad = df[['State', 'Total Doses Administered', 'Male (Doses Administered)', 'Female (Doses Administered)']]
prasad = prasad.dropna(subset=['Total Doses Administered','Male (Doses Administered)', 'Female (Doses Administered)'], axis=0, how='any')
state = prasad['State'].unique()
state = state.tolist()
state.pop(0)
prasad_dic_male ={}
prasad_dic_female ={}
for i in state:
    prasad_dic_male[i] = max(prasad[prasad['State']==i]['Male (Doses Administered)'])
    prasad_dic_female[i] = max(prasad[prasad['State']==i]['Female (Doses Administered)'])
column1 = list(prasad_dic_male.keys())
column2 = list(prasad_dic_male.values())
column3 = list(prasad_dic_female.values())
data = {'State':column1, 'male':column2, 'female':column3}
df1 = pd.DataFrame(data)

shantanu = df
shantanu = shantanu[['Updated On', 'State', 'Total Doses Administered', 'First Dose Administered', 'Second Dose Administered']]
shantanu = shantanu.dropna(subset=['Total Doses Administered','First Dose Administered', 'Second Dose Administered'], axis=0, how='all')
shantanu['Updated On'] = pd.to_datetime(shantanu['Updated On'])

with st.sidebar:
    st.title('Covid Vaccine Dashboard')

    state_list = state
    selected_state = st.selectbox('Select a state', state_list, index=len(state_list)-1)
    df1_selected_state = df1[df1['State']==selected_state]

def plot_male_female(state):
    male = int(df1[df1['State']==state]['male'])
    female = int(df1[df1['State']==state]['female'])
    plot = (male,female)
    fig,x = plt.subplots()
    plt.title('Male/Female vaccination distribution in '+state)
    x.pie(x=plot, startangle=90, colors=['b', 'pink'], labels=['Male', 'Female'])
    plt.tight_layout()
    st.pyplot(fig)
    # return x

def first_second_dose(state):
    df = shantanu[shantanu['State']==state]
    dates = list(df['Updated On'])
    dates = dates[::15]
    total = list(df['Total Doses Administered'])
    total = total[::15]
    first = list(df['First Dose Administered'])
    first = first[::15]
    second = list(df['Second Dose Administered'])
    second = second[::15]
    bw = 0.30
    bw1 = np.arange(len(dates))
    bw2 = [x + bw for x in bw1]
    bw3 = [x + bw for x in bw2]
    fig, x = plt.subplots()
    x.bar(bw1, total, width=bw, label='Total', color='orange', edgecolor='black')
    x.bar(bw2, first, width=bw, label='First Dose', color='red', edgecolor='black')
    x.bar(bw3, second, width=bw, label='Second Dose', color='yellow', edgecolor='black')
    plt.xlabel('Dates') 
    plt.ylabel('Doses') 
    plt.xticks([r + bw for r in range(len(dates))], dates)
    plt.xticks(rotation=90)
    plt.title('Doses Administered in '+state)
    plt.legend()
    st.pyplot(fig)
    # plt.show()

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

plot_male_female(selected_state)
# st.pyplot(q)
first_second_dose(selected_state)
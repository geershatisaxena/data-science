import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("This is the Dashboard Page")

df = sns.load_dataset("titanic")
st.dataframe(df)
#gender filter 
gender = st.sidebar.multiselect('Gender',
                                       options=df['sex'].unique())
#pclass filter
pclass = st.sidebar.multiselect('Pclass',
                                       options=df['pclass'].unique()
                                       deafult=df['pclass'].unique())
filtered_df=df[(df['sex'].isin(gender))] #to check whether the gender has data of sex column of df

fig7 = px.sunburst(df, path=['class', 'sex', 'survived'], title='Survival by Class and Gender',template='plotly_dark',color='age')

st.plotly_chart(fig7)

fig8 = px.treemap(df, path=['class', 'survived'], values='fare', title='Survival by Class',color='age',template='plotly_dark')
st.plotly_chart(fig8)

fig5 = px.box(df, x='class', y='fare', title='Fare Distribution by Class')
st.plotly_chart(fig5)

fig3 = px.scatter(df, x='age', y='fare', size='sibsp', color='survived', 
                  title='Age vs Fare with Siblings/Spouses Count', 
                  labels={'sibsp': 'Siblings/Spouses Aboard'})
st.plotly_chart(fig3)

a=px.sunburst(df,path=['pclass','sex','survived'],values='age',
            title='Survived by class and gender',width=500,height=500,
            template='plotly_dark',color='age',color_continuous_scale='plasma')
st.plotly_chart(a)

b=px.scatter(df,x='age',y='fare',color='survived',title='Age vs Fare by Survival',template='plotly_dark')
st.plotly_chart(b)

survived_counts = filtered_df['survived'].value_counts()
tf=px.pie(names=survived_counts.index, values=survived_counts.values,
       title='Survival Rate',template='plotly_dark',
       width=500,height=500)
st.plotly_chart(tf)

fig4 = px.scatter(df, x='age', y='fare', size='parch', color='survived', 
                  title='Age vs Fare with Parents/Children Count', 
                  labels={'parch': 'Parents/Children Aboard'})
st.plotly_chart(fig4)
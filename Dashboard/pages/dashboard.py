import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("This is the Dashboard Page")

df = sns.load_dataset("titanic")
st.dataframe(df)

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



import pandas as pd
import streamlit as st
import plotly.express as px

st.header("display data frame")

df = pd.DataFrame({
    'name':['alice','michael','andy'],
    'age':[20, 16, 18],
    'city':['new york', 'miami','london']
})
st.write(df)

books_df = pd.read_csv('lesson18/bestseller.csv')
st.title("best seilling books in the amazon store")
st.write("this app shows the best selling books of the amazon store")

st.subheader("summery statics")
quantity = books_df.shape[0]
title = books_df['Name'].nunique()
rating = books_df['User Rating'].mean()
price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("totalbooks", quantity)
col2.metric("titles", title)
col3.metric("Average Rating", f"{rating:.2f}")
col4.metric("Average Price", f"${price:.2f}")

st.subheader("dataset preview")
st.write(books_df.head())


col1,col2 = st.columns(2)
with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)


st.subheader("Genre Distribution")

fig = px.pie(books_df, name='Genre', title='Most Liked Genre (2009 - 2022)', color='Genre', color_discrete_sequence=px.colors.sequential.Plasma)

st.plotly_chart(fig)



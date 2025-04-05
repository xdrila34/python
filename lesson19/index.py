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

st.sidebar.header("Add New Book Data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author Name")
    new_user_rating = st.slider("User Rating", 0.5,5.0, 0.0, 0.1)
    new_review = st.number_input('Review', min_value=0, step=1)
    new_price = st.number_input('Price', min_value=0, step=1)
    new_year = st.number_input('Year', min_value=2009, max_value=2022, step=1)
    new_genre = st.selectbox("Genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="add book")

if submit_button:
    new_data = {
        'Name': new_name,
        'Author': new_author,
        'UserRating': new_user_rating,
        'Review': new_review,
        'Price': new_price,
        'Year': new_year,
        'Genre': new_genre
    }
    books_df = pd.concat([pd.DataFrame(new_data, index=[0]), books_df], ignore_index = True)
    books_df.to_csv('bestseller.csv', index=False)
    st.sidebar.success("Libri u shtua me sukses")

st.sidebar.header("Filter Options")
select_author = st.sidebar.selectbox("Select An Author",['All'] + list(books_df['Author'].unique()))
select_Year = st.sidebar.selectbox("Select A Year",['All'] + list(books_df['Year'].unique()))
select_genre = st.sidebar.selectbox("Select A Genre",['All'] + list(books_df['Genre'].unique()))
min_rating = st.sidebar.slider("Minimum User Rating", 0.0, 5.0, 0.0, 0.1)
max_price = st.sidebar.slider("Maximum Price", 0, books_df['Price'].max((), books_df['Price'].min()))

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

fig = px.pie(books_df, names='Genre', title='Most Liked Genre (2009 - 2022)', color='Genre', color_discrete_sequence=px.colors.sequential.Plasma)

st.plotly_chart(fig)


st.subheader("Number of Fiction vs Non-Fiction Books Over the Years")
size = books_df.groupby(['Year', 'Genre']).size().reset_index(name='Count')
fig = px.bar(size, x='Year', y='Count', color='Genre', title= 'Number of Fiction vs Non-Fiction Books from 2009-2022',
             color_discrete_sequence=px.colors.sequential.Plasma, barmode='group')
st.plotly_chart(fig)




st.header('Top 15 Authors by Counts of Books Over the Years')
top_authors = books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns = ['Author', 'Count']
fig = px.bar(top_authors,x='Count',y='Author',orientation='h',
    title='Top 15 Authors by Counts of Books Published',
    labels={'Count': 'Counts of Books Published', 'Author': 'Author'},
    color='Count',color_continuous_scale=px.colors.sequential.Plasma
)

st.plotly_chart(fig)


st.subheader("Filter Data by Genre")
genre_filter = st.selectbox('Select Genre', books_df['Genre'].unique())
filter_df = books_df[books_df['Genre'] == genre_filter]
st.write(filter_df)

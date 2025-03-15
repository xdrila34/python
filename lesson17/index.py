import streamlit as st



# col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")
#
# with col1:
#     st.header("column 1")
#     st.write("comment for col1")
# with col2:
#     st.header("column 2")
#     st.write("comment for col2")
#
# with col3:
#     st.header("column 3")
#     st.write("comment for col3")
#
# with col4:
#     st.header("column 4")
#     st.write("comment for col4")
#
# with col5:
#     st.header("column 5")
#     st.write("comment for col5")
#
with st.form("my_form", clear_on_submit=True):
    name = st.text_input("your name")
    age = st.slider("your age", min_value=0, max_value=100)
    email = st.text_input("email adress")
    biography = st.text_area("short bio")
    tos = st.checkbox("accept the tos")
    submit_button = st.form_submit_button(label="submit")

if submit_button:
    st.write(f"name:{name}")
    st.write(f"age:{age}")
    st.write(f"email:{email}")
    st.write(f"bio{biography}")
    if tos:
        st.write("you have agreed to our terms and conditions")
    else:
        st.write("you cannot continue without agreeing to our tos")


tab1, tab2, tab3 = st.tabs(["tab1","tab2","tab3"])

with tab1:
    st.header("tab1")
    st.write("tab1 desc")

with tab2:
    st.header("tab2")
    st.write("tab2 desc")

with tab3:
    st.header("tab3")
    st.write("tab3 desc")

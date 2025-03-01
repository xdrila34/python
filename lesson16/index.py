import streamlit as st


def main():
    st.title('hello worlds')


if __name__ == '__main__':
   main();


import streamlit as st

if st.button("click me"):
    st.write("button clicked")


if st.checkbox("chek me"):
    if st.button("try this out"):
        st.write("came a long way")


user_input = st.text_input("enter text", "shkruj naj sen")
st.write("you wrote ", user_input)


age = st.number_input("enter you age ", min_value=1, max_value=100)
st.write(f"you are {age} years old")


message = st.text_area("enter text")
st.write(f"you typed {message}")


choice = st.radio("choose one ",["choice1","choice2","choice3"])
st.write(f"you chose{choice}")


if st.button("succes"):
    st.success("it was succesfuly sent!!")


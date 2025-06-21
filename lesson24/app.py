import streamlit as st
import requests
import pandas as pd

st.title("Project Management App")

st.header("Add a Developer")

dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Experience (Years)", min_value=0, max_value=50, value=0)

if st.button("Create Developer"):
    dev_data = {"name": dev_name, "experience": dev_experience}
    response = requests.post(url="http://localhost:8000/developers/", json=dev_data)
    st.json(response.json())

st.header("Add a Project")
proj_title = st.text_input("Project Title")
proj_desc = st.text_area("Project Description")
proj_lang = st.text_input("Languages Used (Comma-separated)")
lead_dev_name = st.text_input("Lead Developer Name")
lead_dev_exp = st.number_input("Lead Developer Experience (Years)", min_value=0, max_value=50, value=0)

if st.button("Create Project"):
    lead_dev_data = {"name": lead_dev_name, "experience": lead_dev_exp}
    proj_data = {
        "title": proj_title,
        "description": proj_desc,
        "language": proj_lang,
        "lead_developer": lead_dev_data
    }

    response = requests.post(url="http://localhost:8000/projects/", json=proj_data)
    st.json(response.json())
st.header("Project Dashboard")
if st.button("Get Project"):
    response = requests.get("http://localhost:8000/projects/")
    project_data = response.json()['projects']
    if project_data:
        projects_df = pd.DataFrame(project_data)

        st.subheader("Project Overview")
        st.dataframe(projects_df)

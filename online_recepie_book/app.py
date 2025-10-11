from http.client import responses

import streamlit as st
import requests
import pandas as pd
from dotenv import load_dontenv
import os

load_dontenv()

API_BASE_URL = os.getenv("API_BASE_URL")

def get_categories():
    response = requests.get(f"{API_BASE_URL}/categories/")
    return response.json()

def get_recipes(cuisine=None, difficulty=None):
    params = {}
    if cuisine:
        params['cuisine'] = cuisine
    if difficulty:
        params['difficulty'] = difficulty
    response = requests.get(f"{API_BASE_URL}/recipes/", params=params)
    return response.json()

def create_category(category_name):
    response = requests.post(f"{API_BASE_URL}/categories/", json={"name": category_name})
    return response.json()
def update_category(category_id, new_name):
    response = requests.post(f"{API_BASE_URL}/categories/{category_id}", json={"name":new_name})
    return response.json()
def delete_category(category_id):
    response = requests.delete(f"{API_BASE_URL}/categories/{category_id}")
    return response.json()

def create_recipe(recipe_name, description, ingredients, instructions, cuisine, difficulty, category_id):
    response = requests.post(f"{API_BASE_URL}/recipes/", json = {"name": recipe_name,"description": description,"ingredients": ingredients,"instructions": instructions,"cuisine": cuisine,"difficulty": difficulty,"category_id": category_id})
    return response.json()
def update_recipe(recipe_id,recipe_name, description, ingredients, instructions, cuisine, difficulty, category_id):
    response = requests.post(f"{API_BASE_URL}/recipes/{recipe_id}", json = {"name": recipe_name,"description": description,"ingredients": ingredients,"instructions": instructions,"cuisine": cuisine,"difficulty": difficulty,"category_id": category_id})
    return response.json()
def delete_recipe(recipe_id):
    response = requests.delete(f"{API_BASE_URL}/recipes/{recipes_id}")
    return response.json()





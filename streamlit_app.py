import streamlit as st
import pandas as pd

import requests

st.header("Fruityvice Fruit Advice!")
# Add a title
st.title('My parents New Healthy Diner.')

# Add a  subheader
st.subheader("Breakfast Favourites")

# Add multiline text
multiline_text = """
🥣 Omega 3 & Blueberry Oatmeal \n
🥗 Kale, Spinach & Rocket Smoothie \n
🐔 Hard Boiled Free-Range Egg \n
🥑🍞 Avocado Toast
"""

st.write(multiline_text)

# Add a  header
st.header(" 🍌🥭 Build your own Fruit Smoothie 🥝🍇")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#interactive list

fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado' , 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)









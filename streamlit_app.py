import streamlit as st
import pandas as pd

import requests
import snowflake.connector

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

st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# st.text(fruityvice_response.json())


# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.header("The fruit load contains:")
#st.text("The fruit load list contains:")
#st.text("Hello from Snowflake:")
#st.text(my_data_row)
st.dataframe(my_data_rows)

fruit_input = st.text_input('What fruit would you like to add?','Jackfruit')
st.write('Thanks for adding', fruit_input)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")






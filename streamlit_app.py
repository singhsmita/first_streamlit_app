import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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


#create the repetable code block
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  # new section to display fruityvice api response
st.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
      st.error("Please select a fruit to get information.")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      st.dataframe(back_from_function)
except URLError as e:
    st.error()

# write your own comment -what does the next line do? 

# write your own comment - what does this do?

st.header("View Our Fruit List - add Your Favorites !")
#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchall()

# add a  button to load the fruit
if st.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  st.dataframe(my_data_rows)


# Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        #my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        my_cur.execute("insert into fruit_load_list values (' " + (new_fruit) + " ')")
        return "Thanks for adding " + new_fruit

add_my_fruit = st.text_input('What fruit would you like to add?')
if st.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    st.text(back_from_function)

#don't run anything past here until we troubleshoot
st.stop()
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






//import streamlit

//streamlit.title('My parents New Healthy Diner.')

//streamlit.markdown("## Subheading 1")

//streamlit.write("Breakfast Menu")

//text_lines = ["Omega 3 & Blueberry Oatmeal" , "Kale ,Spinach & Rocket Smoothie" , "Hard Boiled Free-Range Egg" ]
//streamlit.write(text_lines)


import streamlit as streamlit

# Set the title
streamlit.title("My parents' New Healthy Diner.")

# Subheading
streamlit.markdown("## Subheading 1")

# Display the breakfast menu
streamlit.write("Breakfast Menu")

# List of menu items
text_lines = ["Omega 3 & Blueberry Oatmeal", "Kale, Spinach & Rocket Smoothie", "Hard Boiled Free-Range Egg"]

# Display the menu items as a list
streamlit.write(text_lines)

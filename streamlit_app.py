import streamlit
streamlit.title('My Parent\'s new healthy diner')

streamlit.header('breakfast Menu')
streamlit.text('🥣 Omega 3 & blueberry meal')
streamlit.text('🥗 kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard boild free range eggs')
streamlit.text('🥑 🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


  
streamlit.dataframe(fruits_to_show)  

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)



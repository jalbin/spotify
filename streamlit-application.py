import streamlit as st
import pandas as pd
import numpy as np
import datetime
st.title("Avast ye land lubbers!! Hohoho, where did the rum go?!!")

x = st.slider("Select a value")
st.write(x,"the square value of x is",x**2)
st.write( pd.DataFrame({ 'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8] }) )

# #### select box
selectbox_basic = st.selectbox( "Select yes or no", ["Yes", "No"] )
st.write(f"You selected {selectbox_basic}")


# #####
checkbox_one = st.checkbox("Yes")
checkbox_two = st.checkbox("No")


st.write(f"You selected {checkbox_one} {checkbox_one}")

# ##### Line Chart
st.write("Line Chart in Streamlit") # 10 * 2
chart_data = pd.DataFrame( np.random.randn(10, 2), columns=[f"Col{i+1}" for i in range(2)] )
st.write(chart_data)
st.line_chart(chart_data)


# ##### bar chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])
st.write(chart_data)
st.bar_chart(chart_data)


# ####### Area Chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.area_chart(chart_data)


# ######## map chart
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [48.85, 2.38],
    columns=['lat', 'lon'])
st.write(df)
st.map(df)

# ######## Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")

# ###### Side bar
# selectbox = st.sidebar.selectbox( "Select yes or no", ["Yes", "No"] ,1) ## 1 is a unique key
# st.write(f"You selected {selectbox}")

# #####  Date input
d = st.date_input(
    "When\'s your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)


song = st.text_input("Please enter a song")

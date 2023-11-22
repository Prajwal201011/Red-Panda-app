import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo 
import math 

st.set_page_config(
        page_title='RedPanda Home',
        page_icon="🐼"
    )

names = ["Peter Parker", "Prajwal VS" , "Ishaan"]
usernames = ["pparker", "pvs", "ishaan"]


colored_header(label= "🏡 Welcome To RedPanda - Home",
                description= "Home",
                color_name='red-70')
if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""


col1 , col2 = st.columns(2)
with col1: 
    my_input = st.text_input("YOUR NAME", st.session_state["my_input"])
    submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
    st.write ("Hello", my_input)
    st.sidebar.write('Welcome', my_input)


like = st.checkbox("Do you like this app?")
button2 = st.button("📩")
if button2: 
    if like:
        st.write("Thanks. I like it too.")
    else:
        st.write("I'm sorry. You have bad tastes.")

animal = st.radio("What animal is your favorite?", ("Lion", "Tiger", "Bear"))
button3 = st.button("🐾")
if button3:
    st.write(animal)
    if animal == "Lion":
        st.write("ROAR!")
    elif animal == "Tiger":
        st.write("🐯, I like them too!!")
    elif animal == "Bear":
        st.balloons()

user_text = st.text_input("What's your favorite movie?", "Star Wars Ep. IV")
if st.button("Text Button"):
    st.write(user_text)
    
user_num = st.number_input("What's your age?")
if st.button("Number Button"):
    st.write("Your age is", user_num,  '!')

d = st.date_input("When's your birthday")
st.write('Your birthday is on', d)

st.write("-----")
st.subheader('Simple Calculator')
n1 = st.number_input("Number 1", 0.0000, 10000000000.0000)
n2 = st.number_input("Number 2", 0.0000, 10000000000.0000)

c1, c2, c3 = st.columns(3)
with c1:
    ope = st.radio("Select an Operation", ('Addition', 'Subtraction', 'Multiplication', 'Division'))

with c2:
    opp = st.radio('#',('Power', "SquareRoot", "CubeRoot"))

def calculate():
    if ope == 'Addition':
        st.write(n1,'+' , n2,'=', n1 + n2)
    elif ope=='Subtraction':
        st.write(n1,'-' , n2,'=', n1 - n2)
    elif ope=='Multiplication':
        st.write(n1,'x' , n2,'=', n1 * n2)
    elif ope == 'Division' and n2!= 0:
        st.write(n1,'/' , n2,'=', n1 / n2)
    elif ope == 'Division' and n1!= 0:
        st.warning("Division by 0 error. Please enter a non-zero number.")
    else: 
        st.warning('Please select an operation')

def evaluate():
    if opp == 'Power':
        st.write( n1, "^", n2 ,"=", n1**n2 )
    elif opp == 'SquareRoot':
        st.warning('Enter 1 number for square root', icon='🤖')
        st.write("√", n1 ,'=', math.sqrt(n1))
    elif opp == 'CubeRoot':
        st.write("3√",n1,'=', n1**1/3)

with c1:
    if st.button ('Calculate'):
        calculate()
with c2:
    if st.button ('Evaluate'):
        evaluate()


if st.button ('Other Calculators'):
    switch_page('Other_Calculators')
import streamlit as st
from streamlit_extras.colored_header import colored_header as ch
from streamlit_extras.app_logo import add_logo 

st.set_page_config(
        page_title='Contact',
        page_icon="🐼"
    )

ch (label= ":mailbox: Get In Touch With us!",
               description= "Contact",
               color_name='red-70')
st.sidebar.success("Welcome")



contact_form = """<style>/* Style inputs with type="text", type="email"and textareas */
input[type=text], input[type=email], textarea {
    width: 100%; /* Full width */
    padding: 12px; /* Some padding */ 
    border: 1px solid #ccc; /* Gray border */
    border-radius: 4px; /* Rounded borders */
    box-sizing: border-box; /* Make sure that padding and width stays in place */
    margin-top: 6px; /* Add a top margin */
    margin-bottom: 16px; /* Bottom margin */
    resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
  }
  
  /* Style the submit button with a specific background color etc */
  button[type=submit] {
    background-color: #04AA6D;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  /* When moving the mouse over the submit button, add a darker green color */
  button[type=submit]:hover {
    background-color: #45a049;
  }</style>
<form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



import streamlit as st 
from streamlit_extras.colored_header import colored_header as ch
from streamlit_extras.app_logo import add_logo 
import math

st.set_page_config(
        page_title='Essential Calculators',
        page_icon="🐼"
    )

ch (label= "⁉️ Simple Interest Calculator",
               description= "Interest calculator",
               color_name='red-70')
st.sidebar.success("Welcome")

st.write("Input Type")
sl = st.selectbox("Input Type", ("Slider", "Text"))
if sl == "Slider":
        p1 = st.slider('Principal',100,10000)
        t1 = st.slider('Term',100,10000)
        r1= st.slider('Rate',0, 100)
        
        btn = st.button("Calculate")
        def calculate():
                st.write("Simple Interest Is: " , (p1*t1*r1)/100)
                st.write("Amount is: " , p+p*t*r/100)
        if btn :
                calculate()
        
elif sl == 'Text':
        p = st.text_input('Principal',100)
        t = st.text_input('Term',100)
        r = st.text_input('Rate',0, 100)

        btn2 = st.button("Calculate")
        def calculate():
                st.write("Simple Interest Is: " , p*t*r/100)
                st.write("Amount is: " , p+p*t*r/100)
                
        if btn2 :
                 calculate()

ch (label= "Perimeter, Area & Volume",
               description= "Calculate Perimeter, Area & Volume",
               color_name='red-70')

sy = st.selectbox("WHICH QUADRILATRAL'S PERIMETER AND AREA YOU WANT: ", ("Square", "Rectangle", "Parallelogram", "Triangle", "Circle", "Trapezium"))
btn = st.button("OK")
if btn:
        if sy == "Square":
                l = st.number_input('Length')
                b = st.number_input('Breadth')
                def evl():
                        st.write('Perimeter') 
                        st.write(2*(l+b), 'units²') 
                        st.write('Area') 
                        st.write(l*b , 'units²') 
                if st.button("Evaluate"):
                                evl()
        elif sy == " Parallelogram":
                
                h = st.number_input('Height')
                l = st.number_input('Length')
                b3 = st.number_input('Breadth')
                def chk():
                        st.write('Perimeter') 
                        st.write(2*(l+b3), 'units²') 
                        st.write('Area') 
                        st.write(h*b3 , 'units²') 
        elif sy == "Rectangle":
                l = st.number_input('Length')
                b = st.number_input('Breadth')
                def ev():
                        st.write('Perimeter') 
                        st.write(2*(l+b), 'units²') 
                        st.write('Area') 
                        st.write(l*b , 'units²') 
                if st.button("Check"):
                                ev()
        elif sy == "Circle":
                r = st.number_input('Radius')
                pi = st.selectbox("How to take PI as (3.14 or 22/7)", ("3.14", "22/7"))
                def comp():
                        st.write("Circumference :", 2*pi*r )
                        st.write("Area :", pi*r**2 )
                if st.button("Compute"):
                                comp()
        
        elif sy == "Triangle":
                g = st.selectbox("Perimeter , Area or Hypotenuse", ("Perimeter" ,'Area', "Hypotenuse"))
                if g == "Perimeter":
                      a = st.number_input('Side A')
                      b = st.number_input('Side B')
                      c = st.number_input('Side c')  
                      def pe():
                                st.write("Perimeter :", a + b + c)
                if st.button("Find"):
                        pe()
                elif g == "Area":
                        bs = st.number_input('Base')
                        he = st.number_input('Height')
                        def area():
                                st.write("Area :", 1/2*bs*he)
                        if st.button("Find Out"):
                                area()
                                                        
                elif g == "Hypotenuse":
                        leg = st.number_input('Leg 1')
                        legs = st.number_input('Leg 2')
                        def hypotenuse():
                                st.write('Hypotenuse :', math.sqrt(leg**2 + legs**2))
                        if st.button("Caliberate"):
                                hypotenuse()
                                
        elif sy == "Trapezium":
                s = st.number_input('Side 1')
                ss = st.number_input('Side 2')
                sss = st.number_input('Side 3')
                ssss = st.number_input('Side 4')
                def sse():
                        st.write("Perimeter :", s + ss + sss + ssss)
st.write('--------')
st.subheader("Volume")

shp = st.selectbox("Select a 3D shape:" , ('Cube', "Cuboid", "Pyramid", "Sphere"))

if shp == 'Cube':
        s = st.number_input("Length of Side")
        def co():
                st.write("Volume is ", s**3 )
        if st.button("Compete"):
                co()
elif shp == "Cuboid":
         w = st.number_input("Width")
         l = st.number_input("Length")
         h = st.number_input("Height")
         def cub():
                 st.write("Volume:", w*l*h,"units³")
         if st.button("Compete"):
                cub()
          
elif shp == "Pyramid":
        b = st.number_input("Base")
        h = st.number_input("Height")

        def coml():
                st.write("Volume is ", 1/3*b*h , "units³")
        if st.button("Figure Out"):
                coml()
st.write('--------')
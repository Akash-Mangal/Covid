import streamlit as st
from config import *
import pandas as pd
import numpy as np
import plotly.express as px
import db
import os
from report import *
from fastai.basic_train import load_learner
from fastai.vision.image import open_image



st.set_page_config(layout="wide")
choice=st.cache()
#st.title(PROJECT_NAME)
with st.beta_container():
    st.write('<style>body { font-family: sans-serif;border-style: } .header{border-bottom-style: solid;padding-left:10px; padding-right: 938px;z-index: 1; background: White; color: #F63366; position:fixed;top:0px;} .sticky { position: fixed;top: 20; } </style><div class="header" id="myHeader"><h2 style="color: #F63366;"><b>'+"Covid-19 Detection"+'</b></h2></div>', unsafe_allow_html=True)



with st.beta_container():
    cols=st.beta_columns(6)
    
a=cols[0].button(MENU_OPTION[0])
b=cols[1].button(MENU_OPTION[1])
c=cols[2].button(MENU_OPTION[2])
d=cols[3].button(MENU_OPTION[3])
e=cols[4].button(MENU_OPTION[4])
f=cols[5].button(MENU_OPTION[5])

if a or b or c or d or e or f:
    delete_var('choice')
if a or load_var('choice')==0:
    save_var(0,'choice')
    
    viewData()
    
    
        #st.error("No data found")

if b :
    save_var(1,'choice')
    cols=st.beta_columns((2,5,2))
    cols[1].text('''\n \n
    .                precision  recall    f1-score   support\n

        Covid-19       1.00      0.68      0.81        25\n
     No_findings       0.82      0.79      0.81       100\n
       Pneumonia       0.79      0.89      0.84       100\n

        accuracy                           0.82       225\n
       macro avg       0.87      0.79      0.82       225\n
    weighted avg       0.83      0.82      0.82       225'''
)
    


if c or load_var('choice')==2:
    delete_var('choice')
    save_var(2,'choice')
    st.title("Charts and graphs")
    cols=st.beta_columns((5,10,4))
    g=cols[0].radio('Select Graph',['Accuracy Graph.png','Iteration Graph.png','Loss Graph.png'])
    cols[1].image(g,use_column_width=True)

if d or load_var('choice')==3:
    delete_var('choice')
    save_var(3,'choice')
    uploadData()
    


if e:
    st.title("What is the project")
    img_col=st.beta_columns((4,2))
    img_col[1].image('CORONA.jpg',use_column_width=True)
    img_col[0].write(ABOUT)

if f:
    st.title("About the Project creators")
    st.write(DEVELOPERS)


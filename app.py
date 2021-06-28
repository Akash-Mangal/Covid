import streamlit as st
from config import *
import pandas as pd
import numpy as np
import plotly.express as px

import os
from report import *
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from datetime import datetime

st.set_page_config(layout="wide")

# setup db code
Base = declarative_base()

# create table as python class
class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer,primary_key=True)
    path = Column(String)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    contact = Column(Integer)
    uploaded_on = Column(String,default=datetime.now().strftime(" %d %b, %Y at %I:%M %p"))
    result=Column(String)
    st.write("create table")
    def __str__(self):
        return self.path
    
    def __repr__(self) -> str:
        return self.path

if __name__ == "__main__":
    engine = create_engine("sqlite:///db.sqlite3")
    Base.metadata.create_all(engine)
    st.write("done")
    

#st.title(PROJECT_NAME)
with st.beta_container():
    st.write('<style>body { font-family: sans-serif;border-style: } .header{border-bottom-style: solid;padding-left:10px; padding-right: 938px;z-index: 1; background: White; color: #F63366; position:fixed;top:0px;} .sticky { position: fixed;top: 20; } </style><div class="header" id="myHeader"><h2 style="color: #F63366;"><b>'+"Covid-19 Detection"+'</b></h2></div>', unsafe_allow_html=True)

#if not os.path.exists("db.sqlite3"):
#    engine = create_engine("sqlite:///db.sqlite3")
#  Base.metadata.create_all(engine)
  

with st.beta_container():
    cols=st.beta_columns(6)
    
a=cols[0].button(MENU_OPTION[0])
b=cols[1].button(MENU_OPTION[1])
c=cols[2].button(MENU_OPTION[2])
d=cols[3].button(MENU_OPTION[3])
e=cols[4].button(MENU_OPTION[4])
f=cols[5].button(MENU_OPTION[5])


if a or b or c or d or e or f:
    delete_var('/tmp/choice')
if a or load_var('/tmp/choice')==0:
    save_var(0,'/tmp/choice')
    #try:
    viewData()
    #except:
        #st.error("No data found")

if b :
    save_var(1,'/tmp/choice')
    cols=st.beta_columns((2,5,2))
    cols[1].text('''\n \n
  
        .                precision  recall    f1-score   support\n

        Covid-19       1.00      0.80      0.89        25\n
          normal       0.85      0.81      0.83       100\n
       Pneumonia       0.82      0.90      0.86       100\n

        accuracy                           0.85       225\n
       macro avg       0.89      0.84      0.86       225\n
    weighted avg       0.85      0.85      0.85       225'''
)
    


if c or load_var('/tmp/choice')==2:
    delete_var('/tmp/choice')
    save_var(2,'/tmp/choice')
    st.title("Charts and graphs")
    cols=st.beta_columns((5,10,4))
    g=cols[0].radio('Select Graph',['Accuracy Graph.png','Iteration Graph.png','Loss Graph.png'])
    cols[1].image(g,use_column_width=True)

if d or load_var('/tmp/choice')==3:
    delete_var('/tmp/choice')
    save_var(3,'/tmp/choice')
    uploadData()
    


if e:
    delete_var('/tmp/choice')
    save_var(4,'/tmp/choice')
    st.title("What is the project")
    img_col=st.beta_columns((4,2))
    img_col[1].image('CORONA.jpg',use_column_width=True)
    img_col[0].write(ABOUT)

if f:
    delete_var('/tmp/choice')
    save_var(4,'/tmp/choice')
    st.title("About the Project creators")
    st.markdown("<p style='text-align: justify; color: #F63366;'>The web application Leukemia detection through CNN has been developed by Akash agarwal and Anupam, the final semester students of Bachelors of Computer Applications in Babu Banarasi Das University, Lucknow.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: #F63366;'>The project is based on python with data science. The basic technologies used for the project are- python 3.9.5, VS code, SQLite3 and Google collab.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: #F63366;'>As a collaborative project, both of us divided our tasks equally. The project consists of 10 modules.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: #F63366;'>Contribution of the student in the project:</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: #F63366;'>Anubhavi Patel: <ul><li>Leukaemia Image Collection</li><li> Image Convolution</li><ul> Maxpooling, Activation Function Selection, Leukaemia Model Training.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: #F63366;'>Anukriti Srivastava: Leukaemia Model Visualization, Prediction System, Database Manager, Setting Manager, View Display Manager.</p>", unsafe_allow_html=True)
    st.write(DEVELOPERS)


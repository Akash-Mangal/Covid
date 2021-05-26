import streamlit as st
import os
import pickle
from PIL import Image
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import or_
import db
from report import *
from fastai.basic_train import load_learner
from fastai.vision.image import open_image
import numpy as np
import pandas as pd
from datetime import datetime

PROJECT_NAME = 'COVID-19 Detection'
CREATOR = "Anupam and Akash Agarwal"
UPLOAD_FOLDER = 'uploads'
GENDER = ['Male','Female','Other']
MENU_OPTION = [
    'Show Data',
    ' Data Stats',
    'Visualization',
    'Prediction',
    'About project',
    'Creator  info',
    'View Report'
]

def save_var(var, path):
    with open(path,'wb') as we: 
        pickle.dump(var, we)

def load_var(path):
    if os.path.exists(path):
        with open(path, 'rb') as we:
            return pickle.load(we)

def delete_var(path):
    if os.path.exists(path):
        os.unlink(path)

def open_db():
    engine = create_engine("sqlite:///db.sqlite3")
    Session = sessionmaker(bind=engine)
    return Session()

if not os.path.exists("uploads"):
    os.mkdir(UPLOAD_FOLDER)

#variable is global
images=None

def uploadData():
    st.header("Prediction using AI model")
    name = st.text_input("Name")
    col = st.beta_columns((1,2,3))
    age = col[0].text_input("Age")
    gender = col[1].selectbox("Gender",GENDER)
    contact = col[2].text_input("Contact Number")
    imgdata = st.file_uploader("Upload Chest X-Ray",type=['jpg','png'])

    if imgdata and name and age and gender and contact:

        learner = None
        info ={
            'covid':'''covid-19 pneumonia causes the density of the lungs to increase. This may be seen as whiteness in the lungs on radiography which, depending on the severity of the pneumonia, obscures the lung markings that are normally seen; however, this may be delayed in appearing or absent.''',
            'pneumonia':'''When interpreting the x-ray, the AI will look for white spots in the lungs (called infiltrates) that identify an infection. This exam will also help determine if you have any complications related to pneumonia such as abscesses or pleural effusions (fluid surrounding the lungs).''',
            'normal':'the xray image does not show symptoms of pneumonia or covid-19'
        }

        with st.spinner("please wait, while model loads"):
            learner = load_learner(path='covid_classifier_model',file='model.pkl')
            st.info('model loaded into memory')
        # load image as a Pillow object
        im = Image.open(imgdata)
        # create a address for image path
        path = os.path.join(UPLOAD_FOLDER,imgdata.name)
        ext= imgdata.type.split('/')[1]
        # save file to upload folder
        im.save(path,format=ext)
        # saves info to db
        sess = open_db()
        
        # show a msg
        img = open_image(path)
        cat,tensor,probs=learner.predict(img)
        
        
        st.success(cat)
        if str(cat) == 'Covid-19':
            st.success(info['covid'])
        elif str(cat) == 'Pneumonia':
            st.success(info['Pneumonia'])
        elif str(cat) == 'normal':
            st.success(info['Normal'])

        result=str(cat).upper()
        imdb = db.Image( name= name, path=path, age=age, gender=gender, contact=contact, result= result)

        sess.add(imdb)
        sess.commit()
        sess.close()
        st.success('Report saved')
        delete_var('choice')
   
    

def viewData():
    st.title("View Report")
    #Ask for Details
    cols=st.beta_columns(2)
    name = cols[0].text_input("Name")
    contact = cols[1].text_input("Contact Number")
  
        
    # open the database
    sess = open_db()
    # get all the images from the image table

    images = sess.query(db.Image).filter((db.Image.contact==contact) | (db.Image.name == name)).all()
    # close database
    sess.close()
    save_var(images, 'images.dk')
    
    # show the image names in sidebar to select one
    if load_var('images.dk'):
        
        content=load_var('images.dk')
        list_data =[]
        list_path =[]
        for i in content:
            li=str((i.name)+" "+str(i.contact))
            list_data.append(li)
            list_path.append(i.id)
        index=list_data.index(st.selectbox("select an image",list_data))
        
        id=list_path[index]
        
        # open the database
        sess = open_db()
        profile=sess.query(db.Image).filter((db.Image.id==id)).all()
        # close database
        sess.close()

        profile=profile[0]
        select_img = profile.path
        # load the image obj using selected image path
        im = Image.open(select_img)
        # show the image, fill the area available
        
        crt_pdf(profile)
        col=st.beta_columns(3)
        col[0].write('**Patient Id:\t\t\t**' + str(profile.id) )
        col[0].write('''
            Name \n
            Age \n
            Gender \n
            Contact \n
            Status''')
        
        
        col[1].write("**Uploaded on: **" + str(profile.uploaded_on))
        col[1].write(profile.name)
        col[1].write(str(profile.age))
        col[1].write(profile.gender)
        col[1].write(str(profile.contact))
        col[1].write(profile.result)
        col[2].image(im,use_column_width=True)
        
        
    if not load_var('images.dk') and name and contact :
        st.info("Not Found")

ABOUT = '''According to the World Health Organization (WHO), the coronavirus (COVID-19) pandemic is putting
even the best healthcare systems across the world under tremendous pressure. The early detection of
this type of virus will help in relieving the pressure of the healthcare systems. Chest X-rays has been
playing a crucial role in the diagnosis of diseases like Pneumonia. As COVID-19 is a type of influenza, it
is possible to diagnose using this imaging technique. With rapid development in the area of Machine
Learning (ML) and Deep learning, there had been intelligent systems to classify between Pneumonia
and Normal patients. '''

DEVELOPERS='ANUPAM and AKASH are great personalities... You will feel good with them. Ab mai apni tareef mai aur kya hi likhun...' + chr(128516)
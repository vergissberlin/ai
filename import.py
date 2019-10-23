import pandas as pd
import numpy as np
import streamlit as st
from os import listdir
from os.path import isfile, join
from PIL import Image

import app.Training 


# Document
st.title('Animal Identification')
st.write("Pick an image from the left. You'll be able to view the image.")
st.write("When you're ready, submit a prediction on the left.")



# Sidebar
st.sidebar.title("About")
st.sidebar.info("This is a demo application written to help you understand Streamlit. The application identifies the animal in the picture. It was built using a Convolution Neural Network (CNN).")

onlyfiles = [f for f in listdir("/Users/andre.lademann/Test/ai/assets/animals/elefante/") if isfile(join("/Users/andre.lademann/Test/ai/assets/animals/elefante/", f))]
imageselect = st.sidebar.selectbox("Pick an image.", onlyfiles)

st.sidebar.title("Train Neural Network")
if st.sidebar.button('Train CNN'): 
     Training.train()


# Content
st.write("")
image = Image.open("/Users/andre.lademann/Test/ai/assets/animals/elefante/" + imageselect)
st.image(image, caption="Let's predict the animal!", use_column_width=True)

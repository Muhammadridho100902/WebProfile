import streamlit as st
import webbrowser
import os
from streamlit.components.v1 import html

## -------------------------- Open File -------------------------- ##
# Mendapatkan path absolut dari direktori 'assets'
assets_dir = os.path.join(os.path.dirname(__file__), 'assets')

# Menggunakan path absolut untuk membuka file 'CV.pdf'
ML_file_path = os.path.join(assets_dir, 'CV_Data.pdf')
DA_file_path = os.path.join(assets_dir, 'CV_Data_Analytics.pdf')
ab_path = os.path.join(assets_dir, 'Abtest.png')
anomaly_path = os.path.join(assets_dir, 'Anomaly.jpg')
car_path = os.path.join(assets_dir, 'car.jpg')
coffee_path = os.path.join(assets_dir, 'Coffee.png')
diabetes_path = os.path.join(assets_dir, 'diabetes.png')
kereta_path = os.path.join(assets_dir, 'kereta.png')
onepiece_path = os.path.join(assets_dir, 'onepiece.jpg')
profile_path = os.path.join(assets_dir, 'profile.jpg')
reporting_path = os.path.join(assets_dir, 'Reporting.png')
sentiment_path = os.path.join(assets_dir, 'sentiment.jpeg')
supply_path = os.path.join(assets_dir, 'Supply.png')


with open(ML_file_path, 'rb') as file:
    ML_Data = file.read()
    
with open(DA_file_path, 'rb') as file:
    DA_Data = file.read()
    
with open(ab_path, 'rb') as file:
    image_ab = file.read()
    
with open(anomaly_path, 'rb') as file:
    image_anomaly = file.read()
    
with open(car_path, 'rb') as file:
    image_car = file.read()
    
with open(coffee_path, 'rb') as file:
    image_coffee = file.read()
    
with open(diabetes_path, 'rb') as file:
    image_diabetes = file.read()
    
with open(kereta_path, 'rb') as file:
    image_kereta = file.read()

with open(onepiece_path, 'rb') as file:
    image_onepiece = file.read()
    
with open(profile_path, 'rb') as file:
    image_profile = file.read()

with open(reporting_path, 'rb') as file:
    image_reporting = file.read()
    
with open(sentiment_path, 'rb') as file:
    image_sentiment = file.read()
        
with open(supply_path, 'rb') as file:
    image_supply = file.read()
    

## -------------------------- File Project -------------------------- ##

kereta_link = "https://www.linkedin.com/posts/muhammad-ridho-phageis-swara_kereta-barang-indonesia-activity-7092352697223319552-NQ6z?utm_source=share&utm_medium=member_desktop"

anomaly_link = "https://github.com/Muhammadridho100902/google_collab/blob/main/Transactions.ipynb"

coffee_link = "https://www.linkedin.com/posts/muhammad-ridho-phageis-swara_dataanalysis-dataanalytics-python-activity-7127199201582579712-r7Ct/?utm_source=share&utm_medium=member_desktop"

supply_link = "https://www.linkedin.com/posts/muhammad-ridho-phageis-swara_supply-chain-analytics-activity-7130900397346476033-5nAY?utm_source=share&utm_medium=member_desktop"

reporting_link = "https://drive.google.com/drive/folders/1ZHw0XlBg43HDmVkTIGJnYfi91zY_eJkK?usp=sharing"

ab_link = "https://github.com/Muhammadridho100902/google_collab/blob/main/A_B_Testing_of_Themes.ipynb"

car_link = "https://github.com/Muhammadridho100902/google_collab/blob/main/Car_vs_Bike_Classification.ipynb"

diabet_link = "https://github.com/Muhammadridho100902/Diabetes_WebApp.git"

sentiment_link = "https://github.com/Muhammadridho100902/Sentiment_WebApp.git"

one_piece_link = "https://github.com/Muhammadridho100902/one_piece_classifie.git"

## -------------------------- Button Project -------------------------- ##
def open_Project(link):
    webbrowser.open_new_tab(link)
        
## -------------------------- GITHUB -------------------------- ##
Github_url = "https://github.com/Muhammadridho100902"
Linkedin_url = "https://www.linkedin.com/in/muhammad-ridho-phageis-swara/"
Gmail_url = "Mridhophs@gmail.com"
def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)
    

## -------------------------- Header -------------------------- ##
col1, col2 = st.columns(2)

with col1:
    st.markdown("Hey There,")
    
    st.markdown("# I'M :red[RIDHO]")
    st.markdown("### A DATA ENTHUSIAST")
    st.markdown("Dedicated to assisting enterprises by supporting :red[data-driven] decision-making")
    
    button1, button2 = st.columns(2)
    # with button1:
    #     if st.button("Hire Me", type="primary"):
    #         st.button()
            
    with button1:
        st.download_button("CV Machine Learning",
                       data = ML_Data,
                       file_name= "Cv Machine Learning.pdf",
                       key = 'download_cv_MachineLearning')
        
    with button2:
        st.download_button("CV Data Analytics",
                       data = DA_Data,
                       file_name= "Cv Data Analytics.pdf",
                       key = 'download_cv_DataAnalytics')

with col2:
    st.image(image_profile, use_column_width="auto")
    
    
## -------------------------- Project -------------------------- ##

st.divider()  # 👈 Draws a horizontal rule

st.title("Portofolio")

st.divider()

col1, col2 = st.columns(2)

kereta1, kereta2 = st.columns(2)

with kereta1:
    st.image(image_kereta, use_column_width="always")
with kereta2:
    st.markdown("##### Kereta Barang Indonesia")
    st.write("Through this analysis, I gained new insight into the use of freight trains in Indonesia, which are starting to be popular on the islands of Java and Sumatra.")
    if st.button("View Project", key='kereta_project'):
        open_page(kereta_link)
    
anomaly1, anomaly2 = st.columns(2)

with anomaly1:
    st.image(image_anomaly, use_column_width="always")
with anomaly2:
    st.markdown("##### Anomaly Detection in Transaction")
    st.write("Anomaly detection in transactions means identifying unusual or unexpected patterns within transactions or related activities.")
    if st.button("View Project", key='anomaly_project'):
        open_page(anomaly_link)
    
coffee1, coffee2 = st.columns(2)

with coffee1:
    st.image(image_coffee, use_column_width="auto")
with coffee2:
    st.markdown("##### Coffee Shop Sales")
    st.write("I'm walking you through an end-to-end analysis journey that covers essential steps like Business Understanding, Problem Statement, Goal Definition, and Exploratory Data Analysis (EDA).")
    if st.button("View Project", key='coffee_project'):
        open_page(coffee_link)

supply1, supply2 = st.columns(2)

with supply1:
    st.image(image_supply, use_column_width="auto")
with supply2:
    st.markdown("##### Supply Chain Analytics")
    st.write("I've immersed myself in the realm of supply chain analytics, and the results are concocting valuable business insights and recommendations.")
    if st.button("View Project", key='supply_project'):
        open_page(supply_link)
    
report1, report2 = st.columns(2)
    
with report1:
    st.image(image_reporting, use_column_width="auto")
with report2:
    st.markdown("##### Self Service Reporting")
    st.write("The Self-Reporting Services Dashboard is a powerful and user-friendly tool meticulously designed for individuals to manage and monitor their self-reported activities seamlessly.")
    if st.button("View Project", key='report_project'):
        open_page(reporting_link)
    
ab1, ab2 = st.columns(2)

with ab1:
    st.image(image_ab, use_column_width="auto")
with ab2:
    st.markdown("##### A/B Testing of Themes")
    st.write("AB testing analysis is a powerful method used in the field of data science and experimentation to evaluate the effectiveness of different strategies, designs, or features within a product or system.")
    if st.button("View Project", key='ab_project'):
        open_page(ab_link)
    
car1, car2 = st.columns(2)
    
with car1:
    st.image(image_car, use_column_width="auto")
with car2:
    st.markdown("##### Car vs Bike Image Classifier")
    st.write("Involving concepts from the field of Computer Vision, this project represents an attempt to teach the model to differentiate and identify images featuring two-wheeled and four-wheeled vehicles.")
    if st.button("View Project", key='car_project'):
        open_page(car_link)

dia1, dia2 = st.columns(2)

with dia1:
    st.image(image_diabetes, use_column_width="auto")
with dia2:
    st.markdown("##### Diabetes Web App")
    st.write("Diabetes Web App is a leading solution designed to support individuals in better management and understanding of their diabetes condition.")
    if st.button("View Project", key='diabet_project'):
        open_page(diabet_link)
    
sent1, sent2 = st.columns(2) 
    
with sent1:
    st.image(image_sentiment, use_column_width="auto")
with sent2:
    st.markdown("##### Sentiment Prediction Web App")
    st.write("Sentiment prediction is a field of sentiment analysis that focuses on developing models and algorithms to identify and understand sentiment or feelings contained in text, such as tweets")
    if st.button("View Project", key='sentiment_project'):
        open_page(sentiment_link)
    
one1, one2 = st.columns(2)

with one1:
    st.image(image_onepiece, use_column_width="auto")
with one2:
    st.markdown("##### One Piece Image Classification")
    st.write("By utilizing machine learning and deep learning techniques, this project focuses on developing a model that can recognize iconic characters, locations or certain scenes in One Piece.")
    if st.button("View Project", key='one_project'):
        open_page(one_piece_link)


## -------------------------- Contact and About Me -------------------------- ##

col1, col2 = st.columns(2)

with col1:  
    st.divider()  # 👈 Draws a horizontal rule

    st.title("About Me")

    st.divider()  # 👈 Another horizontal rule

    st.write("Learn about data is not easy for me because there's many tools to learn but continues my hard work bring my skills to a expert levels in Data Analytics, Data Scientist and Machine Learning.")
    
with col2:  
    st.divider()  # 👈 Draws a horizontal rule

    st.title("Contact Me")

    st.divider()  # 👈 Another horizontal rule
    
    st.write("There are several contacts that you can use to collaborate. Phone Number :red[+6289629656884] and my Gmail :red[mridhophs@gmail.com]")
    
    col1, col2= st.columns(2)
    
    with col1:
        if st.button("Github"):
            open_page(Github_url)
    with col2:
        if st.button("Linkedin"):
            open_page(Linkedin_url)

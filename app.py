from streamlit_option_menu import option_menu
import streamlit as st
import pickle
import second
from PIL import Image   #PILLOW(PIL--- for increasing the size of a image and so on)
import base64
def get_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

image = get_image("indian steel.jpg")
def main():
    st.markdown("""
    <style>
               .st-emotion-cache-13ln4jf {
                background-color: rgb(0 0 0 / .5);!important;
                padding-top:50px !important;
                padding-left:40px !important;
                padding-right:40px !important;

                } 
               
    </style>""",unsafe_allow_html=True)
    st.markdown(
        f"""<style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            
        }}
        </style>""", unsafe_allow_html=True
    )

    with st.sidebar:
        option = option_menu("Navigation", ["Introduction", "Prediction"],
            icons=['house', 'bullseye'], 
            menu_icon="cast", 
            default_index=0,  
            styles={
                "container": {"padding": "5!important", "background-color": "black"},
                "icon": {"color": "white", "font-size": "25px"},
                "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px"},
                "nav-link-selected": {"background-color": "Green"},
            }
        )

    st.title(":red[STEEL INDUSTRY ENERGY CONSUMPTION]")
    if option=='Introduction':
        st.header("Introduction")
        st.write(
            "The Steel Industry Energy Consumption Dataset from Kaggle provides valuable insights into energy usage patterns in the steel manufacturing sector. This dataset is crucial for analyzing energy efficiency and optimizing resource utilization in one of the most energy-intensive industries globally."
        )

        # Objective
        st.header("Objective")
        st.write(
            "- To study and understand energy consumption trends in the steel industry.\n"
            "- To explore relationships between energy usage, production processes, and operational parameters."
        )

        # Source
        st.header("Source")
        st.write(
            "The dataset is sourced from Kaggle and may represent either real-world or simulated data "
            "related to steel manufacturing operations."
        )

        # Use Cases
        st.header("Use Cases")
        st.markdown(
            """
            The dataset can be used for:
            - **Energy efficiency analysis**
            - **Predictive modeling for energy usage**
            - **Identifying factors influencing energy consumption**
            - **Benchmarking and policy-making for sustainable industrial practices**
            """
        )

    elif option=='Prediction':
        st.write("Prediction")
        second.predict()

main()

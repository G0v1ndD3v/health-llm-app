import streamlit as st
from components.sidebar import sidebar  # Import sidebar
from components.footer import add_footer  # Import footer

# Page title and separator  
st.title("Acknowledgements")
st.divider()

# Acknowledgment text  
st.markdown(
    """
    This Streamlit application is a proof of concept for **An Intelligent Health LLM System for Personalized Medication Guidance and Support**
    and was undertaken by **Vignesh**, **Krishna S**, **Govind S Nair**, **Veena G**, and **Manjusha Nair** 
    as part of our research at the **Department of Computer Science and Applications**, **Amrita School of Computing**, **Amrita Vishwa Vidyapeetham**.

    Our work derives direction and ideas from the Chancellor of Amrita Vishwa Vidyapeetham, **Sri Mata Amritanandamayi Devi**.

    We extend our gratitude to our mentors, peers, and institution for their invaluable support and resources.  
    This work is an original contribution, and we acknowledge all referenced studies and technologies  
    that have informed and enhanced our research.
    """
)

sidebar()  # Display sidebar  
add_footer()  # Display footer
import streamlit as st
from streamlit_option_menu import option_menu
import home,GOVERNMENT_BUSES

st.set_page_config(page_title="RedBus")

class MultiApp:

    def __init__(self):
        self.apps=[]
    
    def add_app(self,title,function):
        self.apps.append(
            {
                "tilte":title,
                "function":function
            }
        )
    
    def run():

        with st.sidebar:
            app=option_menu(
                menu_title="Main Menu",
                options=["Home","GOVERNMENT BUSES"],
                menu_icon="cast",
                icons=['house-fill','bus-front'],
                default_index=0
                
            )

        if app=="GOVERNMENT BUSES":
            GOVERNMENT_BUSES.app()
        elif app=="Home":
            home.app()
        

    run()


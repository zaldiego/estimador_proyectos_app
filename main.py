import streamlit as st
from streamlit_option_menu import option_menu


import home, cálculo_extracción, cálculo_modelo, cálculo_despliegue, cálculo_total

#Arreglar el set_page_config
st.set_page_config(
    page_title='Estimador de proyectos',
    page_icon = '/home/zaldiego/Imágenes/neuralbatch_icono.png',
    initial_sidebar_state='expanded'
)


class MultiApp:

    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            'title':title,
            'function':function
        })
    
    def run():

        with st.sidebar:
            app = option_menu(
                menu_title='Neural Batch',
                options=['Inicio', 'Cálculo Extracción', 'Cálculo Modelo', 'Cálculo Despliegue', 'Cálculo Total'],
                icons=['house', 'database', 'code', 'rocket', 'calculator'],
                menu_icon='star',
                default_index=0,
                styles={

                        "container": {"padding": "5!important","background-color":'#FFFFFF'},
                        "icon": {"color": "#39067B", "font-size": "18px"}, 
                        "nav-link": {"color":"#39067B","font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#6B00F7"},
                        "nav-link-selected": {"background-color": "#6B00F7", 'color':'#FFFFFF', 'font-size':'18px'},}
                
                )

        
        if app == "Inicio":
            home.app()
        if app == "Cálculo Extracción":
            cálculo_extracción.app()
        if app == "Cálculo Modelo":
            cálculo_modelo.app()
        if app == "Cálculo Despliegue":
            cálculo_despliegue.app()
        if app == "Cálculo Total":
            cálculo_total.app() 
             
          
             
    run()            
         
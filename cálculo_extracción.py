import streamlit as st
from PIL import Image





def app():
    # Titulo de la aplicación
    st.title("Estimación de extracción")

    with open('styles.css') as f:
        #Cambiar colores generales de la app
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


    # Aplicar estilos a un texto en la barra lateral
    st.sidebar.markdown(
        """
        <style>
        .sidebar-content {
            border-radius: 25px;
            padding: 20px; 
            background-color: #FFFFFF;
            color: #6B00F7;
            text-align: justify;
            text-justify: inter-word;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Agregar texto con los estilos personalizados
    st.sidebar.markdown(
        """
        <div class="sidebar-content"><p>En esta sección 'Cálculo Extracción' está lo que por lo general
        consume más tiempo y recursos en un proyecto basado en IA, debido a que cuantos más datos necesitemos
        extraer de la mayor cantidad de servidores más tiempo necesitaremos en la extracción y limpieza de los
        datos extraídos. 
        <p/></div>
        """,
        unsafe_allow_html=True
    )




#======================================================= PRECIO POR EXTRACCION Y CANTIDAD DE SERVIDORES



    selected_extraction_service = st.radio("Seleccione un servicio de extracción", ["Tengo los datos ya preparados", "Tengo los datos en un servidor, necesito extraerlos"])

    # Definir las tarifas de servicio por hora
    service_rates_extraction = {
        "Tengo los datos ya preparados": 14,
        "Tengo los datos en un servidor, necesito extraerlos": 20
    }



    if selected_extraction_service=='Tengo los datos ya preparados':

        #Calculo de precio por extraccion y cantidad de servidores
        total_hours = service_rates_extraction=='Tengo los datos ya preparados'
        total_price = 42 * 14 # Price rate * hours





    elif selected_extraction_service=='Tengo los datos en un servidor, necesito extraerlos':

        quantity_server = st.slider('Cantidad de servidores o fuentes con datos a extraer (Servidores, archivos, tablas, etc)', min_value=1, max_value=15, value=1, step=1)


        #Calculo de precio por extraccion y cantidad de servidores
        service_rate = service_rates_extraction=='Tengo los datos en un servidor, necesito extraerlos'
        hours_extraction_server = service_rate * quantity_server



    #======================================================== PRECIO POR VOLUMEN Y COMPLEJIDAD DE SERVIDORES

        volume_server = st.slider('Volumen de datos en GB', min_value=1, max_value=3000, value=30, step=5)
        complex_server = st.checkbox('Los datos se encuentran sucios, hay que transformarlos ')

        if complex_server:
            complex_server_policy = 1.2
            st.write('¡No hay problema! Transformaremos esos datos :grinning:')
        else:
            complex_server_policy = 1


        extraction_price = 42
        service_rate_extraction = hours_extraction_server + (volume_server * 0.1)
        total_hours = service_rate_extraction * complex_server_policy
        total_price = total_hours * extraction_price


    
    else:
        st.write('Ha ocurrido un error')





#======================================================== CALCULO DE PRECIO Y TIEMPO POR LA EXTRACCION



    st.subheader("Estimación del proyecto sin IVA incluído:")
    st.header(f"{total_price}€")

    

    if total_hours <= 40:
        st.subheader('Los datos estarán preparados en alrededor de 1 Semana')
    elif total_hours > 40 and total_hours < 80:
        st.subheader('Los datos estarán preparados en alrededor de 2 Semanas')

    elif total_hours >= 80 and total_hours < 160:
        st.subheader('Los datos estarán preparados en alrededor de 1 Mes')

    elif total_hours >= 160 and total_hours < 480:
        st.subheader('Los datos estarán preparados en alrededor de 3 Meses')

    elif total_hours >= 480 and total_hours < 800:
        st.subheader('Los datos estarán preparados en alrededor de 5 Meses')

    elif total_hours >= 800 and total_hours < 1200:
        st.subheader('Los datos estarán preparados en alrededor de 7 Meses')

    elif total_hours >= 1200:
        st.subheader('Los datos estarán preparados en alrededor de 8 Meses')

    else:
        st.write('Ha ocurrido un error')
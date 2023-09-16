import streamlit as st




def app():

    #Titulo de pagina
    st.title('Estimación del despliegue')


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
        <div class="sidebar-content"><p>En esta sección 'Cálculo Despliegue' están las variables respecto a la
        puesta en producción del modelo, ya que si ya el tiempo de desarrollo entre una API REST y una Web App
        desarrollada en Streamlit es distinto, sobretodo si se incluye el tipo de modelo que pone en producción.
        <p/></div>
        """,
        unsafe_allow_html=True
    )


#======================================================= PRECIO POR DESPLIEGUE DE API



    selected_deploy_service = st.radio("Seleccione un tipo de despliegue", ["Web App", "Despliegue de API", 'Dashboard PowerBI'])

    # Definir las tarifas de servicio por hora
    service_rates_deploy = {
        'Web App': 45,
        'Despliegue de API': 50,
        'Dashboard PowerBI': 42
    }

    # Sección de tamaño del despliegue (radio buttons)
    if selected_deploy_service == "Despliegue de API":
        st.markdown("Despliegue de API")
    
        selected_api_service = st.radio("Seleccione un tipo de modelo", ["Modelo Simple", "Modelo Medio", 'Modelo Avanzado'])
        st.write('Modelo Simple: Predicción y clasificación')
        st.write('Modelo Medio: Análisis de texto, OCR, procesar datos geoespaciales')
        st.write('Modelo Avanzado: Modelos de procesado de imagenes, audio y video')

        # Definir las tarifas de servicio por hora
        api_hours_service = {
            "Modelo Simple": 16,
            "Modelo Medio": 24,
            'Modelo Avanzado': 32
        }


        complex_integration = st.checkbox('Necesito ayuda para integrar la API con mi App')

        if complex_integration:
            complex_integration_policy = 1.20
            st.write('¡No hay problema! Te ayudamos con la integración :grinning:')
        else:
            complex_integration_policy = 1

        # Calculo de precio por desarrollo de API
        deploy_rate_api = service_rates_deploy['Despliegue de API']
        api_hours = (api_hours_service[selected_api_service] * complex_integration_policy)
        total_api_dev = api_hours * deploy_rate_api 




    elif selected_deploy_service == "Web App":
        st.markdown("Despliegue de Web App")
        quantity_streamlit = st.slider('Cantidad de páginas para la Web App', min_value=1, max_value=20, value=1, step=1)

        complex_streamlit = st.checkbox('Necesito que mi Web App tengan usuarios y base de datos')

        if complex_streamlit:
            complex_streamlit_policy = 1.25
            st.write('¡No hay problema! Integraremos tambien el acceso a usuarios :grinning:')
        else:
            complex_streamlit_policy = 1
    
        # Calculo de precio por desarrollo de Web App
        webapp_basic_hour = 12
        webapp_hour_page = 6
        webapp_hours = ((webapp_basic_hour +(quantity_streamlit * webapp_hour_page)) * complex_streamlit_policy)
        deploy_rate_webapp = service_rates_deploy['Web App']
        total_webapp_dev = webapp_hours * deploy_rate_webapp 




    elif selected_deploy_service == "Dashboard PowerBI":
        st.markdown("Dashboard PowerBI")
        quantity_dashboard = st.slider('Cantidad de páginas para el Dashboard', min_value=1, max_value=20, value=1, step=1)

        complex_dashboard = st.checkbox('Necesito que mi Dashboard se actualice periodicamente')

        if complex_dashboard:
            complex_dashboard_policy = 1.15
            st.write('¡No hay problema! Tu dashboard se actualizará periodicamente :grinning:')
        else:
            complex_dashboard_policy = 1

        # Calculo de precio por desarrollo de Dashboard PowerBI
        powerbi_basic_hour = 6
        powerbi_hour_page = 4
        powerbi_hours = (powerbi_basic_hour + (quantity_dashboard * powerbi_hour_page) * complex_dashboard_policy)
        deploy_rate_powerbi = service_rates_deploy['Web App']
        total_powerbi_dev = powerbi_hours * deploy_rate_powerbi


    else:
        st.write('Ha ocurrido un error')




#======================================================= CALCULO DE PRECIO Y TIEMPO POR DESPLIEGUE


    if selected_deploy_service == "Despliegue de API":
        st.subheader("Estimación de la API sin IVA incluído:")
        st.header(f"{total_api_dev}€")
        st.subheader('El despliegue estará hecho en alrededor de 1 Semana')


    elif selected_deploy_service == "Web App":
        st.subheader("Estimación de la Web App sin IVA incluído:")
        st.header(f"{total_webapp_dev}€")

        if webapp_hours <= 40:
            st.subheader('El despliegue estará hecho en alrededor de 1 Semana')
        elif webapp_hours > 40 and webapp_hours < 80:
            st.subheader('El despliegue estará hecho en alrededor de 2 Semanas')
        elif webapp_hours >= 80 and webapp_hours < 140:
            st.subheader('El despliegue estará hecho en alrededor de 3 Semanas')
        elif webapp_hours >= 140:
            st.subheader('El despliegue estará hecho en alrededor de 1 Mes')


    elif selected_deploy_service == "Dashboard PowerBI":
        st.subheader("Estimación del Dashboard en PowerBI sin IVA incluído:")
        st.header(f"{total_powerbi_dev}€")

        if powerbi_hours <= 40:
            st.subheader('El despliegue estará hecho en alrededor de 1 Semana')
        elif powerbi_hours > 40 and powerbi_hours < 80:
            st.subheader('El despliegue estará hecho en alrededor de 2 Semanas')
        elif powerbi_hours >= 80:
            st.subheader('El despliegue estará hecho en alrededor de 3 Semanas')

    else:
        st.write('Ha ocurrido un error')
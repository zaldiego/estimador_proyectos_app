import streamlit as st
from PIL import Image




def app():
    # Titulo de la aplicación
    st.title("Estimación de modelo")


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
        <div class="sidebar-content"><p>En esta sección 'Cálculo Modelo' está la información relevante referente
        al tipo de análisis o modelo requerido, sin embargo dado que la estimación depende de cada proyecto hemos
        dejado diferentes ejemplos de modelo y análisis para usar de referencia sobre lo que se necesita.
        <p/></div>
        """,
        unsafe_allow_html=True
    )

#======================================================= TEXTO Y SECTORES

    st.write('''En esta sección tenemos varios ejemplos de modelos
        basados en IA por sector, sin embargo lamentablemente esto es más una referencia que una estimación
        real del postencial sobre el valor de desarrollo del proyecto, debido a que nos falta información, 
        cuanta más personalizado sea el modelo, más se alejará el precio respecto a la esto, ya que en esta 
        'Estimación' no incluímos el proceso de investigación, selección y prueba de modelos... En definitiva
        mira esto solo como una referencia de precios y compararlo con el modelo basado en IA que realmente puedas necesitar. ''')
    st.write('')
    st.write('')



    st.subheader('Modelos de referencia')
    selected_sector = st.radio("Seleccione un sector", ["Marketing y Ventas", "Industrial", 'Financiero', 'Seguridad', 'Salud', 'Educación'])

    sector = {
        'Marketing y Ventas': 45,
        'Industrial': 47,
        'Financiero': 45,
        'Seguridad':42,
        'Salud':47,
        'Educación':42
    }


#=================================================== MODELOS MARKETING Y VENTAS

    if selected_sector=='Marketing y Ventas':
        selected_model = st.radio(
        'Escoge una solución basada en IA:',
        ['Lead Scoring', 'Predicción de ventas', 'Análisis de sentimiento de marca', 'Deserción de clientes o usuarios',
        'Segmentación de Leads', 'Algoritmo de recomendación de producto'])

        model_hours_service = {
            'Lead Scoring':35, 
            'Predicción de ventas':40,
            'Análisis de sentimiento de marca':40,
            'Deserción de clientes o usuarios':45,
            'Segmentación de Leads':35,
            'Algoritmo de recomendación de producto':45
        }


        complex_model = st.checkbox('Lo que necesito es parecido, pero con algunos cambios')

        if complex_model:
            complex_model_policy = 1.20
            st.write('¡No hay problema! Desarrollaremos lo que mejor se adapte a tus necesidades de negocio :grinning:')
        else:
            complex_model_policy = 1

        # Calculo de precio por desarrollo del modelo
        model_rate = sector['Marketing y Ventas']
        model_hours = (model_hours_service[selected_model] * complex_model_policy)
        total_model_dev = model_hours * model_rate

#============================================================ MODELOS INDUSTRIAL

    elif selected_sector=='Industrial':
        selected_model = st.radio(
        'Escoge una solución basada en IA:',
        ['Detección de producto defectuoso', 'Mantenimiento predictivo', 'Predicción de demanda', 'Monitorización de energía',
        'Sistema de gestión de inventario', 'Modelo de mejora en ruta de suministros', 'Control de productos en etiquetado'])

        model_hours_service = {
            'Detección de producto defectuoso':50, 
            'Mantenimiento predictivo':45,
            'Predicción de demanda':35,
            'Monitorización de energía':35,
            'Sistema de gestión de inventario':40,
            'Modelo de mejora en ruta de suministros':55,
            'Control de productos en etiquetado':35,
        }


        complex_model = st.checkbox('Lo que necesito es parecido, pero con algunos cambios')

        if complex_model:
            complex_model_policy = 1.20
            st.write('¡No hay problema! Desarrollaremos lo que mejor se adapte a tus necesidades de negocio :grinning:')
        else:
            complex_model_policy = 1

        # Calculo de precio por desarrollo del modelo
        model_rate = sector['Industrial']
        model_hours = (model_hours_service[selected_model] * complex_model_policy)
        total_model_dev = model_hours * model_rate


#============================================================ MODELOS FINANCIERO


    elif selected_sector=='Financiero':
        selected_model = st.radio(
        'Escoge una solución basada en IA:',
        ['Detección de fraude', 'Sistema de evaluación crediticia', 'Predicción de valoración de activo', 'Predicción de ingresos y gastos',
        'Análisis de sentimiento de noticias y eventos', 'Generador de resúmenes financieros', 'Extracción de datos en documentos'])

        model_hours_service = {
            'Detección de fraude':55, 
            'Sistema de evaluación crediticia':50, 
            'Predicción de valoración de activo':45,
            'Predicción de ingresos y gastos':30,
            'Análisis de sentimiento de noticias y eventos':50,
            'Generador de resúmenes financieros':40,
            'Extracción de datos en documentos':35
        }


        complex_model = st.checkbox('Lo que necesito es parecido, pero con algunos cambios')

        if complex_model:
            complex_model_policy = 1.20
            st.write('¡No hay problema! Desarrollaremos lo que mejor se adapte a tus necesidades de negocio :grinning:')
        else:
            complex_model_policy = 1

        # Calculo de precio por desarrollo del modelo
        model_rate = sector['Financiero']
        model_hours = (model_hours_service[selected_model] * complex_model_policy)
        total_model_dev = model_hours * model_rate

#============================================================ MODELOS SEGURIDAD



    elif selected_sector=='Seguridad':
        selected_model = st.radio(
        'Escoge una solución basada en IA:',
        ['Extracción de matrículas', 'Predicción de riesgos laborales', 'Modelo de reconocimiento facial', 'Modelo de análisis de Logs',
        'Detección de objetos en video', 'Modelo de análisis de correos y chats', 'Sistema de autenticación de usuario por voz'])

        model_hours_service = {
            'Extracción de matrículas':35, 
            'Predicción de riesgos laborales':45, 
            'Modelo de reconocimiento facial':60,
            'Modelo de análisis de Logs':50,
            'Detección de objetos en video':50,
            'Modelo de análisis de correos y chats':45,
            'Sistema de autenticación de usuario por voz':40
        }


        complex_model = st.checkbox('Lo que necesito es parecido, pero con algunos cambios')

        if complex_model:
            complex_model_policy = 1.20
            st.write('¡No hay problema! Desarrollaremos lo que mejor se adapte a tus necesidades de negocio :grinning:')
        else:
            complex_model_policy = 1

        # Calculo de precio por desarrollo del modelo
        model_rate = sector['Seguridad']
        model_hours = (model_hours_service[selected_model] * complex_model_policy)
        total_model_dev = model_hours * model_rate

#============================================================ MODELOS SALUD


    elif selected_sector=='Salud':
        selected_model = st.radio(
        'Escoge una solución basada en IA:',
        ['Detección de anomalías cardíacas', 'Detección de enfermedades en radiografías', 'Clasificación automática de pacientes', 'Análisis de biomarcadores',
        'Predicción temprana de enfermedades', 'Optimización de horario en personal médico', 'Generador de resúmenes médicos'])

        model_hours_service = {
            'Detección de anomalías cardíacas':50, 
            'Detección de enfermedades en radiografías':60, 
            'Clasificación automática de pacientes':45,
            'Análisis de biomarcadores':40,
            'Predicción temprana de enfermedades':60,
            'Optimización de horario en personal médico':40,
            'Generador de resúmenes médicos':40,
        }


        complex_model = st.checkbox('Lo que necesito es parecido, pero con algunos cambios')

        if complex_model:
            complex_model_policy = 1.20
            st.write('¡No hay problema! Desarrollaremos lo que mejor se adapte a tus necesidades de negocio :grinning:')
        else:
            complex_model_policy = 1

        # Calculo de precio por desarrollo del modelo
        model_rate = sector['Salud']
        model_hours = (model_hours_service[selected_model] * complex_model_policy)
        total_model_dev = model_hours * model_rate

#============================================================ MODELOS EDUCACIÓN


    elif selected_sector=='Educación':
        selected_model = st.radio(
        'Escoge una solución basada en IA:',
        ['Generador de audiolibros', 'Predicción de rendimiento acádemico', 'Generador de resúmenes', 'Evaluación automática de pruebas por fotos',
        'Detección de plagio en pruebas', 'Traducción de lenguaje de señas', 'Predicción de deserción estudiantil'])

        model_hours_service = {
            'Generador de audiolibros':50, 
            'Predicción de rendimiento acádemico':40, 
            'Generador de resúmenes':35,
            'Evaluación automática de pruebas por fotos':50,
            'Detección de plagio en pruebas':40,
            'Traducción de lenguaje de señas':60,
            'Predicción de deserción estudiantil':40
        }


        complex_model = st.checkbox('Lo que necesito es parecido, pero con algunos cambios')

        if complex_model:
            complex_model_policy = 1.20
            st.write('¡No hay problema! Desarrollaremos lo que mejor se adapte a tus necesidades de negocio :grinning:')
        else:
            complex_model_policy = 1

        # Calculo de precio por desarrollo del modelo
        model_rate = sector['Educación']
        model_hours = (model_hours_service[selected_model] * complex_model_policy)
        total_model_dev = model_hours * model_rate



#============================================================ CALCULO DEL MODELO
    else:
        st.write('Ha ocurrido un error')



    st.subheader("Estimación de la Modelo sin IVA incluído:")
    st.header(f"{total_model_dev}€")



    if model_hours <= 40:
        st.subheader('El modelo estará acabado en alrededor de 1 Semana')

    elif model_hours > 40 and model_hours < 80:
        st.subheader('El modelo estará acabado en alrededor de 2 Semanas')

    elif model_hours >= 80 and model_hours < 120:
        st.subheader('El modelo estará acabado en alrededor de 3 Semanas')

    else:
        st.write('Ha ocurrido un error')
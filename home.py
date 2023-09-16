import streamlit as st

from PIL import Image



def app():
    #Titulo de pagina
    st.title('Bienvenid@ al "Estimador de Proyectos de Neural Batch" :sparkles:')

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


#======================================================= INFORMACION EN HOMEPAGE

    image_homepage = Image.open('calculator_image_1.jpg')
    st.image(image_homepage)


    st.header('¿Que es el "Estimador de proyectos"?')
    st.write('''Es una calculadora que está pensada para todos aquellos que quieran saber cuanto
         podría costar su proyecto de Machine Learning. Aquí podrás ir probando página por página 
         según nuestro criterio, encontrarás una serie de datos y variables que bajo nuestro
         criterio son relevantes para estimar un valor aproximado para el desarrollo de un
         proyecto de Machine / Deep Learning de principio a fin. ''')


    st.header('¿Como usar esta calculdora?')
    st.write('''Para poder usar esta calculadora solo se necesitan algunos datos que debes saber sobre
         lo que quisieras que hicieramos. Simplemente es ir probando según lo que sepas del proyecto
         e ir agregandolo en los botones, slides y poco más.''')
    st.write('')
    st.write('''Dado que en esta calculadora no guardamos ningún tipo de datos (No es un formulario) es
         importante que conforme la calculadora te de un precio aproximado en una sección, lo anotes
         en algún sitio ya que luego necesitarás ese monto aproximado para la sección de Costo Total,
         en dicha sección deberás colocar lo anotado en las otras secciones Cálculo Extracción o Cálculo
         Modelo, y con esa información en Costo Total podrás ir sumando los presupuestos de distintas
         fases (secciones) del proyecto.''')


    st.header('¿Que son las secciones de "Cálculo"?')
    st.write('''Las secciones de cálculo son 4: Extracción, Modelo y Despliegue se refieren a las fases generales
         en el que se desarrolla un proyecto de Machine / Deep Learning. Mientras que la última "Cálculo Total"
         se refiere a la suma de todas las fases anteriores. Si por ejemplo ya tuvieses desarrollado un proyecto
         de Deep Learning entrenado y testeado pero quisieras hacer solo el despliegue mediante una Web App, entonces
         solo necesitas rellenar los datos de la sección "Cálculo Despliegue" ya que ese es el único presupuesto
         que necesitas para finalizar tu proyecto de Deep Learning ¿A que es algo intuitivo :grinning:?''')





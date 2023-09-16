import streamlit as st



def app():


    #Titulo de pagina
    st.title('Presupuesto total del proyecto')


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
        <div class="sidebar-content"><p>En esta sección 'Cálculo Total' podrá ver el costo total del proyecto basado
        en el resultado de las otras secciones para sumar el resultado total, o su vez interactuar con esto para tener
        una referencia sobre el costo total del proyecto.
        <p/></div>
        """,
        unsafe_allow_html=True
    )



#=============================================================== CALCULO TOTAL

    int_val_ex = st.slider('Presupuesto en fase de EXTRACCIÓN', min_value=0, max_value=30500, value=800, step=100)
    int_val_md = st.slider('Presupuesto en fase de MODELO', min_value=0, max_value=10000, value=600, step=20)
    int_val_dp = st.slider('Presupuesto en fase de DESPLIEGUE', min_value=0, max_value=7500, value=1000, step=50)


    costo_total = int_val_ex + int_val_md + int_val_dp


    st.subheader("Estimación del proyecto sin IVA incluído:")
    st.header(f"{costo_total}€")
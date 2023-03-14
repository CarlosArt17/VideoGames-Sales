import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title('VideoGames Sales')


DATA_URL=('dato.csv')
videogames_data = pd.read_csv(DATA_URL)

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows ,index_col=0, encoding='latin-1')
    return data

def load_data_byname(name):
    data = pd.read_csv(DATA_URL,index_col=0, encoding='latin-1')
    filtered_data_byname = data[data['Publisher'].str.contains(name, case = False)]
    return filtered_data_byname

def load_data_byscore(score):
    data = pd.read_csv(DATA_URL, index_col=0, encoding='latin-1')
    filtered_data_byscore = data[data[ 'Critic_Score_Class' ] == score]
    return filtered_data_byscore

data_load_state = st.text('Carlos Arturo Jose Fragoso - zS20006730@estudiantes.uv.mx')
data = load_data(500)
st.header("Ventas")



st.sidebar.image("logo.png")

sidebar = st.sidebar
agree = sidebar.checkbox("Mostrar todos las las ventas")
if agree:
  st.dataframe(data)

myname = sidebar.text_input('Nombre de la compañia :')
btnRange = sidebar.button('Buscar compañia')
if (myname):
    if (btnRange):
        filterbyname = load_data_byname(myname)
        count_row = filterbyname.shape[0]
        st.write(f"Buscar compañia : {count_row}")
        st.dataframe(filterbyname)


selected_score = sidebar.selectbox("Seleccionar puntaje: ", data ['Critic_Score_Class'].unique())
btnFilterbyScore = sidebar.button('Filtrar por puntaje')
if (btnFilterbyScore):
    filterbyScore = load_data_byscore(selected_score)
    count_row = filterbyScore.shape[0]
    st.write(f"Total items : {count_row}")
    st.dataframe(filterbyScore)

agree2 = sidebar.checkbox("Mostrar histograma de clasificacion")
if agree2:
    fig, ax = plt.subplots()
    ax.hist(videogames_data["Rating"], bins="auto")
    st.header("Histograma de clasificacion de los videojuegos")
    st.pyplot(fig)
    st.text("Este histograma muestra el total de los juegos con su diferente clasificacion")
    st.markdown("___")

agree3 = sidebar.checkbox("Mostrar grafica de barras de clasificacion")
if agree3:
    fig2, ax2 = plt.subplots()
    data = load_data(50)
    y_pos = data['Publisher']
    x_pos = data['Rating']
    ax2.barh(y_pos, x_pos)
    plt.xticks(rotation=90)
    ax2.set_ylabel("Publisher")
    ax2.set_xlabel("Rating")
    ax2.set_title('')
    st.header("Grafica de Barras de para representar la clasificacion de desarrollo")
    st.pyplot(fig2)
    st.caption("Esta grafica representa hasta que clasificacion de videojuegos las compañias desarrollan estos mismos")

agree4 = sidebar.checkbox("Mostrar grafica de scatter de clasificacion")
if agree4:
    fig3, ax3 = plt.subplots()
    data = load_data(500)
    ax3.scatter(data.Critic_Score_Class, data.Rating)
    ax3.set_xlabel("Puntaje")
    ax3.set_ylabel("Clasificacion")
    st.header("Grafica de Dispersión VideoGames Sales")
    st.caption("Esta grafica representa, que califiacion tienen las diferentes clasificaciones de los videojuegos")
    st.pyplot(fig3)




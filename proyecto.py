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

fig2, ax2 = plt.subplots()
data = load_data(10)
y_pos = data['Rating']
x_pos = data['Publisher']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("NA_Sales")
ax2.set_xlabel("EU_Sales")
ax2.set_title('')
st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)


df = pd.read_csv('dato.csv')

# Step 3: Filter data by company
company_name = 'Nintendo' # Replace with desired company name
df_filtered = df.loc[df['Publisher'] == company_name]

# Step 4: Create scatter plot
plt.scatter(df_filtered['Publisher'], df_filtered['Global_Sales'])

# Step 5: Add labels to plot
plt.xlabel('Column 1')
plt.ylabel('Column 2')

# Step 6: Add title to plot
plt.title('Scatter plot of {} data'.format(company_name))

# Step 7: Display plot
st.pyplot(plt)






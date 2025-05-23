
import pandas as pd
import streamlit as st
@st.cache_data  # optionnel mais recommandé pour ne pas recharger à chaque interaction
def load_data(path):
    return pd.read_csv(path)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv")


st.title("Bienvenue sur le site web de Aurélie ")
st.text("Indiquez votre arrondissement de pick-up")
zones = df["pickup_borough"].unique()
selection = st.selectbox("Choisissez une ou plusieurs zones :", zones, key="pickup_borough",)

st.write("Tu as choisis:", selection)

if selection == 'nan':
    st.image("https://arbuz.com/wp-content/uploads/2019/04/Easy-Naan-Recipe.jpg", caption="Naan")
elif selection == 'Brooklyn':
    st.image("https://bonjournewyork.fr/wp-content/uploads/2020/06/quartier-brooklyn-new-york.jpg", caption="Brooklyn")
elif selection == 'Queens':
    st.image("https://bonjournewyork.fr/wp-content/uploads/2021/04/queens-new-york.jpg", caption="Queens")
elif selection == 'Manhattan':
    st.image("https://media.cnewyork.net/resize/uploads/2023/05/manhattan-new-york-1392x0.jpg?format=auto&quality=80&width=1200&height=630", caption="Manhattan")
elif selection == 'Bronx':
    st.image("https://evasion-online.com/images/2016/10/BronxPhoto_3.jpg", caption="Bronx")

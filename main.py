import streamlit as st
from menu import Menu

menu = Menu()
menu.iniciar_menu(st)

with st.container():
    st.write("Bienvenida")
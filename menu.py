class Menu:

    def iniciar_menu(self, st):
        st.sidebar.page_link("main.py", label="Home", icon="🏠")
        st.sidebar.page_link("pages/variables.py", label="Variables", icon="🏠")
        st.sidebar.page_link("pages/modelo.py", label="Modelo", icon="🏠")
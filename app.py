import streamlit as st
import os
from PIL import Image

# Ruta de la carpeta "assets" donde están las imágenes
assets_path = 'C:/Users/Sharon/Desktop/Test_fotos/assets'

# Título de la app
st.title("Testing Up Photos")

# Usa session_state para mantener el estado del botón
if 'show_images' not in st.session_state:
    st.session_state.show_images = False  # Iniciar con las imágenes ocultas

# Listar todas las imágenes en la carpeta assets
images_list = [f for f in os.listdir(assets_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Función para mostrar las imágenes
def mostrar_imagenes():
    for image_name in images_list:
        img = Image.open(os.path.join(assets_path, image_name))
        st.image(img, caption=image_name, use_container_width=True)

# Botón para alternar mostrar/ocultar imágenes
if st.button('Mostrar fotos'):
    st.session_state.show_images = not st.session_state.show_images  # Alterna el estado

# Si el estado es True, muestra las imágenes, si es False, no las muestra
if st.session_state.show_images:
    mostrar_imagenes()


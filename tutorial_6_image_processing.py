
import streamlit as st
import numpy as np
from PIL import Image, ImageEnhance

def main():
    st.title("Image Processing with Sliders")
    
    uploaded_image = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Original Image.", use_column_width=True)
        
        brightness = st.slider("Brightness", 0.0, 2.0, 1.0)
        enhancer = ImageEnhance.Brightness(image)
        image_enhanced = enhancer.enhance(brightness)
        
        st.image(image_enhanced, caption="Processed Image.", use_column_width=True)

if __name__ == '__main__':
    main()

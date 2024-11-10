import streamlit as st
from PIL import Image
import io
import os

# Title
st.title("Image Converter")

# Upload image
st.subheader("Upload Image")
uploaded_image = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg", "gif", "bmp"])

# Select output format
st.subheader("Select Output Format")
output_format = st.selectbox("Output Format", ["JPG", "PNG", "JPEG", "GIF", "BMP"])

# Convert image function
def convert_image(image, output_format):
    img = Image.open(image)
    output_buffer = io.BytesIO()
    img.save(output_buffer, format=output_format.lower())
    return output_buffer.getvalue()

# Download converted image
def download_image(image_data, output_format):
    st.download_button("Download Converted Image", image_data, file_name=f"converted_image.{output_format.lower()}")

# Main logic
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image")
    if st.button("Convert Image"):
        image_data = convert_image(uploaded_image, output_format)
        download_image(image_data, output_format)
        st.success("Image converted successfully!")

# Additional options
st.subheader("Additional Options")
resize_image = st.checkbox("Resize Image")
if resize_image:
    width = st.number_input("Width", min_value=100, max_value=1000, value=800)
    height = st.number_input("Height", min_value=100, max_value=1000, value=600)

    def resize_image_func(image, width, height):
        img = Image.open(image)
        img = img.resize((width, height))
        output_buffer = io.BytesIO()
        img.save(output_buffer, format=output_format.lower())
        return output_buffer.getvalue()

    if st.button("Resize and Convert Image"):
        image_data = resize_image_func(uploaded_image, width, height)
        download_image(image_data, output_format)
        st.success("Image resized and converted successfully!")

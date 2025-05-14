import streamlit as st # type: ignore
from rembg import remove # type: ignore
from PIL import Image # type: ignore

import io

def remove_background(image_path):
    """Remove background from the image using rembg."""
    input_image = Image.open(image_path)
    img_byte_array = io.BytesIO()
    input_image.save(img_byte_array, format='PNG')
    img_byte_array = img_byte_array.getvalue()
    
    # Use rembg to remove background
    output = remove(img_byte_array)
    output_image = Image.open(io.BytesIO(output))
    
    return output_image

def add_background(image, bg_color):
    """Add a background color to the image."""
    img_width, img_height = image.size
    # Create a new image with the chosen background color
    background = Image.new("RGBA", (img_width, img_height), bg_color)
    # Paste the image on top of the background
    background.paste(image, (0, 0), image)
    return background

def generate_professional_image(image, bg_color):
    """Generate and display professional LinkedIn image."""
    final_image = add_background(image, bg_color)
    st.image(final_image, caption="Your Professional LinkedIn Profile Picture", use_container_width=True)
    
    # Save the image to a BytesIO object for download
    img_byte_array = io.BytesIO()
    final_image.save(img_byte_array, format="PNG")
    img_byte_array.seek(0)
    return img_byte_array

# Streamlit interface
st.title("LinkedIn Profile Picture Generator")

# Upload image
uploaded_file = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])

# Background color options
bg_color = st.color_picker("Pick a background color", "#FFFFFF")  # Default white background

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    if st.button("Generate Professional LinkedIn Picture"):
        # Process the image (remove background, add background color)
        processed_image = remove_background(uploaded_file)
        if processed_image:
            final_image_byte_array = generate_professional_image(processed_image, bg_color)  # Add background color and show final image
            
            # Provide a download button for the final image
            st.download_button(
                label="Download LinkedIn Profile Picture",
                data=final_image_byte_array,
                file_name="linkedin_profile_picture.png",
                mime="image/png"
            )

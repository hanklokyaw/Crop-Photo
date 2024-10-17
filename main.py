import os
from PIL import Image


def crop_white_space(image_path, output_path):
    """Crop white space from the top and bottom of an image."""
    with Image.open(image_path) as img:
        # Convert image to RGBA
        img = img.convert("RGBA")

        # Get the bounding box of the non-white pixels
        bbox = img.getbbox()

        if bbox:
            # Crop the image to the bounding box
            cropped_img = img.crop(bbox)
            cropped_img.save(output_path)  # Save the cropped image
            print(f"Cropped and saved: {output_path}")


def process_images(input_directory, output_directory):
    """Process all images in the input directory."""
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)

            crop_white_space(input_path, output_path)


if __name__ == '__main__':
    # Specify the input and output directories
    input_directory = 'product_photos'
    output_directory = 'cropped_photos'

    process_images(input_directory, output_directory)

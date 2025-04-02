from PIL import Image
import os


def crop_image(image_path, output_path):
  
    image = Image.open(image_path).convert("RGBA")
    
   
    bbox = image.getbbox()
    
    if bbox:
        # crop to bbox (end crop at non zero pixel)
        cropped_image = image.crop(bbox)
        cropped_image.save(output_path)
        print(f"Cropped image saved to {output_path}")
    else:
        print(f"No non-transparent area found in {image_path}.")

# batch
def batch_crop_images(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            crop_image(input_path, output_path)

if __name__ == '__main__':
    batch_crop_images('{input directory}', '{output directory}')

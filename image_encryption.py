from PIL import Image
import random

def load_image(path):
    return Image.open(path)

def save_image(image, path):
    image.save(path)

def get_pixel_data(image):
    return list(image.getdata())

def set_pixel_data(image, pixel_data):
    image.putdata(pixel_data)
    return image

def swap_pixels(pixel_data, num_swaps=1000):
    width, height = image.size
    for _ in range(num_swaps):
        pos1 = random.randint(0, len(pixel_data) - 1)
        pos2 = random.randint(0, len(pixel_data) - 1)
        pixel_data[pos1], pixel_data[pos2] = pixel_data[pos2], pixel_data[pos1]
    return pixel_data

def apply_math_operation(pixel_data, operation='add', value=50):
    new_pixel_data = []
    for pixel in pixel_data:
        if operation == 'add':
            new_pixel = tuple((p + value) % 256 for p in pixel)
        elif operation == 'sub':
            new_pixel = tuple((p - value) % 256 for p in pixel)
        elif operation == 'xor':
            new_pixel = tuple(p ^ value for p in pixel)
        new_pixel_data.append(new_pixel)
    return new_pixel_data

def encrypt_image(image, operation='add', value=50, num_swaps=1000):
    pixel_data = get_pixel_data(image)
    pixel_data = apply_math_operation(pixel_data, operation, value)
    pixel_data = swap_pixels(pixel_data, num_swaps)
    encrypted_image = set_pixel_data(image, pixel_data)
    return encrypted_image

if __name__ == "__main__":
    image_path = 'E:\Sem 4\SkillCraft\image.jpg'  #add image path
    image = load_image(image_path)
    encrypted_image = encrypt_image(image, operation='xor', value=100, num_swaps=5000)
    encrypted_image_path = 'encrypted_image.jpg'
    save_image(encrypted_image, encrypted_image_path)
    print(f"Encrypted image saved at {encrypted_image_path}")


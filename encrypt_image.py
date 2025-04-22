from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    
    width, height = img.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    print("Image encrypted and saved to", output_path)

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    
    width, height = img.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    print("Image decrypted and saved to", output_path)

encrypt_image('original_image.png', 'encrypted_image.png', key=50)
decrypt_image('encrypted_image.png', 'decrypted_image.png', key=50)


from PIL import Image, ImageFilter, ImageDraw
import os
from colorama import Fore, Style

def create_rounded_mask(size, coords, radius=30):
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    
    for coord in coords:
        x1, y1, x2, y2 = [int(c) for c in coord]
        # Dessiner un rectangle avec coins arrondis
        draw.rounded_rectangle(
            [x1, y1, x2, y2],
            radius=radius,
            fill=255
        )
    return mask

def modify_image(image_path, output_folder, coords, blur_radius=25):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    image = Image.open(image_path)
    # Créer une copie pour le floutage
    blur_layer = image.copy()
    # Appliquer le flou Gaussien
    blur_layer = blur_layer.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    
    # Créer un masque pour le floutage
    mask = Image.new('L', image.size, 0)
    
    # pixels = image.load()
    width, height = image.size
    basename = os.path.basename(image_path)

    mask = create_rounded_mask(image.size, coords, radius=30)

    # Fusionner l'image originale et la version floutée selon le masque
    result = Image.composite(blur_layer, image, mask)
    
    # Sauvegarder le résultat
    basename = os.path.basename(image_path)
    result.save(os.path.join(output_folder, basename))
    
    print(f"{Fore.GREEN}Image sauvegardé dans {output_folder}/{basename}{Style.RESET_ALL}")
    
    # Libérer la mémoire
    image.close()
    blur_layer.close()
    mask.close()
    result.close()
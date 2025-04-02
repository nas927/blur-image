import cv2
import os
from colorama import Fore, Style

def video_to_frames(video_path, output_folder):  
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Ouvrir la vidéo
    video = cv2.VideoCapture(video_path)

    print(Fore.CYAN + "Lecture de la vidéo : " + video_path + Style.RESET_ALL)
    
    # Vérifier si la vidéo est ouverte correctement
    if not video.isOpened():
        print(Fore.RED + "Erreur: Impossible d'ouvrir la vidéo" + Style.RESET_ALL)
        return
    
    # Initialiser le compteur d'images
    count = 0
    
    # Lire la vidéo frame par frame
    while True:
        # Lire une frame
        success, frame = video.read()
        
        # Sortir de la boucle si la vidéo est terminée
        if not success:
            break
        
        # Sauvegarder la frame comme image
        frame_path = os.path.join(output_folder, f"frame_{count:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        count += 1
        
        # Afficher la progression
        if count % 100 == 0:
            print(f"{Fore.CYAN}Images extraites: {count}{Style.RESET_ALL}")
    
    # Fermer la vidéo
    video.release()
    print(f"{Fore.GREEN}Extraction terminée. {count} images ont été extraites.{Style.RESET_ALL}")

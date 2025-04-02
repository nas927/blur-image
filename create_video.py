import cv2
import os
from moviepy import ImageSequenceClip, AudioFileClip
from bot import bot
from images_modify import modify_image
from colorama import Fore, Back, Style

def create_video_from_frames(images_folder, audio_path, output_path, fps=30):
    # Obtenir la liste des images
    images = sorted([img for img in os.listdir(images_folder) if img.endswith(".jpg")])
    if not images:
        raise Exception("Aucune image trouvée dans le dossier")
    
    image_paths = [os.path.join(images_folder, img) for img in images]
    modified_folder = "extractions/dist_images"
    for index, img in enumerate(image_paths):
        print(f"{Back.GREEN}{Fore.BLACK}Frame n°{str(index)}{Style.RESET_ALL}")
        coords = bot(img)
        modify_image(img, modified_folder, coords)
    image_paths = [os.path.join(modified_folder, img) for img in images]
    
    video_clip = ImageSequenceClip(image_paths, fps=fps)
    
    if os.path.exists(audio_path):
        audio_clip = AudioFileClip(audio_path)
        final_clip = video_clip.with_audio(audio_clip)
    else:
        final_clip = video_clip
        print("Attention: Fichier audio non trouvé")
    
    final_clip.write_videofile(
        output_path,
        codec='libx264',
        audio_codec='aac',
        fps=fps,
        # bitrate="8000k",  # Bitrate vidéo élevé
        # audio_bitrate="320k",  # Bitrate audio élevé
        preset='slower',  # Compression plus lente mais meilleure qualité
        threads=6,  # Utilisation de plusieurs threads
        ffmpeg_params=[
            "-crf", "15",  # Facteur de qualité constant (0-51, plus bas = meilleure qualité)
            "-profile:v", "high",  # Profile d'encodage haute qualité
            "-level", "4.2",  # Niveau de compatibilité
            "-pix_fmt", "yuv420p",  # Format de pixel standard
        ]
    )
    
    final_clip.close()
    if 'audio_clip' in locals():
        audio_clip.close()
        
        
# create_video_from_frames("extractions/images", "extractions/audio/audio.mp3", "test.mp4")
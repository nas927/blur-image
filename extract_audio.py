import os
from moviepy import VideoFileClip
from colorama import Fore, Style

def extract_audio(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    audio_path = os.path.join(output_folder, "audio.mp3")
    
    try:
        # Charger la vidéo avec moviepy
        video_clip = VideoFileClip(video_path)
        # Extraire l'audio
        audio_clip = video_clip.audio
        # Sauvegarder l'audio
        audio_clip.write_audiofile(
            audio_path,
            bitrate="320k",  # Bitrate audio maximum pour MP3
            fps=48000,       # Fréquence d'échantillonnage élevée
            nbytes=4,        # Profondeur de bits élevée
            ffmpeg_params=[
                "-q:a", "0",  # Qualité maximale pour MP3
                "-codec:a", "libmp3lame",  # Utiliser le codec LAME pour une meilleure qualité
            ]
        )
        # Fermer les clips
        audio_clip.close()
        video_clip.close()
        print(f"{Fore.GREEN}Audio extrait avec succès : {audio_path}{Style.RESET_ALL}")
        return {
            "fps": video_clip.fps,
            "duration": video_clip.duration,
            "size": video_clip.size
        }
    except Exception as e:
        print(f"{Fore.RED}Erreur lors de l'extraction audio : {str(e)}{Style.RESET_ALL}")


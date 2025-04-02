# Work with Python 3.12.6 

import cv2
import os
import sys
import shutil
from extract_video import video_to_frames
from extract_audio import extract_audio
from create_video import create_video_from_frames
from notification_bot import send_telegram
from colorama import init, Fore, Style

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py chemin_vers_video liste des objets à reconnaitre PS: python main.py help to know how to use")
        sys.exit(1)
    if sys.argv[2] == "help":
        print("Argument 1 : chemin de la vidéo")
        print("Argument 2 : Liste des objets séparé par des espaces en ANGLAIS ! exemple : python main.py video.mp4 face glasses hands")
        sys.exit(1)
    init()
    video_path = sys.argv[1]
    output_folder = "extractions"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    video_to_frames(video_path, output_folder + "/images")
    audio = extract_audio(video_path, output_folder + "/audio")
    
    output_video = "video_floutage.mp4"
    create_video_from_frames(
        output_folder + "/images",
        output_folder + "/audio/audio.mp3",
        output_video,
        audio["fps"]
    )
    print(f"{Fore.GREEN}Vidéo reconstruite sauvegardée: {output_video}{Style.RESET_ALL}")
    shutil.rmtree("extractions")
    send_telegram()
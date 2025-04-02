# https://stackoverflow.com/questions/49879993/push-notification-from-python-to-android

import requests
from colorama import Fore, Style

def send_telegram():
    # rechercher dans télégram BotFather
    # envoyer /newbot
    # entrer le nom 
    # le token apparaitra
    token = ""

    # Allez dans settings et définissez un nom d'utilisateur
    # allez dans recherche et tapez RawDataBot avec la photo d'une carte
    # envoyer un message et votre id apparaitra
    # ajoutez un @ ou un - avant l'id si ça ne marche pas comme ça
    chat_id = ""
    url = f"https://api.telegram.org/bot{token}"
    params = {"chat_id": chat_id, "text": "Votre vidéo est prête !"}
    r = requests.get(url + "/sendMessage", params=params)

    try:
        r = requests.get(url + "/sendMessage", params=params)
        
        if r.status_code <= 205:
            print(f"{Fore.GREEN}Message envoyé avec succès !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Erreur : Vérifiez l'ID et le token dans notification_bot.py{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Code d'erreur : {r.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur lors de l'envoi : {str(e)}{Style.RESET_ALL}")
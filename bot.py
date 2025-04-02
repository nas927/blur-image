from PIL import Image
import torch
from transformers import Owlv2Processor, Owlv2ForObjectDetection
import sys
from colorama import Fore, Back, Style

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Utilisation de : {Back.YELLOW}{Fore.WHITE}{device}{Style.RESET_ALL}")

processor = Owlv2Processor.from_pretrained("google/owlv2-base-patch16")
model = Owlv2ForObjectDetection.from_pretrained("google/owlv2-base-patch16")

def bot(img):
    image = Image.open(img)
    texts = [sys.argv[2:]]
    inputs = processor(text=texts, images=image, return_tensors="pt")
    
    # Déplacer les entrées sur le même device que le modèle
    for key in inputs:
        inputs[key] = inputs[key].to(device)
    
    with torch.no_grad():  # Désactiver le calcul des gradients pour l'inférence
        outputs = model(**inputs)

    # Target image sizes (height, width) to rescale box predictions [batch_size, 2]
    target_sizes = torch.Tensor([image.size[::-1]])
    # Convert outputs (bounding boxes and class logits) to COCO API
    results = processor.post_process_grounded_object_detection(outputs=outputs, threshold=0.1, target_sizes=target_sizes)

    i = 0  # Retrieve predictions for the first image for the corresponding text queries
    text = texts[i]
    boxes, scores, labels = results[i]["boxes"], results[i]["scores"], results[i]["labels"]

    # Print detected objects and rescaled box coordinates
    for box, score, label in zip(boxes, scores, labels):
        box = [round(i, 2) for i in box.tolist()]
        print(f"{text[label]} détecté avec sureté de : {round(score.item(), 3)} au coordonnées {box}")
    
    return [box.tolist() for box in boxes]

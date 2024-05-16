import os, sys

folder_path = '/Users/edoardocrosera/Desktop/coding/face_recognition3/faces'

if not os.path.exists(folder_path):
        print("La cartella delle immagini dei volti non esiste.")
        sys.exit()

for image in os.listdir(folder_path):
    print(image)
    image_path = os.path.join(folder_path, image)
    if not os.path.isfile(image_path):
        print(f"Il file {image} non esiste nella cartella {folder_path}.")

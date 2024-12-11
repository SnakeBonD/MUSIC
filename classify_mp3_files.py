import os
import shutil
from mutagen.mp3 import MP3

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def classify_mp3_files(base_path):
    # Chemins pour les sous-dossiers
    low_path = os.path.join(base_path, 'LOW')
    high_path = os.path.join(base_path, 'HIGH')
    
    create_folder(low_path)
    create_folder(high_path)

    artist_counts = {}
    print("Début de la classification des fichiers...")

    # Parcourir les fichiers dans le dossier de base
    for filename in os.listdir(base_path):
        file_path = os.path.join(base_path, filename)
        
        if not filename.endswith('.mp3') or not os.path.isfile(file_path):
            print(f"Fichier ignoré : {filename}")
            continue

        # Lire les métadonnées du fichier MP3
        try:
            audio = MP3(file_path)
            bitrate = audio.info.bitrate // 1000  # En kbits/s
            artist = audio.tags.get('TPE1', None)
            artist_name = artist.text[0] if artist else "Unknown"
        except Exception as e:
            print(f"Erreur en lisant {filename}: {e}")
            continue

        # Classification par débit binaire
        target_folder = high_path if bitrate >= 320 else low_path
        shutil.move(file_path, target_folder)
        print(f"Fichier déplacé : {filename} -> {target_folder}")

        # Compter les occurrences des artistes
        artist_counts[artist_name] = artist_counts.get(artist_name, 0) + 1

    # Créer les dossiers par artiste
    print("Vérification des artistes avec au moins 5 fichiers...")
    for artist, count in artist_counts.items():
        if count >= 5:
            artist_folder = os.path.join(base_path, artist)
            create_folder(artist_folder)
            print(f"Dossier créé pour l'artiste : {artist}")

            # Déplacer les fichiers correspondants
            for folder in [low_path, high_path]:
                for filename in os.listdir(folder):
                    file_path = os.path.join(folder, filename)
                    
                    try:
                        audio = MP3(file_path)
                        file_artist = audio.tags.get('TPE1', None)
                        file_artist_name = file_artist.text[0] if file_artist else "Unknown"
                        if file_artist_name == artist:
                            shutil.move(file_path, artist_folder)
                            print(f"Fichier déplacé : {filename} -> {artist_folder}")
                    except Exception as e:
                        print(f"Erreur en traitant {filename}: {e}")

if __name__ == "__main__":
    base_folder = "MUSIC_MP3"
    if not os.path.exists(base_folder):
        print(f"Le dossier {base_folder} n'existe pas.")
    else:
        classify_mp3_files(base_folder)

import os
import shutil
from mutagen
mp3 import MP3

def create_folder(path):
    # Crée un dossier s'il n'existe pas déjà
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Dossier créé : {path}")

def extract_metadata(file_path):
    """
    Extrait les métadonnées d'un fichier MP3, notamment l'artiste.

    :param file_path: Chemin du fichier MP3
    :return: Nom de l'artiste ou "Unknown" si introuvable
    """
    # Vérifier si le fichier est vide ou corrompu
    if os.path.getsize(file_path) == 0:
        raise ValueError("Fichier vide ou corrompu")

    # Valider la structure MP3 avec mutagen
    audio = MP3(file_path)
    if audio.info is None:
        raise ValueError("Fichier MP3 non valide ou corrompu")

    # Extraire le nom de l'artiste
    artist = audio.tags.get('TPE1', None)  # Obtenir le nom de l'artiste
    return artist.text[0] if artist else "Unknown"

def classify_mp3_files(base_path):
    # Dictionnaire pour stocker les chemins des fichiers par artiste
    artist_files = {}

    print("Début de la classification des fichiers MP3...")

    # Générer une liste paresseuse de fichiers MP3 valides
    mp3_files = (f for f in os.listdir(base_path) if f.endswith('.mp3') and os.path.isfile(os.path.join(base_path, f)))
    
    for filename in mp3_files:
        file_path = os.path.join(base_path, filename)
        print(f"Traitement du fichier : {filename}")

        # Lire les métadonnées du fichier MP3
        try:
            artist_name = extract_metadata(file_path)
            print(f"Artiste : {artist_name}")
        except Exception as e:
            # Gérer les erreurs de lecture des métadonnées
            print(f"Erreur en lisant {filename}: {e}")
            continue

        # Mettre à jour le dictionnaire des fichiers par artiste
        if artist_name not in artist_files:
            artist_files[artist_name] = [file_path]
        else:
            artist_files[artist_name].append(file_path)

    # Créer des dossiers pour les artistes avec au moins 3 fichiers
    for artist, files in artist_files.items():
        print(f"Artiste : {artist}, Nombre de fichiers : {len(files)}")
        if len(files) >= 3:
            artist_folder = os.path.join(base_path, artist)
            create_folder(artist_folder)

            # Déplacer les fichiers associés à cet artiste dans son dossier
            for file_path in files:
                try:
                    print(f"Déplacement de {file_path} vers {artist_folder}")
                    shutil.move(file_path, artist_folder)
                except Exception as e:
                    # Gérer les erreurs lors du déplacement des fichiers
                    print(f"Erreur en traitant {file_path}: {e}")

    print("Classification terminée.")

if __name__ == "__main__":
    # Définir le dossier de base pour la classification
    base_folder = "MUSIC_MP3"
    print(f"Dossier de base : {base_folder}")
    classify_mp3_files(base_folder)

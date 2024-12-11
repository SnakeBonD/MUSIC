# README - Script de classification des fichiers MP3

## Description

Ce script Python permet de classer automatiquement des fichiers MP3 en fonction de deux critères principaux :

1. **Débit binaire (bitrate)** :
   - Les fichiers MP3 avec un débit binaire inférieur à 320 kbits/s sont déplacés dans un sous-dossier `LOW`.
   - Ceux avec un débit binaire supérieur ou égal à 320 kbits/s sont déplacés dans un sous-dossier `HIGH`.
2. **Artistes** :
   - Si au moins 5 fichiers MP3 appartiennent au même artiste, un sous-dossier portant le nom de l'artiste est créé, et ces fichiers y sont déplacés.

---

## Prérequis

Pour utiliser ce script, vous aurez besoin de :

1. **Python** :
   - Assurez-vous que Python 3.8 ou une version plus récente est installé.
   - Ajoutez Python à votre `PATH` pendant l'installation.
2. **Bibliothèque `mutagen`** :
   - Installez la bibliothèque `mutagen` pour lire les métadonnées des fichiers MP3.
   - Commande pour installer `mutagen` :
     ```bash
     pip install mutagen
     ```
3. **Structure des fichiers** :
   - Créez un dossier nommé `MUSIC_MP3` et placez-y tous les fichiers MP3 à traiter.

---

## Instructions d’utilisation

1. **Positionnez-vous dans le répertoire contenant le script** :

   - Par exemple :
     ```bash
     cd C:\chemin\vers\le\script
     ```

2. **Vérifiez la présence du dossier `MUSIC_MP3`** :

   - Placez tous vos fichiers MP3 dans ce dossier avant d’exécuter le script.

3. **Exécutez le script** :

   - Commande :
     ```bash
     python classify_mp3_files.py
     ```

4. **Résultat attendu** :

   - Deux dossiers principaux, `LOW` et `HIGH`, seront créés dans `MUSIC_MP3` pour classer les fichiers selon leur débit binaire.
   - Si un artiste a au moins 5 fichiers, un sous-dossier portant son nom sera créé, et ses fichiers seront déplacés dedans.

---

## Points importants

- Les fichiers sans débit binaire détectable ou sans métadonnées valides seront ignorés.
- En cas d’erreur, un message sera affiché dans la console, mais le script continuera de traiter les autres fichiers.

---

## Exemple de structure après exécution

### Avant :
```
├── classify_mp3_files.py
├── MUSIC_MP3
    ├── fichier1.mp3
    ├── fichier2.mp3
    └── fichierN.mp3
```
### Après :
```
MUSIC_MP3/
├── LOW/
│   ├── chanson1.mp3
│   ├── chanson2.mp3
├── HIGH/
│   ├── artiste1_chanson.mp3
│   ├── artiste1_autre_chanson.mp3
├── Artiste1/
│   ├── artiste1_chanson.mp3
│   ├── artiste1_autre_chanson.mp3
```

---

## Dépannage

### Python introuvable

- Assurez-vous que Python est installé et ajouté au `PATH`.
- Vérifiez l'installation avec :
```bash
  python --version
```
### Aucun fichier classé

- Vérifiez que les fichiers MP3 sont bien placés dans le dossier `MUSIC_MP3`
- Assurez-vous que les fichiers ont des métadonnées correctes.


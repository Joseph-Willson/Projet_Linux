#!/bin/bash

# Activer l'environnement virtuel
source ./venv/Scripts/activate

# Récupérer le fichier JSON avec curl et le placer dans un dossier source
curl -o intents.json "https://raw.githubusercontent.com/Karan-Malik/Chatbot/master/chatbot_codes/intents.json"

# Créer le dossier source s'il n'existe pas
mkdir -p source

# Déplacer le fichier téléchargé dans le dossier source
mv intents.json source/

# Donner des permissions au dossier source
chmod 777 source

"""
#!/bin/bash

# Activer l'environnement virtuel
source ./venv/bin/activate

# Récupérer les données avec curl et les placer dans un dossier source
curl -o data.csv "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"

# Créer le dossier source s'il n'existe pas
mkdir -p source

# Déplacer le fichier téléchargé dans le dossier source
mv data.csv source/

# Donner des permissions au dossier source
chmod 777 source
"""
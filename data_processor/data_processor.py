import pandas as pd

# Chemin relatif du fichier CSV
chemin_du_fichier_csv = "../source/data.csv"

# Lire le fichier CSV avec pandas
df = pd.read_csv(chemin_du_fichier_csv)

# Afficher le contenu du DataFrame
print(df)

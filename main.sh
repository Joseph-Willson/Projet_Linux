echo "******************* Initialisation de l'application *******************"
source ./venv/Scripts/activate


echo "******************* Collecte des données *******************"
bash ./data_collector/collect_data.sh
echo "******************* Données collectées *******************"

echo "******************* Entrainement du modèle de réseau de neuronne *******************"
bash ./data_processor/data_processor.sh
echo "******************* Le modèle à été entrainée avec succées *******************"

echo "******************* Affichage de l'application *******************"
streamlit run ./application/nom_du_fichier.py

# echo "******************* affichage des données *******************"
# bash ./data_processor/data_integrator.sh



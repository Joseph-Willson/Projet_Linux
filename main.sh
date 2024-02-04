echo "******************* Initialisation de l'application *******************"
source ./venv/bin/activate


echo "******************* Collecte des données *******************"
bash ./data_collector/collect_data.sh
echo "******************* Données collectées *******************"


echo "******************* affichage des données *******************"
bash ./data_processor/data_processor.sh



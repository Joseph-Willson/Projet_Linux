import json
import pprint

read_json = "../source/intents.json"
# write_json = "F:/OctopusLab/dev/git/les_fichiers_avec_python/ressources/json/sample2.json"


# In[16]:


# Lire un fichier JSON.
with open(read_json, "r") as json_file:
    data = json.load(json_file)
    print(type(data))
    pprint.pprint(data)
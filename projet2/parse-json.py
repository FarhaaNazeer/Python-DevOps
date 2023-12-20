import json
import os

script_dir = os.path.dirname(__file__)
print("Le script est dans : " + script_dir)

script_absolute_path = os.path.join(script_dir, 'files/example.json')
print("Le chemin du script est  : " + script_absolute_path)

json = json.loads(open(script_absolute_path).read())
value = json['name']
print(value)

for key in json:
	value = json[key]
	print("La clé et valeur sont ({}) = ({})".format(key, value))

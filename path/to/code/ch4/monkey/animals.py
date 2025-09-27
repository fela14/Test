import os
import json

def read_animals_preferences():
    animals_file = os.path.expanduser('~/animals.json')
    with open(animals_file, 'r') as anm:
        pref = json.load(anm)
    return pref

def write_animals_preferences(pref):
    animals_file = os.path.expanduser('~/animals.json')
    with open(animals_file, 'w') as anm:
        json.dump(pref, anm, indent=4)

def write_default_animals_preferences():
    write_animals_preferences(_default_animals)

_default_animals = {
    'dog_family': [
        'german shepherd', 
        'golden retriever',
        "siberian husky"
    ],
    'cat_family': [
        'sphynx',
        'maine coon',
        'siamese'
    ]
}

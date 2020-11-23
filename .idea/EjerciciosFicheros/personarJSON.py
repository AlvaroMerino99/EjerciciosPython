#! /usr/bin/env python
import json


fichero = open("personas.json", 'r', encoding="utf8")
contenido = json.load(fichero)
print(contenido)
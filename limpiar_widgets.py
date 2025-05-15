import json
import sys

archivo = sys.argv[1]

with open(archivo, "r", encoding="utf-8") as f:
    notebook = json.load(f)

if "widgets" in notebook.get("metadata", {}):
    del notebook["metadata"]["widgets"]

with open(archivo, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print(f"Widgets eliminados de {archivo} con éxito.")

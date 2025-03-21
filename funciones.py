import json
from datetime import datetime, timedelta

# Cargar el archivo JSON
with open('fleet_data.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

def listar_disponibles():
    print("\nMotos disponibles:")
    print(f"{'Marca':<15} {'Modelo':<15} {'Año':<6} {'Ciudad':<15}")
    print("-" * 51)
    for ciudad in datos["flota_motocicletas"]["ubicaciones"]:
        for moto in ciudad["flota"].values():
            if moto["disponibilidad"]["estado"] == "Disponible":
                marca = moto["detalles"]["marca"]
                modelo = moto["detalles"]["modelo"]
                año = moto["detalles"]["año"]
                print(f"{marca:<15} {modelo:<15} {año:<6} {ciudad['ciudad']:<15}")

def contar_tipos():
    tipos = {}
    for ciudad in datos["flota_motocicletas"]["ubicaciones"]:
        for moto in ciudad["flota"].values():
            tipo = moto["especificaciones"]["tipo"]
            tipos[tipo] = tipos.get(tipo, 0) + 1
    
    print("\nCantidad de motos por tipo:")
    print(f"{'Tipo':<15} {'Cantidad':<10}")
    print("-" * 25)
    for tipo, cantidad in sorted(tipos.items()):
        print(f"{tipo:<15} {cantidad:<10}")

def buscar_moto():
    marca = input("\nMarca a buscar: ").lower()
    modelo = input("Modelo a buscar (enter para ver todas de la marca): ").lower()
    print("\nResultados:")
    print(f"{'Marca':<15} {'Modelo':<15} {'Ciudad':<15} {'Estado':<15}")
    print("-" * 60)
    encontradas = False
    for ciudad in datos["flota_motocicletas"]["ubicaciones"]:
        for moto in ciudad["flota"].values():
            marca_moto = moto["detalles"]["marca"].lower()
            modelo_moto = moto["detalles"]["modelo"].lower()
            if (modelo == "" and marca_moto == marca) or (marca_moto == marca and modelo_moto == modelo):
                print(f"{moto['detalles']['marca']:<15} {moto['detalles']['modelo']:<15} {ciudad['ciudad']:<15} {moto['disponibilidad']['estado']:<15}")
                encontradas = True
    if not encontradas:
        print("No se encontraron motos con esos criterios.")

def filtrar_motos():
    min_cil = input("\nCilindrada mínima (enter si no importa): ")
    max_cil = input("Cilindrada máxima (enter si no importa): ")
    print("\nMotos que cumplen:")
    print(f"{'Marca':<15} {'Modelo':<15} {'Cilindrada':<15}")
    print("-" * 45)
    encontradas = False
    for ciudad in datos["flota_motocicletas"]["ubicaciones"]:
        for moto in ciudad["flota"].values():
            cil = moto["especificaciones"]["cilindrada_cc"]
            if cil is not None:
                if (min_cil == "" and max_cil == "") or \
                   (min_cil != "" and max_cil == "" and cil >= int(min_cil)) or \
                   (min_cil == "" and max_cil != "" and cil <= int(max_cil)) or \
                   (min_cil != "" and max_cil != "" and int(min_cil) <= cil <= int(max_cil)):
                    print(f"{moto['detalles']['marca']:<15} {moto['detalles']['modelo']:<15} {cil:<15}")
                    encontradas = True
    if not encontradas:
        print("No se encontraron motos con esa cilindrada.")

def mas_alquiladas():
    hoy = datetime(2025, 3, 18)
    ultimo_mes = hoy - timedelta(days=30)
    alquileres = {}
    
    for ciudad in datos["flota_motocicletas"]["ubicaciones"]:
        for moto in ciudad["flota"].values():
            nombre = f"{moto['detalles']['marca']} {moto['detalles']['modelo']}"
            contador = 0
            for alquiler in moto["disponibilidad"]["estadisticas_uso"]["historial_alquileres"]:
                fecha = datetime.strptime(alquiler["fecha_inicio"], "%Y-%m-%d")
                if fecha >= ultimo_mes:
                    contador += 1
            if contador > 0:
                alquileres[nombre] = contador
    
    print("\nMotos más alquiladas último mes:")
    print(f"{'Moto':<30} {'Veces':<10}")
    print("-" * 40)
    for nombre, veces in sorted(alquileres.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"{nombre:<30} {veces:<10}")

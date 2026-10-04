import json


def load_pokemons(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as files:
            return json.load(files)
    except FileNotFoundError:
        return []

def get_new_pokemon():
    print("\nIngresa los datos del nuevo Pokémon:")
    name = input("Nombre: ")
    pokemon_type = input("Tipo (ej. Water, Grass): ")
    level = int(input("Nivel (número entero): "))
    weight_kg = float(input("Peso en kg (número decimal): "))
    
    is_shiny = input("¿Es shiny? (s/n): ").strip().lower() == 's'
    
    held_item_input = input("Objeto equipado (deja en blanco si no tiene): ").strip()
    held_item = held_item_input if held_item_input else None
    
    skills = [skill.strip() for skill in input("Habilidades (separadas por comas): ").split(',')]
    
    print("\n--- Ingresa las estadísticas ---")
    stats = {
        "hp": int(input("HP: ")),
        "attack": int(input("Ataque: ")),
        "defense": int(input("Defensa: ")),
        "sp_attack": int(input("Ataque Especial: ")),
        "sp_defense": int(input("Defensa Especial: ")),
        "speed": int(input("Velocidad: "))
    }
    
    return {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }

def save_pokemons(filepath, pokemons):
    with open(filepath, 'w', encoding='utf-8') as files:
        json.dump(pokemons, files, indent=4, ensure_ascii=False)

def main():
    path = "Pokemon.json"
    pokemons = load_pokemons(path)  
    print(f"--- Se cargaron {len(pokemons)} Pokémon(es) del archivo ---")
    
    new_pokemon = get_new_pokemon()  
    pokemons.append(new_pokemon)
    
    save_pokemons(path, pokemons)
    print(f"\n¡Éxito! El Pokémon ha sido agregado y guardado correctamente en '{path}'.")


if __name__ == "__main__":
    main()


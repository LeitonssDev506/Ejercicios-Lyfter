import csv


def register_videogames():
    bd_games = []
    

    while True:
        try:
            element = int(input('How many games do you want to register (1-100): '))
            if 1 <= element <= 100:
                break
            print('Error: Please enter a number between 1 and 100.')
        except ValueError:
            print("Error: Invalid number. Please try again.")


    for i in range(element):
        print(f"\n--- Registering game {i + 1} ---")
        games_information = {}
        
        # Name validation
        while True:
            try:
                name = input('Name of the game: ').strip()
                if not name:
                    raise ValueError("The name cannot be empty.")
                games_information['name'] = name
                break
            except ValueError as e:
                print(f"Error: {e}")

        # Gender validation
        while True:
            try:
                gender = input('Gender of the game: ').strip()
                if not gender:
                    raise ValueError("The gender cannot be empty.")
                games_information['gender'] = gender
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                developer = input('Developer of the game: ').strip()
                if not developer:
                    raise ValueError("The developer cannot be empty.")
                games_information['Developer'] = developer
                break
            except ValueError as e:
                print(f"Error: {e}")

        valid_esrb = ['E', 'E10+', 'T', 'M', 'AO', 'RP']
        while True:
            try:
                classification = input('Class of the game (E, E10+, T, M, etc.): ').strip().upper()
                if classification not in valid_esrb:
                    raise ValueError(f"Invalid classification. Allowed options: {valid_esrb}")
                games_information['Class'] = classification
                break
            except ValueError as e:
                print(f"Error: {e}")

        bd_games.append(games_information)
    #csv_file = 'videojuegos.csv'
    tsv_file = 'videojuegos.tsv'
    try:
        with open(tsv_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['name', 'gender', 'Developer', 'Class']
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t') # con el parametro delimiter
            
            writer.writeheader()
            writer.writerows(bd_games)
            
        print(f"\nInformation successfully saved to '{tsv_file}'!")
    except Exception as e:
        print(f"An error occurred while saving the CSV file: {e}")

if __name__ == '__main__':
    register_videogames()
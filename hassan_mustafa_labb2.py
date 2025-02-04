import csv
import json

# Konvertera CSV till JSON (körs bara om JSON inte finns)
def save_csv_to_json():
 try:

    with open('studenter_labb2_v25.csv', 'r', encoding='iso-8859-1') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open('studenter_labb2_v25.json', 'w', encoding='iso-8859-1') as f:
        json.dump(rows, f, indent=4, ensure_ascii=False)

 except FileNotFoundError:
     print('csv filen hittades inte')
 except Exception as e:
     print(e)

def add_person_to_json():
    with open('studenter_labb2_v25.json', 'r', encoding='iso-8859-1') as f:
        data = json.load(f)

    förnamn = input('Förnamn: ')
    efternamn = input('Efternamn: ')
    användarnamn = input('Användarnamn: ')

    add_person = {'efternamn': efternamn, 'förnamn': förnamn, 'användarnamn': användarnamn}
    data.append(add_person)

    with open('studenter_labb2_v25.json', 'w', encoding='iso-8859-1') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(' Personen har lagts till i JSON och sparats.')


def remove_person_from_json():
    with open('studenter_labb2_v25.json', 'r', encoding='iso-8859-1') as f:
        data = json.load(f)

    användarnamn = input('Ange personens användarnamn som du vill ta bort: ')

    new_data = [person for person in data if person['användarnamn'] != användarnamn]

    if len(new_data) == len(data):
        print("Ingen person hittades med det användarnamnet.")
        return

    with open('studenter_labb2_v25.json', 'w', encoding='iso-8859-1') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)

    print(' Personen har tagits bort från JSON och sparats.')


def show_current_json():
    with open('studenter_labb2_v25.json', 'r', encoding='iso-8859-1') as f:
        data = json.load(f)

    print(json.dumps(data, indent=4, ensure_ascii=False))  # Formaterad JSON-output


def save_current_json_to_csv():
    with open('studenter_labb2_v25.json', 'r', encoding='iso-8859-1') as f:
        data = json.load(f)

    if not data:
        print(" JSON-filen är tom! Inget att spara.")
        return

    with open('studenter_labb2_v25.csv', 'w', newline='', encoding='iso-8859-1') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

    print("JSON har sparats tillbaka som CSV!")


def menu():

    while True:
        print("\n Meny")
        print("1:spara csv till json")
        print("2: Lägg till en person")
        print("3: Ta bort en person")
        print("4: Visa JSON")
        print("5: Spara JSON till CSV")
        print("6: Avsluta")

        user_choice = input("Välj ett alternativ (1-6): ")

        if user_choice == "1":
            save_csv_to_json()
        elif user_choice == "2":
            add_person_to_json()
        elif user_choice == "3":
            remove_person_from_json()
        elif user_choice == "4":
            show_current_json()
        elif user_choice == "5":
            save_current_json_to_csv()
        elif user_choice == "6":
            print("programmet avslutas")
            break
        else:
            print("Ogiltigt val, försök igen.")



# Kör menyn
menu()

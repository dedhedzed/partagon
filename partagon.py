import csv
import os
import sys
import subprocess
import glob

def choose_option():
    print("Please choose an option:")
    print("1. By year")
    print("2. By engine")
    print("3. By part number")
    print("4. By color code")

    option = input("Enter your choice (1-4): ")
    return option

def handle_year():
    year = int(input("Enter a year: "))

    if year < 1900 or year > 1948:
        print("No VW vans produced in that time.")
    elif 1949 <= year <= 1979:
        print("No Vanagons were made during those years.")
    elif 1980 <= year <= 1985:
        print("Vanagon - Aircooled")
        handle_parts("vanagon_aircooled")
    elif 1986 <= year <= 1991:
        print("Vanagon - Watercooled")
        handle_parts("vanagon_watercooled")

def handle_engine():
    print("Engine option selected.")
    print("Choose an engine:")
    print("1.6L")
    print("1.7L")
    print("1.9L")
    print("2.0L")
    print("2.1L")
    print("3.2L")
    print("3.7L")

    engine_option = input("Enter your choice (1-7): ")
    if engine_option == '1':
        handle_1_6_engine()
    elif engine_option == '2':
        handle_1_7_engine()
    elif engine_option == '3':
        handle_1_9_engine()
    elif engine_option == '4':
        handle_2_0_engine()
    elif engine_option == '5':
        handle_2_1_engine()
    # Add logic for other engine options

def handle_1_6_engine():
    print("Choose fuel type:")
    print("Diesel")
    print("Gasoline")

    fuel_option = input("Enter your choice (D/G): ")
    if fuel_option == 'D':
        print("1.6L Diesel engine selected.")
    elif fuel_option == 'G':
        print("1.6L Gasoline engine selected.")
    else:
        print("Invalid fuel option.")

def handle_1_7_engine():
    print("1.7 litre 54bhp engine selected.")
    handle_parts("1_7")

def handle_1_9_engine():
    print("Choose an engine variant:")
    print("DH 83bhp")
    print("DF 59bhp")
    print("DG 76bhp")
    print("EY 55bhp")
    print("GW 89bhp")

    variant_option = input("Enter your choice (1-5): ")
    if variant_option == 'DH':
        print("1.9L DH 83bhp engine selected.")
        handle_parts("1_9_dh")
    elif variant_option == 'DF':
        print("1.9L DF 59bhp engine selected.")
        handle_parts("1_9_df")
    elif variant_option == 'DG':
        print("1.9L DG 76bhp engine selected.")
        handle_parts("1_9_dg")
    elif variant_option == 'EY':
        print("1.9L EY 55bhp engine selected.")
        handle_parts("1_9_ey")
    elif variant_option == 'GW':
        print("1.9L GW 89bhp engine selected.")
        handle_parts("1_9_gw")
    else:
        print("Invalid option.")

def handle_2_0_engine():
    print("2 litre 70bhp engine selected.")
    handle_parts("2_0")

def handle_2_1_engine():
    print("Choose an engine variant:")
    print("MV 95bhp")
    print("SS 90bhp")
    print("DJ 112bhp")

    variant_option = input("Enter your choice (1-3): ")
    if variant_option == 'MV':
        print("2.1L MV 95bhp engine selected.")
        handle_parts("2_1_mv")
    elif variant_option == 'SS':
        print("2.1L SS 90bhp engine selected.")
        handle_parts("2_1_ss")
    elif variant_option == 'DJ':
        print("2.1L DJ 112bhp engine selected.")
        handle_parts("2_1_dj")
    else:
        print("Invalid option.")

def handle_parts(engine_folder, part_number):
    print("Choose a part type:")
    print("1. Electrical")
    print("2. Mechanical")
    print("3. Body")
    print("4. Fluids")
    print("5. Brakes")
    print("6. Suspension")
    print("7. Camper")

    part_type = input("Enter your choice (1-7): ")

    folder_path = f"{engine_folder}/"
    part_type_files = glob.glob(f"{folder_path}*_{part_type}.csv")

    if not part_type_files:
        print("No part files found for the selected type.")
        return

    for file_path in part_type_files:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            found = False
            for row in csv_reader:
                if row['Part Number'] == part_number or part_number in row['Alternate Part Numbers']:
                    print("Part Information:")
                    print(f"Category Name: {row['Category Name']}")
                    print(f"Alternate Part Numbers: {row['Alternate Part Numbers']}")
                    print(f"Part Name: {row['Part Name']}")
                    print(f"Part Number: {row['Part Number']}")
                    found = True

            if not found:
                print(f"No part information found for part number '{part_number}'.")

    category_names = [
        """
        _______
       |       |
       | Body  |
       |_______|
        """,
        """
        _______
       |       |
       |Mechanic|
       |_______|
        """,
        """
        _______
       |       |
       | Electrical |
       |_______|
        """,
        """
        _______
       |       |
       | Fluids |
       |_______|
        """,
        """
        _______
       |       |
       | Brakes |
       |_______|
        """,
        """
        _______
       |       |
       |Suspension|
       |_______|
        """,
        """
        _______
       |       |
       | Camper|
       |_______|
        """
    ]

    try:
        category_name = category_names[int(part_type) - 1]
        print("Category Name:")
        print(category_name)
        handle_part_number()
    except IndexError:
        print("Invalid part type.")

def handle_part_number():
    part_number = input("Enter a part number: ")

    handle_parts(engine_folder, part_number)  # Add part_number parameter
    engine_folder = get_selected_engine_folder()
    folder_path = f"{engine_folder}/"
    part_type_files = glob.glob(f"{folder_path}*_{part_type}.csv
    
    filename = "part_numbers.csv"
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            found = False
            for row in csv_reader:
if row['Part Number'] == part_number or part_number in row['Alternate Part Numbers']:
                    print("Part Information:")
                    print(f"Category Name: {row['Category Name']}")
                    print(f"Alternate Part Numbers: {row['Alternate Part Numbers']}")
                    print(f"Part Name: {row['Part Name']}")
                    print(f"Part Number: {row['Part Number']}")
                    found = True

            if not found:
                print(f"No part information found for part number '{part_number}'.")

    except FileNotFoundError:
        print(f"Error: Could not find {filename}. Please make sure the file exists.")



def handle_color_code():
    print("Color code option selected.")
    color_code = input("Enter a color code: ")

    filename = "color_codes.csv"
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Color Code'] == color_code:
                    print("Color Information:")
                    print(f"Color Name: {row['Color Name']}")
                    print(f"Years: {row['Years']}")
                    print(f"Alternate Color Codes: {row['Alternate Color Codes']}")
                    return

        print(f"No color information found for color code '{color_code}'.")

    except FileNotFoundError:
        print(f"Error: Could not find {filename}. Please make sure the file exists.")
        
def print_current_screen():
    print("Current Screen:")
    print("===============")
    script_path = sys.argv[0]
    subprocess.run(['cat', script_path])

def main():
    option = choose_option()

    if option == '1':
        handle_year()
    elif option == '2':
        handle_engine()
    elif option == '3':
        handle_parts(engine_folder, part_number)
    elif option == '4':
        handle_color_code()
    else:
        print("Invalid option. Please try again.")
        
    while True:
        key = input()  # Wait for user input
        if key == '\x10':  # Ctrl-P pressed
            print_current_screen()

if __name__ == "__main__":
    main()
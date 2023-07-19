import csv
import shutil

def load_csv(csv_file):
    # Open the CSV file in read mode
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row
        rows = list(reader)  # Read the remaining rows
    
    return headers, rows

def backup_csv(csv_file):
    # Create a backup of the original file
    backup_file = csv_file + ".old"
    shutil.copyfile(csv_file, backup_file)

def search_csv(csv_file):
    # Prompt the user to choose to load a backup file or the current file
    choice = input("Do you want to load a backup file? (yes/no): ")
    
    if choice.lower() == "yes":
        backup_file = csv_file + ".old"
        
        try:
            headers, rows = load_csv(backup_file)
            print("Loaded backup file:", backup_file)
        except FileNotFoundError:
            print("Backup file not found. Loading the current file instead.")
            headers, rows = load_csv(csv_file)
    else:
        headers, rows = load_csv(csv_file)
    
    # Display the headers
    print("CSV Headers:")
    print(', '.join(headers))
    
    # Prompt the user for a search term
    search_term = input("Enter a search term: ")
    
    # Perform the search and display matching rows
    matching_rows = []
    for row in rows:
        for value in row:
            if search_term.lower() in value.lower():
                matching_rows.append(row)
                break
    
    if matching_rows:
        print("\nMatching rows:")
        for row in matching_rows:
            print(', '.join(row))
        
        # Prompt the user to select a row to edit
        row_index = int(input("\nEnter the index of the row to edit (starting from 0): "))
        
        # Prompt the user for new values
        new_values = []
        for header in headers:
            value = input(f"Enter the new value for '{header}': ")
            new_values.append(value)
        
        # Update the selected row with the new values
        matching_rows[row_index] = new_values
        
        # Backup the current file before writing the updates
        backup_csv(csv_file)
        
        # Write the updated data back to the CSV file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(rows)
        
        print("\nCSV file updated successfully!")
    else:
        print("No matching rows found.")

# Example usage
csv_file = 'data.csv'
search_csv(csv_file)

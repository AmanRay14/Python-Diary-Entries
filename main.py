# Function to create a new diary entry
def create_entry():
    entry = input("Write your diary entry:\n")

    with open("diary.txt", "a") as file:
        file.write(f"{entry}\n")

    print("Diary entry saved successfully!")

# Function to display all diary entries
def display_entries():
    try:
        with open("diary.txt", "r") as file:
            entries = file.read()
            if entries:
                print("\nDiary Entries:")
                print(entries)
            else:
                print("\nNo entries found in the diary.")
    except FileNotFoundError:
        print("\nNo diary entries found.")

# Main program loop
def main():
    while True:
        print("\nOptions:")
        print("1. Write Diary Entry")
        print("2. View Diary Entries")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            create_entry()
        elif choice == '2':
            display_entries()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

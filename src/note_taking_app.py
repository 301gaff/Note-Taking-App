
import os

NOTES_FILE = "notes.txt"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        open(NOTES_FILE, 'w').close()
    with open(NOTES_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        file.writelines(note + '\n' for note in notes)

def display_notes(notes):
    if not notes:
        print("No notes found.")
    else:
        print("\nYour Notes:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")
    print()

def add_note(notes):
    note = input("Enter your note: ").strip()
    if note:
        notes.append(note)
        save_notes(notes)
        print("Note added!\n")
    else:
        print("Empty notes are not allowed.\n")

def remove_note(notes):
    display_notes(notes)
    if not notes:
        return
    try:
        index = int(input("Enter the number of the note to remove: "))
        if 1 <= index <= len(notes):
            removed = notes.pop(index - 1)
            save_notes(notes)
            print(f"Removed note: '{removed}'\n")
        else:
            print("Invalid number. Please choose a valid note number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    notes = load_notes()
    while True:
        print("Note-Taking App Menu:")
        print("(1) View Notes")
        print("(2) Add a Note")
        print("(3) Remove a Note")
        print("(4) Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            display_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            remove_note(notes)
        elif choice == '4':
            print("Saving and exiting. See you next time!")
            save_notes(notes)
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()

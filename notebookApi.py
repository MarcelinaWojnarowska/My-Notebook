from notebookService import NoteService

myNote = NoteService()

while True:
    choice = input(
        "Wybierz co chcesz zrobić:\n(1)stworzyć notatkę\n(2)pobrać treść wybranej notatki\n"
        "(3)edytować treść notatki\n(4)usunąć wybraną notatkę\n(5)zakończyć\n"
        "Twój wybór:"
    )
    if choice == "1":
        text = input("Wpisz treść notatki:\n")
        myNote.create_note(text)

    given_id = None
    note = None
    if choice in ["2", "3", "4"]:
        given_id = input("Podaj id notatki:\n")
        note = myNote.get_note(int(given_id))
        if not note:
            print("Notatka o podanym id nie istnieje!")

    if choice == "2" and note:
        for (id, tresc) in note:
            print(f"Treść wybranej notatki: {tresc}")

    elif choice == "3" and note:
        text = input("Podaj nową treść notatki:\n")
        myNote.update_note(int(given_id), text)

    elif choice == "4" and note:
        myNote.delete_note(int(given_id))

    elif choice == "5":
        print("ZAKOŃCZONO.")
        break

import mysql.connector


class NoteService:
    db = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='notebook',
                                 auth_plugin='mysql_native_password')

    def create_note(self, text):
        add_note = "INSERT INTO notes(content) VALUES (%s)"
        my_cursor = self.db.cursor()

        my_cursor.execute(add_note, (text,))
        self.db.commit()

        print(f"ID DODANEJ NOTATKI: {my_cursor.lastrowid}")

    def get_note(self, id):
        note = "SELECT * FROM notes WHERE id = %s"
        my_cursor = self.db.cursor()

        my_cursor.execute(note, (id,))
        return my_cursor.fetchall()

    def update_note(self, id, text):
        new_date = "UPDATE notes SET content = %s WHERE id = %s"
        my_cursor = self.db.cursor()

        my_cursor.execute(new_date, (text, id))
        print(f"TREŚĆ PODANEJ NOTATKI ZOSTAŁA ZMIENIONA.")

        self.db.commit()

    def delete_note(self, id):
        remove_data = "DELETE FROM notes WHERE id =  %s"
        my_cursor = self.db.cursor()

        my_cursor.execute(remove_data, (id,))
        print(f"NOTATKA O ID {id} ZOSTAŁA USUNIĘTA.")

        self.db.commit()

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="golden",
    database="college"
)

cursor = conn.cursor()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        cursor.execute("INSERT INTO students VALUES (%s, %s, %s)", (id, name, age))
        conn.commit()
        print("Student added!")

    elif choice == 2:
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)

    elif choice == 3:
        id = int(input("Enter ID to delete: "))
        cursor.execute("DELETE FROM students WHERE id = %s", (id,))
        conn.commit()
        print("Deleted!")

    elif choice == 4:
        break
import mysql.connector

# Database connection configuration
db_config = {
    "host": "mysql-33d76eb2-alustudent-26bb.f.aivencloud.com",
    "port": 18954,
    "user": "avnadmin",
    "password": "AVNS_E0SckWhzsauAXJ9wY5T",
    "database": "defaultdb"
}

try:
    print("Attempting to connect to the database...")
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Successfully connected to MySQL Server version {db_info}")
        cursor = connection.cursor()
        cursor.execute("select database();")
        database = cursor.fetchone()
        print(f"Connected to database: {database[0]}")

        # Get student name from user input
        student_name = input("Enter student name: ")

        # Insert student name
        insert_query = "INSERT INTO test (Student_Name) VALUES (%s)"
        cursor.execute(insert_query, (student_name,))
        connection.commit()
        print(f"Successfully added student: {student_name}")

except Exception as e:
    print(f"An error occurred: {e}")
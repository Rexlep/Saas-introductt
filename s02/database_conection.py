import psycopg2

conn = psycopg2.connect(
    database="task_manager",
    user="postgres",
    password="1384amiR",
    host="localhost",
    port=5432
)















cursor = conn.cursor()

cursor.execute("SELECT * FROM tasks;")
print(cursor.fetchall())
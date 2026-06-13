import psycopg2


conn = psycopg2.connect(
    password="1384amiR",
    user="postgres",
    database="task_manager",
    host="localhost",
    port=5432
)

cursor = conn.cursor()
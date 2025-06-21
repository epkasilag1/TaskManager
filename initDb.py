import pymysql

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'cursorclass': pymysql.cursors.DictCursor
}

def run_sql_script(file_path):
    with open(file_path, 'r') as f:
        sql_script = f.read()

    # Split by semicolon
    statements = [s.strip() for s in sql_script.split(';') if s.strip()]

    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()

    try:
        for statement in statements:
            cursor.execute(statement)
        conn.commit()
        print("SQL script executed successfully.")
    except Exception as e:
        print("Error executing script:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    run_sql_script('initDb.sql')
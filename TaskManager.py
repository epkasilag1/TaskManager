import pymysql
from pymysql.cursors import DictCursor
from Task import Task

class TaskManager:
    def __init__(self, config):
        self.config = config

    def _connect(self):
        return pymysql.connect(**self.config)

    def add_task(self, title, description, due_date, priority='Low'):
        conn = self._connect()
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO tasks (title, description, due_date, priority) VALUES (%s, %s, %s, %s)", [title, description, due_date, priority])
        conn.commit()
        conn.close()
        print("Task added.")

    def list_tasks(self, status=None, priority=None):
        conn = self._connect()
        with conn.cursor(cursor=DictCursor) as cursor:
            query = "SELECT * FROM tasks WHERE 1=1"
            params = []
            if status:
                query += " AND status = %s"
                params.append(status)
            if priority:
                query += " AND priority = %s"
                params.append(priority)
            cursor.execute(query, params)
            rows = cursor.fetchall()
        conn.close()

        if not rows:
            print("No tasks found.")
        for row in rows:
            task = Task(**row)
            print(task)

    def update_task(self, task_id, **kwargs):
        conn = self._connect()
        with conn.cursor() as cursor:
            fields = ", ".join([f"{k} = %s" for k in kwargs])
            values = list(kwargs.values()) + [task_id]
            query = f"UPDATE tasks SET {fields} WHERE id = %s"
            cursor.execute(query, values)
        conn.commit()
        conn.close()
        print(f"Task {task_id} updated.")

    def mark_completed(self, task_id):
        self.update_task(task_id, status='Completed')

    def delete_task(self, task_id):
        conn = self._connect()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id))
        conn.commit()
        conn.close()
        print(f"Task {task_id} deleted.")

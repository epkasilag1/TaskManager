class Task:
    def __init__(self, id, title, description, due_date, priority, status, created_at):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.created_at = created_at

    def __str__(self):
        return (f"[ID: {self.id}] {self.title} ({self.status.upper()})\n"
                f"        Priority: {self.priority.upper()}, Due: {self.due_date}, Created: {self.created_at}\n"
                f"        {self.description}\n")

# src/task_manager.py
# Student Task Manager - Core Logic (FIXED VERSION)

class Task:
    def __init__(self, task_id, title, description, due_date, priority="Medium"):
        self.id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False
    
    def mark_complete(self):
        self.completed = True
    
    def mark_incomplete(self):
        self.completed = False


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1
    
    def add_task(self, title, description, due_date, priority="Medium"):
        """Add a new task and return its ID"""
        task = Task(self.next_id, title, description, due_date, priority)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task.id
    
    def get_task(self, task_id):
        """Return task by ID, or None if not found"""
        return self.tasks.get(task_id)
    
    def delete_task(self, task_id):
        """Delete task by ID"""
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
    
    def mark_task_complete(self, task_id):
        """Mark task as complete"""
        task = self.get_task(task_id)
        if task:
            task.mark_complete()
            return True
        return False
    
    def get_completion_percentage(self):
        """Calculate percentage (OTHER BRANCH VERSION)"""
        """Calculate percentage of completed tasks (FIXED)"""
        if len(self.tasks) == 0:
            return 0.0
        
        completed_count = sum(1 for task in self.tasks.values() if task.completed)
        # FIXED: Multiply by 100 to get percentage
        return (completed_count / len(self.tasks)) * 100
    
    def get_tasks_by_priority(self, priority):
        """Return list of tasks with given priority"""
        return [task for task in self.tasks.values() if task.priority == priority]
    


    def get_tasks_by_status(self, completed_only=True):
        """Get tasks filtered by completion status (NEW FEATURE)"""
        if completed_only:
            return [task for task in self.tasks.values() if task.completed]
        else:
            return [task for task in self.tasks.values() if not task.completed]
    
    def get_task_summary(self):
        """Return summary statistics (NEW FEATURE)"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks.values() if task.completed)
        pending = total - completed
        
        priority_counts = {
            "High": sum(1 for task in self.tasks.values() if task.priority == "High"),
            "Medium": sum(1 for task in self.tasks.values() if task.priority == "Medium"),
            "Low": sum(1 for task in self.tasks.values() if task.priority == "Low")
        }
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_percentage": self.get_completion_percentage(),
            "priority_counts": priority_counts
        }

    def get_overdue_tasks(self, current_date):
        """Return tasks with due_date before current_date and not completed"""
        overdue = []
        for task in self.tasks.values():
            if not task.completed and task.due_date < current_date:
                overdue.append(task)
        return overdue

# src/task_manager.py
# Student Task Manager - Core Logic (REFACTORED VERSION)
# Phase 7: Added type hints, input validation, helper methods

from typing import List, Dict, Optional, Tuple
from datetime import datetime
import re

class Task:
    """Represents a single task"""
    
    # Priority constants
    PRIORITY_HIGH = "High"
    PRIORITY_MEDIUM = "Medium"
    PRIORITY_LOW = "Low"
    VALID_PRIORITIES = [PRIORITY_HIGH, PRIORITY_MEDIUM, PRIORITY_LOW]
    
    def __init__(self, task_id: int, title: str, description: str, 
                 due_date: str, priority: str = PRIORITY_MEDIUM):
        self.id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False
    
    def mark_complete(self) -> None:
        """Mark task as complete"""
        self.completed = True
    
    def mark_incomplete(self) -> None:
        """Mark task as incomplete"""
        self.completed = False


class TaskManager:
    """Main task management system"""

    def _sanitize_input(self, text: str) -> str:
        """Sanitize user input to prevent XSS and injection"""
        if not isinstance(text, str):
            text = str(text)
        # Remove potentially dangerous characters
        dangerous_chars = ['<', '>', '&', '"', "'", ';', '--', '/*', '*/']
        for char in dangerous_chars:
            text = text.replace(char, '')
        return text.strip()
    
    def _validate_task_id(self, task_id: int) -> bool:
        """Validate task ID is positive integer"""
        return isinstance(task_id, int) and task_id > 0
    
    def add_task_secure(self, title: str, description: str, due_date: str, 
                         priority: str = "Medium") -> int:
        """Secure version with sanitization"""
        # Input sanitization
        title = self._sanitize_input(title)
        description = self._sanitize_input(description)
        
        # Validation
        if not title or len(title) < 3:
            raise ValueError("Title must be at least 3 characters")
        if len(title) > 100:
            raise ValueError("Title cannot exceed 100 characters")
        if len(description) > 500:
            raise ValueError("Description cannot exceed 500 characters")
        if not self._validate_date(due_date):
            raise ValueError("Invalid date format - use YYYY-MM-DD")
        
        return self.add_task(title, description, due_date, priority)
    
    # Date format expected
    DATE_FORMAT = "%Y-%m-%d"
    
    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self.next_id: int = 1
        self._cached_percentage: Optional[float] = None
        self._cache_valid: bool = False
    
    def _validate_date(self, due_date: str) -> bool:
        """Validate date format (YYYY-MM-DD)"""
        try:
            datetime.strptime(due_date, self.DATE_FORMAT)
            return True
        except ValueError:
            return False
    
    def _validate_priority(self, priority: str) -> str:
        """Validate and normalize priority value"""
        if priority in Task.VALID_PRIORITIES:
            return priority
        return Task.PRIORITY_MEDIUM  # Default
    
    def _validate_title(self, title: str) -> bool:
        """Validate title is not empty"""
        return bool(title and title.strip())
    
    def _invalidate_cache(self) -> None:
        """Mark percentage cache as invalid (call when tasks change)"""
        self._cache_valid = False
    
    def _get_task_or_none(self, task_id: int) -> Optional[Task]:
        """Helper method to safely get task (TD-001 fix - removes duplication)"""
        return self.tasks.get(task_id)
    
    def add_task(self, title: str, description: str, due_date: str, 
                 priority: str = Task.PRIORITY_MEDIUM) -> int:
        """Add a new task and return its ID"""
        # Input validation (TD-003 fix)
        if not self._validate_title(title):
            raise ValueError("Title cannot be empty")
        
        if not self._validate_date(due_date):
            raise ValueError(f"Invalid date format. Use {self.DATE_FORMAT}")
        
        validated_priority = self._validate_priority(priority)
        
        task = Task(self.next_id, title, description, due_date, validated_priority)
        self.tasks[self.next_id] = task
        self.next_id += 1
        self._invalidate_cache()  # Invalidate percentage cache
        return task.id
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Return task by ID, or None if not found"""
        return self._get_task_or_none(task_id)
    
    def delete_task(self, task_id: int) -> bool:
        """Delete task by ID"""
        if task_id in self.tasks:
            del self.tasks[task_id]
            self._invalidate_cache()
            return True
        return False
    
    def mark_task_complete(self, task_id: int) -> bool:
        """Mark task as complete"""
        task = self._get_task_or_none(task_id)
        if task:
            task.mark_complete()
            self._invalidate_cache()
            return True
        return False
    
    def mark_task_incomplete(self, task_id: int) -> bool:
        """Mark task as incomplete (NEW helper method)"""
        task = self._get_task_or_none(task_id)
        if task:
            task.mark_incomplete()
            self._invalidate_cache()
            return True
        return False
    
    def get_completion_percentage(self) -> float:
        """Calculate percentage of completed tasks (with caching - TD-006)"""
        if len(self.tasks) == 0:
            return 0.0
        
        # Use cached value if valid (TD-006 fix)
        if self._cache_valid and self._cached_percentage is not None:
            return self._cached_percentage
        
        completed_count = sum(1 for task in self.tasks.values() if task.completed)
        self._cached_percentage = (completed_count / len(self.tasks)) * 100
        self._cache_valid = True
        return self._cached_percentage
    
    def get_tasks_by_priority(self, priority: str) -> List[Task]:
        """Return list of tasks with given priority"""
        validated_priority = self._validate_priority(priority)
        return [task for task in self.tasks.values() if task.priority == validated_priority]
    
    def get_tasks_by_status(self, completed_only: bool = True) -> List[Task]:
        """Get tasks filtered by completion status"""
        if completed_only:
            return [task for task in self.tasks.values() if task.completed]
        else:
            return [task for task in self.tasks.values() if not task.completed]
    
    def get_overdue_tasks(self, current_date: str) -> List[Task]:
        """Return tasks with due_date before current_date and not completed"""
        if not self._validate_date(current_date):
            raise ValueError(f"Invalid date format. Use {self.DATE_FORMAT}")
        
        overdue = []
        for task in self.tasks.values():
            if not task.completed and task.due_date < current_date:
                overdue.append(task)
        return overdue
    
    def get_task_summary(self) -> dict:
        """Return summary statistics"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks.values() if task.completed)
        pending = total - completed
        
        priority_counts = {
            Task.PRIORITY_HIGH: sum(1 for task in self.tasks.values() if task.priority == Task.PRIORITY_HIGH),
            Task.PRIORITY_MEDIUM: sum(1 for task in self.tasks.values() if task.priority == Task.PRIORITY_MEDIUM),
            Task.PRIORITY_LOW: sum(1 for task in self.tasks.values() if task.priority == Task.PRIORITY_LOW)
        }
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_percentage": self.get_completion_percentage(),
            "priority_counts": priority_counts
        }

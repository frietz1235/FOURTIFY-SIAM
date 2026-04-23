# tests/test_task_manager.py
import sys
import os
sys.path.insert(0, os.path.abspath("src"))

from task_manager import TaskManager
import pytest

class TestTaskManager:
    
    def setup_method(self):
        """Create fresh TaskManager before each test"""
        self.tm = TaskManager()
    
    # Test 1: Add task returns correct ID
    def test_add_task_returns_id(self):
        task_id = self.tm.add_task("Test Task", "Description", "2024-12-31")
        assert task_id == 1
        assert len(self.tm.tasks) == 1
    
    # Test 2: Add multiple tasks increments ID
    def test_add_multiple_tasks(self):
        id1 = self.tm.add_task("Task 1", "Desc 1", "2024-12-31")
        id2 = self.tm.add_task("Task 2", "Desc 2", "2024-12-31")
        id3 = self.tm.add_task("Task 3", "Desc 3", "2024-12-31")
        
        assert id1 == 1
        assert id2 == 2
        assert id3 == 3
        assert len(self.tm.tasks) == 3
    
    # Test 3: Mark task as complete
    def test_mark_task_complete(self):
        task_id = self.tm.add_task("Complete Me", "Desc", "2024-12-31")
        self.tm.mark_task_complete(task_id)
        
        task = self.tm.get_task(task_id)
        assert task.completed == True
    
    # Test 4: Delete task removes from list
    def test_delete_task(self):
        task_id = self.tm.add_task("Delete Me", "Desc", "2024-12-31")
        assert len(self.tm.tasks) == 1
        
        result = self.tm.delete_task(task_id)
        assert result == True
        assert len(self.tm.tasks) == 0
    
    # Test 5: Get completion percentage (THIS TEST WILL FAIL - intentional bug!)
    def test_completion_percentage(self):
        # Add 2 tasks, complete 1 of them
        task1 = self.tm.add_task("Task 1", "Desc", "2024-12-31")
        task2 = self.tm.add_task("Task 2", "Desc", "2024-12-31")
        
        self.tm.mark_task_complete(task1)
        
        percentage = self.tm.get_completion_percentage()
        
        # Expected: (1/2) * 100 = 50%
        # BUT bug makes it return 0.5 instead of 50
        assert percentage == 50.0  # This will FAIL


    # Test 6: Get tasks by status
    def test_get_tasks_by_status(self):
        task1 = self.tm.add_task("Task 1", "Desc", "2024-12-31")
        task2 = self.tm.add_task("Task 2", "Desc", "2024-12-31")
        
        self.tm.mark_task_complete(task1)
        
        completed = self.tm.get_tasks_by_status(completed_only=True)
        pending = self.tm.get_tasks_by_status(completed_only=False)
        
        assert len(completed) == 1
        assert len(pending) == 1
    
    # Test 7: Get task summary
    def test_get_task_summary(self):
        task1 = self.tm.add_task("Task 1", "Desc", "2024-12-31", "High")
        task2 = self.tm.add_task("Task 2", "Desc", "2024-12-31", "Medium")
        task3 = self.tm.add_task("Task 3", "Desc", "2024-12-31", "Low")
        
        self.tm.mark_task_complete(task1)
        
        summary = self.tm.get_task_summary()
        
        assert summary["total"] == 3
        assert summary["completed"] == 1
        assert summary["pending"] == 2
        assert summary["priority_counts"]["High"] == 1
        assert summary["priority_counts"]["Medium"] == 1
        assert summary["priority_counts"]["Low"] == 1

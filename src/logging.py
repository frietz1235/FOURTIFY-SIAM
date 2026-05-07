# src/logging.py
# Basic logging and monitoring for FOURTIFY

import logging
import time
from datetime import datetime
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Create logs directory
import os
os.makedirs('logs', exist_ok=True)

def log_request(func):
    """Decorator to log function calls"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"Calling: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            logger.info(f"Completed: {func.__name__} in {elapsed:.3f}s")
            return result
        except Exception as e:
            logger.error(f"Failed: {func.__name__} - {str(e)}")
            raise
    return wrapper

class MetricsCollector:
    """Collect and store metrics"""
    
    def __init__(self):
        self.metrics = {
            "api_calls": 0,
            "errors": 0,
            "response_times": []
        }
    
    def record_call(self, duration):
        self.metrics["api_calls"] += 1
        self.metrics["response_times"].append(duration)
    
    def record_error(self):
        self.metrics["errors"] += 1
    
    def get_summary(self):
        avg_time = sum(self.metrics["response_times"]) / len(self.metrics["response_times"]) if self.metrics["response_times"] else 0
        return {
            "total_calls": self.metrics["api_calls"],
            "errors": self.metrics["errors"],
            "avg_response_time": round(avg_time, 3),
            "error_rate": round(self.metrics["errors"] / max(self.metrics["api_calls"], 1) * 100, 2)
        }

metrics = MetricsCollector()

# Simple uptime check endpoint simulation
def uptime_check():
    """Simulate uptime check - returns status"""
    logger.info("Uptime check performed")
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

logger.info("Logging system initialized")

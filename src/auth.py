# src/auth.py
# Simple token-based authentication for CI/CD pipeline

import secrets
import hashlib
import os
from datetime import datetime, timedelta

class AuthManager:
    """Simple token-based authentication manager"""
    
    def __init__(self):
        # In production, this would be stored in a database
        self._users = {}  # username -> hashed_password
        self._tokens = {}  # token -> username, expiry
        self._token_expiry_seconds = 3600  # 1 hour
    
    def _hash_password(self, password: str) -> str:
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username: str, password: str) -> bool:
        """Register a new user"""
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if not password or len(password) < 6:
            raise ValueError("Password must be at least 6 characters")
        
        if username in self._users:
            return False  # User already exists
        
        self._users[username] = self._hash_password(password)
        return True
    
    def authenticate(self, username: str, password: str) -> str | None:
        """Authenticate user and return access token"""
        if username not in self._users:
            return None
        
        hashed = self._hash_password(password)
        if self._users[username] != hashed:
            return None
        
        # Generate a secure token
        token = secrets.token_urlsafe(32)
        expiry = datetime.now() + timedelta(seconds=self._token_expiry_seconds)
        self._tokens[token] = {"username": username, "expiry": expiry}
        
        return token
    
    def verify_token(self, token: str) -> bool:
        """Verify if token is valid and not expired"""
        if token not in self._tokens:
            return False
        
        expiry = self._tokens[token]["expiry"]
        if datetime.now() > expiry:
            # Token expired
            del self._tokens[token]
            return False
        
        return True
    
    def revoke_token(self, token: str) -> bool:
        """Revoke a token (logout)"""
        if token in self._tokens:
            del self._tokens[token]
            return True
        return False

# Singleton instance for app-wide use
auth_manager = AuthManager()

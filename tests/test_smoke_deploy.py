# tests/test_smoke_deploy.py
import pytest
import requests
import os

DEPLOYED_URL = os.environ.get('DEPLOYED_URL', 'https://frietz1235.github.io/FOURTIFY-SIAM/')

class TestDeployedSmokeTests:
    
    def test_homepage_loads(self):
        """Test 1: Page returns HTTP 200"""
        response = requests.get(DEPLOYED_URL, timeout=30)
        assert response.status_code == 200
    
    def test_page_has_content(self):
        """Test 2: Page has CI/CD content"""
        response = requests.get(DEPLOYED_URL, timeout=30)
        content = response.text
        assert "FOURTIFY" in content or "CI/CD" in content
        assert len(content) > 100
    
    def test_response_time_acceptable(self):
        """Test 3: Response under 5 seconds"""
        import time
        start = time.time()
        response = requests.get(DEPLOYED_URL, timeout=30)
        elapsed = time.time() - start
        assert response.status_code == 200
        assert elapsed < 5.0

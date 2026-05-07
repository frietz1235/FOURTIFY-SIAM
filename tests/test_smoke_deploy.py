# tests/test_smoke_deploy.py
import pytest
import requests
import os

DEPLOYED_URL = os.environ.get('DEPLOYED_URL', 'https://frietz1235.github.io/FOURTIFY-SIAM/')

class TestDeployedSmokeTests:
    def test_homepage_loads(self):
        response = requests.get(DEPLOYED_URL, timeout=30)
        assert response.status_code == 200
        assert "FOURTIFY" in response.text or "Student" in response.text
    
    def test_response_time_acceptable(self):
        import time
        start = time.time()
        response = requests.get(DEPLOYED_URL, timeout=30)
        elapsed = time.time() - start
        assert response.status_code == 200
        assert elapsed < 3.0
    
    def test_https_works(self):
        assert DEPLOYED_URL.startswith("https")
        response = requests.get(DEPLOYED_URL, timeout=30, verify=True)
        assert response.status_code == 200

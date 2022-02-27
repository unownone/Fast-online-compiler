import sys
sys.path.append('../code')
from app import app
import pytest, json


@pytest.fixture
def client():
    """Get Test Client"""
    app.testing = True
    return app.test_client()

@pytest.fixture()
def runner():
    """Get TestRunner"""
    app.testing = True
    return app.test_cli_runner()


# --------- Definitions for Codes -----------
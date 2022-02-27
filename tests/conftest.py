from .. import app
import pytest, json


@pytest.fixture
def client():
    """Get Test Client"""
    app.app.testing = True
    return app.test_client()

@pytest.fixture()
def runner():
    """Get TestRunner"""
    app.app.testing = True
    return app.test_cli_runner()


# --------- Definitions for Codes -----------
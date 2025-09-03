import app

def test_greeting_content():
    """Tests the content of the greeting."""
    assert "Hello" in app.get_greeting()

def test_greeting_type():
    """Tests the return type of the greeting."""
    assert isinstance(app.get_greeting(), str)
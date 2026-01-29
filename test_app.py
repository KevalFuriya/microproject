import app

def test_even_number():
    assert app.is_even(10) is True

def test_odd_number():
    assert app.is_even(7) is False

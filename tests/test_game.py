# content of test_sample.py
def test_one():
    x = "this"
    assert "h" in x

def test_two():
    x = "hello"
    assert hasattr(x, "h")
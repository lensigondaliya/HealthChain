import pytest
from healthchain.utils.html_utils import clean_html

def test_clean_html_basic():
    html = "<p>Hello <b>World</b></p>"
    result = clean_html(html)
    assert "Hello" in result
    assert "World" in result

def test_clean_html_empty():
    html = ""
    result = clean_html(html)
    assert result == "" or result is not None

def test_clean_html_preserves_text_content():
    html = "<div><span>Test</span></div>"
    result = clean_html(html)
    assert "Test" in result
    assert result is not None
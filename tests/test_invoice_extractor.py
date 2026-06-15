import json
import os
import sys
from unittest.mock import MagicMock

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import invoice_extractor
from invoice_extractor import extract_invoice_data


def _mock_message(text: str):
    block = MagicMock()
    block.text = text
    message = MagicMock()
    message.content = [block]
    return message


def test_extract_invoice_data_parses_json(monkeypatch):
    payload = {
        "vendor": "Tech Supplies Inc",
        "invoice_number": "INV-2025-001",
        "total": 2695.00,
    }
    monkeypatch.setattr(
        invoice_extractor.client.messages,
        "create",
        lambda **kwargs: _mock_message(json.dumps(payload)),
    )

    result = extract_invoice_data("some email content")
    assert result == payload


def test_extract_invoice_data_strips_markdown_fences(monkeypatch):
    payload = {"vendor": "Acme"}
    fenced = "```json\n" + json.dumps(payload) + "\n```"
    monkeypatch.setattr(
        invoice_extractor.client.messages,
        "create",
        lambda **kwargs: _mock_message(fenced),
    )

    result = extract_invoice_data("email")
    assert result == payload


def test_extract_invoice_data_empty_raises():
    with pytest.raises(ValueError):
        extract_invoice_data("")

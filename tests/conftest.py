#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""
This is a configuration file for pytest containing customizations and fixtures.

In VSCode, Code Coverage is recorded in config.xml. Delete this file to reset reporting.
"""

from __future__ import annotations

from typing import List

import pytest
from _pytest.nodes import Item

from datetime import datetime, timezone


def pytest_collection_modifyitems(items: list[Item]):
    for item in items:
        if "spark" in item.nodeid:
            item.add_marker(pytest.mark.spark)
        elif "_int_" in item.nodeid:
            item.add_marker(pytest.mark.integration)


@pytest.fixture
def unit_test_mocks(monkeypatch: None):
    """Include Mocks here to execute all commands offline and fast."""
    pass

@pytest.fixture
def accessToken():
  return '00DDn00000BzCTS!AQQAQOTIcwG0EPiXOUlFlF7tUK5iEi7c4u07qHLpzM4UCrTr5hDlJEefUrhkIBo9t5yEuIc0XlUo.Nsuym3sDYEDSkWyFb5x'

@pytest.fixture
def data():
  return {
    "Owner Id": '005Dn000004oWGNIA2',
    "Meeting Name": 'Test Meeting 2',
    "Meeting Url": 'test.xyz',
    "Meeting Date": datetime.now(timezone.utc).isoformat(),
    "Meeting Summary": 'Test Summary',
    "Sentiment": 'Very Positive',
    "DurationInMinutes": 30,
    "Attendee": None,
    "Account": None
  }

@pytest.fixture
def mapping():
  return {
    "Owner Id": 'OwnerId',
    "Meeting Name": 'Subject',
    "Meeting Url": 'Description',
    "Meeting Date": 'ActivityDateTime',
    "Meeting Summary": 'Description',
    "Sentiment": 'Description',
    "Attendee": 'WhoId',
    "Account": 'WhatId'
  }

@pytest.fixture
def ownerEmail():
  return '24ntn96@gmail.com'

@pytest.fixture
def accountId():
  return '24ntn96@gmail.com'

@pytest.fixture
def attendeeEmails():
  return ['bond_john@grandhotels.com', 'j.davis@expressl&t.net']


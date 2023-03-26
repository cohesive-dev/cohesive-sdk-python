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
  return '00DDn00000BzCTS!AQQAQIFHZ6JCQOpKBJDBTGKY4FWr_6h2QRvN9W00iTX._G6c.6m4RXueFsT16ncmgF4QUa8FgolE4C9rIMNLUpfNLKl6Zj7B'

@pytest.fixture
def data():
  return {
    "accountId": '005Dn000004oWGNIA2',
    "Meeting Name": 'SFDC upstract demo check-in with Kevin & Nam',
    "Meeting Url": 'zoom.com/kevin-cohesive-demo',
    "Meeting Date": datetime.now(timezone.utc).isoformat(),
    "Meeting Summary": 'Kevin demoed Cohesive to a lot of stakeholders and got their feedback',
    "Sentiment": 'Overall a pretty positive meeting',
    "DurationInMinutes": 45
  }

@pytest.fixture
def mapping():
  return {
    "accountId": 'OwnerId',
    "Meeting Name": 'Subject',
    "Meeting Url": 'Description',
    "Meeting Date": 'ActivityDateTime',
    "Meeting Summary": 'Description',
    "Sentiment": 'Description'
  }

@pytest.fixture
def ownerEmail():
  return '24ntn96@gmail.com'

@pytest.fixture
def accountId():
  #return '24ntn96@gmail.com'
  return '0054K000003nx1VQAQ'

@pytest.fixture
def attendeeEmails():
  return ['bond_john@grandhotels.com', 'j.davis@expressl&t.net']


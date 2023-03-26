#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a sample python file for testing functions from the source code."""
from __future__ import annotations
from datetime import datetime, timezone

from cohesive.client import SalesforceClient

'''
def testUpsertEventsForEmails1(
  accessToken,
  data,
  mapping,
  ownerEmail,
  attendeeEmails
):
  """
  This defines the expected usage, which can then be used in various test cases.
  Pytest will not execute this code directly, since the function does not contain the suffex "test"
  """
  salesforceClient = SalesforceClient.initialize(
    salesforceDomain='https://cohesive2-dev-ed.develop.my.salesforce.com'
  )
  owners = salesforceClient.getSalesforceUserFromEmail(accessToken=accessToken, email=ownerEmail)
  owner = owners[0]
  if (not owner):
    raise Exception('Could not find Salesforce user with email ${email}')
  contacts = salesforceClient.getSalesforceContactFromEmail(accessToken=accessToken)
  attendeeContacts = [contact for contact in contacts if contact['Email'] and contact['Email'] in attendeeEmails] if contacts else []
  eventIds = [salesforceClient.upsertSalesforceEvent(
    accessToken=accessToken,
    data={
      **data,
      "WhoId": contact['Id'],
      "WhatId": contact['AccountId'],
    },
    mapping=mapping
  ) for contact in attendeeContacts if contact['AccountId']]

  print("TEST 1", eventIds)
'''

def testUpsertEventsForEmails2(
  accessToken,
  data,
  mapping,
  accountId,
  attendeeEmails
):
  """
  This is a simple test, which can use a mock to override online functionality.
  unit_test_mocks: Fixture located in conftest.py, implictly imported via pytest.
  """
  salesforceClient = SalesforceClient.initialize(
    salesforceDomain='https://cohesive2-dev-ed.develop.my.salesforce.com'
  )
  eventIds = salesforceClient.createSalesforceEvent(
    accessToken=accessToken,
    data=data,
    mapping=mapping
  )
  print("TEST 2", eventIds)

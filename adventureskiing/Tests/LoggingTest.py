# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import unittest
from unittest import TestCase

from adventureskiing.Database.MySQL.db_commands import SqlCommands


class TestLogging(TestCase):

    def test_login_command(self):
        fail_login, fail_password = "test", "test"
        correct_login, correct_password = "bix709", "fx0507"
        self.assertIsNone(SqlCommands.fetch_logins(fail_login, hash(fail_password)))
        correct_user_properties = SqlCommands.fetch_logins(correct_login, hash(correct_password))
        self.assertIsNotNone(correct_user_properties)
        self.assertEqual(len(correct_user_properties), 4)


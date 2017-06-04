# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import unittest
from unittest import TestCase

from adventureskiing.Database.MySQL.db_commands import SqlCommands
from adventureskiing.Utils.Users import User


class TestDatabaseCommands(TestCase):

    def test_user_creation_and_removal(self):
        incorrect_name, incorrect_lastname, incorrect_login = "Tomek1", "Teter1", "Hihi$"
        correct_name, correct_lastname, self.correct_login = "Test", "Test", "Tester123"
        self.assertFalse(SqlCommands.create_user(firstname=incorrect_name,
                                                 lastname=incorrect_lastname,
                                                 login=incorrect_login))
        self.assertFalse(SqlCommands.create_user(firstname=correct_name,
                                                 lastname=incorrect_lastname,
                                                 login=incorrect_login))
        self.assertFalse(SqlCommands.create_user(firstname=incorrect_name,
                                                 lastname=incorrect_lastname,
                                                 login=self.correct_login))
        self.assertTrue(SqlCommands.create_user(firstname=correct_name,
                                                lastname=correct_lastname,
                                                login=self.correct_login))
        name, lastname, uid, permissions = SqlCommands.fetch_logins(self.correct_login, hash(self.correct_login))
        test_user = User(user_id=uid, permission=permissions, lastname=lastname, name=name)
        self.assertTrue(SqlCommands.remove_user(test_user))

    def test_login_command(self):
        fail_login, fail_password = "test", "test"
        correct_login, correct_password = "bix709", "fx0507"
        self.assertIsNone(SqlCommands.fetch_logins(fail_login, hash(fail_password)))
        correct_user_properties = SqlCommands.fetch_logins(correct_login, hash(correct_password))
        self.assertIsNotNone(correct_user_properties)
        self.assertEqual(len(correct_user_properties), 4)


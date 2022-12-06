#!/usr/bin/python
"""

"""

import unittest
import sys
import models
import os
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
from models.base_model import BaseModel
from models.place import Place
from models import storage

db = os.getenv("HBNB_TYPE_STORAGE", "fs")

class test_console(unittest.TestCase):
    def setUp(self):
        self.backup = sys.stdout
        self.getout = StringIO()
        sys.stdout = self.getout

    def tearDown(self):
        sys.stdout = self.backup
    
    def create(self):
        return HBNBCommand()

    def test_quit(self):
        command = self.create()
        with patch("sys.stdout", new=StringIO()) as f:
            command.onecmd("quit")
            self.assertEqual("", f.getvalue())

    def test_EOF(self):
        command = self.create()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(command.onecmd("EOF"))

    def test_all(self):
        command = self.create()
        command.onecmd("all")
        self.assertTrue(isinstance(self.getout.getvalue(), str))

    @unittest.skipIf(db == "db", "Testing DBStorage only")
    def test_show(self):
        command = self.create()
        command.onecmd("create User")
        user_id = self.getout.getvalue()
        sys.stdout = self.backup
        self.getout.close()
        self.getout = StringIO()
        sys.stdout = self.getout
        command.onecmd("show User " + user_id)
        v = (self.getout.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(v))

    @unittest.skipIf(db == "db", "Testing DBStorage only")
    def test_show_class_name(self):
        command = self.create()
        command.onecmd("create User")
        user_id = self.getout.getvalue()
        sys.stdout = self.backup
        self.getout.close()
        self.getout = StringIO()
        sys.stdout = self.getout
        command.onecmd("show")
        v = (self.getout.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", v)

    def test_show_class_name_error(self):
        command = self.create()
        command.onecmd("create User")
        user_id = self.getout.getvalue()
        sys.stdout = self.backup
        self.getout.close()
        self.getout = StringIO()
        sys.stdout = self.getout
        command.onecmd("show User")
        v = (self.getout.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", v)

    @unittest.skipIf(db == "db", "Testing DBStorage only")
    def test_show_instance_found(self):
        command = self.create()
        command.onecmd("create User")
        user_id = self.getout.getvalue()
        sys.stdout = self.backup
        self.getout.close()
        self.getout = StringIO()
        sys.stdout = self.getout
        command.onecmd("show User " + "17267493")
        v = (self.getout.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", v)

    def test_create(self):
        command = self.create()
        command.onecmd('create User email="5194@hbnb.com" password="1234"')
        self.assertTrue(isinstance(self.getout.getvalue(), str))

    def test_destroy(self):
        pass

    def test_destroy_messege(self):
        pass

    def test_count(self):
        pass

    def test_update(self):
        pass


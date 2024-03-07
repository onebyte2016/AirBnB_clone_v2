#!/usr/bin/python3
"""This is a unittest code that tests the console module"""

import unittest
from console import HBNBCommand
from io import StringIO
import sys
from unittest.mock import patch
from models.user import User


class TestConsole(unittest.TestCase):
    """Test the HBNBCommand class"""

    def test_do_quit(self):
        """Test the quit method"""
        hbnb = HBNBCommand()
        self.assertEqual(hbnb.do_quit(''), True)

    def test_do_EOF(self):
        """Test the do_eof method"""
        hbnb = HBNBCommand()
        self.assertEqual(hbnb.do_EOF(''), True)

    def test_emptyline(self):
        """Test that an empty line doesn't execute anything"""
        hbnb = HBNBCommand()
        output = StringIO()
        sys.stdout = output
        hbnb.onecmd('\n')
        self.assertEqual(output.getvalue(), '')
        sys.stdout = sys.__stdout__

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(output.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_show(self):
        """Test the show command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show")
            self.assertEqual(output.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(output.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show MyModel 1234-5678-9012")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_destroy(self):
        """Test the destroy command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(output.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(output.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy MyModel 1234-5678-9012")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_all(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_update(self):
        """Test the update command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update")
            self.assertEqual(output.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(output.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel 1234-5678-9012")
            self.assertEqual(output.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel 1234-5678-9012 name")
            self.assertEqual(output.getvalue().strip(),
                             "** value missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update MyModel 1234-5678-9012 name value")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_create_user(self):
        """Test the create command with User"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            user_id = output.getvalue().strip()
            self.assertGreater(len(user_id), 0)

    def test_show_user(self):
        """Test the show command with User"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            user_id = output.getvalue().strip()

            with patch('sys.stdout', new=StringIO()) as output:
                HBNBCommand().onecmd(f"show User {user_id}")
                self.assertGreater(len(output.getvalue().strip()), 0)

    def test_destroy_user(self):
        """Test the destroy command with User"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            user_id = output.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(f"destroy User {user_id}")
            self.assertEqual(len(output.getvalue().strip()), 0)

    def test_all_user(self):
        """Test the all command with User"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all User")
            self.assertEqual(len(output.getvalue().strip()), 2)

    def test_update_user(self):
        """Test the update command with User"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            user_id = output.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(f"update User {user_id} first_name John")
            self.assertEqual(len(output.getvalue().strip()), 0)

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(f"show User {user_id}")
            self.assertIn("'first_name': 'John'", output.getvalue())


if __name__ == '__main__':
    unittest.main()

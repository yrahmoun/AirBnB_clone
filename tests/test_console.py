#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest

import pep8
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os


class TestConsoleClass(unittest.TestCase):
    """unittestes for the console file, with most of the classes , at least,"""

    maxDiff = None

    def setUp(self):
        """file to save results"""
        with open("test.json", "w"):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """delete the file created"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_module_doc(self):
        """check for module documentation"""
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_class_doc(self):
        """check for documentation"""
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_method_docs(self):
        """check for method documentation"""
        for func in dir(HBNBCommand):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """test base and test_base for pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        file1 = "console.py"
        file2 = "tests/test_console.py"
        result = style.check_files([file1, file2])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warning)."
        )

    def test_executable_file(self):
        """are all files chmoded??"""

        is_read_true = os.access("console.py", os.R_OK)
        self.assertTrue(is_read_true)

        is_write_true = os.access("console.py", os.W_OK)
        self.assertTrue(is_write_true)

        is_exec_true = os.access("console.py", os.X_OK)
        self.assertTrue(is_exec_true)

    def test_check_help(self):
        """check if functions have a docstring HELP"""
        with patch("sys.stdout", new=StringIO()) as help_val:
            HBNBCommand().onecmd("help create")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as help_val:
            HBNBCommand().onecmd("help all")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as help_val:
            HBNBCommand().onecmd("help show")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as help_val:
            HBNBCommand().onecmd("help destroy")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as help_val:
            HBNBCommand().onecmd("help update")
            self.assertTrue(len(help_val.getvalue()) > 0)

    def test_create_valid_class(self):
        """Test the create function with a valid class name"""
        with patch("sys.stdout", new=StringIO()) as help_val:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(help_val.getvalue()) > 0)

    def test_create_missing_class(self):
        """Test the create function with a missing class name"""
        with patch("sys.stdout", new=StringIO()) as help_val:
            HBNBCommand().onecmd("create")
            self.assertEqual(help_val.getvalue(), "** class name missing **\n")

    def test_create_invalid_class(self):
        """Test the create function with an invalid class name"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create Small")
            self.assertEqual(val.getvalue(), "** class doesn't exist **\n")

    def test_show_normal_parameters(self):
        """Test show with normal parameters"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
            basemodel_id = val.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show BaseModel " + basemodel_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")

    def test_show_notfound_class(self):
        """Test with class that does not exist"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show helloo ")
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_show_missing_class(self):
        """Test with class missing"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show")
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_show_missing_id(self):
        """Test with id missing"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show BaseModel")
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_destroy_missing_class(self):
        """Checks if class is missing"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("destroy")
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_destroy_nonexistent_class(self):
        """Checks if class name does not exist"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("destroy fakeclass")
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_destroy_missing_id(self):
        """Check if the id is missing"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_destroy_notfound(self):
        """Checks if the id belongs to an instance"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            self.assertTrue(val.getvalue() == "** no instance found **\n")

    def test_destroy_working(self):
        """Checks if destroy method deletes an instance successfully"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
            basemodel_id = val.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("destroy BaseModel " + basemodel_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")

    def test_all_fakeclass(self):
        """Checks if class name exists"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("all FakeClass")
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_all_working(self):
        """Checks if the method all works correctly"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("all")
            self.assertTrue(len(val.getvalue()) > 0)

    def test_all_trueclass(self):
        """Checks that the all method works correctly with a class input"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("all BaseModel")
            self.assertTrue(len(val.getvalue()) > 0)

    def test_update_missingclass(self):
        """Checks if the class is missing"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update")
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_update_wrongclass(self):
        """Checks if the class exists"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update FakeClass")
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_update_noinstance(self):
        """Checks if the instance id is missing"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update BaseModel")
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_update_notfound(self):
        """Checks if instance id exists"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update BaseModel 121212")
            self.assertTrue(val.getvalue() == "** no instance found **\n")

    def test_update_missing_name(self):
        """Checks if the attribute name is missing"""
        with patch("sys.stdout", new=StringIO()) as my_id:
            HBNBCommand().onecmd("create BaseModel")
            basemodel_id = my_id.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update BaseModel " + basemodel_id)
            self.assertTrue(val.getvalue() == "** attribute name missing **\n")

    def test_update_missing_value(self):
        """Checks if the attribute value is missing"""
        with patch("sys.stdout", new=StringIO()) as my_id:
            HBNBCommand().onecmd("create BaseModel")
            base_id = my_id.getvalue()
            self.assertTrue(len(base_id) > 0)
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update BaseModel " + base_id + " first_name")
            self.assertTrue(val.getvalue() == "** value missing **\n")

    def test_update_ok(self):
        """update test working"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
            user_id = val.getvalue()
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update BaseModel " + user_id + " name betty")
            HBNBCommand().onecmd("show BaseModel " + user_id)
            self.assertTrue("betty" in val.getvalue())

    def test_update_okextra(self):
        """update test working"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
            uid = val.getvalue()
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update BaseModel " + uid + " name 'betty ho'")
            HBNBCommand().onecmd("show BaseModel " + uid)
            self.assertTrue("'betty ho'" in val.getvalue())

    def test_user_console(self):
        """Test the class User with console"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show User " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("all User")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update User " + user_id + " name 'betty'")
            HBNBCommand().onecmd("show User " + user_id)
            self.assertTrue("'betty'" in val.getvalue())
            HBNBCommand().onecmd("destroy User " + user_id)
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show User " + user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_place_console(self):
        """Test the class Place with console"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create Place")
            place_id = val.getvalue()
            self.assertTrue(place_id != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show Place " + place_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("all Place")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update Place " + place_id + " name 'betty'")
            HBNBCommand().onecmd("show Place " + place_id)
            self.assertTrue("'betty'" in val.getvalue())
            HBNBCommand().onecmd("destroy Place " + place_id)
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show Place " + place_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_state_console(self):
        """Test the class State with console"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create State")
            state_id = val.getvalue()
            self.assertTrue(state_id != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show State " + state_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("all State")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update State " + state_id + " name 'betty'")
            HBNBCommand().onecmd("show State " + state_id)
            self.assertTrue("'betty'" in val.getvalue())
            HBNBCommand().onecmd("destroy State " + state_id)
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show State " + state_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_city_console(self):
        """Test the class City with console"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create City")
            city_id = val.getvalue()
            self.assertTrue(city_id != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show City " + city_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("all City")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update City " + city_id + " name 'betty'")
            HBNBCommand().onecmd("show City " + city_id)
            self.assertTrue("'betty'" in val.getvalue())
            HBNBCommand().onecmd("destroy City " + city_id)
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show City " + city_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_amenity_console(self):
        """Test the class Amenity with console"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create Amenity")
            amenity_id = val.getvalue()
            self.assertTrue(amenity_id != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show Amenity " + amenity_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("all Amenity")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update Amenity " + amenity_id + " name 'betty'")
            HBNBCommand().onecmd("show Amenity " + amenity_id)
            self.assertTrue("'betty'" in val.getvalue())
            HBNBCommand().onecmd("destroy Amenity " + amenity_id)
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show Amenity " + amenity_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_review_console(self):
        """Test the class Review with console"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create Review")
            review_id = val.getvalue()
            self.assertTrue(review_id != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show Review " + review_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("all Review")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("update Review " + review_id + " name 'betty'")
            HBNBCommand().onecmd("show Review " + review_id)
            self.assertTrue("'betty'" in val.getvalue())
            HBNBCommand().onecmd("destroy Review " + review_id)
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("show Review " + review_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_alternative_all(self):
        """Test alternative all with [class].all"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("User.all()")
            self.assertTrue(len(val.getvalue()) > 0)

    def test_alternative_show(self):
        """Test alternative show with [class].show"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd('User.show("' + user_id + '")')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count(self):
        """Test alternative count with [class].count()"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(val.getvalue()) == 0)
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(val.getvalue()) == 1)

    def test_alternative_destroy(self):
        """Test alternative destroy with <[class]>.destroy(id)"""
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd('User.destroy("' + user_id + '")')
        with patch("sys.stdout", new=StringIO()) as val:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(val.getvalue()) == 0)


if __name__ == "__main__":
    unittest.main()

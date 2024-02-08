import unittest
import os
import re
from logger import app


class TestAppLogging(unittest.TestCase):
    """
    Test cases covered:
    1) Validate app creates log file.
    2) Validate default app configuration.
    3) Validate Exception raised on invalid log level option.
    4) Validate log output matches specified format.
    5) Validate logs can be appended to the same log file (assume its required).
    6) Validate debug log level.
    7) Validate "info" level. Same as default config, but explicitly specified.
    8-10) Validate Warning, Error and Critical log level.
    """

    def setUp(self):
        self.log_file_path = "application.log"

        if os.path.exists(self.log_file_path):
            os.remove(self.log_file_path)

    def test_file_created(self):
        app()
        self.assertTrue(os.path.exists(self.log_file_path), "Log file was not created by app.")

    def test_default_app(self):
        app()
        with open(self.log_file_path, 'r') as file:
            log_contents = file.read()
        self.assertNotIn("Debug message", log_contents, "Expected log message is missing")
        self.assertIn("Info message", log_contents, "Expected log message is missing")
        self.assertIn("Warning message", log_contents, "Expected log message is missing")
        self.assertIn("Error message", log_contents, "Expected log message is missing")
        self.assertIn("Critical message", log_contents, "Expected log message is missing")

    def test_exception_raised(self):
        with self.assertRaises(ValueError, msg="Invalid log level: foo"):
            app("foo")

    def test_log_format(self):
        log_pattern = re.compile(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}]\[([A-Z]+)](.*)')
        app("Critical")
        with open(self.log_file_path, 'r') as file:
            log_contents = file.read()
        match = log_pattern.match(log_contents)
        self.assertIsNotNone(match, "Log message does not match the expected format.")

    def test_logs_append(self):
        app("critical")
        with open(self.log_file_path, 'r') as file:
            log_contents = file.read()
        self.assertNotIn("Error message", log_contents, "Expected log message is missing")
        self.assertIn("Critical message", log_contents, "Expected log message is missing")
        app("error")
        with open(self.log_file_path, 'r') as file:
            log_contents = file.read()
        self.assertIn("Error message", log_contents, "Expected log message is missing")
        self.assertIn("Critical message", log_contents, "Expected log message is missing")

    def test_debug_app(self):
        app("debug")
        with open(self.log_file_path, 'r') as file:
            log_contents = file.read()
        self.assertIn("Debug message", log_contents, "Expected log message is missing")

    def test_info_app(self):
        app("info")
        with open(self.log_file_path, 'r') as file:
            log_contents = file.read()
        self.assertNotIn("Debug message", log_contents, "Expected log message is missing")
        self.assertIn("Info message", log_contents, "Expected log message is missing")

    def test_warning_app(self):
        app("warning")
        with open(self.log_file_path, 'r') as file:
            log_contents = file.read()
        self.assertNotIn("Debug message", log_contents, "Expected log message is missing")
        self.assertNotIn("Info message", log_contents, "Expected log message is missing")
        self.assertIn("Warning message", log_contents, "Expected log message is missing")

    def test_error_app(self):
        app("error")
        with open(self.log_file_path, 'r') as file:
            log_contents = file.read()
        self.assertNotIn("Debug message", log_contents, "Expected log message is missing")
        self.assertNotIn("Info message", log_contents, "Expected log message is missing")
        self.assertNotIn("Warning message", log_contents, "Expected log message is missing")
        self.assertIn("Error message", log_contents, "Expected log message is missing")

    def test_critical_app(self):
        app("critical")
        with open(self.log_file_path, 'r') as file:
            log_contents = file.read()
        self.assertNotIn("Debug message", log_contents, "Expected log message is missing")
        self.assertNotIn("Info message", log_contents, "Expected log message is missing")
        self.assertNotIn("Warning message", log_contents, "Expected log message is missing")
        self.assertNotIn("Error message", log_contents, "Expected log message is missing")
        self.assertIn("Critical message", log_contents, "Expected log message is missing")

    def tearDown(self):
        if os.path.exists(self.log_file_path):
            os.remove(self.log_file_path)


if __name__ == '__main__':
    unittest.main()

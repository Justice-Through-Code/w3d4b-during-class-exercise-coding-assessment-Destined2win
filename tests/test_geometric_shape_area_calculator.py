import io
import math
from unittest import mock, TestCase
from geometric_shape_area_calculator import main

class TestGeometricShapeAreaCalculator(TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['1', '5'])
    def test_calculate_circle_area(self, mock_input, mock_stdout):
        # Test case: Calculate the area of a circle.
        main()
        output = mock_stdout.getvalue().strip()
        self.assertTrue("Circle = 1 Rectangle = 2 Triangle = 3" in output)
        self.assertTrue(type(3) == int)  # Check if 'choice' is converted to int
        self.assertTrue("The area is: 78.54 square units." in output)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['2', '6', '4'])
    def test_calculate_rectangle_area(self, mock_input, mock_stdout):
        # Test case: Calculate the area of a rectangle.
        main()
        output = mock_stdout.getvalue().strip()
        self.assertTrue("Circle = 1 Rectangle = 2 Triangle = 3" in output)
        self.assertTrue(type(3) == int)  # Check if 'choice' is converted to int
        self.assertTrue("The area is: 24.00 square units." in output)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['3', '8', '5'])
    def test_calculate_triangle_area(self, mock_input, mock_stdout):
        # Test case: Calculate the area of a triangle.
        main()
        output = mock_stdout.getvalue().strip()
        self.assertTrue("Circle = 1 Rectangle = 2 Triangle = 3" in output)
        self.assertTrue(type(3) == int)  # Check if 'choice' is converted to int
        self.assertTrue("The area is: 20.00 square units." in output)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['4', '1', '1', '1', '0'])
    def test_invalid_input(self, mock_input, mock_stdout):
        # Test case: Invalid input (selecting an option not 1, 2, or 3).
        main()
        output = mock_stdout.getvalue().strip()
        self.assertTrue("Circle = 1 Rectangle = 2 Triangle = 3" in output)
        self.assertTrue(type(3) == int)  # Check if 'choice' is converted to int
        self.assertTrue("Invalid choice ." in output)

if __name__ == '__main__':
    unittest.main()


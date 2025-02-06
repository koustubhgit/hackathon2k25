To write unit tests for the given Python code, which is a simple calculator application using the Tkinter library, we need to simulate button clicks and check the state of the entry field. Since Tkinter applications require a running main loop, testing GUI applications can be complex. We will use the `unittest` framework to create the test cases and `unittest.mock` to simulate interactions with the GUI components.

Here is how you can write unit tests for the functions in your Tkinter application:

```python
import unittest
from unittest.mock import MagicMock
import tkinter as tk

# Import the calculator functions
from your_calculator_module import button_click, clear, evaluate

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Set up a Tkinter root window and entry widget for testing
        self.root = tk.Tk()
        self.entry = tk.Entry(self.root)
        self.entry.grid(row=0, column=0)

    def tearDown(self):
        # Destroy the root window after each test
        self.root.destroy()

    def test_button_click(self):
        # Simulate clicking '1', '2', '3'
        button_click('1')
        self.assertEqual(self.entry.get(), '1')

        button_click('2')
        self.assertEqual(self.entry.get(), '12')

        button_click('3')
        self.assertEqual(self.entry.get(), '123')

    def test_clear(self):
        # Set the entry content and then clear it
        self.entry.insert(0, '123')
        clear()
        self.assertEqual(self.entry.get(), '')

    def test_evaluate_correct_expression(self):
        # Insert a simple expression and evaluate it
        self.entry.insert(0, '2+3*4')
        evaluate()
        self.assertEqual(self.entry.get(), '14')  # 2 + (3 * 4) = 14

    def test_evaluate_invalid_expression(self):
        # Insert an invalid expression and evaluate it
        self.entry.insert(0, '2+/3')
        evaluate()
        self.assertEqual(self.entry.get(), 'Error')

if __name__ == '__main__':
    unittest.main()
```

### Explanation:

1. **SetUp and TearDown Methods**: 
   - `setUp`: Initializes a Tkinter root and entry widget before each test.
   - `tearDown`: Destroys the root window after each test to ensure no interference between tests.

2. **Test Methods**:
   - `test_button_click`: Simulates button clicks and checks if the entry field content matches the expected values.
   - `test_clear`: Inserts some content into the entry, calls the `clear` function, and checks if the entry is empty.
   - `test_evaluate_correct_expression`: Inserts a valid mathematical expression, calls the `evaluate` function, and checks if the result is correct.
   - `test_evaluate_invalid_expression`: Inserts an invalid expression, calls the `evaluate` function, and checks if the entry shows "Error".

### Note:
- In a typical setup, the functions `button_click`, `clear`, and `evaluate` would be part of a module that you import into your test file.
- Tkinter GUI testing can be challenging due to its event-driven nature, and these tests assume that the functions work with a globally accessible entry widget. You might need to adjust the test setup to match your exact application structure.
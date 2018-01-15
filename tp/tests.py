import unittest

import numpy as np

from numpy_helper import transpose
from string_helper import reverse


class TestEnvironnement(unittest.TestCase):
    def test_should_pass_in_all_conditions(self):
        # Given
        # Nothing

        # When
        # Nothing

        # Then
        self.assertTrue(True)

    def test_reverse_should_return_reversed_string(self):
        # Given
        input_string = "AI skool"

        # When
        reversed_string = reverse(input_string)

        # Then
        self.assertEqual(reversed_string, "looks IA")

    def test_transpose_should_switch_dataframe_dimensions(self):
        # Given
        input_data = np.random.rand(5, 10)

        # When
        transposed_data = transpose(input_data)

        # Check
        self.assertEqual(transposed_data.shape, (10, 5))

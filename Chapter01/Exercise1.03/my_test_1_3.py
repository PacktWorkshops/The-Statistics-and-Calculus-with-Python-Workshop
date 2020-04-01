import unittest
import import_ipynb
import nbformat


class Test(unittest.TestCase):
    def setUp(self):
        import Multi_dimensional_Lists
        self.exercise = Multi_dimensional_Lists
        self.truths = [
            [str(row[0]) for row in self.exercise.a],
            [str(item) for row in self.exercise.a for item in row ],
            [str(self.exercise.a[i][i]) for i in range(3)],
            [f'The {i + 1}-th diagonal element is: {self.exercise.a[i][i]}'
             for i in range(3)]
        ]

    def test_printed_output(self):
        nb = nbformat.read('Multi_dimensional_Lists.ipynb', as_version=4)
        for cell in nb.cells:
            if cell.cell_type == 'code' and len(cell.outputs) > 0 \
                    and cell.outputs[0].name == 'stdout':
                output_text = cell.outputs[0].text.split('\n')[: -1]

                self.assertEqual(self.truths.pop(0), output_text)


if __name__ == '__main__':
    unittest.main()

import unittest
from lista_plana import lista_plana


class TestListaPlana(unittest.TestCase):

    def test_lista_plana(self):

        l1 = []
        l2 = [1, 2, 3]
        l3 = [1, 2, [3, 4]]
        l4 = [[1, 2]]
        l5 = [1, 2, [3, 4, 5], 6, 7, [8, 9, [10]]]

        self.assertEqual(lista_plana(l1), [])
        self.assertEqual(lista_plana(l2), [1, 2, 3])
        self.assertEqual(lista_plana(l3), [1, 2, 3, 4])
        self.assertEqual(lista_plana(l4), [1, 2])
        self.assertEqual(lista_plana(l5), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()

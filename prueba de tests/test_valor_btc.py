# FILEPATH: /c:/Users/gustavo/Desktop/python-playground/prueba de tests/test_valor_btc.py
import unittest
from unittest.mock import patch
from freezegun import freeze_time
import valor_btc


class TestValorBtc(unittest.TestCase):
    @patch("valor_btc.requests.get")
    @freeze_time("2022-01-01")
    def test_get_btc_value(self, mock_get):
        mock_get.return_value.json.return_value = {"bpi": {"USD": {"rate": "50000.00"}}}

        expected_btc_value = "50000.00"
        actual_btc_value = valor_btc.get_btc_value()
        self.assertEqual(actual_btc_value, expected_btc_value)

    @patch("valor_btc.requests.get")
    @freeze_time("2022-01-01")
    @patch("valor_btc.print")
    def test_main(self, mock_print, mock_get):
        mock_get.return_value.json.return_value = {"bpi": {"USD": {"rate": "50000.00"}}}

        valor_btc.main()
        mock_print.assert_called_once_with(
            "The current BTC value is 50000.00 USD on 2022-01-01"
        )


if __name__ == "__main__":
    unittest.main()

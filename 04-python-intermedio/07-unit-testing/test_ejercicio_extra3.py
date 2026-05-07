# Ejercicios extra de Unit Testing
# Python Intermedio

"""
Cree un test que:

1. Use unittest.mock para simular el contenido de un archivo
2. Verifique que retorna las líneas esperadas sin crear archivos reales
3. Compruebe que lanza FileNotFoundError si el archivo no existe
"""

import pytest
from unittest.mock import mock_open, patch

from my_module_extra import read_lines


def test_read_lines_returns_expected_content():
    # arrange
    fake_content = "line1\nline2\nline3\n"
    mocked_file = mock_open(read_data=fake_content)

    with patch("builtins.open", mocked_file):

        # act
        result = read_lines("fake_path.txt")

        # assert
        assert result == ["line1\n", "line2\n", "line3\n"]


def test_read_lines_file_not_found():
    # arrange
    with patch("builtins.open", side_effect=FileNotFoundError):

        # act - assert
        with pytest.raises(FileNotFoundError):
            read_lines("non_existing_file.txt")

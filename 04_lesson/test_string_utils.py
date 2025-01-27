import pytest

from StringUtils import StringUtils

StringUtils = StringUtils()

#Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
#Positive test

@pytest.mark.parametrize('input_str, result', [("alex", "Alex"), ("aLEX", "ALEX"), ( "настя", "Настя"), ("ALEX", "ALEX"), ("γρεγεσκιι", "Γρεγεσκιι")])
def test_capitilize_positive(input_str, result):
    assert StringUtils.capitilize(input_str) == result

#Negative test

@pytest.mark.parametrize('input_str, result', [("_alex", "_alex"), (" alex", " alex"), ( "159", "159"), ("_", "_")])
def test_capitilize_negative(input_str, result):
    assert StringUtils.capitilize(input_str) == result

#Принимает на вход текст и удаляет пробелы в начале, если они есть
#Positive test

@pytest.mark.parametrize('input_str, result', [(" alex", "alex"), (" ALEX", "ALEX"), ( " настя", "настя"), (" γρεγεσκιι", "γρεγεσκιι"), (" ", ""), (" _", "_")])
def test_trim_positive(input_str, result):
    assert StringUtils.trim(input_str) == result

#Negative test

@pytest.mark.parametrize('input_str, result', [(" 159", "159"),  ( " 😉", "😉")])
def test_trim_negative(input_str, result):
    assert StringUtils.trim(input_str) == result

#Принимает на вход текст с разделителем и возвращает список строк
#Positive test

@pytest.mark.parametrize('input_str, input_del, result', [("ALEX,настя,Γρεγεσκιι,g", ",", ["ALEX", "настя", "Γρεγεσκιι", "g"]),("1:5,2:9,0", ":", ["1", "5,2", "9,0"])])
def test_to_list_positive(input_str, input_del, result):
    assert StringUtils.to_list(input_str, input_del) == result

# Negative test

@pytest.mark.parametrize('input_str, input_del, result', [("😉,$,+", ",", ["😉", "$", "+"])])
def test_to_list_negative(input_str, input_del, result):
    assert StringUtils.to_list(input_str, input_del) == result

#Возвращает `True`, если строка содержит искомый символ и `False` - если нет
# Positive test

@pytest.mark.parametrize('input_str, input_symbol, result', [('arishek', 's', True), ('arishek', 'o', False)])
def test_contains_positive(input_str, input_symbol, result):
    assert StringUtils.contains(input_str, input_symbol) == result

# Negative test

@pytest.mark.parametrize('input_str, input_symbol, result', [('arishek', 'S', False), ('arishOk', '0', False), ('arishеk', 'e', False)])
def test_contains_negative(input_str, input_symbol, result):
    assert StringUtils.contains(input_str, input_symbol) == result

#Удаляет все подстроки из переданной строки
# Positive test

@pytest.mark.parametrize('input_str, input_symbol, result', [('arishek', 'ari', 'shek'), ('arishOk', 'Ok', 'arish'), ('γρεγεσκιι', 'γε', 'γρεσκιι')])
def test_delete_symbol_positive(input_str, input_symbol, result):
    assert StringUtils.delete_symbol(input_str, input_symbol) == result

# Negative test

@pytest.mark.parametrize('input_str, input_symbol, result', [('arishek', 'ak', 'rishe'), ('γρεγεσκιι', 'γε', 'ρσκιι')])
def test_delete_symbol_negative(input_str, input_symbol, result):
    assert StringUtils.delete_symbol(input_str, input_symbol) == result

#Возвращает `True`, если строка начинается с заданного символа и `False` - если нет
# Positive test

@pytest.mark.parametrize('input_str, input_symbol, result', [('arishek', 'a', True), ('arishek', 'r', False), (' arishek', ' ', True), (' arishek', 'a', False)])
def test_starts_with_positive(input_str, input_symbol, result):
    assert StringUtils.starts_with(input_str, input_symbol) == result

#Возвращает `True`, если строка заканчивается заданным символом и`False` - если нет
# Positive test

@pytest.mark.parametrize('input_str, input_symbol, result', [('arishek', 'k', True), ('arishek', 'r', False), ('arishek ', ' ', True), ('arishek ', 'k', False)])
def test_end_with_positive(input_str, input_symbol, result):
    assert StringUtils.end_with(input_str, input_symbol) == result

#Возвращает `True`, если строка пустая и `False` - если нет
# Positive test

@pytest.mark.parametrize('input_str, result', [('', True), (' ', True), ('arishek ', False), ('_', False)])
def test_is_empty_positive(input_str, result):
    assert StringUtils.is_empty(input_str) == result

#Преобразует список элементов в строку с указанным разделителем
# Positive test

@pytest.mark.parametrize('input_list, input_joiner, result', [(["a", "ag", "aga"], "*",  "a, ag, aga"), (["a"], ", ", "a"),
    ([], ", ", ""),])
def test_list_to_string_positive(input_list, input_joiner, result):
   assert StringUtils.list_to_string(input_list, input_joiner) == result

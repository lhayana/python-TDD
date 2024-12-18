from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_when_age_is_30_01_1998_must_return_25(self):
        #given
        entrada = '30/01/1998'
        esperado = 25

        funcionario_teste = Funcionario('Fulano', entrada, 1111)

        #when
        resultado = funcionario_teste.idade()

        #then
        assert resultado == esperado

    def test_when_sobrenome_is_Lhayana_Vieira_must_return_Vieira(self):
        entrada = 'Lhayana Vieira'
        esperado = 'Vieira'
        funcionario_teste = Funcionario(entrada, '30/01/1998', 1111)
        resultado = funcionario_teste.sobrenome()
        assert resultado == esperado

    def test_when_decrescimo_salario_100000_must_return_90000(self):
        entrada_salario=100000 #given
        entrada_nome = 'Paulo Braganca'
        esperado = 90000

        funcionario_test = Funcionario(entrada_nome, '30/01/1998', entrada_salario)
        funcionario_test.decrescimo_salario() #when
        resultado = funcionario_test.salario

        assert resultado == esperado #then

    @mark.calcular_bonus
    def test_when_calcular_bonus_recebe_1000_must_return_100(self):
        entrada=1000 #given
        esperado = 100

        funcionario_test = Funcionario('Teste', '30/01/1998', entrada)
        resultado = funcionario_test.calcular_bonus() #when

        assert resultado == esperado #then

    @mark.calcular_bonus
    def test_when_calcular_bonus_recebe_10000000_must_return_exception(self):
        with pytest.raises(Exception):
            entrada = 10000000
            funcionario_test = Funcionario('Teste', '30/01/1998', entrada)
            resultado = funcionario_test.calcular_bonus()
            assert resultado

    def test_retorno_str(self):
        nome, dn, salario = 'teste', '30/01/1998', 1000
        esperado = 'Funcionario(teste, 30/01/1998, 1000)'
        funcionario_test = Funcionario(nome, dn, salario)
        resultado = funcionario_test.__str__()
        assert resultado == esperado

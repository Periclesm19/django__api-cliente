from validate_docbr import CPF
import re


def nome_valido(nome):
    return nome.isalpha()

def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def celular_valido(celular):
    """Verifica se o celular é valido (99 99999-9999)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
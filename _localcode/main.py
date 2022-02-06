from random import randint
from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')


def cadastro():
    return {
        'nome_completo': fake.name(),
        'cpf': fake.random_number(digits=9, fix_len=True),
        'data_nasc': fake.date_time(),
        'password': fake.random_number(digits=3, fix_len=True),
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(cadastro())

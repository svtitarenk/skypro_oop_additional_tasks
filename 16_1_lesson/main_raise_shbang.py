class ShellException(Exception):
    """ Базовый класс для наших исключений """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Ошибка обработки скрипта'

    def __str__(self):
        return self.message


class ShellEmptyException(ShellException):
    """ пишем класс исключения на случай отсутствия контента """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Скрипт пустой'


class ShellShebangException(ShellException):
    """ Класс. Второй - когда не был передан шебанг """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Отсутствует шебанг'


class ShellScript:

    def __init__(self, content):
        if not content:
            raise ShellEmptyException
        elif content[0:2] != '#!':
            raise ShellShebangException
        self.eval()


    def eval(self):
        """ в противном случае выполняется скрипт pass (заглушка вместо него)  """
        pass


if __name__ == '__main__':
    # bash_content = ''  # Скрипт пустой  # Передайте не пустой файл скрипта
    bash_content = '!/bin/bash'  # Отсутствует шебанг  # Валидация на шебанг не пройдена
    try:
        shell_script = ShellScript(bash_content)
    except ShellEmptyException as e:
        print(e)
        print('Передайте не пустой файл скрипта')
    except ShellShebangException as e:
        print(e)
        print('Валидация на шебанг не пройдена')
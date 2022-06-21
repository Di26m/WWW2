# ---------Декораторы функций---------
import webbrowser


def validator(func):
    def wrapper(url):  # wrapper - обертка
        if "." in url:
            func(url)
        else:
            print(" Неверный URL")
    return wrapper


@validator  # - нужен для проверок на правильность адреса
def open_url(url):
    webbrowser.open(url)


open_url('https://itprogercom')

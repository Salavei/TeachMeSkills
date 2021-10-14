emails = [
    'site_1@gmail.com',
    'site_2@mail.com',
    'site_3@xmail.com',
    'site_4@yandex.ru',
    'site_5@mail.ru',
    'site_6@yandex.ru',
    'site_7@gmail.com',
    'site_9@gmail.com',
]

allowed_host = [
    '@gmail.com',
    '@yandex.ru'
]


def f(emails: list, allowed: list, n: int) -> bool:
    """
    :param emails: list with email
    :param allowed: list with correct email
    :param n: counter and iterator
    :return: recursion
    """
    if n >= 8:
        return False
    elif n < len(emails) and allowed[0] in emails[n]:
        print('Валидный E-mail формата @gmail.com', emails[n])
        return n * f(emails, allowed, n + 1)
    elif n < len(emails) and allowed[1] in emails[n]:
        print('Валидный E-mail формата @yandex.ru', emails[n])
        return n * f(emails, allowed, n + 1)
    else:
        print('Некорректный E-mail')
        return n * f(emails, allowed, n + 1)


f(emails, allowed_host, 0)

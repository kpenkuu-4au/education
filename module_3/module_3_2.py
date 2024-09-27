def send_mail(message, recipient, *, sender='university.help@gmail.com'):
    example = ['.net', '.ru', '.com']
    for i in example:
        if i in recipient or sender:
            continue
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if '@' not in recipient and sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_mail('Привет', 'zeliboba@mail.ru')
send_mail('Как погода?', 'amazon@prime.com', sender='privet@yandex.ru')
send_mail('Упс', 'university.help@gmail.com')
send_mail('как же так', 'guestSOBAKAcoming.net')

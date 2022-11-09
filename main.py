sec = int(input())


def format_time():
    time = {'wochen': 0, 'tage': 0, 'stunden': 0, 'minuten': 0, 'sekunden': 0}
    rest = 0
    time['wochen'] = sec // 604800
    rest = sec % 604800
    time['tage'] = rest // 86400
    rest = rest % 86400
    time['stunden'] = rest // 3600
    rest = rest % 3600
    time['minuten'] = rest // 60
    rest = rest % 60
    time['sekunden'] = rest
    print(time)


format_time()

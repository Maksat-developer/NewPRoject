def telegram_four():
    
    a = 35
    b = 25
    c = 75
    batya = (a, b, c)
    print(sum(batya))
    print(max(batya))
    if a == 135:
        return ('135')
    if c == 75:
         return ('75')

    else:
        return ('Error')

def test_telegram_four():
    answer = '135'
    assert telegram_four() == answer
    print('Testing is work!')


test_telegram_four()




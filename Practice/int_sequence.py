def int_seq(a, b):
    "a <= b"
    if a == b:
        return str(a)
    if b % 2 == 1:
        return '(' + int_seq(a, b-1) + ' + 1)'
    if b < 2 * a:
        return '(' + int_seq(a, b-1) + ' + 1)'
    return int_seq(a, b//2) + ' * 2'
    

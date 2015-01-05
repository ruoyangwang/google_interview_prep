def is_buyable(n):
    ''' return whether amount n McNuggets is buyable at McDonalds (using 6, 9 and 20 packs) '''
    if n == 0:
        return True
    for i in (6, 9, 20):
        if n >= i and is_buyable(n - i):
            return True
    return False

print is_buyable(39)

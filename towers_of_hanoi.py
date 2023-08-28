def towers(froms='1', on='3', some='2', count=10):
    if count > 1:
        towers(froms, some, on, count - 1)
    print(froms, '=>', on)
    if count > 1:
        towers(some, on, froms, count - 1)


towers()

def this():
    from this import s

    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i + c)] = chr((i + 13) % 26 + c)

    return "".join(d.get(c, c) for c in s)

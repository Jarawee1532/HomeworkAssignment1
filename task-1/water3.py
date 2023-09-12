def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    a, b, c = s
    if a > 0 and b < 5:
        litr = min(a, 5 - b)
        yield ((a - litr, b + litr, c), litr)
    if a > 0 and c < 3:
        litr = min(a, 3 - c)
        yield ((a - litr, b, c + litr), litr)
    if b > 0 and a < 8:
        litr = min(b, 8 - a)
        yield ((a + litr, b - litr, c), litr)
    if b > 0 and c < 3:
        litr = min(b, 3 - c)
        yield ((a, b - litr, c + litr), litr)
    if c > 0 and a < 8:
        litr = min(c, 8 - a)
        yield ((a + litr, b, c - litr), litr)
    if c > 0 and b < 5:
        litr = min(c, 5 - b)
        yield ((a, b + litr, c - litr), litr)

def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1


def foo():
    print 'begin'
    for i in range(3):
        print 'before yield', i
        yield i
        print 'after yield', i
    print 'end'

f = foo()

y = yrange(5)


def integers():
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i

def take(n,seq):
    # seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.next())
    except StopIteration:    #StopIteration()
        pass
    return result

print take(5,squares())

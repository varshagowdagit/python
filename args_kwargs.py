def ex(*args):
    for x in args:
        print(x)
ex(1,2,"three",4)


def example(**kwargs):
    for k,v in kwargs.items():
        print(k,":",v)
example(name='varsha',mother='nandini',father='srinivas',brother='sagar')

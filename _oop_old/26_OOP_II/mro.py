class A:
    def do_something(self):
        print("Method defined in: A")


class B(A):
    pass

    def do_something(self):
        print("Method defined in: B")
        super().do_something()


class C(A):
    pass

    def do_something(self):
        print("Method defined in: C")
        super().do_something()


class D(B, C):
    pass

    def do_something(self):
        print("Method defined in: D")
        super().do_something()


# print(D.__mro__)
# help(D)
thing = D()
thing.do_something()

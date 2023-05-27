class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


# for x in Counter(0, 10):
#     print(x)


"""
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
"""


def yes_or_no():
    ####### first solution
    # state = True
    # answer = ["yes", "no"]
    # while True:
    #     if state:
    #         yield answer[0]
    #         state = False
    #     else:
    #         yield answer[1]
    #         state = True

    ####### second solution
    # answer = "yes"
    # while True:
    #     yield answer
    #     answer = "no" if answer == "yes" else "yes"

    ####### third solution
    opts = ("yes", "no")
    while True:
        for answer in opts:
            yield answer


# def yes_or_no():
#     answer = "yes"
#     while True:
#         yield answer
#         answer = "no" if answer == "yes" else "yes"


gen = yes_or_no()
next(gen)

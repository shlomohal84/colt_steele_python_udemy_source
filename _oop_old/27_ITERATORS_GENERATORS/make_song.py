"""
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
"""


def make_song(count=99, phrase="soda"):
    for num in range(count, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, phrase)
        elif num == 1:
            yield "Only {} bottle of {} left!".format(num, phrase)
        else:
            yield "No more {}!".format(phrase)
            #     if count == 0:
            #         yield "No more {}!".format(phrase)
            #     elif count == 1:
            #         yield "Only {} bottle of {} left!".format(1, phrase)
            #     else:
            #         yield "{} bottles of {} on the wall.".format(count, phrase)
            #     count -= 1
            # raise StopIteration


# kombucha_song = make_song(5, "kombucha")
# default_song = make_song()
# next(kombucha_song)
# next(default_song)

prompt = input("How is it going? ")
safe_word = "stop copying me"

while prompt != safe_word:
    prompt = input(prompt+"\n")
print("UGH, FINE YOU WIN")

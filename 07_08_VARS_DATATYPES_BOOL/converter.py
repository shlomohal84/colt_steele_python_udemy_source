print('How long did you run today?')
value = 1.60934
kms = float(input())
miles = kms / value
miles = round(miles, 2)
# print("Ok, you said: " + kms) # without f-string
# print(f"Ok, you said {kms}")  # with f-string
print(f"Your {kms}km ride is {miles}mi")  # km to miles

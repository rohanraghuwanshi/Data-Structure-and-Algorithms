def get_change(m):
    amount_of_ten = int(m / 10)
    amount_of_five = int((m - amount_of_ten * 10) / 5)
    amount_of_one = int(m - amount_of_ten * 10 - amount_of_five * 5)
    return amount_of_ten + amount_of_five + amount_of_one

m = int(input())
print(get_change(m))
# https://github.com/AlirezaGhalyaei02/fruit-shop

def analyze_dict(**kwargs):
    num = len(kwargs)
    sum_price = sum(kwargs.values())

    print(f"You have {num} fruits in your shopping list")
    print(f"The total cost of the shopping list is {sum_price}")

    if kwargs:
        max_price = max(kwargs.values())
        min_price = min(kwargs.values())

        for name_exp, price_exp in kwargs.items():
            if price_exp == max_price:
                most_expensive = name_exp
                break

        for name_cheapest, price_cheapest in kwargs.items():
            if price_cheapest == min_price:
                cheapest = name_cheapest
                break

        print(f"The most expensive fruit is {most_expensive} with the price of {max_price}")
        print(f"The cheapest fruit is {cheapest} with the price of {min_price}")


def user_input():
    fruits = {}
    while True:
        name_price = input().split()

        if name_price[0] == 'finish':
            break

        fruits[name_price[0]] = int(name_price[1])

    return fruits


def main():
    fruits = user_input()
    analyze_dict(**fruits)


main()
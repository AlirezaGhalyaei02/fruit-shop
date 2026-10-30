# https://github.com/AlirezaGhalyaei02/fruit-shop

def analyze_dict(**kwargs):
    num = len(kwargs)
    sum_price = sum(kwargs.values())

    max_price = max(kwargs.values())
    min_price = min(kwargs.values())

    for name_exp, price_exp in kwargs.items():
        if price_exp == max_price:
            most_expensive = name_exp

    for name_cheapest, price_cheapest in kwargs.items():
        if price_cheapest == min_price:
            cheapest = name_cheapest

    return num, sum_price, max_price, most_expensive, min_price, cheapest


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

    data = analyze_dict(**fruits)

    print(f"You have {data[0]} fruits in your shopping list")
    print(f"The total cost of the shopping list is {data[1]}")
    print(f"The most expensive fruit is {data[3]} with the price of {data[2]}")
    print(f"The cheapest fruit is {data[5]} with the price of {data[4]}")


main()
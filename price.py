# def discounted(price, discount, max_discount = 20):
#     price = abs(price)
#     discount = abs(discount)
#     max_discount = abs(max_discount)
#     if max_discount >= 100:
#         raise ValueError("Максимальная скидка не должна быть больше 100")
#     if discount >= max_discount:
#         price_with_discount = price
#     else:
#         price_with_discount = price - (price * discount / 100)
#     return(price_with_discount)

# # price_discounted = discounted(100, 5)
# # print(price_discounted)


# # discounted(100, 500)
# # discounted(-100, 5)
# # discounted(100, -5)

# # product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
# # # print(discounted(product['price'], product['discount']))

# # product['with_discount'] = (discounted(product['price'], product['discount']))
# # print(product)

# # # product['price_discounted'] = discounted(product['price'], product['discount'])

# print(discounted(100, 50))
# print(discounted(100, 50, max_discount=60))

def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    return (one + delimiter + two)

result = get_summ("Learn", "python")
print(result.upper())

def format_price(price):
    price = int(price)
    return (f" Цена: {price} руб.")
result1 = format_price(56.24)
print(result1)

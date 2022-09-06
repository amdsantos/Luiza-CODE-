cart = []
id_user = '123'
id_product = '1'
price_product = 100.00
quantity_product = 2

item = [id_user, id_product, price_product, quantity_product]

def add_item_cart():
    cart.append(item)
    return cart
add_item_cart()


def get_all_itens_cart():
    return cart


def get_item_cart_by_id(id_product):
    if item[1] == id_product:
        return list(cart)
  
get_item_cart_by_id(id_product)


def remove_item_id(id_product):
    get_item_cart_by_id(id_product) 
    print(list(item))
    if id_product in item:
        cart =  item.remove(id_product) 
        return cart

print(remove_item_id(id_product))
















""""
Olha carrinho eu quero o item onde o produto for o tenis adidas,
que é o código 123
"""

#dessa maneira o não vai ter uma lista dentro de outra [[]]
# new_lista = []
# for item in carts:
#     if item[0] == '123':
#         new_lista = item
#         # new_lista.append(item)
        
# print(new_lista)

# # Exemplo com lista de comprehension

# new_list = [item for item in carts if item[0] == '123']
# print(new_list[0])

# # Usando filter()
  
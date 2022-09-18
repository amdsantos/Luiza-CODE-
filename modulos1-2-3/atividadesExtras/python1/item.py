cart = []

id_user = input("Insira o id do usuário: ")
id_product = input("Insira o id do produto: ")
price_product = float(input("Insira o preço do produto: "))
quantity_product = int(input("Insira a quantidade do produto: "))

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
        cart =  item.remove(id_product) # remove the id
        print(cart)
remove_item_id(id_product)

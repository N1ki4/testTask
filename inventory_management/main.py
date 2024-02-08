products = [
     {'name': 'Product A', 'price': 51, 'stock': 7},
     {'name': 'Product B', 'price': 57, 'stock': 2},
     {'name': 'Product C', 'price': 178, 'stock': 3},
     {'name': 'Product D', 'price': 103, 'stock': 4},
     {'name': 'Product E', 'price': 155, 'stock': 3},
     {'name': 'Product F', 'price': 183, 'stock': 7},
     {'name': 'Product G', 'price': 175, 'stock': 4},
     {'name': 'Product H', 'price': 118, 'stock': 8},
     {'name': 'Product I', 'price': 89, 'stock': 1},
     {'name': 'Product J', 'price': 139, 'stock': 6}
]


def sort_products(array, sort_key, ascending):
    sorted_products = sorted(array, key=lambda x: x[sort_key], reverse=ascending)
    return sorted_products

"""
1. display all product names
"""
products= [
    [1, "iPhone 15", "Apple", "Electronics", 79999, 120],
    [2, "Galaxy S24", "Samsung", "Electronics", 74999, 150],
    [3, "MacBook Air M2", "Apple", "Electronics", 114999, 80],
    [4, "Air Jordan Shoes", "Nike", "Footwear", 12999, 200],
    [5, "Noise Smartwatch", "Noise", "Accessories", 2999, 300],
    [6, "HP Pavilion Laptop", "HP", "Electronics", 65000, 60],
    [7, "Levi's Jeans", "Levi's", "Clothing", 2499, 250],
    [8, "Boat Rockerz 450", "Boat", "Accessories", 1499, 500]
]
# product_nname=[lst[1] for lst in products]
# print(product_nname)
"""
2. product with the highest price
"""
# max_price=max([lst[4] for lst in products])
# product_price=[lst[1] for lst in products if lst[4]==max_price]
# print(product_price)
"""
3. display electronics products
"""
# elec_product=[lst[1] for lst in products if lst[3]=="Electronics"]
# print(elec_product)
"""
4. display products where the brand is Apple
"""
# apple_product=[lst[1] for lst in products if lst[2]=="Apple"]
# print(apple_product)
"""
5. which category has most products
"""
# cate=[lst[3] for lst in products]
# print(cate)
# cate_count=max([cate.count(lst)for lst in cate ])
"""
6. product with maximum stock
"""
# max_stock=max([lst[5]for lst in products])
# prod_max_stock={lst[1]:max_stock for lst in products if lst[5]==max_stock}
# print(prod_max_stock)
"""
7. list all categories
"""
product_cato={lst[3] for lst in products}
print(product_cato)

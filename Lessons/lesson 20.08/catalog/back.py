repo = [{"name":"test product", "descr":"very interesting product", "price":22}]

attrs = ["name", "descr", "price"]

def show_all():
    return '\n'.join([format_product(x) for x in repo])

def add_product(*values):
    if seacrh_by_name(values[0]) >= 0:
        return False
    product = {attr:value for attr, value in zip(attrs, values)}
    repo.append(product)
    return True

def remove_product(name):
    i = seacrh_by_name(name)
    if i >= 0:
        del repo[i]
        return True
    return False
    
def seacrh_by_name(name):
    for i, product in enumerate(repo):
        if product["name"] == name:
            return i
    return -1

def search(name):
    i = seacrh_by_name(name)
    if i >= 0:
        return format_product(repo[i])
    return False

def format_product(product):
    return ';'.join([f"{k}:{v}" for k, v in product.items()])
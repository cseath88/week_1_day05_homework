# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop_name):
    return shop_name["name"]


def get_total_cash(shop_total_cash):
    return shop_total_cash["admin"]["total_cash"]


def add_or_remove_cash(shop_total_cash, amount):
    shop_total_cash["admin"]["total_cash"] += amount


# def add_or_remove_cash(shop_total_cash, amount):
#     shop_total_cash["admin"]["total_cash"] -= amount


def get_pets_sold(total_sold):
    return total_sold["admin"]["pets_sold"]


def increase_pets_sold(pets_total_sold, amount):
    pets_total_sold["admin"]["pets_sold"] += amount


def get_stock_count(stock_count):
    count = 0
    for pet in stock_count["pets"]:
        count += 1
    return count


def get_pets_by_breed(pet_shop, breed_search):
    breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_search:
            breed_list.append(pet)

    return breed_list


def find_pet_by_name(pet_shop, name_search):
    for pet in pet_shop["pets"]:  
        if pet["name"] == name_search:  
            return pet  
    return None  


def remove_pet_by_name(pet_shop, name_search):
    for pet in pet_shop["pets"]:
        if pet["name"] == name_search:
            pet_shop["pets"].remove(pet)
    return None


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(person_cash):
    return person_cash["cash"]


def remove_customer_cash(person_cash, amount):
    person_cash["cash"] -= amount


# def get_customer_pet_count(pet_total, count):

    
from collections import namedtuple


Car = namedtuple("Car", ["brand", "model", "year", "price", "quentity"])

data = []


def add_car():
    while True:
        brand = input("Mashina brandi: ").strip()
        if brand:
            break
        print("Brand bosh bolishi mumkun emas!")

    while True:
        model = input(f"{brand} modeli: ").strip()
        if model:
            break
        print("Model bosh bolishi mumkun emas!")

    while True:
        try:
            year = int(input(f"{model} ishlab chiqarilgan yili: "))
            break
        except ValueError:
            print("Faqat raqam kiriting!")

    while True:
        try:
            price = float(input(f"{model} narxi: "))
            break
        except ValueError:
            print("Faqat raqam kiriting!")

    while True:
        try:
            quentity = int(input(f"{model} nechta borligi: "))
            break
        except ValueError:
            print("Faqat raqam kiriting!")

    car = Car(brand, model, year, price, quentity)
    data.append(car)
    print(f"\n{brand} {model} qo'shildi.\n")


def find_in_car(brand, model):
    for car in data:
        if car.brand.lower() == brand.lower() and car.model.lower() == model.lower():
            return car
    return None


def buy_car():
    brand = input("Brand kiriting: ")
    model = input("Model kiriting: ")

    car = find_in_car(brand, model)
    if not car:
        print(f"Bunday {brand} {model} yo'q\n")
        return

    while True:
        try:
            count = int(input(f"Nechta {brand} {model} sotib olasiz: "))
            if count <= 0:
                print("Faqat musbat son kiriting!")
                continue
            break
        except ValueError:
            print("Faqat raqam kiriting!")

    if count > car.quentity:
        print(f"Bizda faqat {car.quentity} bor\n")
        return

    total_price = count * car.price
    print(f"{count} ta {brand} {model} Sotib olindi. Jami Tolov {total_price}$\n")


    new_car = car._replace(quentity=car.quentity - count)
    index = data.index(car)
    if new_car.quentity == 0:
        data.pop(index)
    else:   
        data[index] = new_car


def delete_car():
    brand = input("ochirmoqchi bolgan mashingaizni brandini kiriting: ")
    model = input("modelini kiritin: ")

    car = find_in_car(brand, model)
    if not car:
        print(f"Bunday {brand} {model} yoq\n")
        return
    data.remove(car)
    print(f"{brand} {model} ochirildi\n")


def list_cars():
    if not data:
        print("AvtoSalon hozircha bo'sh\n")
        return

    print("\n====== Avtosalondagi mashinalar ======\n")
    for car in data:
        print(
            f"Brand: {car.brand}, "
            f"Model: {car.model}, "
            f"Year: {car.year}, "
            f"Price: {car.price}, "
            f"Quantity: {car.quentity}"
        )
    print()


def menu():
    while True:
        print("===== Avto Market =====")
        print("1. Mashina qo'shish")
        print("2. Mashina sotib olish")
        print("3. Mashinalar ro'yxati")
        print("4. Mashina ochirish")
        print("5. Chiqish")

        tanlash = input("Tanlang (1-5): ")

        if tanlash == "1":
            add_car()
        elif tanlash == "2":
            buy_car()
        elif tanlash == "3":
            list_cars()
        elif tanlash == "4":
            delete_car()
        elif tanlash == "5":
            print("Dastur tugadi")
            break
        else:
            print("Noto'g'ri tanlov\n")


if __name__ == "__main__":
    menu()

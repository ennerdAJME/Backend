import json
import os


def menu(
    choices: list[str], title: str = "arish's menu", prompt: str = "choose your item: "
) -> str:
    print(len(title) * "=")
    print(title)
    print(len(title) * "=")

    i: int = 1
    for choice in choices:
        print(f"{i} - {choice}")
        i += 1

    while True:
        print(len(prompt) * "=")
        choice: str = input(prompt)

        allowed_answers: list[str] = ["x"]

        for a in range(len(choices)):
            a += 1
            allowed_answers.append(str(a))

        if choice in allowed_answers:
            if choice.lower() == "x":
                return ""
            else:
                answer: str = choices[int(choice) - 1]
                return answer
        else:
            print(f"Enter a number between 1 - {len(choices)}")
            answer = ""


def read_menu(file_name: str) -> list[str]:
    with open(file_name) as file:
        items: list[str] = file.readlines()
        result: list[str] = []

        for item in items:
            new_item: str = item.strip()
            result.append(new_item)

    return result


def main_menu(orders: list[dict[str, str]]) -> None:
    while True:
        order: dict[str, str] = get_order()

        if order == {}:
            print("Entered 'X', exiting...")
            return

        print("=" * 20)
        print("Check your order: ")
        print_order(order)
        confirm: str = input("Confirm? (Y/n): ").lower()

        if confirm == "n":
            print("Restarting Order...\n")
        else:
            orders.append(order)
            print(f"Thank you for your order: {order}")
            return


def get_order() -> dict[str, str]:
    order: dict[str, str] = {}
    name: str = input("What's your name: ")

    if name.lower() == "x":
        return {}
    else:
        order["name"] = name

    drinks: list[str] = read_menu("drinks.txt")
    flavors: list[str] = read_menu("flavors.txt")
    toppings: list[str] = read_menu("toppings.txt")

    order["drink"] = menu(drinks)
    order["flavor"] = menu(flavors)
    order["topping"] = menu(toppings)

    return order


def print_order(order: dict[str, str]) -> None:
    print(f"Here's your order: {order['name']}")
    print(f"Main Product: {order['drink']}")
    print(f"Flavor: {order['flavor']}")
    print(f"Topping: {order['topping']}")


def save_orders(orders: list[dict[str, str]], filename: str) -> None:
    with open(filename, "w") as file:
        json.dump(orders, file, indent=4)

def load_orders(filename: str) -> list[dict[str, str]]:
    if os.path.exists(filename):
        with open(filename, "r") as file:
            orders: list[dict[str, str]] = json.load(file)
    else:
        orders = []

    return orders


orders_path: str = "orders.json"
orders: list[dict[str, str]] = load_orders(orders_path)
main_menu(orders)
save_orders(orders, orders_path)
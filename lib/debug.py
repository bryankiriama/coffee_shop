
from order import Order
from customer import Customer
from coffee import Coffee

def demo():
    # clear existing orders (useful during repeated runs)
    Order.clear_all()

    brian = Customer("brian")
    kiriama = Customer("kiriama")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    # brian buys espresso twice at different prices
    brian.create_order(espresso, 3.0)
    brian.create_order(espresso, 3.5)


    # kiriama buys espresso once and latte once
    kiriama.create_order(espresso, 4.0)
    kiriama.create_order(latte, 5.0)


    # print("Espresso orders:", espresso.orders())
    print("Espresso num_orders:", espresso.num_orders())
    print("Espresso average_price:", espresso.average_price())
    # print("Espresso customers:", espresso.customers())
    # print("brian coffees:", brian.coffees())
    print("Most aficionado of Espresso:", Customer.most_aficionado(espresso).name)

if __name__ == "__main__":
    demo()

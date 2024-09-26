class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def get_total_price(self):
        return self.price*self.quantity
obj1 = Product("Starteri",60,2)
obj2 = Product("Sūkni",70,3)
print("Cena par starteriem: ",obj1.get_total_price())
print("Cena par sūkņiem: ",obj2.get_total_price())

class ShoppingCart():
    def add_product_to_cart(self, product):
        print(product.name, "ielikts grozā!")
    def remove_product_from_cart(self, product):
        print(product.name, "izņemts no groza!")
    def get_total_price(self, product):
        print("Kopējā summa par",product.name, "ir ", product.get_total_price(),"€")

IepirkumuGrozs = ShoppingCart()
IepirkumuGrozs.add_product_to_cart(obj1)
IepirkumuGrozs.get_total_price(obj1)
IepirkumuGrozs.remove_product_from_cart(obj1)
IepirkumuGrozs.add_product_to_cart(obj2)
IepirkumuGrozs.get_total_price(obj2)


class SystemUser():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    def set_user_info(self, newuser, newpass, newemail):
        self.username = newuser
        self.password = newpass
        self.email = newemail
        print("Informācija ir nomainīta!")
    def get_user_info(self):
        print("Informācija par lietotāju")
        print("Lietotājvārds:",self.username)
        print("Parole:",self.password)
        print("E-pasts:",self.email)

Janka = SystemUser("jankucis", "janka123", "janka@gmail.com")
Janka.set_user_info("jankucitis", "janka321", 'jankucis@gmail.com')
Janka.get_user_info()

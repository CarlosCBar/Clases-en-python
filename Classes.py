class Persono:
    nationality = "Esperantujo"
    hobby = "Lerni"


class Floro:
    color = "Rozkolora"
    shape = "floriforme"
    smell = "Bone"

class Birdo:
    flugi = True


class Camara:
    Precio = 53856
    Modelo = "Canon 5D mark"
    Full_frame = True
    Megapixeles = 56.24
    Comprar = ["Canon", "eBay", "Amazon", "Internet"]
    print(Modelo)

class Virtual_pet:
    color = "verda"
    legs = 5
    lives = 30

# Creating instance

fluffy = Virtual_pet()
benny = Virtual_pet()

print(fluffy.legs)
print(f"La koloro estas {benny.color}")

# Classes with methods

class Amiguito:
    color = "miel"
    patitas = 4

    def bark(self):
        print("woof")
    def display_color(self):
        print(self.color)
    def display_patitas(self):
        print(f"Porfirio tine {self.patitas} patas con olor a rancheritos")

Porfirio = Amiguito()
Porfirio.bark()
Porfirio.display_color()
Porfirio.display_patitas()

# Constructor method

class Nubo:
    def __init__(self,color,tamaño):
        self.color = color
        self.tamaño = tamaño
    def display_koloro(self):
        print(self.color)
    def display_tamaño(self):
        print(self.tamaño)

cumulus_nimbo = Nubo("Blanka","Mediana")
sxtormo = Nubo("Nigra","Gigante")

print(cumulus_nimbo.color)
print(cumulus_nimbo.tamaño)
print(sxtormo.color)
print(sxtormo.tamaño)

class Pokemon:
    def __init__(self,color,name,tipo):
        self.color=color
        self.name=name
        self.tipo=tipo

gastly = Pokemon("Purple","Gastly","Fantasma")
print("\n") #Salto de linea
print(gastly.color)
print(gastly.name)
print(gastly.tipo)



class Pie:
    def __init__(self, flavor, ingredientes):
        self.flavor = flavor
        self.ingredientes = ingredientes

    def print_ingredientes(self):
        for i in self.ingredientes:
            print(i)

applePie = Pie("Apple", ["flour","eggs","apples","butter"])
print("\n")
applePie.print_ingredientes()




class Saga_books:
    def __init__(self,nombre,books):
        self.nombre=nombre
        self.books=books
        self.num_books = len(books)

    def print_nombre(self):
        print(self.nombre)

    def print_books(self):
        print(self.books)
    

Asimov = Saga_books("La Fundación",["Fundación","Fundación e imperio", "Segunda fundación", "Los limites de la fundación"])

Asimov.print_books()
print(Asimov.num_books)

























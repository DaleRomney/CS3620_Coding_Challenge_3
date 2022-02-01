# Part 1

def student_discount(x):
    y = x
    x = x * .1
    x = y - x
    return x


def regular_discount(x):
    y = x
    x = x * .05
    x = y - x
    return x


print(regular_discount(student_discount(2.99)))

# Part 2

print((lambda x: x * (x + 5) ** 2)(5))


# Part 3

def store_discount(x):
    y = x
    x = x * .1
    x = y - x
    return x


storePrices = [5.99, 3.49, 10.50, 6.99, 21.32]

result = list(map(store_discount, storePrices))
print(result)

# Part 4

class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def get_specs(self):
        self.cpu = input("Input CPU type: ")
        self.ram = input("Input amount of ram in Gigs: ")

    def display_specs(self):
        print("CPU: " + self.cpu + " Ram: " + self.ram)


class Desktop(Computer):
    def __init__(self, gpu):
        self.gpu = gpu

    def get_desk_spec(self):
        self.gpu = input("Input GPU type: ")

    def display_desk_spec(self):
        print("GPU: " + self.gpu)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def get_laptop_spec(self):
        self.weight = input("Input weight: ")

    def display_laptop_spec(self):
        print("Weight :" + self.weight)


dell = Laptop("")
alien = Desktop("")

dell.get_specs()
dell.get_laptop_spec()
dell.display_specs()
dell.display_laptop_spec()

alien.get_specs()
alien.get_desk_spec()
alien.display_specs()
alien.display_desk_spec()

# Part 5

class Multi:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return Multi(x)

    def __str__(self):
        return "({0})".format(self.x)


multi1 = Multi(3)
multi2 = Multi(4)
print(multi1 * multi2)
class Phone:
    cat ="Electronics"


apple=Phone() # Create an object of the class Phone and assign it to the variable apple
print(type(apple))
print(apple.cat)# Access the class attribute cat using the object apple and print its value
print('\n')

samsung=Phone()
print(samsung.cat)

redmi=Phone()
redmi.cat=("Super Electronics")# Change the value of the class attribute cat for the object redmi to "Super Electronics"
print(redmi.cat)
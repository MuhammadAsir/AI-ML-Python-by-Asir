#Dictionary Comprehension is a concise way to create dictionaries.
#It consists of an expression pair (key: value) 
#followed by a for statement inside curly braces {}.

print(list(range(10)),'\n')#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

square={x: x**2 for x in range(10)}
print(square,'\n')
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

square={x: x**2 for x in range(1,11) if x%2==0}
print(square,'\n')

co_or=[(0,0),(0,1),(1,0),(1,1)]
location=["chattogram","dhaka","khulna","sylhet"]
exact={lo : cor for lo,cor in zip(location,co_or)}
#this is a dictionary comprehension with zip function to create a dictionary from two lists
print(exact,'\n')
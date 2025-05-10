def callList(listitems, itemsCategory):
    print(f"Listing {itemsCategory} using function")
    print("_____________________________")
 

    i = 0
    while i < len(listitems):
        print(f"{itemsCategory} {i+1} : {listitems[i]}")
        i += 1 #Equal to i = i + 1    
    

movies = ["Tholiprema","Jhonny","Kushi","Gabbar Singh","Badri"]
fruites = ["Banana", "Grapes", "Apple", "cherry", "Orange"]

print("First movie: ", movies[0])
print("Last movie: ", movies[len(movies)-1])

movies.append("Thammudu")

for movie in movies:
    print(movie)

i = 0
while i < len(movies):
    print(f"Movie {i+1} : {movies[i]}")
    i += 1 #Equal to i = i + 1 

callList(movies, "Movies")

callList(fruites, "Fruites")


"""
Nested list
"""
def callNestedListReturn(nestedListItems):
    itemvalues = []  # Initialize an empty list to store values
    for sublist in nestedListItems:
        for i in sublist:
            itemvalues.append(i)  # Append each item to the list
            # print(i, end="")  # If you want to print each value
    print(" ".join(map(str, itemvalues)))  # Join the list into a single string for display
    return itemvalues  # Return the list of values

def callNestedList(nestedListItems):
    
    for sublist in nestedListItems:
        for i in sublist:
            print(i, end="")
    print("\n")



nested_list = [[1,2,3],[4,5,6],[7,8,9]]


print(nested_list[1][1]) #Here value will be index base starting from 0

print("Nested list before modification: ")
callNestedList(nested_list) #Nested list before modification
print("Nested list before modification: ", callNestedListReturn(nested_list)) 

nested_list[2][2]=10
print("Nested list after modification: ")
callNestedList(nested_list) #Nested list after modification
print("Nested list after modification: ", callNestedListReturn(nested_list))

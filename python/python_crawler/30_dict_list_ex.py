# pet List 강아지, 고양이, 도마뱀
pets = [{"nane":"nabi","age":4,"kind":"cat"},
        {"name":"mary","age":5,"kind":"dog"}
        ]
pet3 = {"name":"dragon","age":1,"kind":"lizard"}
pets.append(pet3)
print(pets)
print(len(pets))
print(pet3['kind'])
pet1 = pets[0]
pet2 = pets[1]
print("pet1:",pet1)
print(pet1['kind'])
print(pet2['kind'])
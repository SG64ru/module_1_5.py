mobil = [56,55,57] # Вариант 1
immutable_var = (1 , 2 , 3 , "storm" , mobil , True)
print(immutable_var)

immutable_var = (1 , 2 , 3 , "storm" , [56,55,57] , True) #Вариант 2
print(immutable_var)

#immutable_var.append ("food")
#print(immutable_var.append ("food"))
#print(immutable_var.extend ("food"))
#print(immutable_var.remove ("food"))
#print(immutable_var [1]=2)
# Кортеж относится к неизменяемым типам данных, но может содержать изменяемые типы данных.

mutabl_list = [1, 2, True, "bor"]
print(mutabl_list)
mutabl_list [1] = 22
print(mutabl_list)
mutabl_list [3] = "tor"
print(mutabl_list)


def field():
       field = []       
       for i in range(3):
              field.append([])
              for j in range(3):
                     field[i].append("-")

       return field

def look_field(a):
       print(" ","1","2","3")
       for i in range(3):
              print(str(i+1),*a[i],end = " ")
              print()

def who_win(f, user):
       def check_line(a1,a2,a3,user):
              if a1==user and a2==user and a3==user:
                     return True
       for n in range(3):
              if check_line(f[n][0],f[n][1],f[n][2],user) or \
                 check_line(f[0][n],f[1][n],f[2][n],user) or \
                 check_line(f[0][0],f[1][1],f[2][2],user) or \
                 check_line(f[2][0],f[1][1],f[2][0],user):
                     return True



def change_x_and_o(a):

       while True:
              #print("ЗАШЛИ В ПЕРВЫЙ ЦИКЛ")
              while True:

                     try:
                            print("Ход Крестика")
                            X = int(input("Координаты оси X "))
                            Y = int(input("Коориданты оси Y "))
                            
                            if a[X-1][Y-1] != "-":
                                   print("Ячейка занята! ")
       
                            else:       
                                   a[X-1][Y-1] = "X"
                                   look_field(a)
                                   break
                     except ValueError:
                            print("Вы указали не верный формат координат!\n"
                                  "Вводите только цифры!")
                     except IndexError:
                            print("Вы вышли за максимальный диапозон координат!\n"
                                  "Максимальный диапозон координат 3")
                     
              
              if who_win(a,"X") == True:
                     print("Выйграл игрок X")
                     look_field(a)
                     break
              
                     
              #print("ЗАШЛИ ВО ВТОРОЙ ЦИКЛ")              
              while True:

                     try:
                            print("Ход Нолика")
                            X = int(input("Координаты оси X "))
                            Y = int(input("Коориданты оси Y "))
              
                            if a[X-1][Y-1] != "-":
                                   print("Ячейка занята! ")
                                   
                            else:
                                   a[X-1][Y-1] = "O"
                                   look_field(a)
                                   break

                     except ValueError:
                            print("Вы указали не верный формат координат!\n"
                                  "Вводите только цифры!")
                     except IndexError:
                            print("Вы вышли за максимальный диапозон координат!\n"
                                  "Максимальный диапозон координат 3")
                           

              if who_win(a,"O") == True:
                     print("Выйграл игрок O")
                     look_field(a)
                     break
              
a = field()
look_field(a)
change_x_and_o(a)

#change_x_or_o(a,look)





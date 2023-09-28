import math
a = int

while a != 11:
    print('Введите операцию')
    print('1.Сложить 2 числа')
    print('2.Вычесть  2 числа')
    print('3. Перемнодить 2 числа')
    print ('4.Делить 2 числа')
    print ('5.Возвести 1-ое число в степень 2-го числа')
    print ('6.Извлечь корень из числа')
    print ('7.Факториал числа ')
    print('8.Косинус числа')
    print('9.Синус числа ')
    print ('10.Тангенс числа')
    print('11.Завершить программу')
    a = int (input())
    match a:     
     case 1 :
        while True:
         try:
           b = int(input("Ведите число: "))
           break
         except ValueError:
          print("Это не число")
        while True:
          try:
            c = int(input("Ведите число: "))
            break
          except ValueError:
               print("Это не число")
        f = int  
        f  = b + c
        print (f)
     case 2:
        while True:
         try:
           b = int(input("Ведите число: "))
           break
         except ValueError:
          print("Это не число")
        while True:
          try:
            c = int(input("Ведите число: "))
            break
          except ValueError:
               print("Это не число")
        f = int  
        f  = b - c
        print (f)
     case 3:
        while True:
         try:
           b = int(input("Ведите число: "))
           break
         except ValueError:
          print("Это не число")
        while True:
          try:
            c = int(input("Ведите число: "))
            break
          except ValueError:
               print("Это не число")
        f = int  
        f  = b * c
        print (f)
     case 4:
        while True:
         try:
           b = float(input("Ведите число: "))
           break
         except ValueError:
          print("Это не число")
        while True:
          try:
            c = float(input("Ведите число: "))
            if c == 0:
             print("на ноль делить нельзя")
             continue
            break
          except ValueError:
               print("Это не число")
        f = int  
        f  = b / c
        print (f)
     case 5:
        while True:
         try:
           b = int(input("Ведите число: "))
           break
         except ValueError:
          print("Это не число")
        while True:
          try:
            c = int(input("Ведите число: "))
            break
          except ValueError:
               print("Это не число")
        f = int  
        f  = b ** c
        print (f)
     case 6:
        while True:
         try:
          b = int(input("Ведите число: "))
          if b < 0:
              print('Из отрицательного числа нельзя извлечь корень')
              continue
          break
         except ValueError:
          print("Это не число")
        from math import sqrt 
        f = sqrt(b)
        print(f)
     case 7:
      while True:
         try:
           num = int(input("Ведите число: "))
           break
         except ValueError:
          print("Это не число")

      factorial = 1
 

      if(num%1==0 and num>=0):
    
       for i in range(1, num+1):
        factorial = i*factorial
    
       print(factorial)

      else:
       print('Невозможно вычислить факториал нецелого и/или отрицательного числа')
     case 8:      
        while True:
         try:
           b = int(input("Ведите число: "))
           break
         except ValueError:
          print("Это не число")
        math.cos(b)
        print(math.cos(b))
     case 9:
        while True:
         try:
           b = int(input("Ведите число: "))
           break
         except ValueError:
          print("Это не число")
        math.sin(b)
        print(math.cos(b))
     case 10:
      while True:
         try:
           b = int(input("Ведите число: "))
           break
         except ValueError:
          print("Это не число")
      math.tan(b)
      print(math.tan(b))
    if a > 11:
     print('Вы не выбрали операцию') 
   
      
          
         
      
             
             
    
    
    
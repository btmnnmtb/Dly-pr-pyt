import math
a = int

while a !=1 11:
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
        print('Введите первое число')
        b =  int (input())
        print('Введите второе число')
        c = int (input())
        f = int  
        f = b + c

        print (f)
     case 2:
        print('Введите первое число')
        b = int (input())
        print('Введите второе число')
        c = int (input())
        f = int  
        f = b - c 
        print(f)
     case 3:
        print('Введите первое число')
        b = int (input())
        print('Введите второе число')
        c = int (input())
        f = int
        f = b * c
        print (f) 
     case 4:
        print('Введите первое число')
        b = float (input())
        print('Введите второе число')
        c = float (input())
        if c == 0:
         print ('На ноль делить нельзя')
         break
        f = b / c
        print(f)
     case 5:
        print('Введите первое число')
        b = int (input())
        print('Введите второе число')
        c = int (input()) 
        f = b ** c
        print(f)
     case 6:
        print('Введите первое число')
        b = int (input())
        if b < 0:
         print('Из нуля нельзя извлечь корень')
         continue
        from math import sqrt 
        f = sqrt(b)
        print(f)
     case 7:
      print('Введите число')
      num= int (input())

      factorial = 1
 

      if(num%1==0 and num>=0):
    
       for i in range(1, num+1):
        factorial = i*factorial
    
       print(factorial)

      else:
       print('Невозможно вычислить факториал нецелого и/или отрицательного числа!')
     case 8:      
        print('Введите число')
        b = int (input())
        math.cos(b)
        print(math.cos(b))
     case 9:
        print('Введите число')
        b = int (input())
        math.sin(b)
        print(math.cos(b))
     case 10:
      print('Введите число')
      b = int (input())
      math.tan(b)
      print(math.tan(b))
    if a > 11:
     print('Вы не выбрали операцию') 
   
      
          
         
      
             
             
    
    
    
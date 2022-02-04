# Урок работы с переменные, классами, типами (python_lesson_2)
Варианты создания классов и объектов

Простой класс можно создавать конструкцией:
```python
class Myclass_2:
    x: int
    def __init__(self):
        pass
```
В этом случае если создать объект класса `MyObject_2 = Myclass_2()`, то при попытке вызова свойства возникнет ошибка:
> **AttributeError: 'Myclass_2' object has no attribute 'x'**
Требуется выполняться последовательность: инициализация объекта, указание свойства, вызов свойства:
```python
MyObject_2 = Myclass_2()
MyObject_2.x = 10.5
print (MyObject_2.x)
```
или создавать класс со значением поля по умолчанию:
```python
class Myclass_2:
    x: int = 0 # Атрибут объекта класса
    def __init__(self):
        pass
```

Также можно использовать конструктор с инициализатором:
```python
class Myclass_1:
    #x: int
    def __init__(self,x=0):
        self.x = x # Атрибут экземпляра класса
```

### Пимер отличия **Атрибут объекта класса** от **Атрибут экземпляра класса**:
> Создаём класс:
```python
class MyClass:
    x = 10 # Атрибут объекта класса
    def __init__(self):
        self.y = 20 # Атрибут экземпляра класса
```
> Создаём экземпляры класса, посмотрим содержимое:
```python
c1 = MyClass()
c2 = MyClass()
print(c1.x, c2.x) # 10 10
```
> Изменяем атрибут объекта класса, посмотрим результат
*ожидатся изменение во всех объектах*
```python
MyClass.x = 88
print(c1.x, c2.x) # 88 88
```
> Изменяем атрибут экземпляра класса
*ожидается изменение только в отдельном объекте*
```python
c1.y = 88
print(c1.y, c2.y) # 88 20
```

### Пример работы с классами с неопределённым количеством аргументов
Класс может сожержать определённое и неопределённое заранее количество аргументов

> В даннном прмиере показана ситуация, когда при объявлении класса может быть получено неограниченное количество аргументов. При этом, в зависимости от количетсва и типа аргументов применяются различные операции. Если один целочисленный аргумент - вычисляется квадрат числа, если один строковый аргумент - то выводится строка с его участием, если аргментов больше одного, то они ссумируются. 
```python
# ВАРИАНТ 1: объявления класса с неизвестным количеством аргументов
class example:

    # constructor overloading
    # based on args
    def __init__(self, *args):

        # if args are more than 1
        # sum of args
        if len(args) > 1:
            self.answer = 0
            for i in args:
                self.answer += i

        # if arg is an integer
        # square the arg
        elif isinstance(args[0], int):
            self.answer = args[0] * args[0]

        # if arg is string
        # Print with hello
        elif isinstance(args[0], str):
            self.answer = "Hello! " + args[0] + "."
```

> В даннном прмиере показано применение различных методов класса к аргументам в зависимости от их количества.  Резльтат зависит от числа аргументов.
```puthon
# ВАРИАНТ 2: вызов различных инициализаторов в зависимости от числа аргументов
'''
При инициализации объекта определяется количество аргументов
и в зависимости от количества производится вызов метода
'''
class equations_1:

    # single constructor to call other methods
    def __init__(self, *abc):

        # when 2 arguments are passed
        if len(abc) == 2:
            self.ans = self.eq1(abc)

            # when 3 arguments are passed
        elif len(abc) == 3:
            self.ans = self.eq2(abc)

            # when more than 3 arguments are passed
        else:
            self.ans = self.eq3(abc)

    def eq1(self, args):
        x = (args[0] * args[0]) + (args[1] * args[1])
        return x

    def eq2(self, args):
        y = args[0] + args[1] - args[2]
        return y

    def eq3(self, args):
        temp = 0
        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / 5.0
        z = temp
        return z
```

> В даннном прмиере класс реализует несколько методов, и на этапе объявления инстанса класса в зависимости от числа аргментов вызывается мтод дляинстанса.

```python
# ВАРИАНТ 3: Класс с вызовом меодов по обстоятельствам
'''
В данном  прмиере создаётся класс с множеством методов и
вызов методов определяется в зависимости от решения разраба
на этапе вызова метода для интсанса класса
'''
class equations_2:

    # basic constructor
    def __init__(self, x):
        self.ans = x

    @classmethod
    def eq1(obj, args):
        # create an object for the class to return
        a = obj((args[0] * args[0]) + (args[1] * args[1]))
        return a

    @classmethod
    def eq2(obj, args):
        b = obj(args[0] + args[1] - args[2])
        return b

    @classmethod
    def eq3(obj, args):
        temp = 0

        # square of each element
        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / 5.0
        z = obj(temp)
        return z

class Myclass_1:
    #x: int
    def __init__(self,x=0):
        self.x = x

class Myclass_2:
    x: int = 0
    def __init__(self):
        pass
```
Вызовы для классов с несколькими аргументами
```python
# Вызов для варианта класса с несколькими конструкторами 1
    e1 = example(1, 2, 3, 6, 8)
    print("Sum of list :", e1.answer)
    e2 = example(6)
    print("Square of integer :", e2.answer)
    e3 = example("Programmers")
    print("String :", e3.answer)

    # Вызов для варианта класса с несколькими конструкторами 2
    abc1 = equations_1(4, 2)
    abc2 = equations_1(4, 2, 3)
    abc3 = equations_1(1, 2, 3, 4, 5)

    print("equation 1 :", abc1.ans)
    print("equation 2 :", abc2.ans)
    print("equation 3 :", abc3.ans)

    # Вызов для варианта класса с несколькими конструкторами 3
    li = [[4, 2], [4, 2, 3], [1, 2, 3, 4, 5]]
    i = 0

    # loop to get input three times
    while i < 3:

        input = li[i]

        # no.of.arguments = 2
        if len(input) == 2:
            p = equations_2.eq1(input)
            print("equation 1 :", p.ans)

            # no.of.arguments = 3
        elif len(input) == 3:
            p = equations_2.eq1(input)
            print("equation 2 :", p.ans)

            # More than three arguments
        else:
            p = equations_2.eq3(input)
            print("equation 3 :", p.ans)

            # increment loop
        i += 1
```

### Работа с классами (перезагрузка методов и операторов)

> Данный класс отражает реализацию собственного метода **print_x**, перезагрузку метода **__getattr__** и метода len
```python
class MyClass:
    x: int
    def __init__(self,x: int = 0):  # Конструктор
        self.x: int  = x  # Атрибут экземпляра класса
    def print_x(self):  # self — это ссылка на экземпляр класса
        print(self.x)  # Выводим значение атрибута
    def __getattr__(self, item):
        print("Не получаетс")
        return 0
    def __len__(self):
        i = 0
        n=self.x
        while n > 0:
            n = n // 10
            i += 1
        return  i
```
Вызовы для класса
```python
c = MyClass(13)  # Создание экземпляра класса
    # Вызываем метод print_x()

    c.print_x()  # self не указывается при вызове метода
    print(c.x)  # К атрибуту можно обратиться непосредственно

    res_1 = c.__getattribute__("x")
    res_1 = getattr(c, "x")
    print("Получено знанчение с прмиенением getattr", res_1)
    try:
        setattr(c,"x",2548)
    except:
        res_1 = False
    else:
        res_1= True
    print(res_1)

    # пример попытки вызова несуществующих аргументов
    # с возвратом 0 и выводдом текста "не получается".
    a=c.z

    print("Вывожу a:", a)
    a= len(c)
    print("Вывожу len(c):", a)
```
> В данном примере представлен собственный тип числа с операциями над ним
```python
class MyNumber:
    def __init__(self, number):  # Конструктор
        self.x = number
    def __add__(self, other):
        if isinstance(other, MyNumber):
            return self.x + other.x
        else:
            return self.x + other
    def __len__(self):
        i = 0
        n=self.x
        while n > 0:
            n = n // 10
            i += 1
        return  i
    def __str__(self):
        return (str(self.x*100))
```
Вызовы для класса
```python 
number_1 = MyNumber(14876)
number_2 = MyNumber(1)
x = number_1+30
x = number_1 + number_2

print(x)
```
> Пример создания собственного класса процентов
```python
class MyPercentClass:
    def __init__(self, number=0):  # Конструктор
        self.x = number/100

    def get_value(self, number):
        self.x = number/100
        return self.x

    def __add__(self, other):
        if isinstance(other, MyPercentClass):
            return self.x + other.x
        else:
            return self.x*other + other

    def __radd__(self, other):
        if isinstance(other, MyPercentClass):
            return self.x + other.x
        else:
            return self.x  * other + other

    def __mul__(self, other):
        if isinstance(other, MyPercentClass):
            return self.x + other.x
        else:
            return self.x  * other

    def __rmul__(self, other):
        if isinstance(other, MyPercentClass):
            return self.x+ other.x
        else:
            return self.x * other


    def __str__(self):
        return (str(self.x*100)+"%")
```
вызовы для MyPercentClass
```python
perc=MyPercentClass()
print(type(perc))
perc.get_value(10)
print(type(perc))
print(perc)
res =  200 + perc
print(res)
perc.get_value(20)
res = 300 * perc.get_value(20)
print(res)

c= MyClass("a")
print(type(c.x))
```


## TODO
- [x] НАПИСАТЬ СОБСТВЕННЫЙ КЛАСС ДЛЯ ПРОУЕНТОВ!
- [ ] Чётко выделить разницу поле / свойство
- [ ] Привести пример работы с множеством аргументов с применением kwargs
- [ ] Привести примеры наследования
- [ ] Продолжить работу с примером

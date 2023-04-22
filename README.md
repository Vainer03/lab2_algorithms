# Лабораторная работа по алгоритмам №2
## Точка среди прямоугольников

## ТЗ:
### Задача:
Даны прямоугольники на плоскости с углами в целочисленных координатах ([1..10^9],[1..10^9]).
Требуется как можно быстрее выдавать ответ на вопрос «Скольким прямоугольникам принадлежит точка (x,y)?» 
И подготовка данных должна занимать мало времени.

### Формат ввода:
Первая строка входных данных содержит одно целое число n - количество прямоугольников на плоскости.
Далее следуют n строк с координатами прямоугольников в формате x1 y1 x2 y2
Затем строка с одним целым числом m, обозначающим количество точек, принадлежность которых необходимо проверить.
И в конце m строк с координатами точек в формате x y

### Формат вывода:
Выведите одну строку содержащую количества прямоугольников, которым принадлежит каждая из m точек через пробел

### Пример
#### Ввод
4

2 2 6 8

5 4 9 10

4 0 11 6

8 2 12 12

5

2 2

12 12

10 4

5 5

2 10

#### Вывод
1 1 2 3 0

### Пример задачи:
Прямоугольники: {(2,2),(6,8)}, {(5,4),(9,10)}, {(4,0),(11,6)}, {(8,2),(12,12)}

Точка-ответ: 

(2,2)     -> 1

(12,12)   -> 1

(10,4)    -> 2

(5,5)     -> 3

(2,10)    -> 0

![2023-04-22_12-47-56](https://user-images.githubusercontent.com/106194054/233776695-d840995e-dc17-472e-b3f4-e7ddfa6218cd.png)

### Цели лабораторной работы
Реализовать три разных решения задачи
Выяснить при каком объеме начальных данных и точек какой алгоритм эффективнее.
#### Алгоритм перебора
Без подготовки. При поиске – просто перебор всех прямоугольников
Подготовка O(1), поиск O(N)
#### Алгоритм на карте
Сжатие координат и построение карты.
Подготовка O(N3), поиск O(logN)
#### Алгоритм на дереве
Сжатие координат и построение персистентного дерева отрезков 
Подготовка O(NlogN), поиск O(logN)

### Сдача лабораторной
#### Контест
Необходимо пройти контест с алгоритмом на дереве https://contest.yandex.ru/contest/47517 
Это является обязательным условием для сдачи. Для проведения тестирования в качестве третьего алгоритма необходимо использовать именно код, прошедший контест.
#### Артефакты
Необходимо прислать алгоритмы, использованные в исследовании, код запуска тестов, сырые данные, графики, выводы, логин использованный в контестах. Можно ссылкой на git, но необходимо приложить архив.
Присылать на почты hsepi01@mail.ru, hsepi02@mail.ru, hsepi03@mail.ru, в соответствии с номером вашей группы.
#### Время
Контест будет открыт до конца апреля. Прием лабораторных тоже завершается 31 апреля. 
Позднее можно сдать только на экзаменах/пересдачах, на время которых будет открыт контест.
Лабораторная блокирующая.
#### Рекомендации
Для тестового набора прямоугольников, рекомендуется использовать набор вложенных друг-в-друга с координатами с шагом больше 1, например {(10*i, 10*i), (10*(2N-i), 10*(2N-i))}.
Для тестового набора точек, рекомендуется использовать неслучайный набор распределенных более-менее равномерно по ненулевому пересечению прямоугольников, например хэш функции от i с разным базисом для x и y.   (p*i)^31%(20*N), p-большое простое, разное для x и y

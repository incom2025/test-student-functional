# Лабораторна робота №4

## Тема
Рекурсія, мемоізація та оптимізація функціональних обчислень.

## Мета роботи
Дослідити рекурсивні обчислення, мемоізацію та ітеративний підхід.
Порівняти різні способи обчислення послідовності Трибоначчі та їх продуктивність.

## Реалізація

У лабораторній роботі реалізовано три способи обчислення чисел Трибоначчі:

1. Рекурсивний алгоритм.
2. Рекурсивний алгоритм з кешуванням (memoization).
3. Ітеративний алгоритм.

Основна логіка програми знаходиться у файлі `core.py`.

Файл `main.py` виконує запуск програми та порівняння часу виконання алгоритмів.

Автоматизовані тести знаходяться у:

`tests/test_tribonacci.py`

## Структура проєкту

Lab_04/
- core.py
- main.py
- tests/
  - test_tribonacci.py
- README.md

## Порівняння продуктивності

Звичайна рекурсивна реалізація виконує багато повторних обчислень.

Мемоізація зберігає вже обчислені значення та дозволяє уникнути повторних обчислень.

Ітеративна реалізація не використовує глибоку рекурсію та має низькі накладні витрати.

## Запуск

```bash
python main.py
## Recursion limit and TCO

Python has a recursion limit that restricts the maximum recursion depth.
The current recursion limit can be checked with `sys.getrecursionlimit()`.

If the recursion depth becomes too large, Python can raise
`RecursionError`.

Python does not support Tail Call Optimization (TCO).

Therefore, tail recursion is not optimized into iteration in Python.
Every recursive call still creates a new stack frame.

For large input values, an iterative solution can therefore be safer
than deep recursion.

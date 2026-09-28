# Лабораторна робота №2 — варіант 1

Тема: функції вищого порядку, lambda, композиція.

Варіант 1: клієнти інтернет-магазину.

## Запуск

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
pytest -q
python main.py --data sample_data.json --top 3 --boost-city Delhi --factor 1.1
```

`core.py` містить чисті функції та конвеєр, `main.py` — введення/виведення,
`tests/test_core.py` — автоматичні тести.

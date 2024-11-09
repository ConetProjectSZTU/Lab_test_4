import json

def task() -> float:
    """
    Функция вычисляет сумму произведений значений "score" и "weight"
    в каждом словаре JSON файла.

    Returns:
        float: Сумма произведений, округлённая до 3 знаков после запятой.
    """

    with open('task.json', 'r') as f:
        data = json.load(f)

    total_sum = 0
    for item in data:
        total_sum += item['score'] * item['weight']

    return round(total_sum, 3)

print(task())
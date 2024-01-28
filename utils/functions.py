import json
from datetime import datetime


def open_json(operation) -> list:
    """Читает файл json
    :return: список из json(a)
    """
    with open(operation, encoding='utf-8') as f:
        filename = json.load(f)
        return filename


def sorting_by_executed(operation) -> list:
    """Перебирает список из json(а), и если значение ключа
    "состояние" равняется "выполненному", то в пустой список
    добавляется словарь с этим самым "выполненным" значением
    :param operation: список из json(a)
    :return: список со словарями
    """
    exe = []
    for item in operation:
        if item.get("state") == "EXECUTED":
            exe.append(item)
    return exe


def sorting_by_string(last_string) -> list:
    """Сортирует список по пяти последним операциям по дате
    :param last_string: отсортированный список по значениям
    :return: отсортированный список
    """
    sort = sorted(last_string, key=lambda x: x["date"], reverse=True)  # "%Y-%m-%dT%H:%M:%S.%f"
    last = sort[:5]
    return last

def output_trans(date_from) -> list:
    """Запускает цикл по списку из пяти последних операций, в каждом переформатирует дату, и если
    в списке есть ключ "from", то в новый список добавляется строки в формате:
    # 14.10.2018(date) Перевод организации(description)
    # Visa Platinum 7000 79** **** 6361(to_sander) -> Счет **9638(to_info)
    # 82771.72 руб.(amount_currency)
    в ином случае в список добавляется строки в формате:
    # 05.11.2019(date) Открытие вклада(description)
    # Счет **8381(to_info)
    # 21344.35 руб.(amount_currency)
    :param date_from: список из пяти словарей
    :return: переформатированный список
    """
    data_list = []
    for i in date_from:
        date = datetime.fromisoformat(i["date"]).strftime("%d.%m.%Y")
        description = i["description"]
        amount_currency = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
        if "from" in i:
            sander = i["from"].split()
            recipient = i["to"].split()
            sander_num = sander.pop()
            recipient_num = recipient.pop()
            if len(sander_num) == 16:
                hide_sander_num = f'{sander_num[:4]} {sander_num[4:6]}** **** {sander_num[-4:]}'
            elif len(sander_num) == 20:
                hide_sander_num = f'** {sander_num[-4:]}'
            if len(recipient_num) == 16:
                hide_recipient_num = f'{recipient_num[:4]} {recipient_num[4:6]}** **** {recipient_num[-4:]}'
            elif len(recipient_num) == 20:
                hide_recipient_num = f'**{recipient_num[-4:]}'
            to_info = f'{" ".join(recipient)} {hide_recipient_num}'
            to_sander = f'{" ".join(sander)} {hide_sander_num}'
            data_list.append(f'{date} {description}\n{to_sander} -> {to_info}\n{amount_currency}\n')
        else:
            to_info = f'**{i["to"][-4:]}'
            data_list.append(f'{date} {description}\nСчет {to_info}\n{amount_currency}\n')
    return data_list


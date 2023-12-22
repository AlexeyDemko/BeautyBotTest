TEST_TEXT_1 = '''{name}, ваша запись изменена:
⌚️ {day_month} в {start_time} - {day_of_week} - {end_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}'''

TEST_TEXT_2 = '''{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}'''


def verify_text(test_text, list_keys):
    for key in list_keys:
        placeholder = key
        if placeholder not in test_text:
            return f"Ошибка: Ключ '{key}' отсутствует в тексте."

    open_brackets = test_text.count('{')
    close_brackets = test_text.count('}')

    if open_brackets != close_brackets:
        return "Ошибка: Несоответствие открывающих и закрывающих скобок."

    return f"Текст корректен:\n{test_text}"


list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']

res_1 = verify_text(TEST_TEXT_1, list_keys)
res_2 = verify_text(TEST_TEXT_2, list_keys)
print(res_1)
print(res_2)

# def test_input_phrase_length():
#     phrase = input("Введите фразу: ")
#     assert len(phrase) < 15, "Фраза должна быть короче 15 символов"

## ----------------------------------------
# import requests

# def test_homework_cookie():
#     response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    
#     cookies_dict = response.cookies.get_dict()
#     print(cookies_dict)

#     cookie_name = list(cookies_dict.keys())[0]
#     cookie_value = cookies_dict[cookie_name]

#     print(f"Cookie name: {cookie_name}")
#     print(f"Cookie value: {cookie_value}")

#     assert cookie_name == "HomeWork", "Некорректное имя куки"
#     assert cookie_value == "hw_value", "Некорректное значение куки"
## ------------------

# import requests 

# def test_HW_header():
#     response = requests.get("https://playground.learnqa.ru/api/homework_header")
#     headers = response.headers

#     for header_name, header_value in headers.items():
#         print(f"Header: {header_name}, Value: {header_value}")

#     assert "Content-Type" in headers, "No such header in this response's headers" 
#     assert headers["Content-Type"] == "application/json", "Wrong header value"

# # ----------------------------

import requests
import pytest

@pytest.mark.parametrize('user_agent, expected_values', [
    (
        'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}
    ), 
    (
        'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1', 
        {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}
    ), 
    (
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 
        {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}
    ), 
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0', 
        {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}
    ), 
    (
        'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', 
        {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
    )
])
def test_user_agent_check(user_agent, expected_values):
    url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    data = response.json()

    for key, expected_value in expected_values.items():
        assert data[key] == expected_value, f"Некорректное значение {key}. Ожидаемое: {expected_value}, Фактическое: {data[key]}"


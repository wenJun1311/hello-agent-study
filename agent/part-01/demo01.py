import requests


def get_weather(city: str) -> str:
    # API端点，我们请求JSON格式的数据
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        # 检查响应状态码是否为200 (成功)
        response.raise_for_status()
        # 解析返回的JSON数据
        data = response.json()
        print("this is weahter data", data)

    except Exception as e:
        print(f"Error fetching weather for {city}: {e}")
        return "Unknown"


if __name__ == "__main__":
    city = "Beijing"
    weather = get_weather(city)
    print(f"The weather in {city} is: {weather}")

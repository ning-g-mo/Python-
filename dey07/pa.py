import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

def fetch_website_content(url):
    try:
        # 发送 HTTP GET 请求
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功

        # 使用 BeautifulSoup 解析 HTML 内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取所有文本内容
        text_content = soup.get_text(separator='\n', strip=True)

        return text_content
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None

# 网站 URL
url = "https://fcl.ningmo.fun"

# 获取并打印网站内容
content = fetch_website_content(url)
if content:
    print(content)
import base64

f = open('ssr.txt')
data = f.read()

def data2urls(data: str) -> list:
    decoded = str(base64.urlsafe_b64decode(data),
                  encoding='utf-8')
    urls = decoded.strip().split('\n')
    return urls

d = data2urls(data)

def url2args(url: str) -> str:
    prefix_len = len('ssr://')
    path = url[prefix_len:]
    b64pad_size = 4 - len(url) % 4
    path_padded = f"{path}{'='*b64pad_size}"
    decoded_path = str(base64.urlsafe_b64decode(path_padded),
                       encoding='utf-8')

    return decoded_path




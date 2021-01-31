# Các thư viện cần thiết
import requests
from bs4 import BeautifulSoup
import re


# Hàm sửa link xuất phát
# Truyền vào link xuất phát
# Trả về link xuất phát chuẩn để gửi lệnh Requests không bị lỗi
def sua_url_goc(link_goc):
    if link_goc[-1] == '/':
        link_goc = link_goc[0: -1]
        return link_goc
    else:
        return link_goc


# Hàm tìm kiếm các link liên quan để tải xuống
# Truyền vào link cần được quét, và link xuất phát
# Kết quả trả về là tập hợp các link tìm được
def tim_link_lien_quan(url, link_goc):
    link_tim_duoc = set()
    link = requests.get(url)
    link_soup = BeautifulSoup(link.text, 'html.parser')
    results = link_soup('a', attrs={'href': True})
    for i in results:
        a = i['href']
        so1 = f'^{link_goc}[^?#]*$'
        so2 = '^/[^?#]*$'
        if re.match(so1, a):
            link_tim_duoc.add(a)
        else:
            if re.match(so2, a):
                link_lien_quan = f'{link_goc}{a}'
                link_tim_duoc.add(link_lien_quan)
    return link_tim_duoc


# Tăng số lượng link trong tập hợp lên
# Cần truyền vào một set gồm các phần tử cần được duyệt, và link xuất phát
# Kết quả trả về tập hợp các link có số phần tử đạt yêu cầu
def them_va_duyet_link(test_link, link_goc):
    history = test_link
    while (len(test_link) > 0) and (len(history) < 5):
        link_tim_duoc = tim_link_lien_quan(test_link.pop(), link_goc)
        test_link = test_link | (link_tim_duoc - history)
        history = history | link_tim_duoc
    return history


def main():
    link_tim_duoc = tim_link_lien_quan('https://vietnamnet.vn', 'https://vietnamnet.vn')
    history = them_va_duyet_link(link_tim_duoc)
    for i in history:
        print(i)


if __name__ == '__main__':
    main()

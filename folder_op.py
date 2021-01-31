# Các thư viện cần thiết
import os
import requests
import codecs


# Hàm Tạo thư mục và chuyển đến thư mục đó
# Cần truyền vào cho hàm Tên thư mục
def tao_thu_muc(name):
    os.mkdir(name)
    os.chdir(name)


# Hàm Lưu file
# Truyền vào link cần lưu và Số thứ tự để đặt tên file cần lưu
def luu_file(url, stt):
    file = codecs.open('file' + str(stt) + '.html', 'w', 'utf8')
    file.write(requests.get(url).text)
    file.close()


# Hàm lưu tất cả các link đã tim được
# Truyền vào một List, set, tuples,... các link hợp lệ
def luu_tat_ca_file(history):
    for (stt, link_con) in enumerate(history):
        luu_file(link_con, stt)
        print(f'{stt} {link_con}')


def main():
    tao_thu_muc('tri_thuc')
    luu_file('https://baomoi.com/', 2)


if __name__ == "__main__":
    main()

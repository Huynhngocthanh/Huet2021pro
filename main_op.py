import web_op
import folder_op

def main():
    url_goc = input('Nhập link khởi đầu: ')
    folder_op.tao_thu_muc(input('Tên thư mục: '))
    url_goc = web_op.sua_url_goc(url_goc)
    url_tim_duoc = web_op.tim_url_lien_quan(url_goc, url_goc)
    waiting_line = url_tim_duoc
    history = web_op.them_va_duyet_hang_cho(waiting_line, url_goc)
    folder_op.luu_tat_ca_file(history)


if __name__ == '__main__':
    main()
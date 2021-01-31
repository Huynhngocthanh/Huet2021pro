import web_op
import folder_op

def main():
    link_goc = input('Nhập link khởi đầu: ')
    folder_op.tao_thu_muc(input('Tên thư mục lưu: '))
    link_goc = web_op.sua_url_goc(link_goc)
    link_tim_duoc = web_op.tim_link_lien_quan(link_goc, link_goc)
    waiting_line = link_tim_duoc
    history = web_op.them_va_duyet_link(waiting_line, link_goc)
    folder_op.luu_tat_ca_file(history)


if __name__ == '__main__':
    main()

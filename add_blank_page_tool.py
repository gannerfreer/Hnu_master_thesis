# 添加空白页的小工具
# 使用前请先安装依赖：`pip install PyPDF2`

import PyPDF2

# 在第xxx页后面添加空白页
page_num_list = [0, 1, 2, 3, 4, 9, 12, 82, 83]
input_file_path = 'Master-thesis.pdf'
output_file_path = 'Master-thesis_print_version.pdf'


def add_blank_pages(input_file_path, output_file_path):
    with open(input_file_path, 'rb') as input_file, open(output_file_path, 'wb') as output_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            writer.add_page(page)
            # 在第xxx页后面添加空白页
            if page_num in page_num_list:
                blank_page = PyPDF2.PageObject.create_blank_page(
                    width=page.mediabox.width, height=page.mediabox.height
                )
                writer.add_page(blank_page)

        writer.write(output_file)


add_blank_pages(input_file_path, output_file_path)

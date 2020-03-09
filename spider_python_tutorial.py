import os
import time

import parsel
import pdfkit
import requests
from bs4 import BeautifulSoup



def get_menu(first_menu_list, num):
    for first_menu in first_menu_list:
        menu_dict['chapter_' + str(num)] = first_menu.a.get_text()
        menu_dict['url_' + str(num)] = pre_url + first_menu.a.get('href')
        if first_menu.ul is not None:
            menu_dict['child_' + str(num)] = {}
            grade_f = 1
            css = 'toctree-l' + str(grade_f + 1)
            second_menu_list = first_menu.ul.find_all('li', class_=css)
            for second_menu in second_menu_list:
                menu_dict['child_' + str(num)]['chapter_' + str(num) + '.' + str(grade_f)] = second_menu.a.get_text()
                menu_dict['child_' + str(num)]['url_' + str(num) + '.' + str(grade_f)] = pre_url + second_menu.a.get('href')
                if second_menu.ul is not None:
                    menu_dict['child_' + str(num)]['child_' + str(num) + '.' + str(grade_f)] = {}
                    grade_s = 1
                    css = 'toctree-l' + str(grade_s + 2)
                    third_menu_list = second_menu.ul.find_all('li', class_=css)
                    for third_menu in third_menu_list:
                        menu_dict['child_' + str(num)]['child_' + str(num) + '.' + str(grade_f)][
                            'chapter_' + str(num) + '.' + str(grade_f) + '.' + str(grade_s)] = third_menu.a.get_text()
                        menu_dict['child_' + str(num)]['child_' + str(num) + '.' + str(grade_f)][
                            'url_' + str(num) + '.' + str(grade_f) + '.' + str(grade_s)] = pre_url + third_menu.a.get('href')
                        if third_menu.ul is not None:
                            menu_dict['child_' + str(num)]['child_' + str(num) + '.' + str(grade_f)][
                                'child_' + str(num) + '.' + str(grade_f) + '.' + str(grade_s)] = {}
                            grade_t = 1
                            css = 'toctree-l' + str(grade_t + 3)
                            fourth_menu_list = third_menu.ul.find_all('li', class_=css)
                            for fourth_menu in fourth_menu_list:
                                menu_dict['child_' + str(num)]['child_' + str(num) + '.' + str(grade_f)][
                                    'child_' + str(num) + '.' + str(grade_f) + '.' + str(grade_s)][
                                    'chapter_' + str(num) + '.' + str(grade_f) + '.' + str(grade_s) + '.' + str(grade_t)
                                ] = third_menu.a.get_text()
                                menu_dict['child_' + str(num)]['child_' + str(num) + '.' + str(grade_f)][
                                    'child_' + str(num) + '.' + str(grade_f) + '.' + str(grade_s)][
                                    'url_' + str(num) + '.' + str(grade_f) + '.' + str(grade_s) + '.' + str(grade_t)
                                ] = pre_url + third_menu.a.get('href')
                                if fourth_menu.ul is not None:
                                    menu_dict['child_' + str(num)]['child_' + str(num) + '.' + str(grade_f)][
                                        'child_' + str(num) + '.' + str(grade_f) + '.' + str(grade_s)][
                                        'child_' + str(num) + '.' + str(grade_f) + '.' + str(grade_s) + '.' + str(
                                            grade_t)
                                        ] = {}
                                grade_t += 1
                        grade_s += 1
                grade_f += 1
        num += 1


def get_urls(menu, pre_url, urls):
    for a in menu:
        # print(a.find('a').get('href'))
        urls.append(pre_url + str(a.find('a').get('href')))
        # if len(urls) > 2:
        #     break
    return urls



html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""


def parse_to_html(url, name):
    print(str(name) + '-'*10 + '开始')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.find_all(class_="section")[0]
    html = html_template.format(content=body)
    html = html.encode("utf-8")
    with open(name, 'wb') as f:
        f.write(html)
    return name


def convert_pdf(htmls, file_name):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    config = pdfkit.configuration(wkhtmltopdf='D:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_file(htmls, file_name, options=options, configuration=config)


if __name__ == '__main__':
    start = time.time()
    url = 'https://docs.python.org/zh-cn/3/tutorial/index.html'

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    body = soup.find_all(class_="section")

    title = soup.find_all('h1')[0].get_text()

    p = soup.find_all('p')

    tree = soup.find_all(class_="toctree-wrapper compound")

    menu = tree[0].ul.find_all('li', class_="toctree-l1")
    print(len(menu))

    pre_url = 'https://docs.python.org/zh-cn/3/tutorial/'

    menu_dict = {}
    urls = []
    urls.append(url)

    # print(tree[0].ul.find_all('a'))

    # get_menu(menu, 1)
    get_urls(menu, pre_url, urls)
    file_name = "python.pdf"

    htmls = [parse_to_html(url, str(index) + '.html') for index, url in enumerate(urls)]

    # print(htmls)
    convert_pdf(htmls, file_name)

    # print(urls)
    i = 1
    for html in htmls:
        print('delete html' + str(i))
        i += 1
        os.remove(html)
    total_time = time.time() - start
    print("数据读取完毕,总共用时： %f 秒" % total_time)

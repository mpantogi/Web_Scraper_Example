# coding=utf8
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import os
from xlsxwriter import Workbook
import requests
import shutil
import datetime
import smtplib
from datetime import datetime
import random
import string
from romanize import romanize
from datetime import timedelta


class App:
    def __init__(self, username='examplemail.com', password='******', path='/Users/Administrator/Desktop/pock_Scrape'):
        starttime = datetime.now()
        self.username = username
        self.password = password
        self.path = path
        self.driver = webdriver.Chrome('/Users/Administrator/Downloads/chromedriver.exe')
        self.error = False
        self.base_url = 'https://example.com'
        self.main_url = 'https://example.com/app/products/category/463'
        self.driver.get(self.main_url)
        sleep(9)
        self.list1 = []
        self.list2 = []
        self.list3 = []
        self.list4 = []
        self.list5 = []
        self.list6 = []
        self.list7 = []
        self.list8 = []
        self.list9 = []
        self.list10 = []
        self.list11 = []
        self.list12 = []
        self.list13 = []
        self.compare = []
        self.items_number = []
        self.log_in()
        if self.error is False :
           self.scroll_down()
        if not os.path.exists(path):
            os.mkdir(path)
        self.download_portal()

        # Fill these in with the appropriate info...
        usr = 'example@gmail.com
        psw = '*********'
        fromaddr = 'example@gmail.com'
        toaddr = 'example2.gr'

        # Send notification email
        self.noticeEMail(starttime, usr, psw, fromaddr, toaddr)
        self.driver.close()

    def noticeEMail(self,starttime, usr, psw, fromaddr, toaddr):

        # Calculate run time
        runtime = datetime.now() - starttime

        # Initialize SMTP server
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(usr, psw)

        # Send email
        senddate = datetime.strftime(datetime.now(), '%Y-%m-%d')
        subject = "Your job has completed --------- Diafora"
        m = "Date: %s\r\nFrom: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (senddate, fromaddr, toaddr, subject)
        msg = '''
        Job runtime: ''' + str(runtime)
        server.sendmail(fromaddr, toaddr, m + msg)
        print('email sent')
        server.quit()

    def write_captions_to_excel_file(self, description_path, firstlists, secondlists, thirdlists, fourthlists,
                                     fifthlists, sixthlists, seventhlists, eighthlists, eleventhlists, comparelists,
                                     twelvelists, thirteenlists):
        print('writing to excel')
        workbook = Workbook(os.path.join(description_path, 'all_captions_diafora.xlsx'))
        worksheet = workbook.add_worksheet()
        row = 0
        worksheet.write(row, 0, 'Images')  # 3 --> row number, column number, value
        worksheet.write(row, 1, 'Title')
        worksheet.write(row, 2, 'State')
        worksheet.write(row, 3, 'Short_Description')
        worksheet.write(row, 4, 'Category')
        worksheet.write(row, 5, 'Temp_Description')
        worksheet.write(row, 6, 'Seo_title')
        worksheet.write(row, 7, 'Seo_meta')
        worksheet.write(row, 8, 'Schedule')
        worksheet.write(row, 9, 'Supermarket')
        worksheet.write(row, 10, 'Visibility')
        worksheet.write(row, 11, 'Hidden')
        worksheet.write(row, 12, 'Price')
        worksheet.write(row, 13, 'Sale_Price')
        worksheet.write(row, 14, 'Category_2')
        worksheet.write(row, 15, 'Small_image')
        worksheet.write(row, 16, 'Group ID')
        worksheet.write(row, 17, 'Group Match')
        worksheet.write(row, 18, 'Product Type')
        worksheet.write(row, 19, 'Gift Text')
        worksheet.write(row, 20, 'Temp Market')
        worksheet.write(row, 21, 'Sep Image')
        worksheet.write(row, 22, 'Attribute')
        worksheet.write(row, 23, 'Slug')
        worksheet.write(row, 24, 'Tag')
        row += 1
        format_test = workbook.add_format({'num_format': 'yyyy-m-d'})
        for index, comparelist in enumerate(comparelists):
            if len(comparelist) == 0:
                pass
            elif len(comparelist) == 1:
                if '(πάγκος)' in secondlists[index] or '(κοπής)' in secondlists[index]:
                    pass
                elif firstlists[index] == 'No_Image.png':
                    pass
                elif comparelist[0][5] is None:
                    pass
                elif secondlists[index] == 'Δημητριακά rice krispies 375gr':
                    pass
                elif secondlists[index] == 'Μπισκότα αλλατινη cookie bites με επικάλυψη σοκολάτας 70gr':
                    pass
                else:
                    if comparelist[0][2] is None and comparelist[0][3] is None:
                        pass
                    else:
                        worksheet.write(row, 0, firstlists[index])  # 3 --> row number, column number, value
                        worksheet.write(row, 1, secondlists[index])
                        worksheet.write(row, 2, thirdlists[index])
                        worksheet.write(row, 3, fourthlists[index])
                        worksheet.write(row, 4, fifthlists[index])
                        worksheet.write(row, 5, sixthlists[index])
                        worksheet.write(row, 6, seventhlists[index])
                        worksheet.write(row, 21, eleventhlists[index])
                        worksheet.write(row, 23, twelvelists[index])
                        worksheet.write(row, 7, eighthlists[index])
                        worksheet.write(row, 24, thirteenlists[index])
                        worksheet.write(row, 9, comparelist[0][0])
                        worksheet.write(row, 12, comparelist[0][1])
                        worksheet.write(row, 19, comparelist[0][3])
                        worksheet.write(row, 22, comparelist[0][6])
                        # worksheet.write(row, 20, comparelist[0][4])
                        if comparelist[0][3] is not None:
                            # worksheet.write(row, 22, -1)
                            # worksheet.write(row, 23, 'yes')
                            worksheet.write(row, 8, comparelist[0][5], format_test)
                            # worksheet.write(row, 14, tenthlists[index])
                        worksheet.write(row, 10, 'visible')
                        worksheet.write(row, 18, 'simple')
                        worksheet.write(row, 11, 0)
                        if comparelist[0][2] is not None:
                            worksheet.write(row, 13, comparelist[0][2])
                            # worksheet.write(row, 14, tenthlists[index])
                            worksheet.write(row, 8, comparelist[0][5], format_test)
                            # worksheet.write(row, 22, -1)
                            # worksheet.write(row, 23, 'yes')
                        if comparelist[0][0] == 'Βασιλόπουλος':
                            worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/vasilopoulos.png')
                        elif comparelist[0][0] == 'Μασούτης':
                            worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/masoutis.png')
                        elif comparelist[0][0] == 'Σκλαβενίτης':
                            worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/sklavenitis.png')
                        elif comparelist[0][0] == 'My Market':
                            worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/my_market.png')
                        elif comparelist[0][0] == 'Γαλαξίας':
                            worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/galaxias.png')
                        elif comparelist[0][0] == 'Κρητικός':
                            worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/kritikos.png')
                        elif comparelist[0][0] == 'Market In':
                            worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/market_in.png')
                        elif comparelist[0][0] == 'Bazaar':
                            worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/bazzar.png')
                        row += 1
            else:
                if '(πάγκος)' in secondlists[index] or '(κοπής)' in secondlists[index]:
                    pass
                elif firstlists[index] == 'No_Image.png':
                    pass
                elif secondlists[index] == 'Δημητριακά rice krispies 375gr':
                    pass
                elif secondlists[index] == 'Μπισκότα αλλατινη cookie bites με επικάλυψη σοκολάτας 70gr':
                    pass
                else:
                    group_random = ''.join(
                        random.choice(string.ascii_letters + string.digits) for _ in range(32)) + '_Group_'
                    worksheet.write(row, 0, firstlists[index])  # 3 --> row number, column number, value
                    worksheet.write(row, 1, secondlists[index])
                    worksheet.write(row, 2, thirdlists[index])
                    worksheet.write(row, 3, fourthlists[index])
                    worksheet.write(row, 4, fifthlists[index])
                    worksheet.write(row, 5, sixthlists[index])
                    worksheet.write(row, 6, seventhlists[index])
                    worksheet.write(row, 7, eighthlists[index])
                    worksheet.write(row, 21, eleventhlists[index])
                    worksheet.write(row, 23, twelvelists[index])
                    worksheet.write(row, 24, thirteenlists[index])
                    worksheet.write(row, 10, 'visible')
                    worksheet.write(row, 18, 'grouped')
                    worksheet.write(row, 11, 0)
                    worksheet.write(row, 16, group_random)
                    # for i in comparelist:
                    # if i[2] is not None:
                    # worksheet.write(row, 14, tenthlists[index])
                    # worksheet.write(row, 22, -1)
                    # worksheet.write(row, 23, 'yes')
                    # pass
                    # if i[3] is not None:
                    # worksheet.write(row, 14, tenthlists[index])
                    # worksheet.write(row, 22, -1)
                    # worksheet.write(row, 23, 'yes')
                    # pass
                    row += 1
                    for y in comparelist:
                        if y[5] is None:
                            pass
                        elif y[2] is None and y[3] is None:
                            pass
                        else:
                            worksheet.write(row, 0, firstlists[index])  # 3 --> row number, column number, value
                            worksheet.write(row, 1, secondlists[index])
                            worksheet.write(row, 2, thirdlists[index])
                            worksheet.write(row, 3, fourthlists[index])
                            worksheet.write(row, 4, fifthlists[index])
                            worksheet.write(row, 5, sixthlists[index])
                            worksheet.write(row, 6, seventhlists[index])
                            worksheet.write(row, 7, eighthlists[index])
                            worksheet.write(row, 21, eleventhlists[index])
                            worksheet.write(row, 23, twelvelists[index])
                            worksheet.write(row, 24, thirteenlists[index])
                            worksheet.write(row, 9, y[0])
                            worksheet.write(row, 12, y[1])
                            worksheet.write(row, 19, y[3])
                            worksheet.write(row, 22, y[6])
                            if y[3] is not None:
                                # worksheet.write(row, 22, -1)
                                # worksheet.write(row, 23, 'yes')
                                worksheet.write(row, 8, y[5], format_test)
                                # worksheet.write(row, 14, tenthlists[index])
                            worksheet.write(row, 10, 'hidden')
                            worksheet.write(row, 18, 'simple')
                            worksheet.write(row, 11, 1)
                            worksheet.write(row, 20, y[4])
                            if y[2] is not None:
                                worksheet.write(row, 13, y[2])
                                worksheet.write(row, 8, y[5], format_test)
                                # worksheet.write(row, 14, tenthlists[index])
                                # worksheet.write(row, 22, -1)
                                # worksheet.write(row, 23, 'yes')
                            worksheet.write(row, 17, group_random)
                            if y[0] == 'Βασιλόπουλος':
                                worksheet.write(row, 15,
                                                'https://bagies.gr/wp-content/uploads/2018/11/vasilopoulos.png')
                            elif y[0] == 'Μασούτης':
                                worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/masoutis.png')
                            elif y[0] == 'Σκλαβενίτης':
                                worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/sklavenitis.png')
                            elif y[0] == 'My Market':
                                worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/my_market.png')
                            elif y[0] == 'Γαλαξίας':
                                worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/galaxias.png')
                            elif y[0] == 'Κρητικός':
                                worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/kritikos.png')
                            elif y[0] == 'Market In':
                                worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/market_in.png')
                            elif y[0] == 'Bazaar':
                                worksheet.write(row, 15, 'https://bagies.gr/wp-content/uploads/2018/11/bazzar.png')
                            row += 1
        workbook.close()

    def press_button(self):
        try:
            button = self.driver.find_element_by_link_text('Προσφορές ανά αλυσίδα')
            button.click()
            sleep(1)
            try:
                more_shop = self.driver.find_element_by_xpath(
                    '//section[@class="product-single-comparison"]/div[@class="products-more"]')
                more_shop.click()
                sleep(1)
            except Exception:
                pass
            extra_soup = BeautifulSoup(self.driver.page_source, 'lxml')
            stores = extra_soup.find_all('div', class_='shopping-list-tile-inner')
            xantoukens = self.driver.find_elements_by_xpath(
                '//div[@class="shopping-list-tile-inner"]/div[@class="row"]')
            temp_list = []
            i = 0
            seq = ('<b><font color="red">', '</font></b>')
            for store in stores:
                xantoukens[i].click()
                sleep(9)
                i += 1
                tempstore = store.a['href']
                tempstore = tempstore.split("?", 1)[1]
                finalstore = tempstore
                print(finalstore)
                if finalstore == 'retailer=4&comparison=true':
                    price = store.a.p.next_sibling.next_sibling.getText()
                    try:
                        discount = store.a.span.getText()
                        if discount[-4:] == 'Δώρο':
                            gift_text = discount.join(seq)
                            attrib = discount
                            print(gift_text)
                        else:
                            gift_text = None
                            attrib = None
                    except Exception:
                        gift_text = None
                        attrib = None
                    temp_price = price.replace('€', '').replace('* ', '').replace(',',
                                                                                  '.')  # replace specific character
                    try:
                        words = temp_price.split(" ")
                        final_price = float(words[0])
                        final_offer = float(words[1])
                    except Exception:
                        final_price = float(temp_price)
                        final_offer = None
                    try:
                        extra_soup = BeautifulSoup(self.driver.page_source, 'lxml')
                        dater = extra_soup.find('div', attrs={'class': 'product-single-meta clearfix'})
                        spec_date = dater.p.getText()
                        spec_date_x = spec_date.split("έως ", 1)[1]
                        spec_date_y = '-'.join(spec_date_x.split('-')[::-1])  # reverse and join string
                        spec_date_z = datetime.strptime(spec_date_y, "%Y-%m-%d").date()  # convert string to datetime
                        spec_date_z = spec_date_z - timedelta(days=2)  # substract from a datetime
                        print(spec_date_z)
                    except Exception:
                        spec_date_z = None
                    masoutis = 'Μασούτης', final_price, final_offer, gift_text, ' - <font color="red">Μασούτης</font>', spec_date_z, attrib
                    temp_list.append(masoutis)
                elif finalstore == 'retailer=1&comparison=true':
                    price = store.a.p.next_sibling.next_sibling.getText()
                    try:
                        discount = store.a.span.getText()
                        if discount[-4:] == 'Δώρο':
                            gift_text = discount.join(seq)
                            attrib = discount
                            print(gift_text)
                        else:
                            gift_text = None
                            attrib = None
                    except Exception:
                        gift_text = None
                        attrib = None
                    temp_price = price.replace('€', '').replace('* ', '').replace(',',
                                                                                  '.')  # replace specific character
                    try:
                        words = temp_price.split(" ")
                        final_price = float(words[0])
                        final_offer = float(words[1])
                    except Exception:
                        final_price = float(temp_price)
                        final_offer = None
                    try:
                        extra_soup = BeautifulSoup(self.driver.page_source, 'lxml')
                        dater = extra_soup.find('div', attrs={'class': 'product-single-meta clearfix'})
                        spec_date = dater.p.getText()
                        spec_date_x = spec_date.split("έως ", 1)[1]
                        spec_date_y = '-'.join(spec_date_x.split('-')[::-1])  # reverse and join string
                        spec_date_z = datetime.strptime(spec_date_y, "%Y-%m-%d").date()  # convert string to datetime
                        spec_date_z = spec_date_z - timedelta(days=2)  # substract from a datetime
                        print(spec_date_z)
                    except Exception:
                        spec_date_z = None
                    vasilopoulos = 'Βασιλόπουλος', final_price, final_offer, gift_text, ' - <font color="red">Βασιλόπουλος</font>', spec_date_z, attrib
                    temp_list.append(vasilopoulos)
                elif finalstore == 'retailer=2&comparison=true':
                    price = store.a.p.next_sibling.next_sibling.getText()
                    try:
                        discount = store.a.span.getText()
                        if discount[-4:] == 'Δώρο':
                            gift_text = discount.join(seq)
                            attrib = discount
                            print(gift_text)
                        else:
                            gift_text = None
                            attrib = None
                    except Exception:
                        gift_text = None
                        attrib = None
                    temp_price = price.replace('€', '').replace('* ', '').replace(',',
                                                                                  '.')  # replace specific character
                    try:
                        words = temp_price.split(" ")
                        final_price = float(words[0])
                        final_offer = float(words[1])
                    except Exception:
                        final_price = float(temp_price)
                        final_offer = None
                    try:
                        extra_soup = BeautifulSoup(self.driver.page_source, 'lxml')
                        dater = extra_soup.find('div', attrs={'class': 'product-single-meta clearfix'})
                        spec_date = dater.p.getText()
                        spec_date_x = spec_date.split("έως ", 1)[1]
                        spec_date_y = '-'.join(spec_date_x.split('-')[::-1])  # reverse and join string
                        spec_date_z = datetime.strptime(spec_date_y, "%Y-%m-%d").date()  # convert string to datetime
                        spec_date_z = spec_date_z - timedelta(days=2)  # substract from a datetime
                        print(spec_date_z)
                    except Exception:
                        spec_date_z = None
                    sklavenitis = 'Σκλαβενίτης', final_price, final_offer, gift_text, ' - <font color="red">Σκλαβενίτης</font>', spec_date_z, attrib
                    temp_list.append(sklavenitis)
                elif finalstore == 'retailer=10&comparison=true':
                    price = store.a.p.next_sibling.next_sibling.getText()
                    try:
                        discount = store.a.span.getText()
                        if discount[-4:] == 'Δώρο':
                            gift_text = discount.join(seq)
                            attrib = discount
                            print(gift_text)
                        else:
                            gift_text = None
                            attrib = None
                    except Exception:
                        gift_text = None
                        attrib = None
                    temp_price = price.replace('€', '').replace('* ', '').replace(',',
                                                                                  '.')  # replace specific character
                    try:
                        words = temp_price.split(" ")
                        final_price = float(words[0])
                        final_offer = float(words[1])
                    except Exception:
                        final_price = float(temp_price)
                        final_offer = None
                    try:
                        extra_soup = BeautifulSoup(self.driver.page_source, 'lxml')
                        dater = extra_soup.find('div', attrs={'class': 'product-single-meta clearfix'})
                        spec_date = dater.p.getText()
                        spec_date_x = spec_date.split("έως ", 1)[1]
                        spec_date_y = '-'.join(spec_date_x.split('-')[::-1])  # reverse and join string
                        spec_date_z = datetime.strptime(spec_date_y, "%Y-%m-%d").date()  # convert string to datetime
                        spec_date_z = spec_date_z - timedelta(days=2)  # substract from a datetime
                        print(spec_date_z)
                    except Exception:
                        spec_date_z = None
                    galaxias = 'Γαλαξίας', final_price, final_offer, gift_text, ' - <font color="red">Γαλαξίας</font>', spec_date_z, attrib
                    temp_list.append(galaxias)
                elif finalstore == 'retailer=27&comparison=true':
                    price = store.a.p.next_sibling.next_sibling.getText()
                    try:
                        discount = store.a.span.getText()
                        if discount[-4:] == 'Δώρο':
                            gift_text = discount.join(seq)
                            attrib = discount
                            print(gift_text)
                        else:
                            gift_text = None
                            attrib = None
                    except Exception:
                        gift_text = None
                        attrib = None
                    temp_price = price.replace('€', '').replace('* ', '').replace(',',
                                                                                  '.')  # replace specific character
                    try:
                        words = temp_price.split(" ")
                        final_price = float(words[0])
                        final_offer = float(words[1])
                    except Exception:
                        final_price = float(temp_price)
                        final_offer = None
                    try:
                        extra_soup = BeautifulSoup(self.driver.page_source, 'lxml')
                        dater = extra_soup.find('div', attrs={'class': 'product-single-meta clearfix'})
                        spec_date = dater.p.getText()
                        spec_date_x = spec_date.split("έως ", 1)[1]
                        spec_date_y = '-'.join(spec_date_x.split('-')[::-1])  # reverse and join string
                        spec_date_z = datetime.strptime(spec_date_y, "%Y-%m-%d").date()  # convert string to datetime
                        spec_date_z = spec_date_z - timedelta(days=2)  # substract from a datetime
                        print(spec_date_z)
                    except Exception:
                        spec_date_z = None
                    my_market = 'My Market', final_price, final_offer, gift_text, ' - <font color="red">My Market</font>', spec_date_z, attrib
                    temp_list.append(my_market)
                elif finalstore == 'retailer=6&comparison=true':
                    price = store.a.p.next_sibling.next_sibling.getText()
                    try:
                        discount = store.a.span.getText()
                        if discount[-4:] == 'Δώρο':
                            gift_text = discount.join(seq)
                            attrib = discount
                            print(gift_text)
                        else:
                            gift_text = None
                            attrib = None
                    except Exception:
                        gift_text = None
                        attrib = None
                    temp_price = price.replace('€', '').replace('* ', '').replace(',',
                                                                                  '.')  # replace specific character
                    try:
                        words = temp_price.split(" ")
                        final_price = float(words[0])
                        final_offer = float(words[1])
                    except Exception:
                        final_price = float(temp_price)
                        final_offer = None
                    try:
                        extra_soup = BeautifulSoup(self.driver.page_source, 'lxml')
                        dater = extra_soup.find('div', attrs={'class': 'product-single-meta clearfix'})
                        spec_date = dater.p.getText()
                        spec_date_x = spec_date.split("έως ", 1)[1]
                        spec_date_y = '-'.join(spec_date_x.split('-')[::-1])  # reverse and join string
                        spec_date_z = datetime.strptime(spec_date_y, "%Y-%m-%d").date()  # convert string to datetime
                        spec_date_z = spec_date_z - timedelta(days=2)  # substract from a datetime
                        print(spec_date_z)
                    except Exception:
                        spec_date_z = None
                    market_in = 'Market In', final_price, final_offer, gift_text, ' - <font color="red">Market In</font>', spec_date_z, attrib
                    temp_list.append(market_in)
                elif finalstore == 'retailer=11&comparison=true':
                    price = store.a.p.next_sibling.next_sibling.getText()
                    try:
                        discount = store.a.span.getText()
                        if discount[-4:] == 'Δώρο':
                            gift_text = discount.join(seq)
                            attrib = discount
                            print(gift_text)
                        else:
                            gift_text = None
                            attrib = None
                    except Exception:
                        gift_text = None
                        attrib = None
                    temp_price = price.replace('€', '').replace('* ', '').replace(',',
                                                                                  '.')  # replace specific character
                    try:
                        words = temp_price.split(" ")
                        final_price = float(words[0])
                        final_offer = float(words[1])
                    except Exception:
                        final_price = float(temp_price)
                        final_offer = None
                    try:
                        extra_soup = BeautifulSoup(self.driver.page_source, 'lxml')
                        dater = extra_soup.find('div', attrs={'class': 'product-single-meta clearfix'})
                        spec_date = dater.p.getText()
                        spec_date_x = spec_date.split("έως ", 1)[1]
                        spec_date_y = '-'.join(spec_date_x.split('-')[::-1])  # reverse and join string
                        spec_date_z = datetime.strptime(spec_date_y, "%Y-%m-%d").date()  # convert string to datetime
                        spec_date_z = spec_date_z - timedelta(days=2)  # substract from a datetime
                        print(spec_date_z)
                    except Exception:
                        spec_date_z = None
                    bazaar = 'Bazaar', final_price, final_offer, gift_text, ' - <font color="red">Bazaar</font>', spec_date_z, attrib
                    temp_list.append(bazaar)
                elif finalstore == 'retailer=12&comparison=true':
                    price = store.a.p.next_sibling.next_sibling.getText()
                    try:
                        discount = store.a.span.getText()
                        if discount[-4:] == 'Δώρο':
                            gift_text = discount.join(seq)
                            attrib = discount
                            print(gift_text)
                        else:
                            gift_text = None
                            attrib = None
                    except Exception:
                        gift_text = None
                        attrib = None
                    temp_price = price.replace('€', '').replace('* ', '').replace(',',
                                                                                  '.')  # replace specific character
                    try:
                        words = temp_price.split(" ")
                        final_price = float(words[0])
                        final_offer = float(words[1])
                    except Exception:
                        final_price = float(temp_price)
                        final_offer = None
                    try:
                        extra_soup = BeautifulSoup(self.driver.page_source, 'lxml')
                        dater = extra_soup.find('div', attrs={'class': 'product-single-meta clearfix'})
                        spec_date = dater.p.getText()
                        spec_date_x = spec_date.split("έως ", 1)[1]
                        spec_date_y = '-'.join(spec_date_x.split('-')[::-1])  # reverse and join string
                        spec_date_z = datetime.strptime(spec_date_y, "%Y-%m-%d").date()  # convert string to datetime
                        spec_date_z = spec_date_z - timedelta(days=2)  # substract from a datetime
                        print(spec_date_z)
                    except Exception:
                        spec_date_z = None
                    kritikos = 'Κρητικός', final_price, final_offer, gift_text, ' - <font color="red">Κρητικός</font>', spec_date_z, attrib
                    temp_list.append(kritikos)
                else:
                    print('This store is not in my list')
            sort_list = sorted(temp_list, key=lambda tup: [x for x in tup[2:0:-1] if not isinstance(x, type(None))])
            self.compare.append(sort_list)
            return self.compare
        except Exception:
            self.compare.append([])
            return self.compare

    def download_portal(self):
        temp_descr = '<strong>ΌΡΟΙ ΚΑΙ ΠΡΟΥΠΟΘΈΣΕΙΣ:</strong>\n\n1.Σε περίπτωση που η τιμή του προϊόντος διαφέρει από εκείνη στο κατάστημα  ή ορισμένα από τα προϊόντα δεν υπάρχουν σε όλα τα καταστήματα, λόγω περιορισμένου χώρου ή διαθεσιμότητας, ο προσωπικός αγοραστής σας από την Βagies θα προβεί στην ανάλογη ενέργεια που επιθυμείτε, με κριτίριο τις απαντήσεις σας κατά την ολοκλήρωση της παραγγελίας.\n2.Το ποσό που αναγράφεται κατά την ολοκλήρωση της παραγγελίας είναι το εκτιμώμενο ποσό καθώς ενδέχεται η παραγγελία να έχει ελλείψεις, αντικαταστάσεις, μεταβολές στα ζυγιζόμενα κλπ.'
        seo_title = '- Bagies'
        seo_meta = 'Κάντε εύκολες και έξυπνες αγορές 24 ώρες την ημέρα. Σύγκρινε τιμές και προσφορές προϊόντων supermarket. Παράγγειλε online πανεύκολα. Delivery στην Θεσσαλονίκη · Κερδίστε χρόνο · Κερδίστε Χρήματα · Γλιτώστε Μετακινήσεις.'
        nomos = 'Ν.Θεσσαλονίκης'
        seo_image = 'Συγκριση τιμων, online supermarket'
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        all_divs = soup.find_all('div', class_='product-tile')
        all_links = [self.base_url + div.a['href'] for div in all_divs]
        sleep(4)
        for index, link in enumerate(all_links):
            try:
                self.driver.execute_script("window.open('" + link + "');")
                sleep(4)
                try:
                    print(link)
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    sleep(6)
                    try:
                        final_soup = BeautifulSoup(self.driver.page_source, 'lxml')
                        title = final_soup.find('div', attrs={'class': 'col-sm-6 col-md-7 col-lg-6 col-lg-offset-1'})
                        origin_title = title.h1.getText()
                        print(origin_title)
                        real_title = origin_title.capitalize()
                        image = final_soup.find('div', attrs={'class': 'product-single-image max-width'})
                        slugy = romanize(real_title)
                        filename = slugy.replace(" ", "-") + '.png'
                        # filename = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32)) + '.png'
                        # dater = final_soup.find('div', attrs={'class': 'product-single-meta clearfix'})
                        tag = " "
                        info = final_soup.find('div', attrs={'class': 'product-single-more'})
                        try:
                            short_descr = info.p.getText()
                        except Exception:
                            short_descr = real_title
                            # print('No description found')
                        category = final_soup.find('ol', attrs={'class': 'breadcrumb'})
                        try:
                            temp_category = category.li.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
                            real_category_past = temp_category.a.getText()
                            print(real_category_past)
                            if real_category_past == 'Γάλα Ραφιού':
                                real_category = 'ΓΑΛΑΚΤΟΜΙΚΑ'
                                tag = 'Γάλα Ραφιού'
                            elif real_category_past == 'Γάλα Ψυγείου':
                                real_category = 'ΓΑΛΑΚΤΟΜΙΚΑ'
                                tag = 'Γάλα Ψυγείου'
                            elif real_category_past == 'Γιαούρτια & Επιδόρπια ':
                                real_category = 'ΓΑΛΑΚΤΟΜΙΚΑ'
                                tag = 'Γιαούρτια & Επιδόρπια'
                            elif real_category_past == 'Κρέμες γάλακτος & Σαντιγύ ':
                                real_category = 'ΓΑΛΑΚΤΟΜΙΚΑ'
                                tag = 'Κρέμες γάλακτος & Σαντιγύ'
                            elif real_category_past == 'Σάλτσες τομάτας ':
                                real_category = 'ΣΑΛΤΣΕΣ'
                                tag = 'Σάλτσες τομάτας'
                            elif real_category_past == 'Αλάτι & Μπαχαρικά':
                                real_category = 'ΜΑΓΕΙΡΙΚΗ & ΖΑΧΑΡ/ΣΤΙΚΗ'
                                tag = 'Αλάτι & Μπαχαρικά'
                            elif real_category_past == 'Αυγά, Ζάχαρη, Αλεύρι κ.ά. ':
                                real_category = 'ΜΑΓΕΙΡΙΚΗ & ΖΑΧΑΡ/ΣΤΙΚΗ'
                                tag = 'Αυγά, Ζάχαρη, Αλεύρι'
                            elif real_category_past == 'Σάλτσες, Dips & Dressing ':
                                real_category = 'ΣΑΛΤΣΕΣ'
                                tag = 'Σάλτσες, Dips & Dressing'
                            elif real_category_past == 'Βούτυρα & Μαργαρίνες':
                                real_category = 'ΛΑΔΙ, ΞΥΔΙ & ΒΟΥΤΗΡΟ'
                                tag = 'Βούτυρα & Μαργαρίνες'
                            elif real_category_past == 'Κρέμες, Γλυκίσματα & Παγωτά':
                                real_category = 'ΚΡΕΜΕΣ, ΚΕΙΚ, ΓΛΥΚΙΣΜΑΤΑ & ΠΑΓΩΤΑ'
                                tag = 'Κρέμες, Γλυκίσματα & Παγωτά'
                            elif real_category_past == 'Είδη επάλειψης, κονσέρβες & αλλα τρόφιμα':
                                real_category = 'ΕΙΔΗ ΕΠΑΛΕΙΨΗΣ, ΚΟΝΣΕΡΒΕΣ'
                            elif real_category_past == 'Λάδι & Ξύδι ':
                                real_category = 'ΛΑΔΙ, ΞΥΔΙ & ΒΟΥΤΗΡΟ'
                                tag = 'Λάδι & Ξύδι'
                            elif real_category_past == 'Ζαχαροπλαστική':
                                real_category = 'ΜΑΓΕΙΡΙΚΗ & ΖΑΧΑΡ/ΣΤΙΚΗ'
                                tag = 'Αυγά, Ζάχαρη, Αλεύρι'
                            elif real_category_past == 'Έτοιμα γεύματα ψυγείου':
                                real_category = 'ΕΤΟΙΜΑ ΓΕΥΜΑΤΑ'
                                tag = 'Έτοιμα γεύματα ψυγείου'
                            elif real_category_past == 'Κίτρινο Τυρί':
                                real_category = 'ΓΑΛΑΚΤΟΜΙΚΑ'
                                tag = 'Κίτρινο Τυρί'
                            elif real_category_past == 'Λευκό Τυρί':
                                real_category = 'ΓΑΛΑΚΤΟΜΙΚΑ'
                                tag = 'Λευκό Τυρί'
                            elif real_category_past == 'Ιδιαίτερες Γεύσεις Τυριού':
                                real_category = 'ΓΑΛΑΚΤΟΜΙΚΑ'
                                tag = 'Ιδιαίτερες Γεύσεις Τυριού'
                            elif real_category_past == 'Αλλαντικά ':
                                real_category = 'ΚΡΕΑΣ & ΑΛΛΑΝΤΙΚΑ'
                                tag = 'Αλλαντικά'
                            elif real_category_past == 'Κατεψυγμένα γεύματα με κρέας':
                                real_category = 'ΕΤΟΙΜΑ ΓΕΥΜΑΤΑ'
                                tag = 'Γεύματα με κρέας'
                            elif real_category_past == 'Κατεψυγμένα και φρέσκα θαλασσινά':
                                real_category = 'ΨΑΡΙΑ & ΘΑΛΑΣΣΙΝΑ'
                            elif real_category_past == 'Νωπό κρέας & Πουλερικά':
                                real_category = 'ΚΡΕΑΣ & ΑΛΛΑΝΤΙΚΑ'
                                tag = 'Νωπό κρέας & Πουλερικά'
                            elif real_category_past == 'Ψωμί, ψωμάκια & πίτες ':
                                real_category = 'ΦΟΥΡΝΟΣ & ΔΗΜΗΤΡΙΑΚΑ'
                                tag = 'Ψωμί, ψωμάκια & πίτες'
                            elif real_category_past == 'Δημητριακά':
                                real_category = 'ΦΟΥΡΝΟΣ & ΔΗΜΗΤΡΙΑΚΑ'
                                tag = 'Δημητριακά'
                            elif real_category_past == 'Μπάρες δημητριακών':
                                real_category = 'ΦΟΥΡΝΟΣ & ΔΗΜΗΤΡΙΑΚΑ'
                                tag = 'Μπάρες δημητριακών'
                            elif real_category_past == 'Φρυγανιές & Παξιμάδια':
                                real_category = 'ΦΟΥΡΝΟΣ & ΔΗΜΗΤΡΙΑΚΑ'
                                tag = 'Φρυγανιές & Παξιμάδια'
                            elif real_category_past == 'Κέικ και άλλα γλυκά ':
                                real_category = 'ΚΡΕΜΕΣ, ΚΕΙΚ, ΓΛΥΚΙΣΜΑΤΑ & ΠΑΓΩΤΑ'
                                tag = 'Κέικ και άλλα γλυκά'
                            elif real_category_past == 'Κατεψυγμένα φύλλα ζύμης ':
                                real_category = 'ΦΥΛΛΑ ΖΥΜΗΣ'
                                tag = 'Κατεψυγμένα φύλλα ζύμης'
                            elif real_category_past == 'Φύλλα ζύμης ψυγείου ':
                                real_category = 'ΦΥΛΛΑ ΖΥΜΗΣ'
                                tag = 'Φύλλα ζύμης ψυγείου'
                            elif real_category_past == 'Έτοιμες πίτες ':
                                real_category = 'ΚΑΤΕΨΥΓΜΕΝΑ'
                                tag = 'Έτοιμες πίτες'
                            elif real_category_past == 'Πιτάκια, Croissants κ.ά. ':
                                real_category = 'ΚΑΤΕΨΥΓΜΕΝΑ'
                                tag = 'Πιτάκια, Croissants κ.ά.'
                            elif real_category_past == 'Πίτσες ':
                                real_category = 'ΚΑΤΕΨΥΓΜΕΝΑ'
                                tag = 'Πίτσες'
                            elif real_category_past == 'Ρύζι':
                                real_category = 'ΖΥΜΑΡΙΚΑ, ΡΥΖΙΑ & ΟΣΠΡΙΑ'
                                tag = 'Ρύζι'
                            elif real_category_past == 'Ζυμαρικά ':
                                real_category = 'ΖΥΜΑΡΙΚΑ, ΡΥΖΙΑ & ΟΣΠΡΙΑ'
                                tag = 'Ζυμαρικά'
                            elif real_category_past == 'Όσπρια ':
                                real_category = 'ΖΥΜΑΡΙΚΑ, ΡΥΖΙΑ & ΟΣΠΡΙΑ'
                                tag = 'Όσπρια'
                            elif real_category_past == 'Κύβοι, Σούπες, Πουρές και άλλα σχετικά':
                                real_category = 'ΚΥΒΟΙ, ΣΟΥΠΕΣ & ΠΟΥΡΕΣ'
                            elif real_category_past == 'Έτοιμες σαλάτες ':
                                real_category = 'ΕΤΟΙΜΑ ΓΕΥΜΑΤΑ'
                                tag = 'Έτοιμες σαλάτες'
                            elif real_category_past == 'Κατεψυγμένα Λαχανικά ':
                                real_category = 'ΚΑΤΕΨΥΓΜΕΝΑ'
                                tag = 'Κατεψυγμένα Λαχανικά'
                            elif real_category_past == 'Κατεψυγμένα γεύματα με λαχανικά':
                                real_category = 'ΕΤΟΙΜΑ ΓΕΥΜΑΤΑ'
                                tag = 'Γεύματα με λαχανικά'
                            elif real_category_past == 'Φρούτα & Λαχανικά':
                                real_category = 'ΜΑΝΑΒΙΚΗ'
                            elif real_category_past == 'Μπύρες & Μηλίτης':
                                real_category = 'ΜΠΥΡΕΣ'
                            elif real_category_past == 'Κρασί':
                                real_category = 'ΚΡΑΣΙΑ'
                            elif real_category_past == 'Ποτά ':
                                real_category = 'ΠΟΤΑ'
                            elif real_category_past == 'Επιτραπέζια & ανθρακούχα νερά ':
                                real_category = 'ΝΕΡΟ'
                            elif real_category_past == 'Χυμοί':
                                real_category = 'ΚΑΦΕΣ, ΧΥΜΟΙ & ΑΛΛΑ'
                                tag = 'Χυμοί'
                            elif real_category_past == 'Cola & άλλα αναψυκτικά':
                                real_category = 'ΑΝΑΨΥΚΤΙΚΑ'
                            elif real_category_past == 'Πατατάκια & Γαριδάκια ':
                                real_category = 'ΣΝΑΚΣ'
                                tag = 'Πατατάκια & Γαριδάκια'
                            elif real_category_past == 'Σοκολάτες':
                                real_category = 'ΣΝΑΚΣ'
                                tag = 'Σοκολάτες'
                            elif real_category_past == 'Μπισκότα, κρουασάν & άλλα σνακς':
                                real_category = 'ΣΝΑΚΣ'
                                tag = 'Μπισκότα, κρουασάν κ.ά.'
                            elif real_category_past == 'Ξηροί καρποί & αποξηραμένα φρούτα':
                                real_category = 'ΣΝΑΚΣ'
                                tag = 'Ξηροί καρποί'
                            elif real_category_past == 'Καφές':
                                real_category = 'ΚΑΦΕΣ, ΧΥΜΟΙ & ΑΛΛΑ'
                                tag = 'Καφές'
                            elif real_category_past == 'Τσάι & άλλα ροφήματα ':
                                real_category = 'ΚΑΦΕΣ, ΧΥΜΟΙ & ΑΛΛΑ'
                                tag = 'Τσάι & αφεψήματα'
                            elif real_category_past == 'Ρόφημα κακάο ':
                                real_category = 'ΚΑΦΕΣ, ΧΥΜΟΙ & ΑΛΛΑ'
                                tag = 'Ρόφημα κακάο'
                            elif real_category_past == 'Ξυριστικά & Αποτρίχωση ':
                                real_category = 'ΓΙΑ ΤΗΝ ΓΥΝΑΙΚΑ'
                                tag = 'Ξυριστικά & Αποτρίχωση'
                            elif real_category_past == 'Περιποίηση Προσώπου ':
                                real_category = 'ΓΙΑ ΤΗΝ ΓΥΝΑΙΚΑ'
                                tag = 'Περιποίηση Προσώπου'
                            elif real_category_past == 'Σερβιέτες, Σερβιετάκια κ.ά.':
                                real_category = 'ΓΙΑ ΤΗΝ ΓΥΝΑΙΚΑ'
                                tag = 'Σερβιέτες, Σερβιετάκια'
                            elif real_category_past == 'Μακιγιάζ & Αρώματα':
                                real_category = 'ΓΙΑ ΤΗΝ ΓΥΝΑΙΚΑ'
                                tag = 'Μακιγιάζ & Αρώματα'
                            elif real_category_past == 'Οδοντόκρεμες ':
                                real_category = 'ΣΤΟΜΑΤΙΚΗ ΥΓΙΕΙΝΗ'
                                tag = 'Οδοντόκρεμες'
                            elif real_category_past == 'Οδοντόβουρτσες ':
                                real_category = 'ΣΤΟΜΑΤΙΚΗ ΥΓΙΕΙΝΗ'
                                tag = 'Οδοντόβουρτσες'
                            elif real_category_past == 'Στοματικά διαλύματα ':
                                real_category = 'ΣΤΟΜΑΤΙΚΗ ΥΓΙΕΙΝΗ'
                                tag = 'Στοματικά διαλύματα'
                            elif real_category_past == 'Οδοντικά νήματα ':
                                real_category = 'ΣΤΟΜΑΤΙΚΗ ΥΓΙΕΙΝΗ'
                                tag = 'Οδοντικά νήματα'
                            elif real_category_past == 'Ξυραφάκια & Μηχανές':
                                real_category = 'ΓΙΑ ΤΟΝ ΑΝΤΡΑ'
                                tag = 'Ξυραφάκια & Μηχανές'
                            elif real_category_past == 'Ανταλλακτικά ξυρίσματος':
                                real_category = 'ΓΙΑ ΤΟΝ ΑΝΤΡΑ'
                                tag = 'Ανταλλακτικά ξυρίσματος'
                            elif real_category_past == 'Αφροί, Gel & Κρέμες Ξυρίσματος ':
                                real_category = 'ΓΙΑ ΤΟΝ ΑΝΤΡΑ'
                                tag = 'Αφροί, Gel & Κρέμες Ξυρίσματος'
                            elif real_category_past == 'After Shave & Αρώματα ':
                                real_category = 'ΓΙΑ ΤΟΝ ΑΝΤΡΑ'
                                tag = 'After Shave & Αρώματα'
                            elif real_category_past == 'Ενδύματα ':
                                real_category = 'ΕΝΔΥΜΑΤΑ & ΥΠΟΔΗΜΑΤΑ'
                                tag = 'Ενδύματα'
                            elif real_category_past == 'Ενδύματα':
                                real_category = 'ΕΝΔΥΜΑΤΑ & ΥΠΟΔΗΜΑΤΑ'
                                tag = 'Ενδύματα'
                            elif real_category_past == 'Υποδήματα':
                                real_category = 'ΕΝΔΥΜΑΤΑ & ΥΠΟΔΗΜΑΤΑ'
                                tag = 'Υποδήματα'
                            elif real_category_past == 'Περιποίηση υποδημάτων':
                                real_category = 'ΕΝΔΥΜΑΤΑ & ΥΠΟΔΗΜΑΤΑ'
                                tag = 'Περιποίηση υποδημάτων'
                            elif real_category_past == 'Περιποίηση υποδημάτων ':
                                real_category = 'ΕΝΔΥΜΑΤΑ & ΥΠΟΔΗΜΑΤΑ'
                                tag = 'Περιποίηση υποδημάτων'
                            elif real_category_past == 'Υποδήματα ':
                                real_category = 'ΕΝΔΥΜΑΤΑ & ΥΠΟΔΗΜΑΤΑ'
                                tag = 'Υποδήματα'
                            elif real_category_past == 'Πάνες Ενηλίκων & Υποσέντονα':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ, ΠΡΟΣΩΠΙΚΗ ΦΡΟΝΤΙΔΑ'
                                tag = 'Πάνες Ενηλίκων & Υποσέντονα'
                            elif real_category_past == 'Προφυλακτικά':
                                real_category = 'ΤΕΣΤ ΕΓΚΥΜΟΣΥΝΗΣ, ΑΝΤΙΣΥΛΛΗΨΗ'
                            elif real_category_past == 'Υγρομάντηλα':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ, ΠΡΟΣΩΠΙΚΗ ΦΡΟΝΤΙΔΑ'
                                tag = 'Υγρομάντηλα'
                            elif real_category_past == 'Βαμβάκια, Μπατονέτες κ.ά.':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ, ΠΡΟΣΩΠΙΚΗ ΦΡΟΝΤΙΔΑ'
                                tag = 'Βαμβάκια, Μπατονέτες'
                            elif real_category_past == 'Λίμες & Νυχοκόπτες':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ, ΠΡΟΣΩΠΙΚΗ ΦΡΟΝΤΙΔΑ'
                                tag = 'Λίμες & Νυχοκόπτες'
                            elif real_category_past == 'Αφρόλουτρα':
                                real_category = 'ΑΦΡΟΛΟΥΤΡΑ'
                            elif real_category_past == 'Αποσμητικά ':
                                real_category = 'ΑΠΟΣΜΗΤΙΚΑ'
                            elif real_category_past == 'Αντηλιακά ':
                                real_category = 'ΦΡΟΝΤΙΔΑ ΣΩΜΑΤΟΣ'
                                tag = 'Αντηλιακά'
                            elif real_category_past == 'Αντηλιακά':
                                real_category = 'ΦΡΟΝΤΙΔΑ ΣΩΜΑΤΟΣ'
                                tag = 'Αντηλιακά'
                            elif real_category_past == 'Τσίχλες & Καραμέλες':
                                real_category = 'ΠΑΝΤΟΠΩΛΕΙΟ'
                                tag = 'Τσίχλες & Καραμέλες'
                            elif real_category_past == 'Προϊόντα φροντίδας σώματος ':
                                real_category = 'ΦΡΟΝΤΙΔΑ ΣΩΜΑΤΟΣ'
                                tag = 'Προϊόντα φροντίδας σώματος'
                            elif real_category_past == 'Κρεμοσάπουνα & Σαπούνια Χεριών':
                                real_category = 'ΦΡΟΝΤΙΔΑ ΣΩΜΑΤΟΣ'
                                tag = 'Κρεμοσάπουνα & Σαπούνια'
                            elif real_category_past == 'Εντομοαπωθητικά σώματος ':
                                real_category = 'ΦΡΟΝΤΙΔΑ ΣΩΜΑΤΟΣ'
                                tag = 'Εντομοαπωθητικά σώματος'
                            elif real_category_past == 'Εντομοαπωθητικά σώματος':
                                real_category = 'ΦΡΟΝΤΙΔΑ ΣΩΜΑΤΟΣ'
                                tag = 'Εντομοαπωθητικά σώματος'
                            elif real_category_past == 'Σαμπουάν μαλλιών':
                                real_category = 'ΦΡΟΝΤΙΔΑ ΜΑΛΛΙΩΝ'
                                tag = 'Σαμπουάν μαλλιών'
                            elif real_category_past == 'Conditioner & Μάσκες μαλλιών':
                                real_category = 'ΦΡΟΝΤΙΔΑ ΜΑΛΛΙΩΝ'
                                tag = 'Conditioner & Μάσκες μαλλιών'
                            elif real_category_past == 'Προϊόντα Styling':
                                real_category = 'ΠΡΟΪΟΝΤΑ STYLING'
                            elif real_category_past == 'Βαφές Μαλλιών':
                                real_category = 'ΒΑΦΕΣ ΜΑΛΛΙΩΝ'
                            elif real_category_past == 'Σκύλος ':
                                real_category = 'ΣΚΥΛΟΙ'
                            elif real_category_past == 'Γάτα ':
                                real_category = 'ΓΑΤΕΣ'
                            elif real_category_past == 'Αξεσουάρ & Υγιεινή Ζώων ':
                                real_category = 'ΑΞΕΣΟΥΑΡ & ΥΓΙΕΙΝΗ ΖΩΩΝ'
                            elif real_category_past == 'Σαμπουάν παιδικά':
                                real_category = 'ΠΕΡΙΠΟΙΗΣΗ ΣΩΜΑΤΟΣ'
                                tag = 'Σαμπουάν παιδικά'
                            elif real_category_past == 'Αφρόλουτρα παιδικά':
                                real_category = 'ΠΕΡΙΠΟΙΗΣΗ ΣΩΜΑΤΟΣ'
                                tag = 'Αφρόλουτρα παιδικά'
                            elif real_category_past == 'Κρέμες, Λάδια & Πούδρες ':
                                real_category = 'ΠΕΡΙΠΟΙΗΣΗ ΣΩΜΑΤΟΣ'
                                tag = 'Κρέμες, Λάδια & Πούδρες'
                            elif real_category_past == 'Αξεσουάρ για το μωρό ':
                                real_category = 'ΑΞΕΣΟΥΑΡ'
                            elif real_category_past == 'Γάλατα παιδικά':
                                real_category = 'ΓΑΛΑ & ΡΟΦΗΜΑΤΑ'
                                tag = 'Γάλατα παιδικά'
                            elif real_category_past == 'Παιδικοί Χυμοί & Ροφήματα ':
                                real_category = 'ΓΑΛΑ & ΡΟΦΗΜΑΤΑ'
                                tag = 'Παιδικοί Χυμοί & Ροφήματα'
                            elif real_category_past == 'Παιδικοί Χυμοί & Ροφήματα':
                                real_category = 'ΓΑΛΑ & ΡΟΦΗΜΑΤΑ'
                                tag = 'Παιδικοί Χυμοί & Ροφήματα'
                            elif real_category_past == 'Παιδικά γιαούρτια & Έτοιμα γεύματα':
                                real_category = 'ΠΑΙΔΙΚΕΣ ΤΡΟΦΕΣ'
                                tag = 'Γιαούρτια & Έτοιμα γεύματα'
                            elif real_category_past == 'Βρεφικές κρέμες ':
                                real_category = 'ΠΑΙΔΙΚΕΣ ΤΡΟΦΕΣ'
                                tag = 'Βρεφικές κρέμες'
                            elif real_category_past == 'Έτοιμα Βρεφικά Γεύματα':
                                real_category = 'ΠΑΙΔΙΚΕΣ ΤΡΟΦΕΣ'
                                tag = 'Γιαούρτια & Έτοιμα γεύματα'
                            elif real_category_past == 'Γιαούρτια & Επιδόρπια γιαουρτιού':
                                real_category = 'ΓΑΛΑΚΤΟΜΙΚΑ'
                                tag = 'Γιαούρτια & Επιδόρπια'
                            elif real_category_past == 'Πάνες ':
                                real_category = 'ΠΑΝΕΣ & ΜΩΡΟΜΑΝΤΗΛΑ'
                                tag = 'Πάνες'
                            elif real_category_past == 'Μωρομάντηλα ':
                                real_category = 'ΠΑΝΕΣ & ΜΩΡΟΜΑΝΤΗΛΑ'
                                tag = 'Μωρομάντηλα'
                            elif real_category_past == 'Βρεφικά Απορρυπαντικά ':
                                real_category = 'ΒΡΕΦΙΚΑ ΑΠΟΡΡΥΠΑΝΤΙΚΑ'
                                tag = 'Βρεφικά Απορρυπαντικά'
                            elif real_category_past == 'Βρεφικά Μαλακτικά':
                                real_category = 'ΒΡΕΦΙΚΑ ΑΠΟΡΡΥΠΑΝΤΙΚΑ'
                                tag = 'Βρεφικά Μαλακτικά'
                            elif real_category_past == 'Απορρυπαντικά πιάτων ':
                                real_category = 'ΑΠΟΡΡΥΠΑΝΤΙΚΑ ΠΙΑΤΩΝ'
                            elif real_category_past == 'Φύλαξη & προστασία τροφίμων ':
                                real_category = 'ΚΟΥΖΙΝΑ'
                                tag = 'Φύλαξη & προστασία τροφίμων'
                            elif real_category_past == 'Μπλοκ τουαλέτας, αποφρακτικά & καθαριστικά':
                                real_category = 'ΜΠΑΝΙΟ'
                            elif real_category_past == 'Χαρτί κουζίνας & χαρτοπετσέτες':
                                real_category = 'ΧΑΡΤΙΚΑ'
                                tag = 'Χαρτί κουζίνας & χαρτοπετσέτες'
                            elif real_category_past == 'Χαρτί υγείας & χαρτομάντηλα':
                                real_category = 'ΧΑΡΤΙΚΑ'
                                tag = 'Χαρτί υγείας & χαρτομάντηλα'
                            elif real_category_past == 'Καθαριστικά Οικοσυσκευών':
                                real_category = 'ΚΟΥΖΙΝΑ'
                                tag = 'Καθαριστικά Οικοσυσκευών'
                            elif real_category_past == 'Καθαριστικά επιφανειών':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΣΠΙΤΙΟΥ'
                                tag = 'Καθαριστικά επιφανειών'
                            elif real_category_past == 'Καθαριστικά χαλιών':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΣΠΙΤΙΟΥ'
                                tag = 'Καθαριστικά χαλιών'
                            elif real_category_past == 'Σφουγγάρια, σπογγοπετσέτες & συρματάκια':
                                real_category = 'ΚΟΥΖΙΝΑ'
                                tag = 'Σφουγγάρια & Σπόγγοι'
                            elif real_category_past == 'Σφουγγάρια, σπογγοπετσέτες & πανάκια':
                                real_category = 'ΚΟΥΖΙΝΑ'
                                tag = 'Σφουγγάρια & Σπόγγοι'
                            elif real_category_past == 'Γάντια':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΣΠΙΤΙΟΥ'
                                tag = 'Γάντια'
                            elif real_category_past == 'Εντομοκτόνα, Εντομοαπωθητικά ':
                                real_category = 'ΕΝΤΟΜΟΚΤΟΝΑ, ΕΝΤΟΜΟΑΠΩΘΗΤΙΚΑ'
                            elif real_category_past == 'Εντομοκτόνα, Εντομοαπωθητικά':
                                real_category = 'ΕΝΤΟΜΟΚΤΟΝΑ, ΕΝΤΟΜΟΑΠΩΘΗΤΙΚΑ'
                            elif real_category_past == 'Σακούλες απορριμμάτων ':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΣΠΙΤΙΟΥ'
                                tag = 'Σακούλες απορριμμάτων'
                            elif real_category_past == 'Δραστικά καθαριστικά ':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΣΠΙΤΙΟΥ'
                                tag = 'Δραστικά καθαριστικά'
                            elif real_category_past == 'Φροντίδα επίπλων':
                                real_category = 'ΕΞΟΠΛΙΣΜΟΣ ΣΠΙΤΙΟΥ'
                                tag = 'Φροντίδα επίπλων'
                            elif real_category_past == 'Εξοπλισμός Σπιτιού ':
                                real_category = 'ΕΞΟΠΛΙΣΜΟΣ ΣΠΙΤΙΟΥ'
                            elif real_category_past == 'Υγρό πλυντηρίου ρούχων':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΡΟΥΧΩΝ'
                                tag = 'Υγρό πλυντηρίου ρούχων'
                            elif real_category_past == 'Σκόνη πλυντηρίου ρούχων':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΡΟΥΧΩΝ'
                                tag = 'Σκόνη πλυντηρίου ρούχων'
                            elif real_category_past == 'Κάψουλες πλυντηρίου ρούχων':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΡΟΥΧΩΝ'
                                tag = 'Κάψουλες πλυντηρίου ρούχων'
                            elif real_category_past == 'Πλύσιμο στο χέρι':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΡΟΥΧΩΝ'
                                tag = 'Πλύσιμο στο χέρι'
                            elif real_category_past == 'Μαλακτικά ρούχων':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΡΟΥΧΩΝ'
                                tag = 'Μαλακτικά ρούχων'
                            elif real_category_past == 'Λευκαντικά, Χρωμοπαγίδες & Ενισχυτικά':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΡΟΥΧΩΝ'
                                tag = 'Λευκαντικά & Χρωμοπαγίδες'
                            elif real_category_past == 'Φύλαξη, σιδέρωμα & άπλωμα ρούχων ':
                                real_category = 'ΑΠΛΩΜΑ, ΣΙΔΕΡΩΜΑ & ΤΑΚΤΟΠΟΙΗΣΗ'
                            elif real_category_past == 'Ειδικής Φροντίδας ':
                                real_category = 'ΑΠΛΩΜΑ, ΣΙΔΕΡΩΜΑ & ΤΑΚΤΟΠΟΙΗΣΗ'
                            elif real_category_past == 'Αποσκληρυντικά Πλυντηρίου':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΡΟΥΧΩΝ'
                                tag = 'Αποσκληρυντικά Πλυντηρίου'
                            elif real_category_past == 'Καθαρισμός πατώματος & ξεσκόνισμα':
                                real_category = 'ΚΑΘΑΡΙΟΤΗΤΑ ΣΠΙΤΙΟΥ'
                                tag = 'Καθαρισμός δαπέδου & ξεσκόνισμα'
                            elif real_category_past == 'Μπαταρίες':
                                real_category = 'ΚΟΛΛΕΣ, ΛΑΜΠΕΣ & ΜΠΑΤΑΡΙΕΣ'
                            elif real_category_past == 'Αρωματικά χώρου':
                                real_category = 'ΕΞΟΠΛΙΣΜΟΣ ΣΠΙΤΙΟΥ'
                                tag = 'Αρωματικά χώρου'
                            elif real_category_past == 'Τσάι & αφεψήματα':
                                real_category = 'ΚΑΦΕΣ, ΧΥΜΟΙ & ΑΛΛΑ'
                                tag = 'Τσάι & αφεψήματα'
                            else:
                                real_category = real_category_past
                            print(real_category)
                        except Exception:
                            real_category = " "
                            tag = " "
                        try:
                            temp_category_two = category.li.next_sibling.next_sibling.next_sibling.next_sibling
                            category_two = temp_category_two.a.getText()
                        except Exception:
                            category_two = " "
                        self.compare = self.press_button()
                        print(self.compare)

                        image_path = os.path.join(self.path, filename)
                        newlink = image.img['src']
                        print('Downloading image', index)
                        try:
                            with requests.get(newlink, stream=True) as response:
                                print('request')
                                sleep(1)
                                with open(image_path, 'wb') as file:
                                    sleep(1)
                                    # r.raw.decode_content = True
                                    shutil.copyfileobj(response.raw, file)  # source -  destination
                                    # del response
                        except Exception as e:
                            filename = 'No_Image' + '.png'
                            print(e)
                            print('Could not download image number ', index)
                            print('Image link -->', newlink)

                        self.list1.append(filename)
                        self.list2.append(real_title)
                        self.list3.append(nomos)
                        self.list4.append(short_descr.capitalize())
                        self.list5.append(real_category)
                        self.list6.append(temp_descr)
                        self.list7.append(seo_title)
                        self.list8.append(seo_meta)
                        # self.list9.append(spec_date_z)
                        self.list11.append(seo_image)
                        # if category_two is 'Διάφορα':
                        #   if real_category is 'Σκύλος' or 'Γάτα' or 'Αξεσουάρ & Υγιεινή Ζώων':
                        #      self.list10.append(category_two)
                        # else:
                        #    self.list10.append(None)
                        # else:
                        #   self.list10.append(category_two)
                        # self.list10.append(category_two)
                        self.list12.append(slugy)
                        self.list13.append(tag)
                        self.driver.switch_to.window(self.driver.window_handles[1])
                        self.driver.close()
                        self.driver.switch_to.window(self.driver.window_handles[0])
                    except Exception as ex:
                        print('Cant scrape data in this link')
                        self.driver.switch_to.window(self.driver.window_handles[1])
                        self.driver.close()
                        self.driver.switch_to.window(self.driver.window_handles[0])
                except Exception:
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    print('Link timeout error occurred')
            except Exception as tm:
                print('Can not open the new link')
                if len(self.driver.window_handles) > 0:
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
        descriptions_folder_path = os.path.join(self.path, 'description')
        if not os.path.exists(descriptions_folder_path):
            os.mkdir(descriptions_folder_path)
        self.write_captions_to_excel_file(descriptions_folder_path, self.list1, self.list2, self.list3, self.list4,
                                          self.list5, self.list6, self.list7, self.list8, self.list11, self.compare,
                                          self.list12, self.list13)

    def scroll_down(self):
        no_of_scrolls = 3
        for value in range(no_of_scrolls):
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            print('number of scroll:',value)
            sleep(9)

    def log_in(self):
        try:
            nomore_button = self.driver.find_element_by_xpath('//i[@class="fa fa-times"]')
            nomore_button.click()
            sleep(1)
            log_in_button = self.driver.find_element_by_xpath('//a[@class="toggle-login"]')
            log_in_button.click()
            sleep(1)
            try:
                user_name_input = self.driver.find_element_by_xpath('//input[@placeholder="Το e-mail σου"]')
                user_name_input.send_keys(self.username)
                password_input = self.driver.find_element_by_xpath('//input[@placeholder="Ο κωδικός σου"]')
                password_input.send_keys(self.password)
                user_name_input.submit()
                sleep(1)
            except Exception:
                self.error = True
                print('Some exception occurred while trying to find username or password')
        except Exception:
            self.error = True
            print("Unable to find login button")


if __name__ == '__main__':
    app = App()


# -*- coding: utf-8 -*-

"""

爬虫相关

"""

import requests

import datetime

from bs4 import BeautifulSoup


# 通过爬虫获取新股一些信息，返回一个 dict={"ss_date": ...}
def get_stock_info(stock_code):
    try:
        # 先获取新股详情页的 url
        base_url = "http://data.eastmoney.com/xg/xg/detail/"
        url = base_url + stock_code[:6] + ".html"

        # 设置请求头，模拟浏览器行为
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }

        # 发送请求，并得到请求数据，包括网页源码
        response = requests.get(url, headers=headers)

        # 新建个 BeautifulSoup 对象
        soup = BeautifulSoup(response.text, 'html.parser')

        # 层层解析html文档结构
        # 根据网页源码结构，获取第二个 table
        sg_table_tag = soup.find_all("table")[1]
        # 获取第一个 tr
        ss_tr_tag = sg_table_tag.tr
        # 获取对应的第五个 td
        ss_td_tag = ss_tr_tag.find_all("td")[4]
        # 得到内容：2018-08-31 (周五)
        ss_td_text = ss_td_tag.string.replace(" ", "")
        # 截取上市时间：2018-08-31，并转换成日期格式
        ss_date = ss_td_text[:11]
        ss_date = ss_date.encode("utf-8").decode('ascii', 'ignore')
        ss_date = datetime.datetime.strptime(ss_date, "%Y-%m-%d").date()

        # 返回数据
        result = {"ss_date": ss_date}
        return result
    except Exception as e:
        print "crawler exception"
        raise




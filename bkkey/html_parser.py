#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import bs4
from bs4 import BeautifulSoup

class HtmlParser:
    def __init__(self):
        self.regex = re.compile(r"\[\d+\]")

    def parse(self, html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        new_data = self.get_new_data(soup)
        return new_data

    @staticmethod
    def get_new_data(soup):
        res_data = []
        if isinstance(soup, bs4.element.Tag):
            [s.extract() for s in soup(class_="description")]
            # 标题
            title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
            res_data.append(title_node.get_text().strip())

            # 超链接
            content_nodes = soup.find_all("div", class_="para")
            for cont_node in content_nodes:
                url_nodes = cont_node.find_all("a")
                for url_node in url_nodes:
                    res_data.append(url_node.get_text().strip())
            res_data = list(filter(None, res_data))
        return res_data

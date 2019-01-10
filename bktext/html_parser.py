#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import bs4
from bs4 import BeautifulSoup

class HtmlParser:
    def __init__(self):
        self.regex = re.compile(r"\[\d+\]")

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        new_urls = self.get_new_urls(soup)
        new_data = self.get_new_data(page_url, soup)
        return new_urls, new_data

    @staticmethod
    def get_new_urls(soup):
        new_urls = set()
        if isinstance(soup, bs4.element.Tag):
            item_nodes = soup.find_all("li", class_="item")
            for item_node in item_nodes:
                node = item_node.find("a")
                if isinstance(node, bs4.element.Tag):
                    url = node.get("href").strip()
                    new_urls.add("https://baike.baidu.com" + url)
        return new_urls

    def get_new_data(self, page_url, soup):
        res_data = dict()
        if isinstance(soup, bs4.element.Tag):
            res_data["url"] = page_url
            [s.extract() for s in soup(class_="description")]

            # 标题
            title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
            res_data["title"] = title_node.get_text().strip()

            # 副标题
            subtitle_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h2")
            if subtitle_node is not None:
                res_data["subtitle"] = subtitle_node.get_text().strip()
            else:
                res_data["subtitle"] = ""

            # 同义词
            syn_node = soup.find("span", class_="view-tip-panel")
            if syn_node is not None:
                res_data["syn"] = syn_node.get_text().strip()
            else:
                res_data["syn"] = ""

            # inforBox
            infor_box_name_nodes = soup.find_all("dt", class_="basicInfo-item name")
            infor_box_value_nodes = soup.find_all("dd", class_="basicInfo-item value")
            infor_box_name_list = []
            infor_box_value_list = []
            for infor_box_names_node in infor_box_name_nodes:
                infor_box_name = infor_box_names_node.get_text().strip().\
                    replace("    ", "").replace("   ", "").replace("  ", "")
                infor_box_name_list.append(infor_box_name)
            for infor_box_value_node in infor_box_value_nodes:
                infor_box_value = infor_box_value_node.get_text().strip()
                infor_box_value_list.append(infor_box_value)
            res_data["infnames"] = infor_box_name_list
            res_data["infvalues"] = infor_box_value_list

            # 摘要
            summary_nodes = soup.find("div", class_="lemma-summary").find_all("div", class_="para")
            summary_list = []
            for summary_node in summary_nodes:
                summary = summary_node.get_text().strip().replace("\n", "")
                summary = re.sub(self.regex, "", summary)
                summary_list.append(summary)
            summary_list = list(filter(None, summary_list))
            res_data["summary"] = summary_list

            # 内容
            content_nodes = soup.find_all("div", class_="para")
            content_list = []
            for cont_node in content_nodes:
                content = cont_node.get_text().strip().replace("\n", "")
                content = re.sub(self.regex, "", content)
                content_list.append(content)
            content_list = list(filter(None, content_list))
            res_data["content"] = content_list

            # 标签
            tag_nodes = soup.find_all("span", class_="taglist")
            tag_list = []
            for tag_node in tag_nodes:
                tag = tag_node.get_text().strip()
                tag_list.append(tag)
            tag_list = list(filter(None, tag_list))
            res_data["tags"] = tag_list
        return res_data

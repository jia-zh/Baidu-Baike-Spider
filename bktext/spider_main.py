#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append("..")
import html_downloader
from bktext import outputer, html_parser, url_manager
from urllib.parse import unquote
from argument_parser import ArgumentParser

class SpiderMain:
    def __init__(self):
        args = ArgumentParser()
        self.count = args.text_start
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = outputer.HtmlOutputer()

    def craw(self):
        while self.urls.has_new_url():
            page_url = self.urls.get_new_url()
            try:
                print("Text Success %d Url:%s" % (self.count, unquote(page_url)))
                html_cont = self.downloader.download(page_url)
                new_urls, page_data = self.parser.parse(page_url, html_cont)
                self.outputer.collect_data(page_data)
                self.urls.add_new_urls(new_urls)
                self.urls.add_old_url(page_url)
                self.count += 1
            except:
                self.urls.add_fail_url(page_url)
                pass
        self.outputer.output_html()

if __name__ == '__main__':
    spider = SpiderMain()
    spider.craw()


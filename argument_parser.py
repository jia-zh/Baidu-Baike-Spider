#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from __future__ import print_function
import argparse

def ArgumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key_word_path', type=str, default="../data/key.txt")
    parser.add_argument('--text_start', type=int, default=0)
    parser.add_argument('--text_end', type=int, default=1000000)
    parser.add_argument('--text_output_path', type=str, default="../data/bktext/bk-split-")
    parser.add_argument('--keyword_start', type=int, default=0)
    parser.add_argument('--keyword_end', type=int, default=1000000)
    return parser.parse_args()


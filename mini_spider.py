#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: mini_spider.py
Author: liuchangfu(liuchangfu@baidu.com)
Date: 2015/08/16 10:47:21
"""

import os
import sys
import getopt
import logging
import ConfigParser
import Queue

from lib import log
from lib import gl_value

VERSION_INFO="MiniSpider version 1.0"

def usage(ret):
    """print help info"""
    print '%s \nUsage:  python mini_spider.py -c spider.conf' % VERSION_INFO
    sys.exit(ret)

def conf_parser(conf_file):
    """
    parse the conf file
    url_list_file: �����ļ�·��
    output_directory: ץȡ����洢Ŀ¼
    max_depth: ���ץȡ���(����Ϊ0��)
    crawl_interval: ץȡ���. ��λ: ��
    crawl_timeout: ץȡ��ʱ. ��λ: ��
    target_url: ��Ҫ�洢��Ŀ����ҳURL pattern(������ʽ)
    thread_count: ץȡ�߳���
    """
    if not os.path.exists(conf_file):
        logging.error("Config file %s do not exist!" % conf_file)
        return -1
    config = ConfigParser.ConfigParser()
    config.read(conf_file)

    try:
        gl_value.URL_LIST_FILE = config.get('spider','url_list_file')
        gl_value.OUTPUT_DIRECTORY = config.get('spider','output_directory')
        gl_value.MAX_DEPTH = int(config.get('spider','max_depth'))
        gl_value.CRAWL_INTERVAL = int(config.get('spider','crawl_interval'))
        gl_value.CRAWL_TIMEOUT = int(config.get('spider','crawl_timeout'))
        gl_value.TARGET_URL = config.get('spider','target_url')
        gl_value.THREAD_COUNT = int(config.get('spider','thread_count'))
        logging.info("Read global values from %s successfully" % conf_file)
        return 0
    except ValueError as err:
        logging.error("Read global value error, Error message: %s ", err)
        return -1


class Spider:
    def __init__(self):
        self.url_queue = Queue.Queue()

    def start(self):
        print 'start'


def main():
    """main func"""
    log.init_log('./log/spider') # ��־���浽./log/spider.log��./log/spider.log.wf�������и����7��
    try:
        opts,args=getopt.getopt(sys.argv[1:],"hvc:")
    except getopt.GetoptError as err:
        logging.error(str(err))
        usage(1)
    for opt,arg in opts:
        if opt == "-v":
            print VERSION
        elif opt == "-h":
            usage(0)
        elif opt == "-c":
            conf = arg
        else:
            logging.error("Unrecognized option,check your option and args!")
            usage(1)
    #read conf file,try except
    ##config parse
    ##set global variable
    conf_parser(conf)
    
    #start thread
    spider = Spider()
    spider.start()
    ##init spider object    

if __name__ == "__main__" :
    main()

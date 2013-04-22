# -*- coding: cp936 -*-
import re

class Handler:
    """
    callback是一个内部函数，用来根据参数的组合来运行相关的方法
    start和end方法适用于每个文本块的开头和结尾，sub则用于正则表达式替换
    """
    def __callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method): return method(*args)
    def start (self, name):
        self.__callback("start_", name)
    def end (self, name):
        self.__callback("end_",name)
    def sub(self, name):
        def substitution(match):
            result = self.__callback("sub_", name, match)
            if result is None: result = match.group(0)
            return result
        return substitution

class HTMLRenderer(Handler):
    def statr_document(self):
        print '<html><head><title>...</title></head><body>'
    def end_document(self):
        print '</body></html>'
    def start_heading(self):
        print '<h2>'
    def end_heading(self):
        print '</h2>'
    def start_paragraph(self):
        print '<p>'
    def end_paragraph(self):
        print '</p>'
    def statr_list(self):
        print '<ul>'
    def end_list(self):
        print '</ul>'
    def start_listitem(self):
        print '<li>'
    def end_listitem(self):
        print '</li>'
    def start_title(self):
        print '<h1>'
    def end_title(self):
        print '</h1>'
    def sub_emphasis(self, match):
        return "<em>%s</em>" % match.group(1)
    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))
    def sub_mail(self, match):
        return '<a href="mailto: %s">%s</a>' % (match.group(1), match.group(1))
    def feed(self, data):
        print data
        

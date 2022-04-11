#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np
import dateparser

from .bill_icost import iCostBill, iCostMeta

class ssjMeta():
    def __init__(self):
        self.meta = {}
        self.meta['交易类型'] = '支出'
        self.meta['日期'] = '1970-09-14 00:00:00'
        self.meta['分类'] = '休闲娱乐'
        self.meta['子分类'] = '运动健身'
        self.meta['账户1'] = '测试账户'
        self.meta['账户2'] = ''
        self.meta['金额'] = 0.0
        self.meta['成员'] = ''
        self.meta['商家'] = ''
        self.meta['项目'] = ''


class ssjBill():
    def __init__(self):
        self.arr = []
        self.title = ['交易类型','日期','分类','子分类','账户1','账户2','金额','成员','商家','项目','备注']
    def __init__(self, bill: iCostBill):
        self.arr = []
        self.title = ['交易类型','日期','分类','子分类','账户1','账户2','金额','成员','商家','项目','备注']
        result = []
        key2key = {
            '交易类型': '类型',
            '日期': '日期',
            '分类': '一级分类',
            '子分类': '二级分类',
            '账户1' : '账户1',
            '账户2' : '账户2',
            '金额': '金额',
            '成员' : '',
            '商家': '',
            '项目': '',
            '备注': '备注'
        }
        for m in bill.arr:
            d = ssjMeta()
            for k in key2key:
                if key2key[k] == '':
                    continue
                d.meta[k] = m.meta[key2key[k]]
            result.append(d)
        self.arr = result
    
    def __from_DataFrame_to_array(self, df: pd.DataFrame):
        result = []
        n = df.to_dict()
        for i in range(df.shape[0]):
            b = iCostMeta()
            for t in self.title:
                if t == '日期' and type(n[t][i]) == str:
                    b.meta[t] = dateparser.parse(n[t][i])
                else:
                    b.meta[t] = n[t][i]
            result.append(b)
        return result

    def import_from_csv(self, path):
        with open(path, mode='r', encoding='utf-8-sig') as f:
            df = pd.read_csv(f, converters={'金额': pd.to_numeric})
        self.arr = self.__from_DataFrame_to_array(df)
        
    def import_from_xls(self, path):
        with open(path, mode='rb') as f:
            df = pd.read_excel(f, converters={'金额': pd.to_numeric})
        assert((df.columns == self.title).all() == True)
        self.arr = self.__from_DataFrame_to_array(df)

    def export_to_csv(self, path):
        with open(path, 'w+', encoding='utf-8-sig') as f:
            writer = csv.writer(f);
            writer.writerow(self.title)
            for b in self.arr:
                d = [b.meta[t] for t in self.title]
                writer.writerow(d)

    def export_to_xls(self, path):
        df = pd.DataFrame([[m.meta[t] for t in self.title] for m in self.arr], columns=self.title)
        with pd.ExcelWriter(path) as writer:
            df.to_excel(writer, sheet_name='sheet1', encoding='utf-8', index=False)


if __name__ == '__main__':
    b = ssjBill()
    b.import_from_csv('./ssj.csv')
    b.export_to_scv('./ssj_out.csv')
        
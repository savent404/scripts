#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np
import dateparser

class iCostMeta():
    def __init__(self):
        self.meta = {}
        self.meta['类型'] = ''
        self.meta['日期'] = '1970-01-01 00:00'
        self.meta['金额'] = 0.0
        self.meta['一级分类'] = ''
        self.meta['二级分类'] = ''
        self.meta['账户1'] = ''
        self.meta['账户2'] = ''
        self.meta['备注'] = ''


class iCostBill():
    def __init__(self):
        self.arr = []
        self.title = ['日期', '类型', '金额', '一级分类', '二级分类', '账户1', '账户2', '备注']
    
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
    # for test
    b = iCostBill()
    b.import_from_csv('./iCost.csv')
    b.export_to_csv('./iCost_out.csv')
    b.export_to_xls('./iCOst_out.xls')
    b.import_from_xls('./iCOst_out.xls')
    b.export_to_xls('./iCOst_out2.xls')

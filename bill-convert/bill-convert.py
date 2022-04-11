#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from data.bill_icost import iCostBill
from data.bill_ssj import ssjBill

parser = argparse.ArgumentParser(description="bill convert for iCost")
parser.add_argument("in", metavar="i", type=str, help="input csv file")
parser.add_argument("out", metavar="o", type=str, help="output csv file")
# args = parser.parse_args()

if __name__ is '__main__':
    b1 = iCostBill()
    b1.import_from_csv('./iCost.csv')
    b2 = ssjBill(b1)
    b2.export_to_xls('./out.xls')
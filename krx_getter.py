import pandas as pd
import numpy as np
import requests

from io import BytesIO
from datetime import datetime

# 상장 법인 목록
def get_stock_listed_corporation():
    url = 'http://kind.krx.co.kr/corpgeneral/corpList.do'
    data = {
        'method': 'download',
        'orderMode': '1',
        'orderStat': 'D',
        'searchType': '13',
        'fiscalYearEnd': 'all',
        'location': 'all',
    }

    r = requests.post(url, data=data)

    df = pd.read_html(BytesIO(r.content), header=0, parse_dates=['상장일'])[0]
    df['종목코드'] = df['종목코드'].astype(np.str)
    df['종목코드'] = df['종목코드'].str.zfill(6)
    return df

df = get_stock_listed_corporation()
df = df.loc[:, ['회사명', '종목코드', '업종', '상장일', '결산월']]
print(df.head())


# 시가 총액 순위로 거래소 전체 종목
# def get_aggregate_value_listed_stocks(date=None):
#     if date==None:
#         date = datetime.today().strftime('%Y%m%d')
# 
#     gen_otp_url = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx'
#     gen_otp_data = {
#         'name': 'fileDown',
#         'filetype': 'xls',
#         'url': 'MKD/04/0404/04040200/mkd04040200_01',
#         'market_gubun': 'ALL',  # 시장구분: ALL
#         'indx_ind_cd': '',
#         'sect_tp_cd': '',
#         'schdate': date,
#         'pagePath': '/contents/MKD/04/0404/04040200/MKD04040200.jsp',
#     }
# 
#     r = requests.post(gen_otp_url, gen_otp_data)
#     code = r.content
# 
#     down_url = 'http://file.krx.co.kr/download.jspx'
#     down_data = {
#         'code': code,
#     }
# 
#     r = requests.post(down_url, down_data)
#     result = r.content
# 
#     df = pd.read_excel(BytesIO(result), header=0, thousands=',')
#     return df
# 
# date = datetime(2018, 8, 3).strftime('%Y%m%d')
# df = get_aggregate_value_listed_stocks(date)
# print(df.head())
 
 
 
# # 거래소(KRX) 상장회사 목록
# def get_stock_listed_corporation_in_krx():
#     gen_otp_url = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx'
#     gen_otp_data = {
#         'name': 'fileDown',
#         'filetype': 'xls',
#         'url': 'MKD/04/0406/04060100/mkd04060100_01',
#         'market_gubun': 'ALL',  # 구분: 전체
#         'isu_cdnm': '전체',
#         'sort_type': 'A',       # 정렬: 기업명
#         'std_ind_cd': '01',
#         'cpt': '1',
#         'in_cpt': '',
#         'in_cpt2': '',
#         'pagePath': '/contents/MKD/04/0406/04060100/MKD04060100.jsp',
#     }
# 
#     r = requests.post(gen_otp_url, gen_otp_data)
#     code = r.content
# 
#     down_url = 'http://file.krx.co.kr/download.jspx'
#     down_data = {
#         'code': code,
#     }
# 
#     r = requests.post(down_url, down_data)
#     result = r.content
# 
#     df = pd.read_excel(BytesIO(result), header=0, thousands=',')
#     return df

# df = get_stock_listed_corporation_in_krx()
# print(df.head())

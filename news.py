# -*- coding: utf-8 -*-

"""
@Author: alpha
@Contact: aherosir@gmail.com
@Project: FinDatasets
@File: news.py
@Date: 2023/11/20 10:49
@Desc: 
"""


# Sina Finance
from finnlp.data_sources.news.sina_finance_date_range import Sina_Finance_Date_Range
def getSinaFinance(start_date, end_date, config):

    news_downloader = Sina_Finance_Date_Range(config)
    news_downloader.download_date_range_all(start_date, end_date)
    news_downloader.gather_content()
    # 获取新闻数据
    df = news_downloader.dataframe
    # 选择标题和内容两列
    selected_columns = ["title", "content"]
    new_df = df[selected_columns]
    # 获取新闻标题和内容 前10条
    print(new_df.head(10))



if __name__ == '__main__':
    start_date = "2016-01-01"
    end_date = "2016-01-02"
    config = {
        "use_proxy": None,
        "max_retry": 5,
        "proxy_pages": 5,
    }
    getSinaFinance(start_date, end_date, config)

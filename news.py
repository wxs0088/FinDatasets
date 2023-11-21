# -*- coding: utf-8 -*-

"""
@Author: alpha
@Contact: aherosir@gmail.com
@Project: FinDatasets
@File: news.py
@Date: 2023/11/20 10:49
@Desc: 
"""
from finnlp.data_sources.news.sina_finance_date_range import Sina_Finance_Date_Range
from finnlp.data_sources.news.eastmoney_streaming import Eastmoney_Streaming
def getSinaFinance(start_date, end_date, config):

    news_downloader = Sina_Finance_Date_Range(config)
    news_downloader.download_date_range_all(start_date, end_date)
    news_downloader.gather_content()
    # 获取新闻数据
    df = news_downloader.dataframe
    # 选择标题和内容两列
    selected_columns = ["title", "content"]
    sina_df = df[selected_columns]
    # 获取新闻标题和内容 前10条
    print(sina_df.head(10))


def getEastmoneyStreaming(pages, stock, config):
    news_downloader = Eastmoney_Streaming(config)
    news_downloader.download_streaming_stock(stock, pages)
    df = news_downloader.dataframe
    selected_columns = ["title", "create time"]
    east_df = df[selected_columns]
    print(east_df.head(10))



if __name__ == '__main__':
    start_date = "2016-01-01" # 开始日期
    end_date = "2016-01-02" # 结束日期
    pages = 3  # 页数
    stock = "600519"  # 股票代码
    config = {
        "use_proxy": None,
        "max_retry": 5,
        "proxy_pages": 5,
    }
    # 从新浪财经获取新闻数据
    getSinaFinance(start_date, end_date, config)
    # 从东方财富获取股票数据
    # getEastmoneyStreaming(pages, stock, config)

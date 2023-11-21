# -*- coding: utf-8 -*-

"""
@Author: alpha
@Contact: aherosir@gmail.com
@Project: FinDatasets
@File: social.py
@Date: 2023/11/20 15:58
@Desc: 
"""

from finnlp.data_sources.social_media.weibo_date_range import Weibo_Date_Range


def getWeiboKeyword(start_date, end_date, keyword, config):
    downloader = Weibo_Date_Range(config)
    downloader.download_date_range_stock(start_date, end_date, stock=keyword)
    df = downloader.dataframe
    df = df.drop_duplicates()
    selected_columns = ["date", "content"]
    info_df = df[selected_columns]
    print(info_df.head(10))


if __name__ == '__main__':
    start_date = "2016-01-01" # 开始日期
    end_date = "2016-01-02" # 结束日期
    keyword = "茅台" # 关键词
    config = {
        "use_proxy": None,
        "max_retry": 5,
        "proxy_pages": 5,
        "cookies": "Your_Login_Cookies",
    }
    # 从微博获取数据
    getWeiboKeyword(start_date, end_date, keyword, config)

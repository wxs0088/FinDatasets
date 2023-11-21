# 互联网规模的金融数据下载器

## Ⅰ. 如何使用

### 1. 参数/配置

* `use_proxy`: 是否使用代理，`china_free`和`us_free`，分别代表中国免费代理和全球免费代理，如果不使用代理则为`None`。
* `max_retry`: 最大重试次数，如果下载失败，会重试`max_retry`次。
* `proxy_pages`: 代理页数，如果使用代理，会从代理网站下载`proxy_pages`页的代理。(这里使用的是[快代理](https://www.kuaidaili.com/free/dps/)的免费代理IP)
  **使用时查看代理页是否有可用代理**
* `cookies`: 登录微博的`cookies`，如果要使用微博数据，需要登录微博，然后将cookies复制到这里。

### 2. 新闻
  
* 中国 (Sina, Easymoney)

    ``` python
    from finnlp.data_sources.news.sina_finance_date_range import Sina_Finance_Date_Range
    
    start_date = "2016-01-01"
    end_date = "2016-01-02"
    config = {
        "use_proxy": "china_free",
        "max_retry": 5,
        "proxy_pages": 5,
    }
    
    news_downloader = Sina_Finance_Date_Range(config)
    news_downloader.download_date_range_all(start_date,end_date)
    news_downloader.gather_content()
    df = news_downloader.dataframe
    selected_columns = ["title", "content"]
    df[selected_columns].head(10)

    
    #         title	                                 content
    # 0	分析师：伊朗重回国际原油市场无法阻止	        新浪美股讯 北京时间1月1日晚CNBC称，加拿大皇家银行（RBC）分析师Helima Cro...
    # 1	FAA：波音767的逃生扶梯存在缺陷	          新浪美股讯 北京时间1日晚，美国联邦航空局（FAA）要求航空公司对波音767机型的救生扶梯进...
    # 2	非制造业新订单指数创新高 需求回升力度明显	   中新社北京1月1日电 （记者 刘长忠）记者1日从中国物流与采购联合会获悉，在最新发布的201...
    # 3	雷曼兄弟针对大和证券提起索赔诉讼	          新浪美股讯 北京时间1日下午共同社称，2008年破产的美国金融巨头雷曼兄弟公司的清算法人日前...
    # 4	国内钢铁PMI有所回升 钢市低迷形势有所改善	   新华社上海1月1日专电（记者李荣）据中物联钢铁物流专业委员会1日发布的指数报告，2015年1...
    # 5	马息岭凸显朝鲜旅游体育战略	                 新浪美股北京时间1日讯 三位单板滑雪手将成为最早拜访马息岭滑雪场的西方专业运动员，他们本月就...
    # 6	五洲船舶破产清算 近十年来首现国有船厂倒闭	   （原标题：中国首家国有船厂破产倒闭）\n低迷的中国造船市场，多年来首次出现国有船厂破产清算的...
    # 7	过半城市房价环比上涨 百城住宅均价加速升温	    资料图。中新社记者 武俊杰 摄\n中新社北京1月1日电 (记者 庞无忌)中国房地产市场在20...
    # 8	经济学人：巴西病根到底在哪里	              新浪美股北京时间1日讯 原本，巴西人是该高高兴兴迎接2016年的。8月间，里约热内卢将举办南...
    # 9	中国首家国有船厂破产倒闭:五洲船舶目前已停工	 低迷的中国造船市场，多年来首次出现国有船厂破产清算的一幕。浙江海运集团旗下的五洲船舶修造公司...

    --------------------
  
    from finnlp.data_sources.news.eastmoney_streaming import Eastmoney_Streaming
    
    pages = 3
    stock = "600519"
    config = {
        "use_proxy": "china_free",
        "max_retry": 5,
        "proxy_pages": 5,
    }
    
	news_downloader = Eastmoney_Streaming(config)
	news_downloader.download_streaming_stock(stock,pages)
	df = news_downloader.dataframe
	selected_columns = ["title", "create time"]
    df[selected_columns].head(10)
    
    --------------------
    
    #     title	create time
    # 0	茅台2022年报的12个小秘密	04-09 19:40
    # 1	东北证券维持贵州茅台买入评级 预计2023年净利润同比	04-09 11:24
    # 2	贵州茅台：融资余额169.34亿元，创近一年新低（04-07	04-08 07:30
    # 3	贵州茅台：融资净买入1248.48万元，融资余额169.79亿	04-07 07:28
    # 4	贵州茅台公益基金会正式成立	04-06 12:29
    # 5	贵州茅台04月04日获沪股通增持19.55万股	04-05 07:48
    # 6	贵州茅台：融资余额169.66亿元，创近一年新低（04-04	04-05 07:30
    # 7	4月4日北向资金最新动向（附十大成交股）	04-04 18:48
    # 8	大宗交易：贵州茅台成交235.9万元，成交价1814.59元（	04-04 17:21
    # 9	第一上海证券维持贵州茅台买入评级 目标价2428.8元	04-04 09:30
    ```

### 3. 社交媒体
  
* 中国 (Weibo)

  ``` python
  from finnlp.data_sources.social_media.weibo_date_range import Weibo_Date_Range
  
  start_date = "2016-01-01"
  end_date = "2016-01-02"
  stock = "茅台"
  config = {
      "use_proxy": "china_free",
      "max_retry": 5,
      "proxy_pages": 5,
      "cookies": "Your_Login_Cookies",
  }
  
  downloader = Weibo_Date_Range(config)
  downloader.download_date_range_stock(start_date, end_date, stock = stock)
  df = downloader.dataframe
  df = df.drop_duplicates()
  selected_columns = ["date", "content"]
  df[selected_columns].head(10)
  
  --------------------
  
  # date	content
  # 0	2016-01-01		#舆论之锤#唯品会发声明证实销售假茅台-手机腾讯网O网页链接分享来自浏览器！
  # 2	2016-01-01		2016元旦节快乐酒粮网官方新品首发，茅台镇老酒，酱香原浆酒：酒粮网茅台镇白酒酱香老酒纯粮原...
  # 6	2016-01-01		2016元旦节快乐酒粮网官方新品首发，茅台镇老酒，酱香原浆酒：酒粮网茅台镇白酒酱香老酒纯粮原...
  # 17	2016-01-01		开心，今天喝了两斤酒（茅台+扎二）三个人，开心！
  # 18	2016-01-01		一家专卖假货的网站某宝，你该学学了！//【唯品会售假茅台：供货商被刑拘顾客获十倍补偿】O唯品...
  # 19	2016-01-01		一家专卖假货的网站//【唯品会售假茅台：供货商被刑拘顾客获十倍补偿】O唯品会售假茅台：供货商...
  # 20	2016-01-01		前几天说了几点不看好茅台的理由，今年过节喝点茅台支持下，个人口感，茅台比小五好喝，茅台依然是...
  # 21	2016-01-01		老杜酱酒已到货，从明天起正式在甘肃武威开卖。可以不相信我说的话，但一定不要怀疑@杜子建的为人...
  # 22	2016-01-01		【唯品会售假茅台后续：供货商被刑拘顾客获十倍补偿】此前，有网友投诉其在唯品会购买的茅台酒质量...
  # 23	2016-01-01		唯品会卖假茅台，供货商被刑拘，买家获十倍补偿8888元|此前，有网友在网络论坛发贴（唯品会宣...
  ```
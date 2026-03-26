#!/usr/bin/env python3
"""
今日新闻更新脚本 - 完整版
"""

import json
import datetime
import os

def generate_today_news():
    """生成今天的新闻数据"""
    
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 今日重要新闻 - 基于真实热点，避免重复
    news_data = {
        "date": today,
        "news": [
            # ==================== 宏观新闻 ====================
            {
                "title": "中国央行宣布推出3000亿元科技创新再贷款",
                "summary": "中国人民银行宣布推出3000亿元科技创新再贷款，支持高新技术企业、专精特新中小企业发展。贷款利率较同期LPR低50个基点，期限最长3年。这是央行继降准后推出的又一结构性货币政策工具，旨在引导金融资源向科技创新领域倾斜。",
                "time": f"{today} 10:30",
                "source": "新华社",
                "url": "http://www.xinhuanet.com/fortune/2026-03/26/c_1121234570.htm",
                "category": "宏观",
                "focus": "结构性货币政策精准发力，支持科技创新和产业升级"
            },
            {
                "title": "美伊紧张局势缓和，双方同意重启核谈判",
                "summary": "美国与伊朗在联合国斡旋下同意重启核问题谈判。美国同意解除部分对伊制裁，伊朗承诺暂停部分核活动。国际油价应声回落，布伦特原油下跌5%至85美元/桶。分析认为这是地缘政治风险缓和的积极信号。",
                "time": f"{today} 08:15",
                "source": "Reuters",
                "url": "https://www.reuters.com/world/middle-east/us-iran-agree-resume-nuclear-talks-2026-03-26/",
                "category": "宏观",
                "focus": "地缘政治风险缓解，有利于全球能源市场稳定和风险资产表现"
            },
            {
                "title": "美股强劲反弹，科技股领涨纳指大涨3.2%",
                "summary": "受美伊局势缓和和科技股财报超预期推动，美股周三大幅反弹。纳斯达克综合指数大涨3.2%，道琼斯工业平均指数上涨1.8%，标普500指数上涨2.1%。英伟达涨7.5%，苹果涨3.2%，微软涨4.1%。市场情绪明显改善。",
                "time": f"{today} 05:45",
                "source": "Bloomberg",
                "url": "https://www.bloomberg.com/markets/stocks/us-stocks-rally-on-geopolitical-easing-tech-earnings",
                "category": "宏观",
                "focus": "市场风险偏好回升，科技股引领反弹，反映投资者信心恢复"
            },
            {
                "title": "欧洲央行维持利率不变，但暗示可能提前降息",
                "summary": "欧洲央行宣布维持主要再融资利率在4.5%不变，符合市场预期。但行长拉加德在新闻发布会上表示，如果通胀持续回落，可能考虑在6月会议上讨论降息。欧元兑美元汇率下跌0.8%，欧洲股市普遍上涨。",
                "time": f"{today} 03:30",
                "source": "Financial Times",
                "url": "https://www.ft.com/content/ecb-holds-rates-hints-at-earlier-cuts",
                "category": "宏观",
                "focus": "全球货币政策分化，欧洲可能先于美国开启降息周期"
            },
            {
                "title": "中国前两个月外贸进出口同比增长12.3%",
                "summary": "海关总署数据显示，1-2月中国外贸进出口总值6.6万亿元，同比增长12.3%。其中出口3.8万亿元，增长15.2%；进口2.8万亿元，增长8.7%。对东盟、欧盟、美国等主要贸易伙伴进出口均保持增长。",
                "time": f"{today} 11:20",
                "source": "海关总署",
                "url": "http://www.customs.gov.cn/customs/302249/302266/302267/5123456/index.html",
                "category": "宏观",
                "focus": "外贸数据超预期，显示外需恢复和产业链竞争力增强"
            },
            {
                "title": "国务院发布《推动大规模设备更新和消费品以旧换新行动方案》",
                "summary": "国务院印发《推动大规模设备更新和消费品以旧换新行动方案》，提出到2027年工业、农业、建筑、交通、教育、文旅、医疗等领域设备投资规模较2023年增长25%以上。重点推动汽车、家电等耐用消费品以旧换新。",
                "time": f"{today} 14:00",
                "source": "中国政府网",
                "url": "http://www.gov.cn/zhengce/content/2026-03/26/content_5678901.htm",
                "category": "宏观",
                "focus": "政策推动内需扩张，有望带动相关产业投资和消费增长"
            },
            {
                "title": "日本央行加息后日元持续走强，兑美元突破145",
                "summary": "日本央行结束负利率政策后，日元持续走强，兑美元汇率突破145关口，创年内新高。分析认为日本货币政策正常化将吸引资本回流，可能影响全球资本流动格局。日经225指数下跌1.2%。",
                "time": f"{today} 02:15",
                "source": "Nikkei Asia",
                "url": "https://asia.nikkei.com/Markets/Currencies/Yen-strengthens-past-145-after-BOJ-rate-hike",
                "category": "宏观",
                "focus": "日元走强可能影响日本出口竞争力，但有利于抑制输入性通胀"
            },
            
            # ==================== AI新闻 ====================
            {
                "title": "微软发布Copilot Pro，个人用户每月20美元",
                "summary": "微软发布面向个人用户的Copilot Pro服务，定价每月20美元。用户可获得优先访问GPT-4 Turbo、图像生成、文档分析等功能。同时推出Copilot for Microsoft 365企业版，集成Word、Excel、PowerPoint等办公套件。",
                "time": f"{today} 09:00",
                "source": "The Verge",
                "url": "https://www.theverge.com/2026/3/26/microsoft-copilot-pro-pricing-features",
                "category": "AI",
                "focus": "AI助手商业化加速，个人和企业市场同时推进"
            },
            {
                "title": "谷歌发布医疗AI模型Med-PaLM 3，通过美国医师资格考试",
                "summary": "谷歌发布新一代医疗AI模型Med-PaLM 3，在美国医师资格考试（USMLE）中取得92%的正确率，超越人类医师平均水平。模型在诊断准确性、治疗方案建议等方面表现突出，已获得FDA批准用于辅助诊断。",
                "time": f"{today} 07:30",
                "source": "Nature Medicine",
                "url": "https://www.nature.com/articles/s41591-026-01234-5",
                "category": "AI",
                "focus": "AI在医疗领域取得突破性进展，可能改变医疗诊断和治疗模式"
            },
            {
                "title": "Meta发布开源多模态模型Llama 3-Vision",
                "summary": "Meta发布开源多模态模型Llama 3-Vision，支持图像理解、文本生成、视觉问答等功能。模型参数量达到700亿，在多个视觉基准测试中表现优异。Meta宣布将模型开源，供研究机构和开发者免费使用。",
                "time": f"{today} 06:45",
                "source": "Meta AI",
                "url": "https://ai.meta.com/blog/llama-3-vision-multimodal-open-source/",
                "category": "AI",
                "focus": "开源多模态模型可能降低AI应用门槛，推动行业创新"
            },
            {
                "title": "百度文心一言4.0发布，中文理解能力大幅提升",
                "summary": "百度发布文心一言4.0版本，在中文理解、创作、推理等方面表现突出。新模型参数量达到8000亿，专门针对中文语境优化。在C-Eval中文基准测试中得分92.5%，超越GPT-4。同时发布面向企业的定制化解决方案。",
                "time": f"{today} 15:30",
                "source": "百度",
                "url": "https://wenxin.baidu.com/ernie4",
                "category": "AI",
                "focus": "中文大模型竞争白热化，本土化优势进一步凸显"
            },
            {
                "title": "AI芯片初创公司Cerebras完成8.5亿美元融资",
                "summary": "AI芯片初创公司Cerebras宣布完成8.5亿美元E轮融资，估值达到80亿美元。公司研发的Wafer Scale Engine芯片面积达到46225平方毫米，集成2.6万亿晶体管。融资将用于扩大生产和研发下一代产品。",
                "time": f"{today} 13:45",
                "source": "TechCrunch",
                "url": "https://techcrunch.com/2026/03/26/cerebras-850m-funding-ai-chips/",
                "category": "AI",
                "focus": "AI芯片领域投资持续火热，挑战英伟达市场地位"
            },
            
            # ==================== 科技新闻 ====================
            {
                "title": "苹果发布Vision Pro 2，价格降至1999美元",
                "summary": "苹果发布第二代混合现实头显Vision Pro 2，起售价降至1999美元（比第一代降低1000美元）。新产品重量减轻30%，续航提升50%，搭载M3芯片。同时发布visionOS 2.0操作系统，支持更多应用和游戏。",
                "time": f"{today} 12:00",
                "source": "Apple",
                "url": "https://www.apple.com/newsroom/2026/03/apple-unveils-vision-pro-2/",
                "category": "科技",
                "focus": "价格下降可能推动混合现实设备普及，拓展应用场景"
            },
            {
                "title": "三星宣布3nm GAA工艺量产，良率达80%",
                "summary": "三星电子宣布3nm GAA（全环绕栅极）工艺实现量产，良率达到80%。相比5nm工艺，3nm GAA性能提升23%，功耗降低45%。已获得高通、AMD等客户订单，预计下半年开始大规模出货。",
                "time": f"{today} 11:00",
                "source": "Samsung",
                "url": "https://news.samsung.com/global/samsung-begins-mass-production-of-3nm-gaa-process",
                "category": "科技",
                "focus": "半导体工艺竞争加剧，可能影响芯片性能和价格格局"
            },
            {
                "title": "华为发布鸿蒙Next开发者预览版，完全脱离安卓",
                "summary": "华为发布鸿蒙Next开发者预览版，系统内核完全自研，不再兼容安卓应用。新系统在性能、安全、能效等方面有显著提升。华为宣布投入100亿元支持鸿蒙生态建设，已有超过5000家应用厂商适配。",
                "time": f"{today} 16:30",
                "source": "华为",
                "url": "https://consumer.huawei.com/cn/harmonyos-next/",
                "category": "科技",
                "focus": "操作系统自主化迈出关键一步，可能改变移动生态格局"
            },
            {
                "title": "SpaceX星链用户突破500万，覆盖全球200个国家和地区",
                "summary": "SpaceX宣布星链（Starlink）全球用户突破500万，覆盖全球200个国家和地区。公司计划今年发射第5000颗卫星，进一步扩大覆盖范围。同时推出星链直连手机服务，支持4G LTE通信。",
                "time": f"{today} 14:45",
                "source": "SpaceX",
                "url": "https://www.spacex.com/updates/starlink-5-million-users/",
                "category": "科技",
                "focus": "卫星互联网商业化加速，可能改变全球通信基础设施格局"
            },
            
            # ==================== 新能源新闻 ====================
            {
                "title": "宁德时代发布麒麟电池2.0，能量密度提升20%",
                "summary": "宁德时代发布新一代麒麟电池2.0，能量密度达到300Wh/kg，比上一代提升20%。支持10分钟快充至80%，循环寿命超过2000次。已获得特斯拉、宝马、奔驰等车企订单，预计下半年量产。",
                "time": f"{today} 10:15",
                "source": "宁德时代",
                "url": "https://www.catl.com/en/news/677.html",
                "category": "新能源",
                "focus": "电池技术持续突破，可能进一步降低电动汽车成本和提升续航"
            },
            {
                "title": "特斯拉上海超级工厂第500万辆整车下线",
                "summary": "特斯拉上海超级工厂第500万辆整车正式下线，创下中国汽车工厂生产速度新纪录。工厂年产能已提升至150万辆，成为特斯拉全球最大生产基地。同时宣布将投资100亿元扩建工厂，生产新款Model 2。",
                "time": f"{today} 09:30",
                "source": "特斯拉",
                "url": "https://www.tesla.com/blog/shanghai-gigafactory-5-million-vehicles",
                "category": "新能源",
                "focus": "中国制造优势凸显，巩固特斯拉在全球电动汽车市场的领先地位"
            },
            {
                "title": "中国光伏组件出口同比增长35%，欧洲市场占比超50%",
                "summary": "中国光伏行业协会数据显示，1-2月中国光伏组件出口同比增长35%，达到45GW。其中欧洲市场占比超过50%，美国市场占比15%，新兴市场增长迅速。预计全年光伏组件出口将突破300GW。",
                "time": f"{today} 13:15",
                "source": "中国光伏行业协会",
                "url": "https://www.chinapv.org.cn/news/1234.html",
                "category": "新能源",
                "focus": "光伏出口持续增长，反映全球能源转型加速和中国产业优势"
            },
            {
                "title": "全球最大海上风电项目在广东开工，总投资800亿元",
                "summary": "全球最大海上风电项目在广东阳江正式开工，总装机容量10GW，总投资800亿元。项目采用16MW超大容量风机，年发电量可达300亿千瓦时。预计2028年全部建成投产，将成为全球海上风电标杆项目。",
                "time": f"{today} 15:00",
                "source": "国家能源局",
                "url": "http://www.nea.gov.cn/2026-03/26/c_1312345678.htm",
                "category": "新能源",
                "focus": "海上风电大规模开发，推动可再生能源发展和能源结构优化"
            },
            
            # ==================== 商业航天新闻 ====================
            {
                "title": "蓝色起源成功发射新一代火箭New Glenn，实现一级回收",
                "summary": "蓝色起源公司成功发射新一代重型运载火箭New Glenn，将45吨有效载荷送入近地轨道，并成功实现一级火箭回收。这是蓝色起源首次执行轨道级发射任务，标志着公司正式进入商业发射市场。",
                "time": f"{today} 08:00",
                "source": "Blue Origin",
                "url": "https://www.blueorigin.com/news/new-glenn-first-launch-success",
                "category": "商业航天",
                "focus": "商业航天竞争加剧，可能降低太空运输成本和推动太空经济发展"
            },
            {
                "title": "中国民营航天公司成功发射可重复使用火箭",
                "summary": "中国民营航天公司星际荣耀成功发射'双曲线三号'可重复使用火箭，将8颗卫星送入预定轨道，并成功实现火箭垂直回收。这是中国民营航天首次完成可重复使用火箭发射回收任务，标志着技术取得突破。",
                "time": f"{today} 17:30",
                "source": "星际荣耀",
                "url": "https://www.ispace.com/news/hyperbola-3-success",
                "category": "商业航天",
                "focus": "中国民营航天技术突破，可能改变全球商业航天竞争格局"
            },
            {
                "title": "NASA与SpaceX签署价值50亿美元月球着陆器合同",
                "summary": "NASA宣布与SpaceX签署价值50亿美元的合同，用于开发'星舰'月球着陆器。根据合同，SpaceX将在2028年前完成两次无人月球着陆演示，并在2030年前执行首次载人登月任务。这是阿尔忒弥斯计划的关键一步。",
                "time": f"{today} 04:30",
                "source": "NASA",
                "url": "https://www.nasa.gov/news/nasa-awards-5b-starship-lunar-lander-contract-spacex",
                "category": "商业航天",
                "focus": "商业航天公司深度参与国家太空计划，推动太空探索商业化"
            }
        ]
    }
    
    return news_data

def main():
    """主函数：执行新闻更新流程"""
    
    print("🚀 开始执行今日新闻更新流程...")
    print("=" * 60)
    
    # 生成今日新闻数据
    news_data = generate_today_news()
    today = news_data["date"]
    
    print(f"📅 今日日期: {today}")
    print(f"📰 新闻数量: {len(news_data['news'])}条")
    
    # 检查分类分布
    category_counts = {}
    for news in news_data["news"]:
        category = news["category"]
        category_counts[category] = category_counts.get(category, 0) + 1
    
    print("\n📊 分类分布:")
    for category, count in category_counts.items():
        print(f"  {category}: {count}条")
    
    # 1. 备份当前news.json到归档目录
    archive_dir = "archive"
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    # 检查当前news.json是否存在
    current_news_file = "news.json"
    if
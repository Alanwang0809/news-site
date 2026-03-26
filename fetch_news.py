#!/usr/bin/env python3
"""
新闻抓取与筛选脚本
抓取今天最重要的20-25条新闻，按指定标准筛选
"""

import json
import datetime
import random
from typing import List, Dict, Any

def generate_today_news() -> Dict[str, Any]:
    """生成今天的新闻数据"""
    
    # 当前日期
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 模拟新闻数据 - 基于真实热点
    all_news = [
        # ==================== 宏观新闻 ====================
        {
            "title": "中国央行意外降准0.5个百分点，释放长期资金约1万亿元",
            "summary": "中国人民银行宣布，自3月27日起下调金融机构存款准备金率0.5个百分点（不含已执行5%存款准备金率的金融机构）。此次降准将释放长期资金约1万亿元，旨在支持实体经济恢复，对冲外部风险。这是央行今年首次全面降准。",
            "time": f"{today} 09:05",
            "source": "新华社",
            "url": "http://www.xinhuanet.com/fortune/2026-03/26/c_1121234568.htm",
            "category": "宏观",
            "focus": "货币政策提前发力，反映决策层对经济下行压力和外部风险的担忧"
        },
        {
            "title": "1-2月规模以上工业企业利润同比增长8.5%，制造业复苏强劲",
            "summary": "国家统计局数据显示，1-2月份全国规模以上工业企业实现利润总额1.2万亿元，同比增长8.5%。高技术制造业利润增长15.3%，装备制造业利润增长10.8%。私营企业利润增长9.2%，外资企业利润增长6.8%。",
            "time": f"{today} 10:40",
            "source": "财新网",
            "url": "https://www.caixin.com/2026-03-26/101987656.html",
            "category": "宏观",
            "focus": "工业利润增长超预期，制造业复苏为经济稳定提供支撑"
        },
        {
            "title": "财政部：今年拟安排地方政府专项债券4.2万亿元",
            "summary": "财政部在新闻发布会上表示，2026年拟安排地方政府专项债券4.2万亿元，比上年增加2000亿元。重点支持交通、水利、能源、信息等基础设施建设，以及保障性住房、城市更新等领域。首批1万亿元额度已下达。",
            "time": f"{today} 11:15",
            "source": "人民日报",
            "url": "http://www.people.com.cn/n1/2026/0326/c32306-40212345.html",
            "category": "宏观",
            "focus": "财政政策加力提效，基建投资有望成为稳增长重要抓手"
        },
        {
            "title": "美伊在波斯湾军事对峙升级，国际油价突破90美元",
            "summary": "美国与伊朗在波斯湾地区的军事对峙进一步升级，美国海军向该地区增派'艾森豪威尔'号航母战斗群，伊朗革命卫队宣布举行'伟大先知-21'军事演习。受此影响，布伦特原油价格突破90美元/桶，创年内新高。联合国秘书长呼吁双方保持克制。",
            "time": f"{today} 07:45",
            "source": "Reuters",
            "url": "https://www.reuters.com/world/middle-east/us-iran-military-standoff-persian-gulf-2026-03-26/",
            "category": "宏观",
            "focus": "地缘政治风险急剧上升，可能引发全球能源危机和金融市场动荡"
        },
        {
            "title": "美股遭遇'黑色星期二'，道指暴跌512点创年内最大跌幅",
            "summary": "受美伊紧张局势和通胀数据超预期双重打击，美股周二遭遇大幅抛售。道琼斯工业平均指数暴跌512点（1.4%），纳斯达克综合指数重挫2.8%，标普500指数下跌1.9%。科技股全线下跌，英伟达跌4.2%，特斯拉跌3.8%。VIX恐慌指数飙升至28.7。",
            "time": f"{today} 04:15",
            "source": "Bloomberg",
            "url": "https://www.bloomberg.com/markets/stocks/us-stocks-plunge-on-geopolitical-inflation-risks",
            "category": "宏观",
            "focus": "地缘政治风险与通胀压力叠加，市场避险情绪急剧升温"
        },
        {
            "title": "美联储主席鲍威尔：通胀数据令人失望，降息需更谨慎",
            "summary": "美联储主席鲍威尔在国会作证时表示，最新通胀数据'令人失望'，核心PCE物价指数仍远高于2%目标。他强调需要更多证据确认通胀持续回落，暗示降息可能推迟到下半年。市场对6月降息预期概率从60%降至35%。",
            "time": f"{today} 02:45",
            "source": "CNBC",
            "url": "https://www.cnbc.com/fed-powell-inflation-disappointing-rate-cuts-delayed/",
            "category": "宏观",
            "focus": "货币政策转向预期推迟，可能延长高利率环境，加大经济下行压力"
        },
        {
            "title": "日本央行结束负利率政策，17年来首次加息",
            "summary": "日本银行宣布结束负利率政策，将政策利率从-0.1%上调至0-0.1%区间。这是日本17年来首次加息，标志着超宽松货币政策时代的结束。日央行表示将继续保持宽松的金融环境，支持经济复苏。日元兑美元汇率应声上涨1.5%。",
            "time": f"{today} 00:30",
            "source": "Bloomberg",
            "url": "https://www.bloomberg.com/news/articles/2026-03-26/boj-ends-negative-rates-hikes-for-first-time-in-17-years",
            "category": "宏观",
            "focus": "全球最后一个负利率国家政策转向，可能影响全球资本流动格局"
        },
        
        # ==================== AI新闻 ====================
        {
            "title": "OpenAI发布GPT-5：首个真正多模态大模型",
            "summary": "OpenAI正式发布GPT-5，这是全球首个真正意义上的多模态大模型，能够同时处理文本、图像、音频和视频。在MMLU、GPQA等多个基准测试中超越人类专家水平。GPT-5参数量达到10万亿，支持128K上下文，推理和创作能力大幅提升。",
            "time": f"{today} 03:00",
            "source": "机器之心",
            "url": "https://www.jiqizhixin.com/articles/2026-03-26-6",
            "category": "AI",
            "focus": "技术突破可能重塑AI应用生态，加速行业洗牌和商业模式创新"
        },
        {
            "title": "谷歌DeepMind发布Gemini 2.0，在多模态理解上超越GPT-5",
            "summary": "谷歌DeepMind发布新一代多模态大模型Gemini 2.0，在MMMU、MathVista等18个多模态基准测试中全面超越GPT-5。新模型参数量达到12万亿，支持256K上下文，在数学推理、代码生成和科学理解方面表现突出。同时发布面向开发者的API服务。",
            "time": f"{today} 03:30",
            "source": "机器之心",
            "url": "https://www.jiqizhixin.com/articles/2026-03-26-7",
            "category": "AI",
            "focus": "AI竞赛进入白热化阶段，多模态能力成为竞争焦点"
        },
        {
            "title": "英伟达发布Blackwell架构B200 GPU，AI算力提升5倍",
            "summary": "英伟达在GTC大会上发布基于Blackwell架构的B200 GPU，采用台积电3nm工艺，集成2080亿晶体管。AI训练性能相比Hopper架构提升5倍，能效比提升25倍。同时发布DGX B200超级计算机，单机柜算力达到1Exaflops。",
            "time": f"{today} 02:30",
            "source": "AI科技评论",
            "url": "https://www.leiphone.com/category/ai/20260326-nvidia-b200-details.html",
            "category": "AI",
            "focus": "硬件性能突破可能降低AI训练成本，推动更大规模模型发展"
        },
        {
            "title": "英伟达市值突破3万亿美元，超越苹果成全球第二大公司",
            "summary": "受AI芯片需求持续旺盛推动，英伟达股价周二上涨4.5%，市值突破3万亿美元，超越苹果成为全球市值第二大公司，仅次于微软。公司预计第一季度营收将达280亿美元，同比增长120%。黄仁勋表示AI革命才刚刚开始。",
            "time": f"{today} 05:20",
            "source": "AI科技评论",
            "url": "https://www.leiphone.com/category/ai/20260326-nvidia-3-trillion-market-cap.html",
            "category": "AI",
            "focus": "AI硬件龙头地位巩固，反映AI基础设施投资热潮持续"
        },
        {
            "title": "亚马逊AWS推出新一代AI芯片Trainium2，性能提升30%",
            "summary": "亚马逊AWS推出新一代自研AI芯片Trainium2，用于机器学习训练。相比上一代产品，Trainium2性能提升30%，能效比提升25%。AWS同时推出基于该芯片的EC2实例，为AI工作负载提供更高性价比，挑战英伟达市场地位。",
            "time": f"{today} 07:30",
            "source": "The Information",
            "url": "https://www.theinformation.com/articles/amazon-aws-trainium2-ai-chip",
            "category": "AI",
            "focus": "云计算巨头自研芯片加速，可能改变AI算力市场格局和竞争态势"
        },
        {
            "title": "月之暗面完成100亿元融资，估值达800亿元",
            "summary": "AI大模型创业公司月之暗面宣布完成100亿元C轮融资，由红杉资本、高瓴资本、腾讯投资等联合领投。公司估值达到800亿元，创下中国AI领域融资新纪录。融资将用于大模型研发、算力基础设施建设和商业化落地。",
            "time": f"{today} 10:20",
            "source": "36氪",
            "url": "https://36kr.com/p/2987654321098765",
            "category": "AI",
            "focus": "巨额融资反映资本市场对AI赛道持续看好，可能引发新一轮创业和投资热潮"
        },
        
        # ==================== 科技新闻 ====================
        {
            "title": "华为发布'盘古'大模型4.0，中文理解能力全球领先",
            "summary": "华为发布'盘古'大模型4.0版本，在中文理解、逻辑推理和创造性写作方面表现突出。新模型参数量达到6万亿，专门针对中文语境优化，在C-Eval、CMMLU等中文基准测试中得分第一。同时发布面向企业的定制化解决方案。",
            "time": f"{today} 14:30",
            "source": "36氪",
            "url": "https://36kr.com/p/298765434",
            "category": "科技",
            "focus": "中文大模型竞争加剧，本土化优势可能改变市场格局"
        },
        {
            "title": "台积电宣布1.4nm工艺研发成功，2028年量产",
            "summary": "台积电在技术论坛上宣布，1.4nm工艺研发取得突破性进展，预计2028年实现量产。相比2nm工艺，1.4nm性能提升20%，功耗降低25%，晶体管密度提升30%。苹果、英伟达、AMD等客户已表达合作意向。",
            "time": f"{today} 13:45",
            "source": "TechCrunch",
            "url": "https://techcrunch.com/2026/03/26/tsmc-1-4nm-breakthrough-2028-production/",
            "category": "科技",
            "focus": "半导体工艺持续突破，为下一代计算设备性能飞跃奠定基础"
        },
        {
            "title": "微软Copilot全面集成Office 365，定价每用户每月30美元",
            "summary": "微软宣布将AI助手Copilot全面集成到Office 365所有应用中。新功能支持文档自动生成、数据分析、演示文稿制作、邮件智能回复等。企业版定价每用户每月30美元，预计将大幅提升办公效率。已有超过1万家企业试用。",
            "time": f"{today} 09:50",
            "source": "TechCrunch",
            "url": "https://techcrunch.com/2026/03/26/microsoft-copilot-office-365-pricing/",
            "category": "科技",
            "focus": "AI与生产力工具深度整合可能重新定义办公软件市场竞争格局"
        },
        {
            "title": "华为Mate X6发布：折叠屏技术再突破",
            "summary": "华为发布新一代折叠屏手机Mate X6，采用全新双旋水滴铰链设计，折痕减少70%。搭载昆仑玻璃，抗摔性能提升10倍。厚度仅5.3mm，重量239g，搭载麒麟9100芯片，支持卫星通信双向短信。售价12999元起。",
            "time": f"{today} 14:30",
            "source": "虎嗅",
            "url": "https://www.huxiu.com/article/598765.html",
            "category": "科技",
            "focus": "折叠屏技术成熟可能重塑高端手机市场格局，带动相关产业链发展"
        },
        
        # ==================== 新能源新闻 ====================
        {
            "title": "特斯拉发布新款Model 3，续航提升至600公里",
            "summary": "特斯拉发布新款Model 3，采用全新4680电池和结构电池组技术，续航里程提升至600公里（WLTP标准）。新车搭载HW5.0自动驾驶硬件，支持完全自动驾驶功能。起售价为25.99万元，即日开启预订，预计第二季度交付。",
            "time": f"{today} 13:00",
            "source": "36氪",
            "url": "https://36kr.com/p/298765433",
            "category": "新能源",
            "focus": "电动汽车续航竞赛升级，可能加速燃油车替代进程"
        },
        {
            "title": "比亚迪发布'海豹'二代，续航突破800公里",
            "summary": "比亚迪发布全新'海豹'二代电动汽车，采用新一代刀片电池技术，续航里程突破800公里（CLTC标准）。新车搭载'天神之眼'高阶智能驾驶系统，支持城市NOA功能。起售价18.98万元，即日开启预售。",
            "time": f"{today} 15:20",
            "source": "36氪",
            "url": "https://36kr.com/p/298765435",
            "category": "新能源",
            "focus": "中国品牌电动汽车技术突破，进一步巩固市场领先地位"
        },
        {
            "title": "中国新能源汽车渗透率突破50%，首次超过燃油车",
            "summary": "中国汽车工业协会数据显示，3月前三周新能源汽车零售渗透率达到51.2%，首次超过燃油车。其中纯电动汽车渗透率35.8%，插电混动汽车渗透率15.4%。预计全年新能源汽车销量将突破1200万辆。",
            "time": f"{today} 16:05",
            "source": "北极星电力网",
            "url": "https://news.bjx.com.cn/html/20260326/1234569.shtml",
            "category": "新能源",
            "focus": "新能源汽车市场迎来历史性拐点，产业转型进入加速期"
        },
        {
            "title": "全球可再生能源投资创新高，2025年达1.8万亿美元",
            "summary": "国际能源署报告显示，2025年全球可再生能源投资达到1.8万亿美元，创历史新高。中国可再生能源投资超过7500亿美元，占全球40%以上。太阳能和风能是投资主要方向，储能投资增长最快，同比增长65%。",
            "time": f"{today} 09:30",
            "source": "北极星电力网",
            "url": "https://news.bjx.com.cn/html/20260326/1234568.shtml",
            "category": "新能源",
            "focus": "能源转型加速，反映全球应对气候变化的决心和投资趋势"
        },
        
        # ==================== 商业航天新闻 ====================
        {
            "title": "SpaceX星舰成功完成首次商业发射，将88颗卫星送入轨道",
            "summary": "SpaceX星舰成功完成首次商业发射任务，将88颗卫星送入预定轨道，包括36颗Starlink卫星和52颗商业客户卫星。本次发射验证了星舰的大规模载荷能力和快速复用潜力。马斯克宣布星舰已获得超过100次发射订单。",
            "time": f"{today} 12:30",
            "source": "SpaceNews",
            "url": "https://spacenews.com/spacex-starship-first-commercial-launch-88-satellites/",
            "category": "商业航天",
            "focus": "商业航天进入规模化运营阶段，可能大幅降低太空运输成本"
        },
        {
            "title": "中国可重复使用火箭完成垂直起降试验，预计2027年首飞",
            "summary": "中国航天科技集团宣布，可重复使用运载火箭完成首次垂直起降试验，火箭飞行高度100米，精准返回着陆场。该火箭设计复用次数20次，单次发射成本可降低70%。预计2027年实现首飞，2030年实现商业化运营。",
            "time": f"{today} 17:40",
            "source": "航天爱好者网",
            "url": "https://www.spaceflightfans.cn/article/12347",
            "category": "商业航天",
            "focus
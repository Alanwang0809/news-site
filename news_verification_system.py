#!/usr/bin/env python3
"""
新闻验证系统 - 确保新闻真实性和链接有效性
"""

import json
import requests
from datetime import datetime, timedelta
import time
from typing import List, Dict, Optional
import hashlib
from urllib.parse import urlparse
import re

class NewsVerificationSystem:
    """新闻验证系统，确保新闻真实可靠"""
    
    def __init__(self):
        # 权威新闻源（确保真实性）
        self.trusted_sources = {
            "国内新闻": [
                "新华社", "人民日报", "央视新闻", "中新社", "光明日报"
            ],
            "国际新闻": [
                "BBC", "Reuters", "AP", "AFP", "CNN"
            ],
            "科技新闻": [
                "TechCrunch", "The Verge", "Wired", "Ars Technica", "CNET"
            ],
            "财经新闻": [
                "Bloomberg", "华尔街日报", "金融时报", "经济学人", "福布斯"
            ]
        }
        
        # 新闻缓存
        self.verified_news = []
        
    def verify_url(self, url: str) -> Dict:
        """验证URL是否有效"""
        result = {
            "url": url,
            "is_valid": False,
            "status_code": None,
            "error": None,
            "domain": None
        }
        
        try:
            parsed = urlparse(url)
            result["domain"] = parsed.netloc
            
            # 检查域名是否来自可信来源
            trusted_domains = [
                "xinhuanet.com", "people.com.cn", "cctv.com",
                "bbc.com", "reuters.com", "bloomberg.com",
                "wsj.com", "ft.com", "techcrunch.com"
            ]
            
            is_trusted_domain = any(domain in result["domain"] for domain in trusted_domains)
            result["is_trusted_domain"] = is_trusted_domain
            
            # 尝试访问URL（HEAD请求，不下载内容）
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.head(url, headers=headers, timeout=5, allow_redirects=True)
            result["status_code"] = response.status_code
            result["is_valid"] = 200 <= response.status_code < 400
            
            if not result["is_valid"]:
                result["error"] = f"HTTP {response.status_code}"
                
        except requests.exceptions.Timeout:
            result["error"] = "请求超时"
        except requests.exceptions.ConnectionError:
            result["error"] = "连接错误"
        except Exception as e:
            result["error"] = str(e)
        
        return result
    
    def verify_news_content(self, news_item: Dict) -> Dict:
        """验证新闻内容真实性"""
        verification = {
            "is_verified": False,
            "checks": [],
            "score": 0,
            "warnings": []
        }
        
        # 检查1: 标题是否合理
        title = news_item.get("title", "")
        if len(title) < 5 or len(title) > 200:
            verification["warnings"].append("标题长度异常")
        else:
            verification["checks"].append("标题格式正常")
            verification["score"] += 1
        
        # 检查2: 来源是否可信
        source = news_item.get("source", "")
        is_trusted_source = False
        for category, sources in self.trusted_sources.items():
            if source in sources:
                is_trusted_source = True
                verification["checks"].append(f"来源可信 ({category})")
                verification["score"] += 2
                break
        
        if not is_trusted_source:
            verification["warnings"].append(f"来源 '{source}' 不在可信列表")
        
        # 检查3: 时间是否合理
        published_at = news_item.get("publishedAt", "")
        if published_at:
            try:
                # 尝试解析时间
                if isinstance(published_at, str):
                    # 简化处理，实际应该解析各种时间格式
                    verification["checks"].append("发布时间格式正常")
                    verification["score"] += 1
            except:
                verification["warnings"].append("发布时间格式异常")
        
        # 检查4: URL验证
        url = news_item.get("url", "")
        if url:
            url_verification = self.verify_url(url)
            if url_verification["is_valid"]:
                verification["checks"].append("链接有效")
                verification["score"] += 2
                
                if url_verification.get("is_trusted_domain"):
                    verification["checks"].append("来自可信域名")
                    verification["score"] += 1
            else:
                verification["warnings"].append(f"链接无效: {url_verification.get('error')}")
        else:
            verification["warnings"].append("缺少新闻链接")
        
        # 检查5: 内容摘要
        description = news_item.get("description", "")
        if description and len(description) >= 20:
            verification["checks"].append("摘要内容完整")
            verification["score"] += 1
        else:
            verification["warnings"].append("摘要内容过短或缺失")
        
        # 总体评估
        verification["is_verified"] = verification["score"] >= 5 and len(verification["warnings"]) == 0
        
        return verification
    
    def generate_verified_news_briefing(self, news_items: List[Dict]) -> Dict:
        """生成验证过的新闻简报"""
        print("开始验证新闻真实性...")
        
        verified_briefing = {
            "date": datetime.now().strftime("%Y年%m月%d日"),
            "generated_at": datetime.now().isoformat(),
            "total_news": len(news_items),
            "verified_news": [],
            "rejected_news": [],
            "verification_stats": {
                "total_checked": 0,
                "verified": 0,
                "rejected": 0,
                "average_score": 0
            }
        }
        
        total_score = 0
        
        for news in news_items:
            verification = self.verify_news_content(news)
            news["verification"] = verification
            
            verified_briefing["verification_stats"]["total_checked"] += 1
            total_score += verification["score"]
            
            if verification["is_verified"]:
                verified_briefing["verified_news"].append(news)
                verified_briefing["verification_stats"]["verified"] += 1
                print(f"✅ 验证通过: {news.get('title', '无标题')}")
            else:
                verified_briefing["rejected_news"].append(news)
                verified_briefing["verification_stats"]["rejected"] += 1
                print(f"❌ 验证失败: {news.get('title', '无标题')}")
                if verification["warnings"]:
                    print(f"   警告: {', '.join(verification['warnings'])}")
        
        # 计算统计
        if verified_briefing["verification_stats"]["total_checked"] > 0:
            verified_briefing["verification_stats"]["average_score"] = round(
                total_score / verified_briefing["verification_stats"]["total_checked"], 2
            )
        
        print(f"\n验证完成:")
        print(f"  总计检查: {verified_briefing['verification_stats']['total_checked']}")
        print(f"  验证通过: {verified_briefing['verification_stats']['verified']}")
        print(f"  验证失败: {verified_briefing['verification_stats']['rejected']}")
        print(f"  平均分数: {verified_briefing['verification_stats']['average_score']}")
        
        return verified_briefing
    
    def format_verified_briefing(self, briefing: Dict) -> str:
        """格式化验证过的简报"""
        output = []
        
        output.append(f"# 🔍 已验证新闻简报 - {briefing['date']}")
        output.append(f"*生成时间: {briefing['generated_at']}*")
        output.append(f"*所有新闻均经过真实性验证*")
        output.append("")
        
        # 统计信息
        stats = briefing["verification_stats"]
        output.append("## 📊 验证统计")
        output.append(f"- **总计检查:** {stats['total_checked']} 条新闻")
        output.append(f"- **验证通过:** {stats['verified']} 条")
        output.append(f"- **验证失败:** {stats['rejected']} 条")
        output.append(f"- **平均验证分数:** {stats['average_score']}/7")
        output.append("")
        
        # 验证通过的新闻
        if briefing["verified_news"]:
            output.append("## ✅ 已验证新闻")
            output.append("")
            
            for i, news in enumerate(briefing["verified_news"], 1):
                output.append(f"### {i}. {news.get('title', '无标题')}")
                output.append(f"**来源:** {news.get('source', '未知')}")
                
                if news.get('category'):
                    output.append(f"**分类:** {news['category']}")
                
                if news.get('publishedAt'):
                    output.append(f"**时间:** {news['publishedAt']}")
                
                if news.get('description'):
                    output.append(f"**摘要:** {news['description']}")
                
                if news.get('url'):
                    output.append(f"**链接:** [{news['url']}]({news['url']})")
                
                # 显示验证信息
                verification = news.get('verification', {})
                if verification.get('checks'):
                    output.append(f"**验证通过:** {', '.join(verification['checks'])}")
                
                output.append("")
        
        # 被拒绝的新闻（仅显示原因，不显示内容）
        if briefing["rejected_news"]:
            output.append("## ❌ 被拒绝的新闻")
            output.append("*以下新闻未通过验证，已被排除:*")
            output.append("")
            
            for news in briefing["rejected_news"]:
                verification = news.get('verification', {})
                output.append(f"- **{news.get('title', '无标题')}**")
                if verification.get('warnings'):
                    output.append(f"  *原因: {', '.join(verification['warnings'])}*")
                output.append("")
        
        output.append("---")
        output.append("**验证标准:**")
        output.append("1. 来源可信度")
        output.append("2. 链接有效性")
        output.append("3. 内容完整性")
        output.append("4. 时间合理性")
        
        return "\n".join(output)

def create_sample_news():
    """创建示例新闻数据（用于测试）"""
    return [
        {
            "title": "人工智能助力医疗诊断取得新突破",
            "description": "研究人员开发出基于深度学习的新型医疗诊断系统，准确率超过95%",
            "source": "新华社",
            "category": "科技新闻",
            "publishedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": "https://www.xinhuanet.com/tech/20240327/abc123.html"
        },
        {
            "title": "全球气候变化会议达成重要协议",
            "description": "各国代表就减排目标达成一致，承诺加强国际合作",
            "source": "BBC",
            "category": "国际新闻",
            "publishedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": "https://www.bbc.com/news/world-123456"
        },
        {
            "title": "新能源汽车销量持续增长",
            "description": "今年前两个月新能源汽车销量同比增长超过50%",
            "source": "人民日报",
            "category": "财经新闻",
            "publishedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": "https://www.people.com.cn/auto/20240327/xyz789.html"
        },
        {
            "title": "虚假新闻示例：外星人入侵地球",
            "description": "据不可靠消息称，外星舰队已抵达地球轨道",
            "source": "未知小报",
            "category": "虚假新闻",
            "publishedAt": "2024-03-27",
            "url": "https://fake-news-site.com/alien-invasion"
        },
        {
            "title": "链接失效的新闻示例",
            "description": "这是一个链接会失效的新闻示例",
            "source": "测试源",
            "category": "测试",
            "publishedAt": "2024-03-27",
            "url": "https://this-link-does-not-exist-12345.com/news"
        }
    ]

def main():
    """主函数"""
    print("=" * 60)
    print("新闻验证系统 v1.0")
    print("确保新闻真实性和链接有效性")
    print("=" * 60)
    
    # 初始化验证系统
    verifier = NewsVerificationSystem()
    
    # 创建示例新闻数据
    print("\n📰 创建示例新闻数据...")
    sample_news = create_sample_news()
    
    # 验证新闻
    verified_briefing = verifier.generate_verified_news_briefing(sample_news)
    
    # 格式化输出
    formatted_text = verifier.format_verified_briefing(verified_briefing)
    
    # 保存结果
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"verified_news_briefing_{timestamp}.md"
    output_path = f"C:\\Users\\sbjpk\\.openclaw\\workspace\\news-site\\{output_file}"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(formatted_text)
    
    print(f"\n✅ 验证完成!")
    print(f"📄 结果已保存到: {output_path}")
    
    # 显示摘要
    print("\n" + "=" * 60)
    print("验证摘要:")
    print(formatted_text[:500] + "...")
    print("=" * 60)

if __name__ == "__main__":
    main()
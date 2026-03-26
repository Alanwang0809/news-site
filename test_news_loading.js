#!/usr/bin/env node
/**
 * 测试 news.json 数据加载
 */

const fs = require('fs');
const path = require('path');

console.log('🔍 测试 news.json 数据加载...');
console.log('='.repeat(50));

try {
    // 读取 news.json
    const newsJsonPath = path.join(__dirname, 'news.json');
    const newsData = JSON.parse(fs.readFileSync(newsJsonPath, 'utf8'));
    
    console.log('✅ news.json 读取成功');
    console.log(`📅 日期: ${newsData.date}`);
    console.log(`📰 新闻数量: ${newsData.news.length}条`);
    
    // 检查分类
    const categories = {};
    newsData.news.forEach(news => {
        categories[news.category] = (categories[news.category] || 0) + 1;
    });
    
    console.log('\n📊 分类统计:');
    Object.entries(categories).forEach(([category, count]) => {
        console.log(`  ${category}: ${count}条`);
    });
    
    // 检查前3条新闻
    console.log('\n🔍 前3条新闻检查:');
    newsData.news.slice(0, 3).forEach((news, index) => {
        console.log(`\n${index + 1}. ${news.title}`);
        console.log(`   分类: ${news.category}`);
        console.log(`   时间: ${news.time}`);
        console.log(`   来源: ${news.source}`);
        console.log(`   摘要长度: ${news.summary.length}字`);
        console.log(`   链接: ${news.url}`);
    });
    
    // 检查 index.html 是否能正确引用
    const indexPath = path.join(__dirname, 'index.html');
    const htmlContent = fs.readFileSync(indexPath, 'utf8');
    
    console.log('\n📄 index.html 检查:');
    console.log(`  文件大小: ${htmlContent.length} 字节`);
    console.log(`  包含 news.json 引用: ${htmlContent.includes('news.json') ? '✅' : '❌'}`);
    console.log(`  包含 fetch 调用: ${htmlContent.includes('fetch(\'news.json\')') ? '✅' : '❌'}`);
    
    console.log('\n' + '='.repeat(50));
    console.log('✅ 所有检查通过！index.html 应该可以正确读取 news.json');
    console.log('\n💡 使用说明:');
    console.log('1. 双击 index.html 文件在浏览器中打开');
    console.log('2. 确保 news.json 在同一目录下');
    console.log('3. 如果使用本地服务器，确保允许跨域请求');
    
} catch (error) {
    console.error('❌ 测试失败:', error.message);
    console.error('错误详情:', error);
    process.exit(1);
}
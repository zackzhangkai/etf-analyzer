# ETF 智能分析平台

实时展示热门 ETF 行情数据的智能分析平台。

## 功能特性

- 📊 实时行情 - 从新浪财经获取 ETF 实时数据
- 📈 走势分析 - 支持多种时间范围查看 K 线走势
- 🏷️ 分类筛选 - 按芯片、AI、科技等板块筛选 ETF
- 🔄 自动刷新 - 每 30 秒自动更新最新数据
- 📱 响应式设计 - 支持桌面和移动设备

## 技术栈

- 前端: HTML + Tailwind CSS + Chart.js
- 后端: Vercel Serverless Functions
- 数据源: 新浪财经 API

## 快速开始

### 本地运行

```bash
# 克隆项目
git clone https://github.com/zackzhangkai/etf-analyzer.git
cd etf-analyzer

# 使用 Python 启动简单服务器
python3 -m http.server 8080
# 或使用 Node.js
npx serve .
```

访问 http://localhost:8080

### 部署

项目已部署到 Vercel: https://etf-analyzer.vercel.app

## ETF 列表

| 代码 | 名称 | 类别 |
|------|------|------|
| 512480 | 半导体ETF | 芯片 |
| 515880 | 科技ETF | 科技 |
| 159819 | 人工智能ETF | AI |
| 512760 | 芯片ETF | 芯片 |
| 588000 | 科创50ETF | 科技 |

## License

MIT
// ETF 实时数据 API
// 使用新浪财经接口获取 ETF 行情数据

const iconv = require('iconv-lite');

export default async function handler(req, res) {
  // 设置 CORS 头
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // ETF 列表配置
  const etfCodes = [
    { code: '512480', name: '半导体ETF', category: 'chip' },
    { code: '515880', name: '科技ETF', category: 'tech' },
    { code: '159819', name: '人工智能ETF', category: 'ai' },
    { code: '512760', name: '芯片ETF', category: 'chip' },
    { code: '588000', name: '科创50ETF', category: 'tech' },
    { code: '159995', name: '芯片龙头ETF', category: 'chip' },
    { code: '512720', name: '计算机ETF', category: 'ai' },
    { code: '515050', name: '5GETF', category: 'tech' },
    { code: '159801', name: '5G通信ETF', category: 'tech' },
    { code: '512660', name: '军工ETF', category: 'all' },
  ];

  try {
    // 构建新浪财经 API 请求
    const symbols = etfCodes.map(etf => {
      // 上海交易所 ETF 以 sh 开头，深圳以 sz 开头
      const prefix = etf.code.startsWith('5') || etf.code.startsWith('1') ? 'sh' : 'sz';
      return `${prefix}${etf.code}`;
    }).join(',');

    const response = await fetch(
      `https://hq.sinajs.cn/list=${symbols}`,
      {
        headers: {
          'Referer': 'https://finance.sina.com.cn',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
      }
    );

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const text = await response.arrayBuffer();
    const buffer = iconv.decode(Buffer.from(text), 'GBK');

    // 解析新浪财经返回的数据
    // 格式: var hq_str_sh512480="半导体ETF,1.245,1.198,1.246,1.248,1.197,1.245,1.246,123456789,12345,...";
    const etfData = [];
    const lines = text.split('\n');

    for (const line of lines) {
      if (!line.includes('hq_str_')) continue;

      const match = line.match(/hq_str_(sh|sz)(\d+)="(.+)"/);
      if (!match) continue;

      const [, exchange, code, data] = match;
      const fields = data.split(',');

      if (fields.length < 3) continue;

      const name = fields[0];
      const open = parseFloat(fields[1]) || 0;
      const price = parseFloat(fields[2]) || 0;
      const high = parseFloat(fields[3]) || 0;
      const low = parseFloat(fields[4]) || 0;
      const volume = parseFloat(fields[5]) || 0; // 成交量(手)
      const amount = parseFloat(fields[6]) || 0; // 成交额(元)

      // 计算涨跌幅
      const change = open > 0 ? ((price - open) / open * 100) : 0;
      const changeValue = price - open;

      // 格式化成交量和成交额
      let volumeStr = '';
      if (volume >= 100000000) {
        volumeStr = (volume / 100000000).toFixed(1) + '亿';
      } else if (volume >= 10000) {
        volumeStr = (volume / 10000).toFixed(1) + '万';
      } else {
        volumeStr = volume.toFixed(0) + '手';
      }

      let amountStr = '';
      if (amount >= 100000000) {
        amountStr = (amount / 100000000).toFixed(1) + '亿';
      } else if (amount >= 10000) {
        amountStr = (amount / 10000).toFixed(1) + '万';
      } else {
        amountStr = amount.toFixed(0) + '元';
      }

      // 找到对应的 ETF 分类
      const etfInfo = etfCodes.find(e => e.code === code);

      etfData.push({
        code,
        name,
        price: price.toFixed(3),
        change: change.toFixed(2),
        changeValue: changeValue.toFixed(3),
        open: open.toFixed(3),
        high: high.toFixed(3),
        low: low.toFixed(3),
        volume: volumeStr,
        amount: amountStr,
        category: etfInfo?.category || 'all',
        exchange: exchange === 'sh' ? '上海' : '深圳'
      });
    }

    // 获取大盘指数
    const indices = ['sh000001', 'sz399001', 'sz399006', 'sh000688'];
    const indicesResponse = await fetch(
      `https://hq.sinajs.cn/list=${indices.join(',')}`,
      {
        headers: {
          'Referer': 'https://finance.sina.com.cn',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
      }
    );

    const indicesText = await indicesResponse.text();
    const marketData = {
      sh000001: { name: '上证指数', index: 'sh' },
      sz399001: { name: '深证成指', index: 'sz' },
      sz399006: { name: '创业板指', index: 'sz' },
      sh000688: { name: '科创50', index: 'sh' }
    };

    for (const line of indicesText.split('\n')) {
      if (!line.includes('hq_str_')) continue;

      const match = line.match(/hq_str_(sh|sz)(\d+)="(.+)"/);
      if (!match) continue;

      const [, exchange, code, data] = match;
      const key = `${exchange}${code}`;
      const fields = data.split(',');

      if (fields.length >= 4) {
        const price = parseFloat(fields[1]) || 0;
        const change = parseFloat(fields[2]) || 0;
        const pctChange = parseFloat(fields[3]) || 0;

        marketData[key] = {
          ...marketData[key],
          price: price.toFixed(2),
          change: pctChange.toFixed(2),
          isPositive: pctChange >= 0
        };
      }
    }

    res.status(200).json({
      success: true,
      timestamp: new Date().toISOString(),
      data: {
        etfs: etfData,
        market: Object.values(marketData).filter(m => m.price)
      }
    });

  } catch (error) {
    console.error('Error fetching data:', error);
    res.status(500).json({
      success: false,
      error: error.message,
      timestamp: new Date().toISOString()
    });
  }
}
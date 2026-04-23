#!/usr/bin/env python3
"""Generate ETF dashboard preview images using matplotlib"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def create_dashboard_overview():
    """Create main dashboard overview"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Header
    header = FancyBboxPatch((0, 90), 100, 10, boxstyle="round,pad=0.02", 
                            facecolor='#667eea', edgecolor='none')
    ax.add_patch(header)
    ax.text(5, 95, 'ETF 智能分析平台', fontsize=18, fontweight='bold', color='white', va='center')
    ax.text(85, 95, '14:17:32', fontsize=10, color='white', va='center')
    
    # Market indices
    indices = [
        ('上证指数', '3,247.12', '+0.58%', '#10b981'),
        ('深证成指', '10,356.82', '+0.82%', '#10b981'),
        ('创业板指', '2,089.45', '+1.24%', '#10b981'),
        ('科创50', '1,156.78', '+2.15%', '#10b981'),
    ]
    
    for i, (name, price, change, color) in enumerate(indices):
        x = 2 + i * 24
        box = FancyBboxPatch((x, 75), 22, 12, boxstyle="round,pad=0.5", 
                             facecolor='white', edgecolor='#e5e7eb', linewidth=1)
        ax.add_patch(box)
        ax.text(x + 11, 84, name, fontsize=9, color='#6b7280', ha='center')
        ax.text(x + 11, 80, price, fontsize=14, fontweight='bold', ha='center')
        ax.text(x + 11, 77, change, fontsize=9, color=color, ha='center')
    
    # ETF Table
    table_box = FancyBboxPatch((2, 30), 60, 42, boxstyle="round,pad=0.5", 
                               facecolor='white', edgecolor='#e5e7eb', linewidth=1)
    ax.add_patch(table_box)
    ax.text(5, 68, '热门ETF排行', fontsize=12, fontweight='bold')
    
    # Table header
    headers = ['ETF名称', '最新价', '涨跌幅', '成交额']
    header_x = [8, 32, 42, 52]
    for h, x in zip(headers, header_x):
        ax.text(x, 64, h, fontsize=9, color='#6b7280', fontweight='bold')
    
    # ETF data
    etfs = [
        ('半导体ETF', '512480', '1.245', '+3.58%', '12.5亿'),
        ('科技ETF', '515880', '0.892', '+2.76%', '8.3亿'),
        ('人工智能ETF', '159819', '1.156', '+4.23%', '15.2亿'),
        ('芯片ETF', '512760', '1.089', '+3.12%', '9.8亿'),
        ('科创50ETF', '588000', '0.956', '+2.15%', '22.1亿'),
    ]
    
    for i, (name, code, price, change, volume) in enumerate(etfs):
        y = 58 - i * 5
        # Icon
        circle = Circle((6, y), 1.5, facecolor='#3b82f6', edgecolor='none')
        ax.add_patch(circle)
        ax.text(6, y, name[0], fontsize=7, color='white', ha='center', va='center')
        ax.text(10, y + 0.5, name, fontsize=9, fontweight='bold')
        ax.text(10, y - 1, code, fontsize=7, color='#9ca3af')
        ax.text(34, y, price, fontsize=9, ha='center')
        ax.text(44, y, change, fontsize=9, color='#10b981', ha='center', fontweight='bold')
        ax.text(56, y, volume, fontsize=9, ha='right', color='#6b7280')
    
    # Chart area
    chart_box = FancyBboxPatch((2, 2), 60, 26, boxstyle="round,pad=0.5", 
                               facecolor='white', edgecolor='#e5e7eb', linewidth=1)
    ax.add_patch(chart_box)
    ax.text(5, 25, '走势分析', fontsize=11, fontweight='bold')
    
    # Time range buttons
    time_ranges = ['1日', '1周', '1月', '3月', '1年']
    for i, tr in enumerate(time_ranges):
        color = '#3b82f6' if i == 0 else '#e5e7eb'
        text_color = 'white' if i == 0 else '#374151'
        btn = FancyBboxPatch((48 + i * 6, 23), 5, 2.5, boxstyle="round,pad=0.2", 
                             facecolor=color, edgecolor='none')
        ax.add_patch(btn)
        ax.text(50.5 + i * 6, 24.2, tr, fontsize=7, color=text_color, ha='center')
    
    # Line chart
    x_data = np.linspace(5, 58, 50)
    y_base = 12
    y_data = y_base + np.sin(x_data * 0.3) * 3 + np.random.randn(50) * 0.5
    ax.plot(x_data, y_data, color='#3b82f6', linewidth=2)
    ax.fill_between(x_data, y_data, y_base - 5, alpha=0.1, color='#3b82f6')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Sidebar - ETF Detail
    detail_box = FancyBboxPatch((65, 55), 33, 40, boxstyle="round,pad=0.5", 
                                facecolor='white', edgecolor='#e5e7eb', linewidth=1)
    ax.add_patch(detail_box)
    ax.text(68, 91, '选中ETF详情', fontsize=11, fontweight='bold')
    
    # Detail content
    circle = Circle((81.5, 84), 3, facecolor='#3b82f6', edgecolor='none')
    ax.add_patch(circle)
    ax.text(81.5, 84, '半', fontsize=10, color='white', ha='center', va='center')
    ax.text(81.5, 79, '半导体ETF', fontsize=10, fontweight='bold', ha='center')
    ax.text(81.5, 76, '512480', fontsize=8, color='#9ca3af', ha='center')
    
    # Stats grid
    stats = [('最新价', '1.245'), ('涨跌幅', '+3.58%'), ('市盈率', '45.2'), ('市净率', '3.8')]
    for i, (label, value) in enumerate(stats):
        x = 70 + (i % 2) * 12
        y = 70 - (i // 2) * 8
        stat_box = FancyBboxPatch((x - 2, y - 2), 10, 5, boxstyle="round,pad=0.2", 
                                  facecolor='#f3f4f6', edgecolor='none')
        ax.add_patch(stat_box)
        ax.text(x + 3, y + 1.5, label, fontsize=7, color='#6b7280', ha='center')
        ax.text(x + 3, y - 0.5, value, fontsize=9, fontweight='bold', ha='center')
    
    # Sector pie chart
    pie_box = FancyBboxPatch((65, 30), 33, 23, boxstyle="round,pad=0.5", 
                             facecolor='white', edgecolor='#e5e7eb', linewidth=1)
    ax.add_patch(pie_box)
    ax.text(68, 50, '板块分布', fontsize=11, fontweight='bold')
    
    # Simple pie representation
    sectors = [('芯片', 35, '#3b82f6'), ('AI', 28, '#8b5cf6'), ('通信', 18, '#10b981'), 
               ('新能源', 12, '#f59e0b'), ('其他', 7, '#6b7280')]
    start_angle = 0
    center_x, center_y, radius = 81.5, 38, 6
    for name, pct, color in sectors:
        angle = pct / 100 * 360
        wedge = patches.Wedge((center_x, center_y), radius, start_angle, start_angle + angle,
                              facecolor=color, edgecolor='white', linewidth=2)
        ax.add_patch(wedge)
        start_angle += angle
    
    # Legend
    for i, (name, pct, color) in enumerate(sectors):
        y = 32 - i * 2
        ax.add_patch(patches.Rectangle((88, y - 0.5), 1.5, 1.5, facecolor=color, edgecolor='none'))
        ax.text(90, y, f'{name} {pct}%', fontsize=7, va='center')
    
    # Hot topics
    topics_box = FancyBboxPatch((65, 2), 33, 26, boxstyle="round,pad=0.5", 
                                facecolor='white', edgecolor='#e5e7eb', linewidth=1)
    ax.add_patch(topics_box)
    ax.text(68, 25, '热门概念', fontsize=11, fontweight='bold')
    
    topics = [('光模块', '#ef4444'), ('算力', '#3b82f6'), ('钠电池', '#10b981'), 
              ('AI芯片', '#8b5cf6'), ('液冷', '#f59e0b')]
    x, y = 68, 20
    for name, color in topics:
        topic_box = FancyBboxPatch((x, y), 7, 2.5, boxstyle="round,pad=0.3", 
                                   facecolor=color, edgecolor='none', alpha=0.15)
        ax.add_patch(topic_box)
        ax.text(x + 3.5, y + 1.2, name, fontsize=7, color=color, ha='center')
        x += 9
        if x > 90:
            x = 68
            y -= 4
    
    plt.tight_layout()
    plt.savefig('/Users/zack/.openclaw/workspace-kaizige/etf-analyzer/preview-1-overview.png', 
                dpi=150, bbox_inches='tight', facecolor='#f9fafb')
    plt.close()
    print("Generated: preview-1-overview.png")

def create_etf_list_detail():
    """Create ETF list detail view"""
    fig, ax = plt.subplots(figsize=(10, 12))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Header
    header = FancyBboxPatch((0, 94), 100, 6, boxstyle="round,pad=0.02", 
                            facecolor='#667eea', edgecolor='none')
    ax.add_patch(header)
    ax.text(5, 97, 'ETF 智能分析平台', fontsize=16, fontweight='bold', color='white', va='center')
    
    # Filter buttons
    filters = ['全部', '科技', '芯片', 'AI', '5G', '新能源']
    for i, f in enumerate(filters):
        color = '#3b82f6' if i == 0 else '#e5e7eb'
        text_color = 'white' if i == 0 else '#374151'
        btn = FancyBboxPatch((5 + i * 12, 88), 10, 4, boxstyle="round,pad=0.3", 
                             facecolor=color, edgecolor='none')
        ax.add_patch(btn)
        ax.text(10 + i * 12, 90, f, fontsize=9, color=text_color, ha='center', va='center')
    
    # Table header
    headers = ['ETF名称', '最新价', '涨跌幅', '成交额', '市盈率', '操作']
    header_x = [15, 38, 50, 62, 75, 88]
    for h, x in zip(headers, header_x):
        ax.text(x, 84, h, fontsize=10, color='#6b7280', fontweight='bold', ha='center')
    
    # Divider
    ax.plot([5, 95], [82, 82], color='#e5e7eb', linewidth=1)
    
    # ETF data rows
    etfs = [
        ('半导体ETF', '512480', '1.245', '+3.58%', '12.5亿', '45.2', '#10b981'),
        ('科技ETF', '515880', '0.892', '+2.76%', '8.3亿', '38.5', '#10b981'),
        ('人工智能ETF', '159819', '1.156', '+4.23%', '15.2亿', '52.1', '#10b981'),
        ('芯片ETF', '512760', '1.089', '+3.12%', '9.8亿', '42.8', '#10b981'),
        ('科创50ETF', '588000', '0.956', '+2.15%', '22.1亿', '65.3', '#10b981'),
        ('芯片龙头ETF', '159995', '1.234', '+3.45%', '7.6亿', '44.1', '#10b981'),
        ('计算机ETF', '512720', '0.876', '+2.89%', '5.4亿', '35.2', '#10b981'),
        ('5GETF', '515050', '0.923', '+1.98%', '6.7亿', '28.9', '#10b981'),
        ('5G通信ETF', '159801', '1.045', '+2.34%', '4.8亿', '31.2', '#10b981'),
        ('军工ETF', '512660', '1.123', '-0.56%', '3.2亿', '55.8', '#ef4444'),
    ]
    
    for i, (name, code, price, change, volume, pe, color) in enumerate(etfs):
        y = 78 - i * 7
        bg_color = '#f9fafb' if i % 2 == 0 else 'white'
        row = FancyBboxPatch((5, y - 3), 90, 6, boxstyle="round,pad=0.1", 
                             facecolor=bg_color, edgecolor='none')
        ax.add_patch(row)
        
        # Icon
        circle = Circle((10, y), 2, facecolor='#3b82f6', edgecolor='none')
        ax.add_patch(circle)
        ax.text(10, y, name[0], fontsize=8, color='white', ha='center', va='center')
        
        # Data
        ax.text(15, y + 1, name, fontsize=10, fontweight='bold')
        ax.text(15, y - 1.5, code, fontsize=8, color='#9ca3af')
        ax.text(38, y, price, fontsize=10, ha='center')
        ax.text(50, y, change, fontsize=10, color=color, ha='center', fontweight='bold')
        ax.text(62, y, volume, fontsize=10, ha='center', color='#6b7280')
        ax.text(75, y, pe, fontsize=10, ha='center')
        
        # Action button
        btn = FancyBboxPatch((84, y - 1.5), 8, 3, boxstyle="round,pad=0.2", 
                             facecolor='#dbeafe', edgecolor='none')
        ax.add_patch(btn)
        ax.text(88, y, '分析', fontsize=8, color='#3b82f6', ha='center', va='center')
    
    plt.tight_layout()
    plt.savefig('/Users/zack/.openclaw/workspace-kaizige/etf-analyzer/preview-2-list.png', 
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: preview-2-list.png")

def create_chart_detail():
    """Create chart detail view"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Header
    header = FancyBboxPatch((0, 92), 100, 8, boxstyle="round,pad=0.02", 
                            facecolor='#667eea', edgecolor='none')
    ax.add_patch(header)
    ax.text(5, 96, 'ETF 智能分析平台 - 走势分析', fontsize=14, fontweight='bold', color='white', va='center')
    
    # ETF selector
    ax.text(5, 88, '当前选中: 半导体ETF (512480)', fontsize=12, fontweight='bold')
    
    # Time range buttons
    time_ranges = ['1日', '1周', '1月', '3月', '1年']
    for i, tr in enumerate(time_ranges):
        color = '#10b981' if i == 2 else '#e5e7eb'
        text_color = 'white' if i == 2 else '#374151'
        btn = FancyBboxPatch((70 + i * 6, 86), 5, 3, boxstyle="round,pad=0.2", 
                             facecolor=color, edgecolor='none')
        ax.add_patch(btn)
        ax.text(72.5 + i * 6, 87.5, tr, fontsize=8, color=text_color, ha='center')
    
    # Chart box
    chart_box = FancyBboxPatch((5, 15), 90, 68, boxstyle="round,pad=0.5", 
                               facecolor='white', edgecolor='#e5e7eb', linewidth=1)
    ax.add_patch(chart_box)
    
    # Generate realistic price data
    np.random.seed(42)
    days = 30
    x = np.linspace(10, 90, days)
    
    # Price line
    base_price = 1.1
    price_data = base_price + np.cumsum(np.random.randn(days) * 0.02)
    price_data = np.maximum(price_data, base_price * 0.9)
    
    # Scale to chart area
    y_min, y_max = 20, 75
    price_scaled = (price_data - price_data.min()) / (price_data.max() - price_data.min()) * (y_max - y_min) + y_min
    
    # Plot line
    ax.plot(x, price_scaled, color='#10b981', linewidth=2.5)
    ax.fill_between(x, price_scaled, y_min, alpha=0.1, color='#10b981')
    
    # Add grid
    for y in range(25, 76, 10):
        ax.plot([10, 90], [y, y], color='#f3f4f6', linewidth=0.5)
    
    # Y-axis labels
    for i, y in enumerate(range(25, 76, 10)):
        price_label = f'{1.0 + i * 0.05:.2f}'
        ax.text(7, y, price_label, fontsize=8, color='#9ca3af', ha='right', va='center')
    
    # X-axis labels
    for i, x_pos in enumerate(range(10, 91, 16)):
        day_label = f'{i*6+1}日'
        ax.text(x_pos, 17, day_label, fontsize=8, color='#9ca3af', ha='center')
    
    # Stats overlay
    stats_box = FancyBboxPatch((75, 70), 18, 10, boxstyle="round,pad=0.3", 
                               facecolor='rgba(255,255,255,0.95)', edgecolor='#e5e7eb', linewidth=1)
    ax.add_patch(stats_box)
    ax.text(84, 78, '本月表现', fontsize=9, fontweight='bold', ha='center')
    ax.text(84, 74, '+12.58%', fontsize=14, color='#10b981', fontweight='bold', ha='center')
    ax.text(84, 71, '最高点: 1.245', fontsize=7, color='#6b7280', ha='center')
    
    plt.tight_layout()
    plt.savefig('/Users/zack/.openclaw/workspace-kaizige/etf-analyzer/preview-3-chart.png', 
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: preview-3-chart.png")

if __name__ == '__main__':
    create_dashboard_overview()
    create_etf_list_detail()
    create_chart_detail()
    print("\nAll preview images generated!")

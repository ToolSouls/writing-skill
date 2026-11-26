# 公众号排版组件库 —— 数据简报

> **适用**：行业报告、商业分析、数据复盘、运营总结、市场观察、研究解读。
>
> **设计语言**：深海军蓝建立可信度，橙色只用于关键数据与结论；版式强调结论先行、指标、对照和来源。

## 1. 设计变量

| 变量 | 色值 / 值 |
|---|---|
| 主色 | `#0F172A` |
| 次主色 | `#334155` |
| 强调色 | `#D97706` |
| 浅底 | `#F8FAFC` |
| 正文 | `#1F2937` |
| 次文 | `#64748B` |
| 分割线 | `#E2E8F0` |
| 字体 | `source-hans-sans` |
| 圆角 | `8px` |
| 阴影 | 基本不用 |
| 正文下划线 | `border-bottom:2px solid #FCD34D;font-weight:600;` |

## 2. 组件

### 2.1 报告封面

```html
<section style="margin:0 0 18px 0;padding:22px 20px;background:#0F172A;border-top:6px solid #D97706;border-radius:8px;">
  <p style="margin:0 0 8px 0;color:#FCD34D;font-size:11px;letter-spacing:1.5px;"><span leaf="">DATA BRIEF · {{报告期}}</span></p>
  <p style="margin:0 0 10px 0;color:#FFFFFF;font-size:22px;line-height:1.45;font-weight:700;"><span leaf="">{{报告标题}}</span></p>
  <p style="margin:0;color:#CBD5E1;font-size:13px;line-height:1.8;"><span leaf="">{{一句话结论占位}}</span></p>
</section>
```

### 2.2 执行摘要

```html
<section style="margin:18px 0;padding:17px 18px;background:#FFF7ED;border:1px solid #FED7AA;border-radius:8px;">
  <p style="margin:0 0 8px 0;color:#C2410C;font-size:12px;font-weight:700;letter-spacing:1px;"><span leaf="">执行摘要</span></p>
  <p style="margin:0;color:#7C2D12;font-size:14px;line-height:1.9;"><span leaf="">{{摘要内容占位}}</span></p>
</section>
```

### 2.3 核心指标条

```html
<section style="margin:18px 0;padding:16px 12px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:8px;text-align:center;">
  <span style="display:inline-block;width:31%;vertical-align:top;"><p style="margin:0;color:#D97706;font-size:20px;font-weight:700;"><span leaf="">{{23%}}</span></p><p style="margin:5px 0 0 0;color:#64748B;font-size:11px;"><span leaf="">{{指标一}}</span></p></span><span style="display:inline-block;width:31%;vertical-align:top;border-left:1px solid #E2E8F0;border-right:1px solid #E2E8F0;"><p style="margin:0;color:#D97706;font-size:20px;font-weight:700;"><span leaf="">{{48%}}</span></p><p style="margin:5px 0 0 0;color:#64748B;font-size:11px;"><span leaf="">{{指标二}}</span></p></span><span style="display:inline-block;width:31%;vertical-align:top;"><p style="margin:0;color:#D97706;font-size:20px;font-weight:700;"><span leaf="">{{7.2}}</span></p><p style="margin:5px 0 0 0;color:#64748B;font-size:11px;"><span leaf="">{{指标三}}</span></p></span>
</section>
```

### 2.4 报告章节标题

```html
<section style="margin:26px 0 14px 0;padding-bottom:10px;border-bottom:2px solid #0F172A;">
  <p style="margin:0;color:#0F172A;font-size:19px;line-height:1.5;font-weight:700;"><span leaf=""><span style="color:#D97706;margin-right:8px;">{{01}}</span>{{章节标题}}</span></p>
</section>
```

### 2.5 小节标题

```html
<section style="margin:22px 0 10px 0;">
  <p style="margin:0;color:#334155;font-size:15px;font-weight:700;"><span leaf=""><span style="display:inline-block;width:7px;height:18px;background:#D97706;vertical-align:-3px;margin-right:8px;"><span leaf=""><br></span></span>{{小节标题}}</span></p>
</section>
```

### 2.6 正文段落

```html
<section style="margin:13px 0;">
  <p style="margin:0;color:#1F2937;font-size:15px;line-height:1.95;"><span leaf="">{{正文内容占位，用<span style="border-bottom:2px solid #FCD34D;font-weight:600;">关键结论</span>建立阅读重点。}}</span></p>
</section>
```

### 2.7 结论先行卡

```html
<section style="margin:18px 0;padding:16px 18px;background:#FFFFFF;border-left:4px solid #D97706;border-top:1px solid #E2E8F0;border-right:1px solid #E2E8F0;border-bottom:1px solid #E2E8F0;border-radius:0 8px 8px 0;">
  <p style="margin:0 0 7px 0;color:#D97706;font-size:11px;font-weight:700;letter-spacing:1px;"><span leaf="">结论</span></p>
  <p style="margin:0;color:#1E293B;font-size:15px;line-height:1.85;font-weight:600;"><span leaf="">{{核心结论占位}}</span></p>
</section>
```

### 2.8 研究发现列表

```html
<section style="margin:18px 0;padding:16px 18px;background:#F8FAFC;border-radius:8px;">
  <p style="margin:0 0 10px 0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><strong style="color:#D97706;">01</strong>　{{研究发现占位}}</span></p>
  <p style="margin:0 0 10px 0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><strong style="color:#D97706;">02</strong>　{{研究发现占位}}</span></p>
  <p style="margin:0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><strong style="color:#D97706;">03</strong>　{{研究发现占位}}</span></p>
</section>
```

### 2.9 迷你柱状图占位

```html
<section style="margin:18px 0;padding:18px;background:#FFFFFF;border:1px solid #E2E8F0;border-radius:8px;">
  <p style="margin:0 0 12px 0;color:#334155;font-size:13px;font-weight:700;"><span leaf="">{{图表标题占位}}</span></p>
  <p style="margin:0 0 8px 0;color:#64748B;font-size:11px;"><span leaf="">{{类别A}}</span></p>
  <section style="height:9px;background:#FEF3C7;border-radius:9px;"><span style="display:block;width:82%;height:9px;background:#D97706;border-radius:9px;"><span leaf=""><br></span></span></section>
  <p style="margin:12px 0 8px 0;color:#64748B;font-size:11px;"><span leaf="">{{类别B}}</span></p>
  <section style="height:9px;background:#FEF3C7;border-radius:9px;"><span style="display:block;width:58%;height:9px;background:#D97706;border-radius:9px;"><span leaf=""><br></span></span></section>
  <p style="margin:12px 0 8px 0;color:#64748B;font-size:11px;"><span leaf="">{{类别C}}</span></p>
  <section style="height:9px;background:#FEF3C7;border-radius:9px;"><span style="display:block;width:35%;height:9px;background:#D97706;border-radius:9px;"><span leaf=""><br></span></span></section>
</section>
```

### 2.10 数据表

```html
<table style="width:100%;margin:18px 0;border-collapse:collapse;font-size:13px;">
  <tr>
    <th style="padding:10px;background:#0F172A;color:#FFFFFF;border:1px solid #0F172A;text-align:left;"><span leaf="">{{指标}}</span></th>
    <th style="padding:10px;background:#0F172A;color:#FFFFFF;border:1px solid #0F172A;text-align:right;"><span leaf="">{{本期}}</span></th>
    <th style="padding:10px;background:#0F172A;color:#FFFFFF;border:1px solid #0F172A;text-align:right;"><span leaf="">{{变化}}</span></th>
  </tr>
  <tr>
    <td style="padding:10px;color:#334155;border:1px solid #E2E8F0;"><span leaf="">{{数据项}}</span></td>
    <td style="padding:10px;color:#334155;border:1px solid #E2E8F0;text-align:right;"><span leaf="">{{数值}}</span></td>
    <td style="padding:10px;color:#D97706;border:1px solid #E2E8F0;text-align:right;"><span leaf="">{{变化值}}</span></td>
  </tr>
</table>
```

### 2.11 对比卡

```html
<section style="margin:18px 0;padding:17px 18px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:8px;">
  <p style="margin:0 0 12px 0;color:#0F172A;font-size:14px;font-weight:700;"><span leaf="">{{对比主题}}</span></p>
  <p style="margin:0 0 9px 0;color:#475569;font-size:13px;line-height:1.8;"><span leaf=""><strong>{{对象A}}</strong>　{{对比说明占位}}</span></p>
  <p style="margin:0;color:#475569;font-size:13px;line-height:1.8;"><span leaf=""><strong>{{对象B}}</strong>　{{对比说明占位}}</span></p>
</section>
```

### 2.12 风险提示

```html
<section style="margin:18px 0;padding:15px 17px;background:#FFF7ED;border:1px solid #FDBA74;border-radius:8px;">
  <p style="margin:0 0 6px 0;color:#C2410C;font-size:12px;font-weight:700;"><span leaf="">风险提示</span></p>
  <p style="margin:0;color:#7C2D12;font-size:14px;line-height:1.85;"><span leaf="">{{风险说明占位}}</span></p>
</section>
```

### 2.13 方法说明

```html
<section style="margin:18px 0;padding:14px 16px;background:#F1F5F9;border-radius:8px;">
  <p style="margin:0 0 6px 0;color:#334155;font-size:12px;font-weight:700;"><span leaf="">口径说明</span></p>
  <p style="margin:0;color:#64748B;font-size:12px;line-height:1.75;"><span leaf="">{{数据来源、样本范围或统计口径占位}}</span></p>
</section>
```

### 2.14 时间线

```html
<section style="margin:18px 0;padding-left:16px;border-left:2px solid #FCD34D;">
  <p style="margin:0 0 13px 0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><strong style="color:#D97706;">{{时间一}}</strong>　{{事件占位}}</span></p>
  <p style="margin:0 0 13px 0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><strong style="color:#D97706;">{{时间二}}</strong>　{{事件占位}}</span></p>
  <p style="margin:0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><strong style="color:#D97706;">{{时间三}}</strong>　{{事件占位}}</span></p>
</section>
```

### 2.15 引述

```html
<section style="margin:20px 0;padding:18px 20px;background:#0F172A;border-radius:8px;">
  <p style="margin:0;color:#F8FAFC;font-size:16px;line-height:1.8;font-weight:600;"><span leaf="">“{{引述内容占位}}”</span></p>
  <p style="margin:9px 0 0 0;color:#94A3B8;font-size:12px;"><span leaf="">{{引述来源占位}}</span></p>
</section>
```

### 2.16 案例卡

```html
<section style="margin:18px 0;padding:16px 18px;background:#FFFFFF;border:1px solid #E2E8F0;border-radius:8px;">
  <p style="margin:0 0 8px 0;color:#D97706;font-size:11px;font-weight:700;"><span leaf="">CASE {{案例编号}}</span></p>
  <p style="margin:0 0 7px 0;color:#1E293B;font-size:14px;font-weight:700;"><span leaf="">{{案例标题}}</span></p>
  <p style="margin:0;color:#64748B;font-size:13px;line-height:1.8;"><span leaf="">{{案例说明占位}}</span></p>
</section>
```

### 2.17 图片图注

```html
<figure style="margin:18px 0;">
  <img src="{{图片URL}}" alt="报告配图" style="max-width:100%;height:auto;display:block;margin:0 auto;border-radius:6px;">
  <figcaption style="margin-top:7px;color:#64748B;font-size:11px;line-height:1.6;"><span leaf="">{{图片说明与来源占位}}</span></figcaption>
</figure>
```

### 2.18 FAQ

```html
<section style="margin:18px 0;padding:15px 17px;background:#F8FAFC;border-radius:8px;">
  <p style="margin:0 0 7px 0;color:#0F172A;font-size:14px;font-weight:700;"><span leaf="">Q　{{问题占位}}</span></p>
  <p style="margin:0;color:#475569;font-size:13px;line-height:1.85;"><span leaf="">A　{{回答占位}}</span></p>
</section>
```

### 2.19 行动建议

```html
<section style="margin:18px 0;padding:16px 18px;background:#FFFBEB;border-left:4px solid #D97706;border-radius:0 8px 8px 0;">
  <p style="margin:0 0 7px 0;color:#92400E;font-size:12px;font-weight:700;"><span leaf="">下一步建议</span></p>
  <p style="margin:0;color:#78350F;font-size:14px;line-height:1.85;"><span leaf="">{{建议内容占位}}</span></p>
</section>
```

### 2.20 来源与结尾

```html
<section style="margin:24px 0 0 0;padding-top:14px;border-top:1px solid #E2E8F0;">
  <p style="margin:0 0 6px 0;color:#64748B;font-size:11px;line-height:1.7;"><span leaf="">数据来源：{{来源占位}}</span></p>
  <p style="margin:0;color:#94A3B8;font-size:11px;line-height:1.7;"><span leaf="">{{免责声明或口径说明占位}}</span></p>
</section>
```

## 3. 完整文章模板骨架

1. 报告封面
2. 执行摘要
3. 核心指标条
4. 报告章节标题
5. 结论先行卡与正文
6. 图表、数据表、对比卡、时间线按内容插入
7. 风险提示
8. 行动建议
9. 来源与口径说明

## 4. 文章类型配方

| 类型 | 核心组合 | 点缀 |
|---|---|---|
| 行业报告 | 封面 + 摘要 + 指标条 + 图表 + 数据表 + 来源 | 结论卡 |
| 商业分析 | 封面 + 结论先行 + 研究发现 + 对比卡 + 行动建议 | 引述 |
| 数据复盘 | 封面 + 指标条 + 图表 + 数据表 + 风险提示 | 时间线 |
| 运营总结 | 摘要 + 指标条 + 案例卡 + 行动建议 + 来源 | FAQ |
| 市场观察 | 封面 + 结论卡 + 研究发现 + 引述 + 风险 | 时间线 |
| 研究解读 | 方法说明 + 结论卡 + 图表 + FAQ + 来源 | 对比卡 |

## 5. Markdown 映射

| Markdown | 组件 |
|---|---|
| `# 标题` | 报告封面 |
| `## 标题` | 报告章节标题 |
| `### 标题` | 小节标题 |
| 开头 `>` | 执行摘要 |
| 普通段落 | 正文段落 |
| 非开头 `>` | 引述 |
| `---` | 章节分隔 |
| 有序列表 | 研究发现列表 |
| 无序列表 | 要点列表 |
| `![说明](URL)` | 图片图注 |
| 表格 | 数据表 |
| FAQ | FAQ |

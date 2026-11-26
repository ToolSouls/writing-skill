# 公众号排版组件库 —— ToolSoul 科技蓝

> **适用**：AI 工具、产品教程、功能测评、效率方法、科技观察、工具清单。
>
> **设计语言**：白底、蓝色信息锚点、细边框模块、状态条与编号步骤。克制但比石墨极简更有产品感。

## 1. 设计变量

| 变量 | 色值 / 值 |
|---|---|
| 主色 | `#2563EB` |
| 深色 | `#0F172A` |
| 浅底 | `#EFF6FF` |
| 正文 | `#1F2937` |
| 次文 | `#64748B` |
| 分割线 | `#DBEAFE` |
| 强调 | `#06B6D4` |
| 字体 | `pingfang` |
| 圆角 | `12px` |
| 阴影 | 轻阴影，仅关键卡片 |
| 正文下划线 | `border-bottom:2px solid #93C5FD;font-weight:600;` |

## 2. 组件

### 2.1 科技封面

```html
<section style="margin:0 0 18px 0;padding:24px 20px;background:#0F172A;border-radius:12px;box-sizing:border-box;">
  <p style="margin:0 0 12px 0;color:#67E8F9;font-size:11px;letter-spacing:1.5px;"><span leaf="">TOOLSOUL · TECH GUIDE</span></p>
  <p style="margin:0 0 10px 0;color:#FFFFFF;font-size:23px;line-height:1.4;font-weight:700;"><span leaf="">{{主标题}}</span></p>
  <p style="margin:0;color:#CBD5E1;font-size:14px;line-height:1.8;"><span leaf="">{{导语或核心结论}}</span></p>
  <p style="margin:16px 0 0 0;"><span leaf=""><span style="display:inline-block;padding:5px 10px;background:#2563EB;color:#FFFFFF;border-radius:999px;font-size:11px;">{{标签占位}}</span></span></p>
</section>
```

### 2.2 极简目录

```html
<section style="margin:18px 0;padding:16px 18px;background:#F8FAFC;border:1px solid #DBEAFE;border-radius:12px;">
  <p style="margin:0 0 10px 0;color:#2563EB;font-size:12px;font-weight:700;letter-spacing:1px;"><span leaf="">本篇导航</span></p>
  <p style="margin:0 0 7px 0;color:#334155;font-size:13px;line-height:1.7;"><span leaf=""><span style="display:inline-block;width:22px;color:#2563EB;font-weight:700;">01</span>{{章节标题占位}}</span></p>
  <p style="margin:0 0 7px 0;color:#334155;font-size:13px;line-height:1.7;"><span leaf=""><span style="display:inline-block;width:22px;color:#2563EB;font-weight:700;">02</span>{{章节标题占位}}</span></p>
  <p style="margin:0;color:#334155;font-size:13px;line-height:1.7;"><span leaf=""><span style="display:inline-block;width:22px;color:#2563EB;font-weight:700;">03</span>{{章节标题占位}}</span></p>
</section>
```

### 2.3 编号章节标题

```html
<section style="margin:26px 0 14px 0;">
  <p style="margin:0 0 8px 0;"><span leaf=""><span style="display:inline-block;padding:4px 9px;background:#2563EB;color:#FFFFFF;border-radius:6px;font-size:11px;font-weight:700;">{{01}}</span></span></p>
  <p style="margin:0;color:#0F172A;font-size:20px;line-height:1.45;font-weight:700;"><span leaf="">{{章节标题}}</span></p>
  <section style="width:42px;height:3px;background:#06B6D4;border-radius:3px;margin-top:10px;"><span leaf=""><br></span></section>
</section>
```

### 2.4 标签小标题

```html
<section style="margin:22px 0 12px 0;">
  <p style="margin:0;"><span leaf=""><span style="display:inline-block;padding:5px 10px;background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE;border-radius:999px;font-size:12px;font-weight:700;">{{小标题}}</span></span></p>
</section>
```

### 2.5 导语段落

```html
<section style="margin:16px 0;padding:16px 18px;background:#EFF6FF;border-left:4px solid #2563EB;border-radius:0 10px 10px 0;">
  <p style="margin:0;color:#1E3A8A;font-size:15px;line-height:1.9;"><span leaf="">{{导语内容占位}}</span></p>
</section>
```

### 2.6 正文段落

```html
<section style="margin:14px 0;">
  <p style="margin:0;color:#1F2937;font-size:15px;line-height:1.95;"><span leaf="">{{正文内容占位，用<span style="border-bottom:2px solid #93C5FD;font-weight:600;">关键词</span>建立阅读锚点。}}</span></p>
</section>
```

### 2.7 深色观点框

```html
<section style="margin:20px 0;padding:20px;background:#0F172A;border-radius:12px;">
  <p style="margin:0 0 8px 0;color:#67E8F9;font-size:11px;letter-spacing:1px;"><span leaf="">KEY INSIGHT</span></p>
  <p style="margin:0;color:#FFFFFF;font-size:17px;line-height:1.75;font-weight:600;"><span leaf="">{{核心观点占位}}</span></p>
</section>
```

### 2.8 行内强调卡

```html
<section style="margin:16px 0;padding:14px 16px;background:#FFFFFF;border:1px solid #BFDBFE;border-radius:10px;box-shadow:0 4px 16px rgba(37,99,235,0.06);">
  <p style="margin:0 0 6px 0;color:#2563EB;font-size:12px;font-weight:700;"><span leaf="">{{强调标签}}</span></p>
  <p style="margin:0;color:#334155;font-size:14px;line-height:1.85;"><span leaf="">{{强调说明占位}}</span></p>
</section>
```

### 2.9 信息卡

```html
<section style="margin:16px 0;padding:16px 18px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;">
  <p style="margin:0 0 8px 0;color:#0F172A;font-size:14px;font-weight:700;"><span leaf="">{{信息标题}}</span></p>
  <p style="margin:0;color:#475569;font-size:14px;line-height:1.85;"><span leaf="">{{信息说明占位}}</span></p>
</section>
```

### 2.10 提示卡

```html
<section style="margin:16px 0;padding:15px 17px;background:#FFFBEB;border:1px solid #FDE68A;border-radius:10px;">
  <p style="margin:0 0 6px 0;color:#B45309;font-size:12px;font-weight:700;"><span leaf="">注意</span></p>
  <p style="margin:0;color:#78350F;font-size:14px;line-height:1.85;"><span leaf="">{{提示内容占位}}</span></p>
</section>
```

### 2.11 编号步骤

```html
<section style="margin:18px 0;padding:16px;background:#FFFFFF;border:1px solid #DBEAFE;border-radius:12px;">
  <p style="margin:0 0 12px 0;color:#1E3A8A;font-size:12px;font-weight:700;letter-spacing:1px;"><span leaf="">操作步骤</span></p>
  <p style="margin:0 0 12px 0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><span style="display:inline-block;width:25px;height:25px;line-height:25px;text-align:center;background:#2563EB;color:#FFFFFF;border-radius:50%;font-size:12px;font-weight:700;margin-right:8px;">1</span>{{步骤内容占位}}</span></p>
  <p style="margin:0 0 12px 0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><span style="display:inline-block;width:25px;height:25px;line-height:25px;text-align:center;background:#2563EB;color:#FFFFFF;border-radius:50%;font-size:12px;font-weight:700;margin-right:8px;">2</span>{{步骤内容占位}}</span></p>
  <p style="margin:0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><span style="display:inline-block;width:25px;height:25px;line-height:25px;text-align:center;background:#2563EB;color:#FFFFFF;border-radius:50%;font-size:12px;font-weight:700;margin-right:8px;">3</span>{{步骤内容占位}}</span></p>
</section>
```

### 2.12 时间线

```html
<section style="margin:18px 0;border-left:2px solid #BFDBFE;padding-left:18px;">
  <p style="margin:0 0 14px 0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><strong style="color:#2563EB;">{{节点一}}</strong>　{{节点内容占位}}</span></p>
  <p style="margin:0 0 14px 0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><strong style="color:#2563EB;">{{节点二}}</strong>　{{节点内容占位}}</span></p>
  <p style="margin:0;color:#334155;font-size:14px;line-height:1.8;"><span leaf=""><strong style="color:#2563EB;">{{节点三}}</strong>　{{节点内容占位}}</span></p>
</section>
```

### 2.13 图片卡

```html
<figure style="margin:20px 0;padding:12px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;">
  <img src="{{图片URL}}" alt="内容配图" style="max-width:100%;height:auto;display:block;margin:0 auto;border-radius:8px;">
  <figcaption style="margin-top:8px;color:#64748B;font-size:12px;line-height:1.6;text-align:center;"><span leaf="">{{图片说明占位}}</span></figcaption>
</figure>
```

### 2.14 深色代码块

```html
<section style="margin:18px 0;padding:16px 18px;background:#111827;border-radius:10px;">
  <p style="margin:0 0 10px 0;color:#67E8F9;font-size:11px;"><span leaf="">CODE</span></p>
  <p style="margin:0;color:#E5E7EB;font-family:Consolas,monospace;font-size:13px;line-height:1.6;"><span leaf="">{{代码行占位}}</span></p>
  <p style="margin:0;color:#E5E7EB;font-family:Consolas,monospace;font-size:13px;line-height:1.6;"><span leaf="">{{代码行占位}}</span></p>
</section>
```

### 2.15 指标卡

```html
<section style="margin:18px 0;padding:18px;background:#FFFFFF;border:1px solid #DBEAFE;border-radius:12px;text-align:center;">
  <p style="margin:0 0 4px 0;color:#2563EB;font-size:23px;font-weight:700;"><span leaf="">{{88%}}</span></p>
  <p style="margin:0;color:#64748B;font-size:12px;"><span leaf="">{{指标名称占位}}</span></p>
</section>
```

### 2.16 数据对照表

```html
<table style="width:100%;margin:18px 0;border-collapse:collapse;font-size:13px;">
  <tr>
    <th style="padding:10px;background:#EFF6FF;color:#1E3A8A;border:1px solid #DBEAFE;text-align:left;"><span leaf="">{{维度}}</span></th>
    <th style="padding:10px;background:#EFF6FF;color:#1E3A8A;border:1px solid #DBEAFE;text-align:left;"><span leaf="">{{方案A}}</span></th>
    <th style="padding:10px;background:#EFF6FF;color:#1E3A8A;border:1px solid #DBEAFE;text-align:left;"><span leaf="">{{方案B}}</span></th>
  </tr>
  <tr>
    <td style="padding:10px;color:#334155;border:1px solid #E2E8F0;"><span leaf="">{{项目占位}}</span></td>
    <td style="padding:10px;color:#334155;border:1px solid #E2E8F0;"><span leaf="">{{对照内容}}</span></td>
    <td style="padding:10px;color:#334155;border:1px solid #E2E8F0;"><span leaf="">{{对照内容}}</span></td>
  </tr>
</table>
```

### 2.17 检查清单

```html
<section style="margin:18px 0;padding:16px 18px;background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;">
  <p style="margin:0 0 9px 0;color:#166534;font-size:14px;line-height:1.8;"><span leaf="">✓　{{清单项占位}}</span></p>
  <p style="margin:0 0 9px 0;color:#166534;font-size:14px;line-height:1.8;"><span leaf="">✓　{{清单项占位}}</span></p>
  <p style="margin:0;color:#166534;font-size:14px;line-height:1.8;"><span leaf="">✓　{{清单项占位}}</span></p>
</section>
```

### 2.18 FAQ

```html
<section style="margin:18px 0;padding:16px 18px;background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;">
  <p style="margin:0 0 8px 0;color:#0F172A;font-size:14px;font-weight:700;"><span leaf="">Q　{{问题占位}}</span></p>
  <p style="margin:0;color:#475569;font-size:14px;line-height:1.85;"><span leaf="">A　{{回答占位}}</span></p>
</section>
```

### 2.19 作者卡

```html
<section style="margin:24px 0 16px 0;padding:18px;background:#F8FAFC;border-top:3px solid #2563EB;border-radius:0 0 12px 12px;">
  <p style="margin:0 0 6px 0;color:#0F172A;font-size:14px;font-weight:700;"><span leaf="">{{作者名}}</span></p>
  <p style="margin:0;color:#64748B;font-size:13px;line-height:1.8;"><span leaf="">{{作者介绍占位}}</span></p>
</section>
```

### 2.20 结尾 CTA

```html
<section style="margin:20px 0;padding:20px;background:#2563EB;border-radius:12px;text-align:center;">
  <p style="margin:0 0 8px 0;color:#FFFFFF;font-size:17px;font-weight:700;"><span leaf="">{{结尾标题占位}}</span></p>
  <p style="margin:0 0 14px 0;color:#DBEAFE;font-size:13px;line-height:1.8;"><span leaf="">{{互动说明占位}}</span></p>
  <p style="margin:0;"><span leaf=""><span style="display:inline-block;padding:8px 18px;background:#FFFFFF;color:#1D4ED8;border-radius:999px;font-size:12px;font-weight:700;">{{按钮文案占位}}</span></span></p>
</section>
```

## 3. 完整文章模板骨架

1. 科技封面
2. 极简目录（3个以上章节时）
3. 导语段落
4. 编号章节标题
5. 正文段落与行内强调卡交替
6. 按文章类型插入步骤、图片、代码、指标或对照表
7. 深色观点框（全文 1–2 次）
8. 结尾 CTA
9. 作者卡（需要署名时）

## 4. 文章类型配方

| 类型 | 核心组合 | 点缀 |
|---|---|---|
| 教程/操作指南 | 封面 + 目录 + 步骤 + 代码块 + 检查清单 | 提示卡、图片卡 |
| 工具测评 | 封面 + 导语 + 指标卡 + 对照表 + 观点框 | 图片卡、FAQ |
| 工具清单 | 封面 + 目录 + 标签小标题 + 信息卡 + 检查清单 | 行内强调卡 |
| 产品说明 | 封面 + 导语 + 信息卡 + 图片卡 + 对照表 | FAQ、作者卡 |
| 深度分析 | 封面 + 导语 + 正文 + 深色观点框 + 时间线 | 指标卡 |
| 案例复盘 | 封面 + 指标卡 + 时间线 + 对照表 + 观点框 | 图片卡、FAQ |

## 5. Markdown 映射

| Markdown | 组件 |
|---|---|
| `# 标题` | 科技封面 |
| `## 标题` | 编号章节标题 |
| `### 标题` | 标签小标题 |
| 开头 `>` | 导语段落 |
| 普通段落 | 正文段落 |
| 非开头 `>` | 深色观点框 |
| `---` | 分割线（3px 蓝色短线） |
| 有序列表 | 编号步骤 |
| 无序列表 | 检查清单 |
| `![说明](URL)` | 图片卡 |
| 代码块/行内代码 | 深色代码块 |
| 表格 | 数据对照表 |
| FAQ | FAQ |

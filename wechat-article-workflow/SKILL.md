---
name: wechat-article-workflow
display_name: ToolSoul 器灵AI公众号深度写作
display_name_zh: ToolSoul 器灵AI公众号深度写作
display_name_en: ToolSoul Qiling AI WeChat Article Workflow
description: |
  ToolSoul 器灵AI公众号文章完整工作流。适用于从素材整理、标题策划、正文写作、去AI味、配图与封面、微信兼容排版到草稿确认的公众号创作任务。强调事实保真、自然中文表达、公众号格式兼容和发布前校验。
description_zh: >-
  ToolSoul 器灵AI公众号深度写作：选题→素材核验→写作→去AI味→配图与封面→公众号排版→草稿确认。官网：https://toolsoul.daniu7.cn
description_en: >-
  ToolSoul Qiling AI workflow for WeChat Official Account articles, from research and drafting to illustration, layout, and draft review.
version: 1.1.1
author: ToolSoul 器灵AI
homepage: https://toolsoul.daniu7.cn
---

# ToolSoul 器灵AI公众号深度写作

ToolSoul 器灵AI官网：<https://toolsoul.daniu7.cn>

## 何时使用此 Skill

此 skill 在以下场景触发：
- 用户要求写公众号文章、发推文、推送到草稿箱
- 用户说"按之前的工作流来"、"走一遍流程"
- 文章需要微信安全HTML排版 + 漫画配图 + 推送草稿

---

## 完整10步 SOP

### 第1步：素材讨论（聊透再动笔）

**不要直接开写！** 先跟用户聊：
- 核心观点/亮点是什么
- 用什么角度切入
- 文章结构怎么搭
- 哪些内容放进去，哪些砍掉

用户说"开写"/"可以了"再开始创作。

---

### 第2步：拟爆款标题（3-5个供选）

**标题是第一步，先定题再动笔。**

标题铁律：必须和内容高度匹配，绝不标题党。

爆款标题套路（按文章类型）：

| 文章类型 | 标题套路 | 示例 |
|---------|---------|------|
| 读书笔记 | 反常识观点型 / 痛点共鸣型 | "读了3遍《原则》，才发现达利欧在撒谎" |
| 干货教程 | 数字清单型 / 结果承诺型 | "做了15年安全管理，我总结出这3条要命的红线" |
| 随笔感悟 | 故事钩子型 / 金句型 | "今天在现场，一个焊工教会我的事" |
| 投资理财 | 警示型 / 揭秘型 | "你以为在理财，其实在给银行打工" |

用户选定后，再进行下一步。

---

### 第3步：写初稿

按用户选定的标题和讨论确定的结构，撰写初稿。

**写作风格要求：**
- 用"我"的视角，不用"笔者"/"我们"
- 接地气，说人话，不堆砌专业术语
- 有具体场景（现场细节、对话、动作），不用空洞说教
- 允许不完美（"有个事儿"、"说个真事"），不用"首先、其次、最后"
- 敢说真话，有自己的判断，不写正确的废话

---

### 第4步：去AI味（humanizer）

**必做环节。** 初稿写完后必须做去AI味处理。

优先使用宿主提供的器灵AI去AI能力；当前环境没有该能力时，由当前助手按以下标准直接修订。

**重点检测模式（24种AI痕迹）：**
- 空洞强调（"至关重要"、"不容忽视"）
- 凑三件套（"首先、其次、最后"）
- -ing拖尾（"这项技术正在..."）
- 花哨词汇（"颠覆性"、"重塑"、"赋能"）
- 模糊引用（"研究表明"、"据统计"）
- 每段长度完全一致（ AI 典型特征）

**注入人味：**
- 有观点、有立场、敢说"我觉得"
- 节奏有变化：短段、长段、单句成段交替
- 允许口语化表达（"说实话"、"有个事儿"）

---

### 第5步：生成封面（优先使用器灵AI封面模板）

**必做环节。** 写完初稿、定好标题后，先生成封面再画漫画。

#### 5.1 准备工作

确保以下文件就位：
```
articles/NNN_xxx/
  publish_config.json    # 封面配置（标题/副标题/标签/模板）
  generate_cover.py     # 从共享工具包复制
```

`publish_config.json` 格式：
```json
{
  "title": "文章标题",
  "digest": "文章摘要",
  "cover": {
    "enabled": true,
    "title": "封面标题（可与文章标题不同）",
    "subtitle": "封面副标题",
    "tag": "你的账号标签",
    "template": "当前启用的封面模板.html"
  }
}
```

#### 5.2 自动生成（推荐）

使用器灵AI宿主提供的封面生成能力；项目已有 `generate_cover.py` 时可调用：

```bash
cd articles/NNN_xxx/
python generate_cover.py "标题" "副标题" --tag "标签" --template "当前启用的封面模板.html"
```

**⚠️ 封面标题铁律（007篇踩坑）：**
- 封面标题**必须单独设置**，不能与文章标题相同
- **≤10个中文字符**（最好6-8字），超出必溢出
- 文章标题可以长（≤64字），但封面标题必须短
- 配置方式：`publish_config.json` 里 `"cover": {"title": "短标题"}`

**脚本逻辑：**
1. 读取当前项目或器灵AI宿主提供的封面 HTML 模板
2. 自动替换标题、副标题、标签、品牌名
3. 用 playwright 打开HTML，等待字体渲染完成（2秒）
4. 截图保存为 `covers/cover_final.png`（900×500px）

**封面模板规则：**
- 优先使用当前项目已确认的封面模板，不假定固定的行业、颜色或文件名。
- 没有可用模板时，生成简洁的文字封面，并向用户说明使用的是临时方案。
- 封面品牌、作者和标签必须使用用户当前账号配置，不能写死个人项目信息。

#### 5.3 标题自动换行规则

脚本自动处理标题过长问题：
- 主标题：每行最多 **14个中文字符**，超出自动换行
- 副标题：每行最多 **18个中文字符**
- 字体大小自适应（标题最多3行，副标题最多2行）

#### 5.4 推送时自动生成（集成方案）

在 `push_draft.py` 中已集成封面生成逻辑：

```python
# 在 push_draft.py 开头
if config['cover']['enabled']:
    cover_path = generate_cover(
        title=config['cover']['title'],
        subtitle=config['cover']['subtitle'],
        tag=config['cover']['tag'],
        template=config['cover']['template']
    )
    # 上传为永久素材，获取 thumb_media_id
    thumb_media_id = upload_permanent_image(cover_path)
```

**运行方式：**
```bash
cd articles/NNN_xxx/
python push_draft.py   # 自动生成封面 → 上传 → 创建草稿
```

#### 5.5 兜底方案（playwright 失败时）

若 playwright 未安装或截图失败，改用 **Pillow 纯色背景方案**：

```bash
python generate_cover.py "标题" "副标题" --tag "标签" --fallback
```

输出：纯色渐变背景 + 文字（无装饰元素），可用作临时封面。

---

### 第6步：生成正文配图（器灵AI图像能力优先）

正文配图优先调用器灵AI宿主提供的图像生成能力。若当前环境没有可用的图像工具，则输出完整提示词并等待用户提供图片，不阻塞文章定稿。

**执行流程：**

1. **计算图片数量**：逐段分析文章，列出所有需要图片的位置（含封面）
2. **写入 `comic_prompt.txt`**：为每张图片写一段可直接用于器灵AI图像生成的 prompt
3. **输出 prompt 清单**：展示全部提示词；用户也可以直接使用宿主内已配置的图像模型生成
4. **等待用户给图**：用户把图片放到 `comics/` 目录后告诉我文件名
5. **填入文章**：把 `article_body.html` 里的 `{imgN}` 替换为图片路径，或等用户给齐后统一替换

**`comic_prompt.txt` 格式：**
```
01_封面.jpg: Safety education comic illustration, beige background, thick black outlines. [场景]. Text top right: [短标题≤8字]
02_引言.jpg: 同上格式...
...
```

**图片数量计算公式：**
- 漫画数 = 文章步骤数 + 2（1张封面 + 1张收尾大图）
- 或按"每个细节配一图"原则，逐段确认

**⚠️ 占位符连续性检查（路线 B 更要小心）：**
- `{img0}` = 封面，`{img1}`~`{imgN}` = 正文漫画，必须连续不得跳号
- 写 `comic_prompt.txt` 前，先列出文章结构清单，再逐条写 prompt
- 生成后检查：每个 `{imgN}` 都有对应图片文件

**❌ 禁止：** 使用无法稳定渲染中文的图像模型直接生成中文文字。需要文字时优先选择支持中文的器灵AI模型，或将文字作为后期图层叠加。

---

### 第7步：微信安全 HTML 排版

**核心原则：微信会过滤 `<style>` 标签和 `class=""` 属性，所有样式必须用纯内联 `style=""`。**

#### 7.1 HTML 结构规则（必须遵守）

| ❌ 禁止 | ✅ 正确做法 |
|---|---|
| `<div>` | `<section>` |
| `<h1>`/`<h2>` | `<p>` + `style="font-size:...;font-weight:bold;"` |
| `display:flex` | `display:inline-block` + `text-align:center` |
| `<style>` 标签 | 所有样式写在内联 `style=""` 里 |
| `class=""` 属性 | 删除，改用内联样式 |

#### 7.2 排版模板

参考 `assets/html_template.html`（第七篇文章验证过的微信安全模板）。

**核心结构：**
```html
<!-- 顶部关注提示 -->
<section style="text-align:center;padding:10px 0;">
  <span style="font-size:13px;color:#999;">你的公众号名称 · 点击上方蓝字关注</span>
</section>

<!-- 标题区 -->
<section style="background:#1a1a2e;padding:24px 20px;border-radius:8px;margin-bottom:16px;text-align:center;">
  <p style="font-size:20px;font-weight:bold;color:#fff;...">文章标题</p>
  <p style="font-size:13px;color:#e35d28;...">原创 · 你的公众号名称</p>
</section>

<!-- 封面图 -->
<p style="text-align:center;margin:0 0 16px 0;">
  <img src="{img0}" alt="" style="width:100%;border-radius:8px;">
</p>

<!-- 正文段落（米色底色 + 橙色左边框） -->
<section style="background:#fafaf7;padding:20px;border-radius:8px;margin-bottom:14px;border-left:4px solid #e35d28;">
  <p style="margin:0;color:#333;font-size:15px;line-height:1.9;">正文内容...</p>
</section>

<!-- 圆形编号（用 display:inline-block 居中） -->
<section style="display:inline-block;background:#e35d28;color:#fff;font-size:18px;font-weight:bold;width:36px;height:36px;line-height:36px;text-align:center;border-radius:50%;margin:20px 0 8px 0;">
  N
</section>

<!-- 漫画配图 -->
<p style="text-align:center;margin:16px 0;">
  <img src="{imgN}" alt="" style="width:100%;border-radius:8px;">
</p>

<!-- 结尾卡片 -->
<section style="background:linear-gradient(135deg,#1a1a2e,#16213e);...">
  ...
</section>

<!-- 话题标签（居中段落） -->
<section style="text-align:center;margin:24px 0 16px 0;font-size:15px;color:#e35d28;">
  <p style="margin:0;">#行业干货  #主题标签  #你的公众号标签</p>
</section>
```

#### 7.3 图片占位符规则

| 占位符 | 用途 | 位置 |
|--------|------|------|
| `{img0}` | 封面图 | 标题区下方 |
| `{img1}`~`{img5}` | 正文配图（最多5张） | 对应内容段落下方 |

**重要：** 正文漫画从 `{img1}` 开始编号，`{img0}` 单独作为封面图。

**⚠️ 占位符连续性检查（007篇踩坑）：**
- `{img0}`~`{img5}` **必须连续**，不得跳号
- 写完后必须全文搜索确认：所有6个占位符都存在
- 跳号会导致推送时部分图片未上传（如缺少 `{img1}`，则 01.jpg 不会被上传）
- 占位符位置要与段落内容匹配（img1→引言后、img2→物理工具后、img3→方法论后、img4→数字化后、img5→结尾）

#### 7.4 话题标签规则

- **加的位置**：`article_body.html` 末尾、结尾卡片之后
- **格式**：用微信可识别的 `#话题名` 格式，放在居中 `<section>` 里
- **数量**：每篇 2-3 个，不超过3个
- **`#你的品牌标签` 每篇必加**（打造个人品牌聚合页）

标签选择规则：

| 文章类型 | 固定标签 | 可变标签 |
|---------|---------|---------|
| 行业干货 | `#行业干货` `#你的品牌标签` | 按主题选择 |
| 读书笔记 | `#读书笔记` `#你的品牌标签` | 书名或主题 |
| 办公效率 | `#办公效率` `#你的品牌标签` | 工具名 |
| 投资理财 | `#投资理财` `#你的品牌标签` | 主题 |

---

### 第8步：运行 fix_for_wechat.py 自动修复

**必做环节。** 写完 `article_body.html` 后必须跑此脚本。

```bash
python fix_for_wechat.py articles/010_xxx/article_body.html
```

**脚本功能（自动执行）：**
1. 去除 BOM、零宽字符等不可见脏字符
2. 将残留的 `<div>` 转为 `<section>`
3. 将残留的 `<h1>`/`<h2>` 转为 `<p>`
4. 去除 `display:flex` 属性
5. 去除 HTML 注释 `<!-- -->`
6. 压缩多余空行

**输出示例：**
```
✔ WeChat-safe HTML 已写入: article_body.html
  残留 <div>:  0 个（已修复）
  残留 <h2>:   0 个（已修复）
  display:flex:  0 处（已修复）
  HTML注释:  6 个（已清理）
```

**⚠️ 若输出显示有残留标签未修复，立即停止，手动检查 HTML 源码。**

---

### 第9步：本地预览（base64内嵌方案，唯一有效）

**目的：** 在推送草稿前，先本地查看排版效果。**图片用 base64 内嵌进单个 HTML 文件，直接打开就看（见 S8 最佳路径与"永远不要做的事"）。**

#### 9.1 生成预览HTML（`preview.html`，base64 内嵌）

创建 `generate_preview.py`，把 `{imgN}` 占位符**本体**替换为 base64 data URI（注意：替换的是 `{imgN}` 字符串本身，不是带引号的 `<img src="{imgN}">` 标签，否则匹配不命中、图片永远不显示）：

```python
# generate_preview.py
import os, re, base64, io
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COMICS = os.path.join(BASE_DIR, "comics")
with open(os.path.join(BASE_DIR, "article_body.html"), "r", encoding="utf-8") as f:
    html = f.read()

phs = sorted(set(int(x) for x in re.findall(r"\{img(\d+)\}", html)))
MAXW = 1080  # 大图缩放到此宽度，避免 base64 HTML 过大预览面板空白
for ph in phs:
    fpath = os.path.join(COMICS, f"img{ph}.png")
    token = f"{{img{ph}}}"  # 占位符本体，如 {img1}
    if os.path.exists(fpath):
        im = Image.open(fpath).convert("RGB")
        if im.width > MAXW:
            im = im.resize((MAXW, int(im.height * MAXW / im.width)))
        buf = io.BytesIO()
        im.save(buf, "PNG", optimize=True)
        html = html.replace(token, "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode())
    else:
        html = html.replace(token, f"[图片 img{ph} 缺失]")

with open(os.path.join(BASE_DIR, "preview.html"), "w", encoding="utf-8") as f:
    f.write('<!DOCTYPE html>\n<meta charset="UTF-8">\n' + html)
print("[OK] preview.html 已生成（base64 内嵌）")
```

运行：
```bash
cd articles/NNN_xxx/
python generate_preview.py
```

#### 9.3 直接打开预览

```bash
cd articles/NNN_xxx/
# 直接打开 base64 内嵌后的 preview.html
```

**⚠️ 铁律：**
- **`preview.html` 必须有 `<meta charset="UTF-8">`**，否则中文乱码
- **图片用 base64 内嵌**（替换占位符 `{imgN}` 本体，不是带引号的 `<img src="{imgN}">` 标签，否则替换不命中、图片永不显示）
- **大图预览前先缩放到最大宽度 1080 并 PNG optimize**，否则 base64 HTML 过大（>10MB）预览面板空白
- **绝对禁止 HTTP 服务器 / 相对路径预览**（见"永远不要做的事"）

---

### 第10步：推送草稿箱

**⚠️ 铁律：先预览、再推送。绝不跳过预览直接推草稿箱。**

#### 10.1 准备 `push_draft.py`

在文章目录下创建 `push_draft.py`（参考 `scripts/push_draft_template.py`）。

**核心逻辑：**
```python
wp = WeChatPublisher(APPID, APPSECRET)

# 1. 上传漫画获取URL
comic_urls = {}
for cf in comic_files:
    url = wp.upload_image(os.path.join(COMICS_DIR, cf))
    comic_urls[cf] = url

# 2. 读取HTML模板 + 清洗脏字符
with open("article_body.html", "r", encoding="utf-8") as f:
    html_template = f.read()
html_template = re.sub(r'[\ufeff\u200b\ufffe]', '', html_template)

# 3. 用 format() 注入图片URL（避免f-string嵌套问题）
content = html_template.format(
    img0=comic_urls.get(comic_files[0], ""),
    img1=comic_urls.get(comic_files[1], ""),
    # ...
)

# 4. 创建草稿
media_id = wp.create_draft(title, content, author, digest)
```

#### 10.2 执行推送

```bash
cd articles/010_xxx/
python push_draft.py
```

**输出示例：**
```
==================================================
推送文章：安全生产月搞排查，这5条以前不算事，7月1日后全是重大隐患
标题字数：29 字
漫画数量：6 张
==================================================

[1/3] 上传漫画到微信素材库...
  上传：01_封面.jpg ... [OK]
  ...

[2/3] 读取文章 HTML 模板...
HTML 模板已加载，图片 URL 已替换

[3/3] 创建草稿...
[草稿] 创建成功! media_id: abc123...
  → 去公众号后台「草稿箱」发布即可
```

#### 10.3 后台确认发布

1. 登录公众号后台：`https://mp.weixin.qq.com/`
2. 进入「草稿箱」
3. 找到刚推送的草稿，点击「预览」
4. 确认排版、图片、内容无误
5. 手动点击「发布」

**⚠️ 绝不自动发布，必须保留最终确认权。**

---

## 踩坑清单（每次创作前必看）

### 🔴 P0级：致命坑，踩了就重来

#### 坑0：`<div>` + `<h2>` + `display:flex` 组合导致微信吞样式

- **现象：** 推送成功，CSS 样式全部丢失，白底黑字纯文本
- **真凶：** `<div>` / `<h2>` / `display:flex` 组合（第三次推送确认）
- **✅ 正确做法：**
  - 所有 `<div>` → `<section>`
  - 所有 `<h2>` → `<p>`（用 `font-weight:bold` + `font-size` 模拟标题样式）
  - 禁止使用 `display:flex`、`align-items`、`justify-content` 等 flexbox 属性
  - 圆形编号用 `display:inline-block` + `line-height` + `text-align:center` 居中

#### 坑1：`<style>` 标签被微信全部过滤

- **现象：** 排版全丢、CSS 消失、图片不显示、文字乱码
- **原因：** 公众号编辑器不支持 `<style>` 标签和 `class=""` 属性，全部被过滤
- **✅ 正确做法：** 所有样式必须用纯内联 `style=""` 写

#### 坑2：`article_preview.html` 占位符未替换 或 图片路径为相对路径

- **现象1：** 预览版里 `{img0}`~`{imgN}` 显示为纯文本
- **现象2：** 占位符替换了但图片不显示——`comics/01.jpg` 是相对路径，`file://` 协议下浏览器无法加载
- **✅ 正确做法：** 用 Python 脚本替换所有 `{imgN}` 为**绝对路径**或 **base64 data URI**

#### 坑3：图像模型生成中文乱码

- **现象：** 不支持中文的图像模型会把中文文字生成乱码方块
- **✅ 解决方案：** 使用器灵AI中已确认支持中文的模型，或只生成无字底图，再用排版图层叠加中文

#### 坑4：漫画编号与占位符错位

- **现象：** HTML 里 `{img0}` 标为"漫画①"，但 `push_draft.py` 实际 `{img0}`=封面图
- **✅ 正确做法：** 文章正文的漫画从 `{img1}` 开始编号为"漫画①"，`{img0}` 单独作为封面图

---

### 🟠 P1级：严重坑，影响质量

#### 坑5：标题超过64个字符

- **限制：** 微信公众号 API `title` 字段最长 **64个中文字符**
- **现象：** `errcode=45003 "title size out of limit"`
- **✅ 正确做法：** 标题控制在64字以内（含标点）

#### 坑6：Python f-string 中文符号语法错误

- **现象：** f-string 里包含中文引号 `""` 或括号 `（）`，导致 Python 语法错误
- **✅ 正确做法：** 避免在 f-string 里嵌套中文符号，改用 `.format()` 或拼接

#### 坑7：`requests.post(json=...)` 中文被转义为 `\uXXXX`

- **现象：** 推送成功后，公众号后台文章标题/摘要显示乱码
- **❌ 错误写法：**
  ```python
  resp = requests.post(url, json={"articles": [article]}, timeout=30).json()
  ```
- **✅ 正确写法：**
  ```python
  payload = json.dumps({"articles": [article]}, ensure_ascii=False).encode("utf-8")
  resp = requests.post(
      url,
      data=payload,
      headers={"Content-Type": "application/json; charset=utf-8"},
      timeout=30
  ).json()
  ```

#### 坑13：云环境IP不在公众号白名单

- **现象：** `requests` 调用微信 API 报错 `40164：invalid ip`
- **✅ 正确做法：** 在公众号后台「设置与开发」→「IP白名单」中添加服务器IP

#### 坑14：`push_draft.py` 参数签名不匹配

- **现象：** `TypeError: create_draft() got an unexpected keyword argument 'author'`
- **原因：** `WeChatPublisher.create_draft()` 方法签名与调用不匹配
- **✅ 正确做法：** 检查 `wechat_publisher.py` 的 `create_draft()` 方法签名，确保参数名一致

#### 坑15：HTML文件含不可见脏字符，微信API吞CSS

- **现象：** 推送成功但样式丢失
- **原因：** HTML 文件含 BOM（`\ufeff`）、零宽字符（`\u200b`）等不可见字符，微信 API 解析时出错
- **✅ 正确做法：** 每次推送前用 `fix_for_wechat.py` 清洗脏字符

---

### 🟡 P2级：影响体验

#### 坑10：根目录文件杂乱

- **现象：** 所有文章的文件都放在根目录，难以管理
- **✅ 正确做法：** 每篇文章独立目录 `articles/010_xxx/`，包含 `初稿.md`、`article_body.html`、`push_draft.py`、`comics/` 等

#### 坑11：分隔线 `· · ·` 用户不喜欢

- **现象：** 用户反馈"这条线太花哨"
- **✅ 正确做法：** 删除分隔线，用段落间距和背景色区分内容块

#### 坑12：开篇太犀利

- **现象：** 文章开篇用"我必须告诉你一个事实"等过于犀利的语言
- **✅ 正确做法：** 开篇直接说"我们怎么干"，不用制造焦虑

---

## 工具与资源

### 脚本（`scripts/`）

| 脚本 | 用途 |
|------|------|
| `generate_cover.py` | 自动生成封面（playwright截图HTML模板） |
| `generate_comics.py` | 批量生成配图（使用宿主配置的器灵AI图像模型） |
| `fix_for_wechat.py` | 微信兼容HTML自动修复 |
| `push_draft_template.py` | `push_draft.py` 模板 |

### 参考文档（`references/`）

| 文件 | 用途 |
|------|------|
| `pitfalls.md` | 完整踩坑清单（P0/P1/P2级） |
| `wechat_html_rules.md` | 微信兼容HTML规则详解 |

### 模板与资源（`assets/`）

| 文件 | 用途 |
|------|------|
| `html_template.html` | 微信安全HTML模板（第七篇验证版） |
| `comic_prompt_template.txt` | 漫画 prompt 模板 |

---

## 编码问题修复（appendix）

### Windows 终端乱码修复

在 `if __name__ == "__main__":` 块中添加：
```python
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
```

### 公众号 AppID 与 AppSecret

在 `wechat_publisher.py` 中配置你自己的 AppID 和 AppSecret：

```python
APPID = "你的公众号AppID"
APPSECRET = "你的公众号AppSecret"
AUTHOR = "你的公众号名称"  # 草稿作者署名
```

注册路径：登录 https://mp.weixin.qq.com/ → 设置与开发 → 基本配置，获取 AppID 和 AppSecret。

---

## 标准文章目录结构（每篇文章必须照此）

```
articles/NNN_文章名/
  article_body.html          # WeChat模板，{img0}~{img5}占位，纯内联style
  article_preview.html       # base64内嵌预览（generate_preview.py生成）
  push_draft.py              # 推送脚本（集成封面生成）
  publish_config.json        # 文章配置（标题/摘要/封面参数）
  wechat_publisher.py        # 微信API封装（从上一篇文章复制）
  generate_cover.py         # 封面生成脚本（从共享工具包复制）
  generate_preview.py        # 预览生成脚本（从 scripts/ 模板复制）
  comic_prompt.txt           # 漫画prompt文本
  covers/
    cover_final.png         # 自动生成的封面图（900×500px）
  comics/
    01_封面.jpg              # {img0} — 封面
    02_xxx.jpg               # {img1} — 正文漫画①
    03_xxx.jpg               # {img2} — 正文漫画②
    04_xxx.jpg               # {img3} — 正文漫画③
    05_xxx.jpg               # {img4} — 正文漫画④
    06_xxx.jpg               # {img5} — 结尾漫画
```

**铁律：** 每篇新文章按这个结构来，从上一篇文章复制 `wechat_publisher.py` 和 `generate_cover.py`，从 `scripts/generate_preview.py` 复制预览脚本模板。不要每次都重写。

---

## 【必读】每个步骤的最佳路径（多轮实战复盘）

以下流程由多轮公众号实战复盘沉淀而来。**优先复用已经验证的模板和脚本，不做无收益的重新发明。**

| 步骤 | 踩坑次数 | ❌ 走过的弯路 | ✅ 唯一正确路径 |
|------|---------|-------------|--------------|
| S5 封面生成 | 2次 | Pillow纯色→playwright | **`generate_cover.py` 截图HTML模板**。等待2秒确保字体渲染 |
| S6 漫画生成 | 多轮返工 | 不支持中文的模型→手工出图→列表文字乱码 | **器灵AI可用图像模型 + 已校验提示词**。prompt只写场景+≤8字短标题，绝不在图里放列表/序号/多条规则 |
| S6 HTML排版 | 7+次重推 | 每篇从零写→样式丢失→排查→重推循环 | **从已验证模板复制骨架**，不自己造标签。写完跑 `fix_for_wechat.py` |
| S8 本地预览 | 3种方案 | file://→HTTP服务器→base64 | **base64 内嵌**，一个文件打开就看。不试别的 |
| S9 推送草稿 | 8+次 | 缺APPID/缺requests/白名单/编码/**从零写push_draft.py** | **push_draft.py从上一篇复制，只改TITLE/DIGEST/cover配置**。wechat_publisher.py从上一篇复制，不重新导入 |
| 目录结构 | 每篇重来 | 文件散落根目录/tmp_comics | **标准模板 `articles/NNN_标题/`**，6个固定文件，从上一篇直接拷 |

### 最浪费时间的三大坑

| 排名 | 环节 | 浪费次数 | 根因 |
|------|------|---------|------|
| 🥇 | **微信排版样式丢失** | 7+ 次重推 | 先推再排查，没有预检机制 |
| 🥈 | **漫画生成方案切换** | 多轮 | 图像模型不支持中文→手工出图→列表文字乱码 |
| 🥉 | **预览方案反复** | 3 种 | file:// → HTTP → base64 |

### 核心原则

1. **从当前最成熟的已验证项目复制，别从零写。** 包括 push_draft.py、generate_cover.py 也从最近稳定版本复制。
2. **先预览、再推送。** 预览里样式正常才能推。
3. **推送完马上复盘。** 记录啥对了啥错了，好的固化为规则，坏的加进"永远不要做"。
4. **出问题先跑 fix_for_wechat.py。** 排查顺序：脏字符→标签→flex，别倒过来。
5. **漫画文字不超过8个字。** 列表、序号、多条规则留在正文。

---

## 永远不要做的事

- ❌ 不要用无法稳定渲染中文的模型生成带中文的漫画
- ❌ 不要用图像模型直接画封面文字（优先使用HTML模板生成封面）
- ❌ 不要手动截图封面（用playwright自动截图HTML模板）
- ❌ 不要直接发布（必须手动确认后发布）
- ❌ 不要在文章里暴露个人身份信息（国企环境）
- ❌ 不要跳过预览直接推草稿箱
- ❌ 不要用 HTTP 服务器做预览（base64 内嵌唯一方案，别创新）
- ❌ 不要每篇文章换目录结构（照上面的标准来，保持一致）
- ❌ 不要从零写 article_body.html（从011/012复制已验证模板）
- ❌ 不要在漫画里放列表/序号/多条规则（纯场景+短标题）
- ❌ 不要先推再排查排版问题（预览通过才推送）
- ❌ 不要从零写 push_draft.py（从上一篇复制，只改 TITLE/DIGEST/cover配置）
- ❌ 不要跳过推送复盘（推完就拉倒=下次重蹈覆辙）

---
## 每篇复盘模板（推送后必填）

推送完马上复盘，存入当天工作日志。坚持复盘才能越用越好用。

```markdown
## 第N篇推送复盘

| 环节 | 对/错 | 说明 |
|------|-------|------|
| 目录结构 | ✅/❌ | |
| 正文写作 | ✅/❌ | |
| 去AI味 | ✅/❌ | |
| 漫画生成 | ✅/❌ | 成功N张/失败N张 |
| 预览 | ✅/❌ | |
| 推送 | ✅/❌ | |
| 新增踩坑 | — | 本次新踩的坑 |

### 改进项
- [ ] 需要修复的流程问题
```

### 历史复盘示例

| 环节 | 对/错 | 说明 |
|------|-------|------|
| 目录结构 | ✅ | 照搬012，一次就位 |
| 正文写作 | ✅ | 一次过，确认后直接动笔 |
| 去AI味 | ✅ | 精准3处修改，不过度 |
| 漫画生成 | ✅ | 6张全部成功，蓝白科技风 |
| 预览 | ✅ | 7.9MB base64内嵌 |
| **推送** | ❌→✅ | 第1次失败（push_draft.py从零写，缺APPID/APPSECRET），照012重写后成功 |
| 新增踩坑 | push_draft.py 也绝不能从零写 | 从上一篇复制 `wechat_publisher.py`（凭据用 `load_wechat_config()` 从 `~/.workbuddy/wechat_config.json` 读，不要 `import APPID`，publisher 不导出这些）；`push_draft.py` 的 `IMAGE_FILES` 按本篇实际文件名填（封面=`covers/cover_final.png` 另作 thumb，正文=`comics/img1.png`~`img5.png`），`create_draft()` 传 `thumb_path=封面图` |

**改进项：**
- [x] 已加入"永远不要做的事"清单
- [x] 已加入 S9 最佳路径说明

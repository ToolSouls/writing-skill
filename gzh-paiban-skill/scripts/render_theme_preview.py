#!/usr/bin/env python3
"""Render every ```html component in a theme Markdown file into one preview page."""

from __future__ import annotations

import argparse
import html
import pathlib
import re


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("theme_markdown")
    parser.add_argument("output_html")
    args = parser.parse_args()

    source = pathlib.Path(args.theme_markdown).read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", source, re.M)
    title = title_match.group(1).strip() if title_match else "主题预览"
    headings = list(re.finditer(r"^(#{2,4})\s+([^\n]+)$", source, re.M))
    parts = []
    for index, match in enumerate(headings):
        level = len(match.group(1))
        end = len(source)
        for following in headings[index + 1 :]:
            if len(following.group(1)) <= level:
                end = following.start()
                break
        chunk = source[match.end() : end]
        code = re.search(r"```html\s*\n(.*?)```", chunk, re.S)
        if not code:
            continue
        name = html.escape(match.group(2).strip())
        if re.search(
            r"设计变量|完整文章模板|文章类型|Markdown|视觉层级|添加新主题|生成阶段",
            match.group(2),
        ) or re.fullmatch(r"(?:\d+\.\s*)?组件", match.group(2).strip()):
            continue
        component = code.group(1).strip()
        parts.append(
            f'<section class="preview-item"><p class="preview-label">{name}</p>'
            f'<div class="preview-canvas">{component}</div></section>'
        )

    output = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<style>
body{{margin:0;padding:32px;background:#eef2f7;color:#1f2937;font-family:"Microsoft YaHei",sans-serif}}
main{{max-width:760px;margin:0 auto}}
h1{{font-size:24px;margin:0 0 24px}}
.preview-item{{margin:0 0 28px}}
.preview-label{{margin:0 0 8px;font-size:12px;color:#64748b}}
.preview-canvas{{padding:22px;background:#fff;border-radius:12px;box-shadow:0 6px 24px rgba(15,23,42,.08)}}
</style>
</head>
<body><main><h1>{html.escape(title)}</h1>{''.join(parts)}</main></body>
</html>
"""
    path = pathlib.Path(args.output_html)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(f"rendered {len(parts)} components -> {path}")


if __name__ == "__main__":
    main()

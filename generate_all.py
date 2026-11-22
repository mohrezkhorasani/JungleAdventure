# -*- coding: utf-8 -*-
import os
import json
import base64

base_dir = r"f:\DOTNET\FNSymposium\JungleAdventure"

# Read embedded font CSS
font_css_path = r"F:\DOTNET\FNSymposium\embedded_fonts.css"
with open(font_css_path, "r", encoding="utf-8") as f:
    EMBEDDED_FONT_CSS = f.read()

from make_app import SVG_DEFS, DEFAULT_PROJECT_DATA, generate_game_engine_code

# 1. Generate standalone sample game: بازی_ماجراجویی_جنگل.html
game_html = generate_game_engine_code(DEFAULT_PROJECT_DATA)
sample_game_path = os.path.join(base_dir, "بازی_ماجراجویی_جنگل.html")
with open(sample_game_path, "w", encoding="utf-8") as f:
    f.write(game_html)
print(f"Generated {sample_game_path} (size: {os.path.getsize(sample_game_path)} bytes)")

# 2. Base game template with placeholder encoded in Base64 (prevents any HTML parser collision with nested scripts)
default_json_str = json.dumps(DEFAULT_PROJECT_DATA, ensure_ascii=False)
base_template_for_embed = game_html.replace(default_json_str, "__GAME_CONFIG_PLACEHOLDER__")
base_template_b64 = base64.b64encode(base_template_for_embed.encode('utf-8')).decode('ascii')

# 3. Read template for index.html
with open(os.path.join(base_dir, "index_template.html"), "r", encoding="utf-8") as f:
    template_content = f.read()

final_index_html = template_content.replace("__EMBEDDED_FONT_CSS__", EMBEDDED_FONT_CSS)
final_index_html = final_index_html.replace("__DEFAULT_PROJECT_DATA_JSON__", default_json_str)
final_index_html = final_index_html.replace("__BASE_GAME_TEMPLATE_B64__", base_template_b64)

index_path = os.path.join(base_dir, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(final_index_html)
print(f"Generated {index_path} (size: {os.path.getsize(index_path)} bytes)")

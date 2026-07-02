#!/usr/bin/env python3
"""重新生成 assets/images-b64.js（将 bg.png 和 piggy_transparent.png 转为 base64 内联）"""
import base64, os

ASSETS = os.path.join(os.path.dirname(__file__), 'assets')

def to_b64(filename):
    with open(os.path.join(ASSETS, filename), 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

bg_b64    = to_b64('bg.png')
koala_b64 = to_b64('piggy_transparent.png')

out = os.path.join(ASSETS, 'images-b64.js')
with open(out, 'w') as f:
    f.write(f'const IMG_BG    = "data:image/png;base64,{bg_b64}";\n')
    f.write(f'const IMG_KOALA = "data:image/png;base64,{koala_b64}";\n')

print(f'Done! images-b64.js updated.')
print(f'  bg.png:                {len(bg_b64):,} chars')
print(f'  piggy_transparent.png: {len(koala_b64):,} chars')

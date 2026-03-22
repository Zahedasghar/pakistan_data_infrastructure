import os, re, glob

folders = [
    r'D:\RepTemplates\pbs_vision\images',
    r'D:\RepTemplates\pbs_vision\docs\images'
]

for folder in folders:
    for path in glob.glob(os.path.join(folder, '*.svg')):
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        m = re.search(r'viewBox="0 0 (\d+) (\d+)"', text)
        if m and 'width=' not in text:
            w, h = m.group(1), m.group(2)
            text = text.replace('<svg ', f'<svg width="{w}" height="{h}" ', 1)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f'Fixed: {os.path.basename(path)}')
        else:
            has_w = 'width=' in text
            print(f'Skipped (has_width={has_w}): {os.path.basename(path)}')

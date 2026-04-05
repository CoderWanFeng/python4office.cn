import os
with open('./30-01-pdf2docx.md', 'rb') as f:
    data = f.read()

paths = os.listdir('./')
for path in paths:
    if path.endswith('.md') and path not in ['30-01-pdf2docx.md', '30-02-docx2pdf.md', '30-03-ppt2img.md']:
        with open(f'./{path}', "wb")as f:
            f.write(data)
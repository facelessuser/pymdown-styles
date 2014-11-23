import os
import pyg_css_convert as pcc

pth = os.path.dirname(os.path.abspath(__file__))
css = os.path.join(pth, 'stylesheets')
output = os.path.join(pth, 'pymdown_styles')
added = []

for f in os.listdir(css):
    file_pth = os.path.join(css, f)
    name, ext = os.path.splitext(file_pth)
    if ext == '.css':
        pcc.PygmentsCss2Py(file_pth, name, output=output)
        added.append(os.path.basename(name))

with open(os.path.join(output, '__init__.py'), 'w') as f:
    for a in added:
        f.write('from .%s import %sStyle\n' % (a.lower(), a[:1].upper() + a[1:].lower()))

with open('entry_points.py', 'w') as f:
    f.write("entry_points = '''\n[pygments.styles]\n")
    for a in added:
        f.write('%s=pymdown_styles:%sStyle\n' % (a.lower(), a[:1].upper() + a[1:].lower()))
    f.write("'''\n")

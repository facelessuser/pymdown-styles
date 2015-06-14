"""Build the Pygments modules from the CSS."""
import os
import tools.pyg_css_convert as pcc

pth = os.path.dirname(os.path.abspath(__file__))
css = os.path.join(pth, 'stylesheets')
output = os.path.join(pth, 'pymdown_styles')
added = []

for f in os.listdir(output):
    os.remove(os.path.join(output, f))

for f in os.listdir(css):
    file_pth = os.path.join(css, f)
    name, ext = os.path.splitext(file_pth)
    if ext == '.css':
        print('Generating python module for %s...' % os.path.basename(file_pth))
        c2p = pcc.PygmentsCss2Py(file_pth, os.path.basename(name), output=output)
        c2p.convert()
        added.append(os.path.basename(name))

with open(os.path.join(output, '__init__.py'), 'w') as f:
    styles = []
    f.write('"""Import the style modules."""\n')
    for a in added:
        styles.append('    "%sStyle"' % (a[:1].upper() + a[1:].lower()))
        f.write('from .%s import %sStyle\n' % (a.lower(), a[:1].upper() + a[1:].lower()))
    if len(styles) == 1:
        f.write('\n__all__ = (%s,)\n' % styles[0].strip())
    else:
        f.write('\n__all__ = (\n%s\n)\n' % ',\n'.join(styles))

with open('entry_points.py', 'w') as f:
    f.write('"""Entry points for the style module."""\nentry_points = \'\'\'\n[pygments.styles]\n')
    for a in added:
        f.write('%s=pymdown_styles:%sStyle\n' % (a.lower(), a[:1].upper() + a[1:].lower()))
    f.write("'''\n")

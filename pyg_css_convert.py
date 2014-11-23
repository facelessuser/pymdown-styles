"""
pyg_css_convert

Quick and dirty reverse generation of Pygments style module
from the CSS.

Licensed under MIT
Copyright (c) 2014 Isaac Muse <isaacmuse@gmail.com>
"""
import sys
from webcolors import name_to_hex, normalize_hex
from os.path import dirname, abspath, join
import re
from file_strip.comments import Comments
import traceback

__version__ = '1.0.0'

HEADER = '''"""
Reverse generated from CSS back to PY via pyg_css_convert.py
"""
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \\
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


'''

CLASS_START = '''class %sStyle(Style):
    background_color = "%s"  %s
    highlight_color = "%s"   %s

    styles = {
%s
    }
'''

from pygments.token import STANDARD_TYPES as st

tokens = {"hll": "highlight_color"}

for k, v in st.items():
    if v == "":
        continue
    tokens[v] = str(k).replace("Token.", '')

# Convert
RE_STYLES = r'''
    (?:
        (?P<text>^\s*%(prefix)s\s*\{(?P<t_rule>[^}]+?)\}\s*$)|
        (?P<rule>^\s*%(prefix)s\s*\.(?P<class>\w+)\s*\{(?P<c_rule>[^}]+?)\}\s*$)|
        (?P<other>^\s*[^{]+\{[^}]+?\})|
        (?P<invalid>.)
    )
'''


class PygmentsCss2Py(object):
    def __init__(self, css, module, prefix='.highlight', output='.'):
        self.css = css
        self.module = module[:1].upper() + module[1:].lower()
        self.prefix = prefix
        self.output = output
        self.css_style = re.compile(
            RE_STYLES % {"prefix": prefix},
            re.MULTILINE | re.DOTALL | re.VERBOSE
        )

    def get_settings(self, rule):
        obj = {
            "bold": False,
            "italic": False,
            "underline": False,
            "foreground": None,
            "background": None,
            "border": None
        }

        if re.search(r"(?<!-)\bfont-weight\s*:\s*bold", rule) is not None:
            obj["bold"] = True
        if re.search(r"(?<!-)\bfont-style\s*:\s*italic", rule) is not None:
            obj["italic"] = True
        if re.search(r"(?<!-)\btext-decoration\s*:\s*underline", rule) is not None:
            obj["underline"] = True
        m = re.search(r"(?<!-)\bborder\s*:\s*[\d]+px\s*\w+\s*(?P<color>#[a-zA-z\d]{6}|#[a-zA-z\d]{3}|\w+)", rule)
        if m:
            color = m.group('color')
            obj["border"] = normalize_hex(color) if color.startswith('#') else name_to_hex(color)
        m = re.search(r"(?<!-)\bcolor\s*:\s*(?P<color>#[a-zA-z\d]{6}|#[a-zA-z\d]{3}|\w+)", rule)
        if m:
            color = m.group('color')
            obj["foreground"] = normalize_hex(color) if color.startswith('#') else name_to_hex(color)
        m = re.search(r"(?<!-)\bbackground-color\s*:\s*(?P<color>#[a-zA-z\d]{6}|#[a-zA-z\d]{3}|\w+)", rule)
        if m:
            color = m.group('color')
            obj["background"] = normalize_hex(color) if color.startswith('#') else name_to_hex(color)
        return obj

    def process(self, m):
        if m.group('text'):
            obj = self.get_settings(m.group('t_rule'))
            obj["class"] = "text"
            return obj
        elif m.group('rule'):
            c = m.group('class')
            obj = self.get_settings(m.group('c_rule'))
            obj["class"] = c
            return obj
        elif m.group('other'):
            return {"class": "other", "rule": m.group(0)}
        else:
            return {"class": "invalid"}

    def strip_exclusions(self, rules):
        count = 0
        total = len(rules)
        for i in range(0, total):
            item = rules[i]
            compare = item[0]
            sub_compare = None
            for attr in ("bold", "italic", "underline"):
                if attr in item[1]:
                    for x in range(count + 1, total):
                        sibling = rules[x]
                        if sibling[0].startswith(compare):
                            if sub_compare is not None and sibling[0].startswith(sub_compare):
                                # Ignore children of already negative matched
                                # sub-child
                                pass
                            elif attr not in sibling[1]:
                                # Negative matched sub-child
                                sibling[1].append("no" + attr)
                                sub_compare = sibling[0]
                            else:
                                # Match child inherited
                                sibling[1].remove(attr)
                        else:
                            break
            count += 1

    def format_rules(self, rules, undetected, invalid, max_length):
        self.strip_exclusions(rules)
        text = ""
        last = len(rules) - 1
        idx = 0
        for r in rules:
            text += ('        %-' + str(max_length + 1) + 's "%s"') % (r[0] + ":", ' '.join(r[1]))
            if idx != last:
                text += ","
                if r[2] != "":
                    text += "  %s" % r[2]
                text += "\n"
            elif r[2] != "":
                text += "  %s" % r[2]
            idx += 1
        text += "\n\n        # Below are classes that could not be resolved:"
        for undef in undetected:
            text += (
                "\n        # class=.%(class)s "
                "bold=%(bold)s "
                "italic=%(italic)s "
                "underline=%(underline)s "
                "color=%(foreground)s "
                "bg=%(background)s "
                "border=%(border)s"
            ) % undef
        text += "\n\n        # Below are invalid rules:"
        for inv in invalid:
            text += "\n        # %s" % inv
        return text

    def convert(self):
        with open(self.css, "r") as r:
            text = []
            source = Comments('css', False).strip(r.read())
            m = re.search(r"(^\s*|\}\n*\s*)\s*%s\s*\{(?P<b_rule>[^}]+?)\}\s*" % self.prefix, source)
            bg = "#ffffff"
            hl = "#ffffcc"
            fg = "#000000"
            hl_comment = "# <-- Not defined; defaulted"
            bg_comment = "# <-- Not defined; defaulted"
            fg_comment = "# <-- Not defined; defaulted"

            undetected = []
            invalid = []
            max_length = 0

            for m in self.css_style.finditer(source):
                obj = self.process(m)
                if obj is None:
                    continue

                if obj['class'] in ("other", "invalid"):
                    if obj['class'] == "other":
                        invalid.append(obj['rule'])
                    continue

                if obj['class'] == "text":
                    if obj['background'] is not None:
                        bg = obj['background']
                        bg_comment = '# Background'
                    if obj['foreground'] is not None:
                        fg = obj['foreground']
                        fg_comment = '# Foreground'
                    continue

                c = tokens.get(obj['class'], None)
                if c is not None:
                    if obj['class'] == "hll":
                        if obj["background"]:
                            hl = obj['background']
                            hl_comment = "# Highlight Line"
                        continue

                    attr = []
                    if obj["bold"]:
                        attr.append("bold")
                    if obj["italic"]:
                        attr.append("italic")
                    if obj["underline"]:
                        attr.append("underline")
                    if obj["border"]:
                        attr.append("border:%s" % obj["border"])
                    if obj["background"]:
                        attr.append("bg:%s" % obj["background"])
                    if obj["foreground"]:
                        attr.append("%s" % obj["foreground"])

                    text.append([c, attr, ""])
                    length = len(c)
                    if length > max_length:
                        max_length = length
                else:
                    print("ERROR: %s: Unrecognized Class!" % obj["class"])
                    undetected.append(obj)

            text.append(["Text", [fg], fg_comment])
            text.sort()

            with open(join(self.output, "%s.py" % self.module.lower()), "w") as w:
                w.write(
                    HEADER + (
                        CLASS_START % (
                            self.module, bg, bg_comment, hl, hl_comment,
                            self.format_rules(text, undetected, invalid, max_length)
                        )
                    )
                )


if __name__ == "__main__":
    import argparse

    def main():
        parser = argparse.ArgumentParser(prog='pyg_css_convert', description='Convert pygments css to python modules.')
        # Flag arguments
        parser.add_argument('--version', action='version', version="%(prog)s " + __version__)
        parser.add_argument('--debug', '-d', action='store_true', default=False, help=argparse.SUPPRESS)
        parser.add_argument('--prefix', '-p', default='.highlight', help="Prefix before pygments CSS selectors.")
        parser.add_argument('--output-dir', '-o', default=None, help='Output folder for Python module.')
        parser.add_argument('module_name', help='Name of Pygments module.')
        parser.add_argument('css', help='CSS input file.')

        args = parser.parse_args()

        if args.output_dir is not None:
            output = args.output_dir
        else:
            output = dirname(abspath(args.css))
        if output == '':
            output = '.'

        try:
            c2p = PygmentsCss2Py(
                args.css, args.module_name,
                prefix=args.prefix, output=output
            )

            c2p.convert()
            status = True
        except:
            print(traceback.format_exc())
            status = False
        return status

    sys.exit(main())

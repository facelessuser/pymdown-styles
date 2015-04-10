"""
Reverse generated from CSS back to PY via pyg_css_convert.py
"""
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


class TomorrowmorningStyle(Style):
    background_color = "#fcfcfc"  # Background
    highlight_color = "#ffffe6"   # Highlight Line

    styles = {
        Comment:                     "italic #8e908c",
        Comment.Multiline:           "#8e908c",
        Comment.Preproc:             "bold #8e908c noitalic",
        Comment.Single:              "#8e908c",
        Comment.Special:             "#8e908c",
        Error:                       "#c82829",
        Generic.Deleted:             "#c82829",
        Generic.Emph:                "italic",
        Generic.Heading:             "bold #4d4d4c",
        Generic.Inserted:            "#718c00",
        Generic.Prompt:              "bold #8e908c",
        Generic.Strong:              "bold",
        Generic.Subheading:          "bold #3e999f",
        Keyword:                     "bold #8959a8",
        Keyword.Constant:            "#8959a8",
        Keyword.Declaration:         "#8959a8",
        Keyword.Namespace:           "#8959a8",
        Keyword.Pseudo:              "#8959a8",
        Keyword.Reserved:            "#8959a8",
        Keyword.Type:                "#eab700",
        Literal:                     "#f5871f",
        Literal.Date:                "#718c00",
        Literal.Number:              "#f5871f",
        Literal.Number.Bin:          "#f5871f",
        Literal.Number.Float:        "#f5871f",
        Literal.Number.Hex:          "#f5871f",
        Literal.Number.Integer:      "#f5871f",
        Literal.Number.Integer.Long: "#f5871f",
        Literal.Number.Oct:          "#f5871f",
        Literal.String:              "#718c00",
        Literal.String.Backtick:     "#718c00",
        Literal.String.Char:         "#4d4d4c",
        Literal.String.Doc:          "#8e908c",
        Literal.String.Double:       "#718c00",
        Literal.String.Escape:       "#f5871f",
        Literal.String.Heredoc:      "#718c00",
        Literal.String.Interpol:     "#f5871f",
        Literal.String.Other:        "#718c00",
        Literal.String.Regex:        "#718c00",
        Literal.String.Single:       "#718c00",
        Literal.String.Symbol:       "#718c00",
        Name:                        "#4d4d4c",
        Name.Attribute:              "#4271ae",
        Name.Builtin:                "#4271ae",
        Name.Builtin.Pseudo:         "#f5871f",
        Name.Class:                  "bold #c82829",
        Name.Constant:               "#c82829",
        Name.Decorator:              "#3e999f",
        Name.Entity:                 "#4d4d4c",
        Name.Exception:              "bold #c82829",
        Name.Function:               "bold #4271ae",
        Name.Label:                  "#4d4d4c",
        Name.Namespace:              "#4d4d4c",
        Name.Other:                  "#4271ae",
        Name.Property:               "#4d4d4c",
        Name.Tag:                    "#c82829",
        Name.Variable:               "#c82829",
        Name.Variable.Class:         "#c82829",
        Name.Variable.Global:        "#c82829",
        Name.Variable.Instance:      "#c82829",
        Operator:                    "#3e999f",
        Operator.Word:               "#3e999f",
        Punctuation:                 "#4d4d4c",
        Text:                        "#4d4d4c",  # Foreground
        Text.Whitespace:             "#4d4d4c"

        # Below are classes that could not be resolved:

        # Below are invalid rules:
    }

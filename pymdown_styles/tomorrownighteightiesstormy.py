"""Reverse generated from CSS back to PY via pyg_css_convert.py."""
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, Number  # noqa
from pygments.token import Operator, Generic, Whitespace, Punctuation, Other, Literal  # noqa


class TomorrownighteightiesstormyStyle(Style):

    """Pygments style TomorrownighteightiesstormyStyle."""

    background_color = "#232628"  # Background
    highlight_color = "#5a5d5f"   # Highlight Line

    styles = {
        Comment:                     "italic #888888",
        Comment.Multiline:           "#888888",
        Comment.Preproc:             "bold #888888 noitalic",
        Comment.Single:              "#888888",
        Comment.Special:             "#888888",
        Error:                       "#f2777a",
        Generic.Deleted:             "#f2777a",
        Generic.Emph:                "italic",
        Generic.Heading:             "bold #cccccc",
        Generic.Inserted:            "#99cc99",
        Generic.Prompt:              "bold #888888",
        Generic.Strong:              "bold",
        Generic.Subheading:          "bold #66cccc",
        Keyword:                     "bold #cc99cc",
        Keyword.Constant:            "#cc99cc",
        Keyword.Declaration:         "#cc99cc",
        Keyword.Namespace:           "#cc99cc",
        Keyword.Pseudo:              "#cc99cc",
        Keyword.Reserved:            "#cc99cc",
        Keyword.Type:                "#ffcc66",
        Literal:                     "#f99157",
        Literal.Date:                "#99cc99",
        Literal.Number:              "#f99157",
        Literal.Number.Bin:          "#f99157",
        Literal.Number.Float:        "#f99157",
        Literal.Number.Hex:          "#f99157",
        Literal.Number.Integer:      "#f99157",
        Literal.Number.Integer.Long: "#f99157",
        Literal.Number.Oct:          "#f99157",
        Literal.String:              "#99cc99",
        Literal.String.Backtick:     "#99cc99",
        Literal.String.Char:         "#cccccc",
        Literal.String.Doc:          "#888888",
        Literal.String.Double:       "#99cc99",
        Literal.String.Escape:       "#f99157",
        Literal.String.Heredoc:      "#99cc99",
        Literal.String.Interpol:     "#f99157",
        Literal.String.Other:        "#99cc99",
        Literal.String.Regex:        "#99cc99",
        Literal.String.Single:       "#99cc99",
        Literal.String.Symbol:       "#99cc99",
        Name:                        "#cccccc",
        Name.Attribute:              "#6699cc",
        Name.Builtin:                "#6699cc",
        Name.Builtin.Pseudo:         "#f99157",
        Name.Class:                  "bold #f2777a",
        Name.Constant:               "#f2777a",
        Name.Decorator:              "#66cccc",
        Name.Entity:                 "#cccccc",
        Name.Exception:              "bold #f2777a",
        Name.Function:               "bold #6699cc",
        Name.Label:                  "#cccccc",
        Name.Namespace:              "#cccccc",
        Name.Other:                  "#6699cc",
        Name.Property:               "#cccccc",
        Name.Tag:                    "#f2777a",
        Name.Variable:               "#f2777a",
        Name.Variable.Class:         "#f2777a",
        Name.Variable.Global:        "#f2777a",
        Name.Variable.Instance:      "#f2777a",
        Operator:                    "#66cccc",
        Operator.Word:               "#66cccc",
        Punctuation:                 "#cccccc",
        Text:                        "#cccccc",  # Foreground
        Text.Whitespace:             "#cccccc"

        # Below are classes that could not be resolved:

        # Below are invalid rules:
    }

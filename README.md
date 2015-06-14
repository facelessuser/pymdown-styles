# PyMdown Extra Styles
`pymdown-styles` is a package that adds additional styles to Pygments.  It was created for the [PyMdown project](https://github.com/facelessuser/PyMdown), but it can be used by anyone who wants to add the contained styles to Pygments, or just simply grab the CSS.  The idea was to have Pygments generate the CSS for PyMdown.  Also if no CSS was desired, Pygments could just write the style directly into the style attribute of the HTML tags.  If working with the Python module is not needed, then grabbing the CSS should be all you need.

# Included Styles
These are the included styles:

| Style | Description |
|-------|-------------|
| github | Pygments style that Github used to use before 2014 |
| github2014 | Pygments style that was used during 2014 until Github abandoned using Pygments. |
| readthedocs | Read the Docs Pygments style that is used in the [Read the Docs Sphinx theme](https://github.com/snide/sphinx_rtd_theme) which originally comes from [wyrm repo](https://github.com/snide/wyrm). |
| tomorrowmorning | Pygments style from [Aprosopo](https://github.com/facelessuser/Aprosopo) based off the [Tomorrow themes](https://github.com/chriskempson/tomorrow-theme). |
| tomorrownighteightiesstormy | Pygments style from [Aprosopo](https://github.com/facelessuser/Aprosopo) based off the [Tomorrow themes](https://github.com/chriskempson/tomorrow-theme). |

## Adding New Styles
Adding a new style is fairly easy.  Ultimately, this repo expects CSS files.  So if all you have is the CSS, you should be okay.  If you already have a Python module, then you should be able to get the CSS from that with Pygments.

### Starting from a CSS File
To add a new style, the Pygments CSS should be dropped in the `stylesheets` directory.  The style sheets are the only files that should be added; everything else is auto-generated.  The style sheets should also be namespaced with the class `.highlight`; see the other CSS files as examples.

After adding the new style sheet(s), `build_modules.py` should be run.  This will crawl the style sheets and convert them to Python modules in the `pymdown_styles` directory.  Pygments will use those python modules to generate CSS.  The `__init__.py` file will also get updated exposing all of the modules.  Lastly, `entry_points.py` will get updated with the proper entry points that Pygments will look for when loading the styles.

### Starting from a Python Module
If you already have a Python Module, you should convert it to CSS first and drop the CSS module into the project following the steps outlined in [Starting from a CSS File](#staring-from-a-css-file).

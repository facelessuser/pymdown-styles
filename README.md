pymdown-styles
==================

A package created to add additional styles for use in Pygments.  This package was created to be used in the [PyMdown project](https://github.com/facelessuser/PyMdown), but it can be used by anyone who wants to add the contained styles to Pygments.

# Overview
The purpose of this package was to natively add the styles to Pygments via a plugin.  This was so that PyMdown could use 3rd party and native styles without having to directly modify a Pygments installation or add a bunch of code that would conditionally use 3rd party CSS files or Pygments modules.

The idea was to drop in custom CSS files into this package and reverse convert them into Python modules that could extend Pygments via the plugin entry points.  A user could then specify a 3rd party style as if they were native Pygments styles, and Pygments would return the proper CSS style when asked.

# Included Styles
Currently only contains the popular Github styles, and some custom themes from my Sublime Text theme [Aprosopo](https://github.com/facelessuser/Aprosopo), which are variations of [Tomorrow themes](https://github.com/chriskempson/tomorrow-theme).

| Style | Description |
|-------|-------------|
| github | Pygments style that Github used to use before 2014 |
| github2014 | Pygments style that was used during 2014 until Github abandoned using Pygments. |
| tomorrowmorning | Pygments style from [Aprosopo](https://github.com/facelessuser/Aprosopo) based of the [Tomorrow themes](https://github.com/chriskempson/tomorrow-theme). |
| tomorrownighteightiesstormy | Pygments style from [Aprosopo](https://github.com/facelessuser/Aprosopo) based of the [Tomorrow themes](https://github.com/chriskempson/tomorrow-theme). |

## Adding New Styles
To add a new style, the Pygments CSS should be dropped in the `stylesheets` directory.  The style sheets are the only files that should be added, everything else is auto-generated.

After adding the new stylesheet(s), `build_modules.py` should be run.  This will crawl the stylesheets and convert them to Python modules in the `pymdown_styles` directory that will be recognized by Pygments.  The `__init__.py` file will also get updated exposing all of the modules.  Lastly, `entry_points.py` will get updated as well setting the proper entry points that Pygments will look for when loading the styles.

So if all that you have is a Python Module, you should convert it to CSS first and just drop the CSS module into the project.

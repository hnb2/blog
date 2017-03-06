Title: Creating a static site with Pelican part 3
Date: 2017-03-06 17:00
Category: Misc
Tags: github, python, markdown

This article will conclude our serie on Pelican, from [part 2]({filename}/pelican-part2.md) you should be able to create and publish a complete website. Now we will learn how to customize the theme and add some plugins:

 * Change the default theme
 * Customize the theme
 * Setup the plugins environment
 * Generate a sitemap.xml

## Change the default theme

By default, Pelican ships with 2 themes:

 * simple
 * not my idea

You have a large repository of [themes for pelican](https://github.com/getpelican/pelican-themes) which is a collection of submodules into a single repo.

For my current blog I decided to go for [pelican-clean-blog](https://github.com/gilsondev/pelican-clean-blog), it's responsive and well maintained. Here are the steps I took to install it:

Get the theme in my git repository:

 * `mkdir themes`
 * `git submodule add https://github.com/gilsondev/pelican-clean-blog.git themes/pelican-clean-blog`

At this point you should have a new `.gitmodule` file at the root of your project with the following content:

```md
[submodule "themes/pelican-clean-blog"]
    path = themes/pelican-clean-blog
    url = https://github.com/gilsondev/pelican-clean-blog.git
```

Then add the following line in my `pelicanconf.py`:

```py
THEME = 'themes/pelican-clean-blog'
```

After a full regeneration of the content, you should be able to see a whole different website. If it did not worked, make sure you wrote correctly the path in `THEME` or in the `submodule` command.

## Customize the theme

Now at this point, you should have realized that there are a few issues, or that you would like to customize some more.

#### Syntax highlighting issues:

Add the following line in your `pelicanconf.py`:

```py
COLOR_SCHEME_CSS = 'tomorrow_night.css'
```

All possible values are referred in [Code highlights](https://github.com/gilsondev/pelican-clean-blog#code-highlights) on the author's repo.

#### No more links in the footer

Let's create a template for a footer so we can display our `LINKS` in `templates/custom-footer.html`:

```html
{% if LINKS %}
    {% for name,link in LINKS %}
        <a href="{{ link }}">
            {{name}}
        </a>
    {% endfor %}
{% endif %}
```

And now add the following lines in your `pelicanconf.py`:

```py
FOOTER_INCLUDE = 'custom-footer.html'
IGNORE_FILES = [FOOTER_INCLUDE]
EXTRA_TEMPLATES_PATHS = ['templates']
```

This code will register your footer and the path where custom templates can be found. After a full refresh you should be able to see your links again.

## Setup the plugins environment

There is also a large repository of [Pelican plugins](https://github.com/getpelican/pelican-plugins) where you can find either git submodules or directories directly.

Here is how you can setup those plugins in your repo:

 * `mkdir plugins` 
 * `git submodule add https://github.com/getpelican/pelican-plugins.git plugins`

At this point you should have some more lines in your `.gitmodules`:

```md
[submodule "plugins"]
    path = plugins
    url = https://github.com/getpelican/pelican-plugins.git
```

Now you should have access to this huge collection from your directory plugin, let's try to install and use the sitemap plugin next.

## Generate a sitemap.xml

Add the following in your `pelicanconf.py`:

```py
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1.0,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
```

Now Pelican will generate a sitemap.xml for you each time your re-generate the content, you can see it at the following url: [http://localhost:8000/sitemap.xml](http://localhost:8000/sitemap.xml)

This is the end of this 3 part tutorial, I hope it was useful to some of you. Thumbs up to the creator and maintainer of the [pelican-clean-blog](https://github.com/gilsondev/pelican-clean-blog) project !

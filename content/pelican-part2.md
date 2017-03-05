Title: Creating a static site with Pelican part 2
Date: 2017-03-05 12:00
Category: Misc
Tags: github, python, markdown

This article continues where we left in [part 1]({filename}/pelican-part1.md), at this point you should understand how Pelican work and have the skills to create a simple website. This is what we will cover in this part:

 * Adding social media and links
 * Linking to internal content
 * Using images
 * Feed generation
 * Using `typogrify`
 * Using a favicon and robots.txt
 * Integrating Disqus
 * Deploying on netlify

## Social media and links

You can add links which will appear in the footer of your website, if you are using the default theme, it's a simple list of tuples in `pelicanconf.py`.

Example:

```py
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python', 'https://docs.python.org'),
)
```

You can add social media links as well in `pelicanconf.py`, it is using the same format as `LINKS` except that the `url` is parsed to try and display the icon of the social media. The `url` must be one of the following values listed in [the icons directory of the theme](https://github.com/getpelican/pelican/tree/master/pelican/themes/notmyidea/static/images/icons) if you want to have an icon next to your URL.


Example:

```py
SOCIAL = (
    ('Github', 'https://github.com/hnb2'),
)
```

## Linking to internal content

There is a complete writing on [how to link to internal content](http://docs.getpelican.com/en/3.6.3/content.html#linking-to-internal-content), but the quick answer to this is:

```md
This article continues where we left in [part 1]({filename}/pelican-part1.md), at this point...
```

At compilation time, the `{filename}` directive is replaced and concatenated with the path of the article you are targeting.

## Using images

You can either use external images:

```md
![](https://yhatt.github.io/marp/images/marp-screenshot.png)
```

Or you can use local images:

```md
![]({filename}/images/potato.png)
```

Usually you put images in a subdirectory in `content/`.

## Favicon and robots.txt

You can put your favicon and robots.txt file in `content/extra` directory for instance. Then you need to add the following in your `pelicanconf.py`:

```py
STATIC_PATHS = ['extra/favicon.ico', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
```

In `STATIC_PATHS` we define the list of static assets to serve, it also accepts directories. And in `EXTRA_PATH_METADATA` we define where those files should be moved to at compilation time, in this example we put them at the root of the project, which is the logical place for them.

## Feed generation

By default, Pelican generates feeds, but for them to be properly generated and usable for a client, you will need to set your production address in `publishconf.py`:

```py
SITEURL = 'https://developers-notes.netlify.com'
```

## Typogrify

The package typogrify is a set of improvements for the HTML generated content and can be installed through pip:

```
pip install typogrify
```

But I would suggest adding it to `requirements.txt` the way we did for the rest in [part 1]({filename}/pelican-part1.md).

Then to enable it in your project you need to add the following in `pelicanconf.py`:

```py
TYPOGRIFY = True
```

## Disqus

You will need an account on disqus and select the option 'install for a site', you will then get a 'website' which you can refer in the `publishconf.py`:

```py
DISQUS_SITENAME = 'developers-notes'
```

## Deploying on netlify

[Netlify](https://www.netlify.com/) is a website for hosting static websites, they have multiple plans including a __free one for open source projects__ which is what I am currently using.

They have many out of the box support for static website generators like: hugo, jekyll, ... Including Pelican. They wrote a [great guide](https://www.netlify.com/blog/2015/10/15/a-step-by-step-guide-pelican-on-netlify/), I guess you can take it up from 'Connecting to Netlify'. The idea is that Netlify will connect with your github repo and do automatic deployments and more, go through the guide is complete and quick, except for one small 'mistake':

![](https://raw.githubusercontent.com/munkymack/netlify-assets/master/Step5Pelican.png)

When referring the __Build command__, do not write `pelican content`, but instead write `pelican content -s publishconf.py`. Otherwise, everything you wrote in `publishconf.py` would be ignored (analytics, disqus, url for feeds, etc).

## Next

On the next article I will talk about:

 * Customizing/using another theme
 * Using plugins

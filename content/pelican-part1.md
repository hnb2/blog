Title: Creating a static site with Pelican part 1
Date: 2017-03-02 17:00
Category: Misc
Tags: github, python, markdown

After some research on static site generation, I found the [Pelican](https://github.com/getpelican/pelican) project (which is actually 'Calepin' reversed, which means notepad in French, no relations whatsoever to the majestic bird). This is what I am using to manage this blog [hosted on github](https://github.com/hnb2/blog), feel free to go through the source to have an idea of how it works.

In this article, I will explain the basics of Pelican:

 * Setup a project
 * Write articles
 * write pages
 * Development mode
 * Publishing
 * Google Analytics

## Setup a project

I would recommend using python 3 (3.6 is preferred). You can create a requirements.txt at the root of the project with the following:

```
pelican
Markdown
```

Then you can run:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Now you have an environment ready to setup a pelican installation, run: `pelican-quickstart`. You will be asked a couple of questions in interactive mode.

You can modify your `pelicanconf.py` file to complete information you missed in the interactive mode or update the default links in the footer for instance.

## Write content

By default, the content goes in `/content` (duh), and you can write articles using markdown thanks to the dependency we installed earlier.


### Write articles

To create an article, you can create an md file in the '/content' directory and you can start writing markdown.

```md
Title: Creating a static site with Pelican part 1
Date: 2017-03-02 17:00
Category: Misc
Tags: github, python, markdown

After some research...
```

This is the actual header of my article that you can find in the source code. The 4 first lines are [metadata](http://docs.getpelican.com/en/latest/content.html#file-metadata) that Pelican will use to generate the page.

 * Title: will set the title of the page
 * Date: will set the date of the page, depending on your theme, you will only see the year/month/day, not the time.
 * Category: will define the category of the page, depending on your theme each categories will be displayed in the header.
 * Tags: will define a group of tags for the page.

Pelican will generate pages for each tags and each categories, so that you can click on 'python' on the website and you will have a static page with all the articles related to 'python'.


### Write pages

You can create static pages by creating a folder 'pages' in the '/content' folder. The pages will be added by default, depending on your theme, in the header. But you can set `DISPLAY_PAGES_ON_MENU` to  `False` to prevent this from happening.


## Development mode

After running `pelican-quickstart` you should have a nice `Makefile` at the root of your project. Here are the commands I use all the time:

 * `make devserver`: It will launch in the background a web server available on http://localhost:8000 and a file watcher, meaning content is re-generated every time you modify a file in content. I find it less convenient than a server running in the foreground that you can keep in a separate tab/session though, I do not know if there is an option to achieve that.
 * `make stopserver`: It will stop the server running in background.
 * `make clean`: It will clear the content of the '/output' directory completely.

## Publishing

`pelicanconf.py` is useful for base configuration, and `publishconf.py` is used for a live environment, this is where you would set Google Analytics configuration for instance.

To generate production pages, you can run: `make publish`

There are many remote publishing options, like S3, github pages, etc. I am currently using [Netlify](https://www.netlify.com/), which is great for their github integration, I will detail this integration in part 2.


## Google Analytics

You simply need to open `publishconf.py` and uncomment `GOOGLE_ANALYTICS` and set your code starting by `UA-`. The GA javascript snippet will be automatically added in your final HTML pages, but only in publishing mode, not development mode.


## Next

On the next article I will talk about:

 * Netlify integration
 * Disqus integration
 * Feed generation
 * Using typogrify
 * Adding a favicon and robots.txt
 * Using images

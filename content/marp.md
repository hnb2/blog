Title: Writing presentations in Markdown with marp
Date: 2017-03-01 16:00
Category: Tools
Tags: github, markdown

During my time at the university I was introduced to [Latex](https://www.latex-project.org/), and later on to [Beamer](https://www.sharelatex.com/learn/Beamer) which allowed to create very nice presentations (powerpoint style) by using Latex. Quality was near perfect, but I never got used to the syntax. Then, I got my diploma and joined the wonderful corporate world, this is where I completely stopped using Latex: I just do not have time at the office to write and compile a Beamer presentation. I had to fallback on Libre Office (Back then Open Office) and now Google Slides directly integrated in Google Drive. Then, I found out [Marp](https://yhatt.github.io/marp/), I give you the headline: "Create slides with Markdown".

## Writing awesome presentations using Marp

Marp is a desktop application written in coffeescript using Electron, it contains a markdown editor and a live preview on the right side. It interprets very well Markdown, has 2 themes so far ([default](https://speakerdeck.com/yhatt/marp-basic-example) and [Gaia](https://speakerdeck.com/yhatt/introducing-marps-gaia-theme)) and can be exported to PDF.

## Installation

The installation is pretty simple, on the [home page of the project](https://yhatt.github.io/marp/) you have a direct download link, pointing to the latest version (v0.0.10 at the time I am writing those lines). For Linux, you will have a `tar` archive with a `Marp` binary.

But I would advise you to clone the project and install it manually:

 * npm install
 * npm start

 The reason is that there is a pretty good [pull request](https://github.com/yhatt/marp/pull/154) adding support for slide jumping. You can use this branch, it will be much more comfortable during presentation instead of using your mouse of frenetically pressing `UP` or `DOWN`.

## Usage

You can call `./Marp` or `./Marp filename.md` directly. It will open an application with two columns: text editor on the left and live preview on the right.

![](https://yhatt.github.io/marp/images/marp-screenshot.png)

 * To write slides it's just like if you were writing your usual README.md file, except that you need to type `---` to separate slides.
 * Pagination is available, but you can only get the current page number (no total, like: `current_page/total_page`). You need to insert on each slides the following HTML comment `<!-- page_number: true -->`, there are currently no way to do so globally.
 * You can resize your slides with the following HTML comment: `<!-- $size: 16:9 -->`, multiple sizes are available.
 * In case, like me, you like to keep some notes in your presentation, in Marp I simply write HTML comments so that it is visible in the source code, but invisible in the presentation itself.
 * You can switch to the Gaia theme by using the following HTML comment: `<!-- $theme: gaia -->`
 * To export your slides into a PDF, you can simply go to `FIle > Export Slides as PDF...`

Here is an example I wrote:

```md
# Introduction to GIT

##### By Pierre Guillemot - 27/02/2017
###### Comments in the source code

---
<!-- page_number: true -->
# Start from scratch

`git init` <!-- Initializes a git repository in a directory, empty or not. A hidden directory .git will be created, it will contain configuration file and the whole history of the project.-->

---
<!-- page_number: true -->
# Checking the status

`git status` <!-- Display modified files which are indexed in git, and files which are not indexed in git -->

Using a .gitignore file <!-- Hidden file you can create and should index, it will contain a list of file you DO NOT want to index in git -->
```


## My two cents

i already gave a presentation at the office (about Git btw) using this application, I did not had to think about cloning slides or aligning content by drag and drop, nothing. Simply write markdown just like I would do with any readme. The application itself is lightweight and simple, I actually used it only for presentation mode, to keep my notes on the side, I wrote the presentation in VIM (wink wink). The only thing worrying me is that the last commit was end of November 2016, and there are a few PR open, I hope the project is not abandoned as I think it has quite the potential (5000+ stars on github !).

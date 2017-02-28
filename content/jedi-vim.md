Title: Python auto-completion with jedi-vim
Date: 2017-02-28 10:30
Category: Vim
Tags: python, github, vim, programming

I have been using VIM for many years now. I have been introduced to it by a colleague back when I was working in Shanghai, and I fell in love with it (the editor) and no one could make me use anything else. So of course, as a fervent VIM user I like to fiddle with my `.vimrc` and install plugins.

## Python developing in VIM with jedi-vim

I tried recently [jedi-vim](https://github.com/davidhalter/jedi-vim), a VIM plugin to do auto-completion (and more) for python development. This plugin is from the same person that wrote [jedi](https://github.com/davidhalter/jedi), the library for static analysis and code completion in python, ranked over 2500 stars on github.

## Installation

I am running VIM 8.0 on Antergos, I installed it using the package manager `pacman` and I use Pathogen for plugin management. With this context, this is how I installed it on my local machine:

 * I had to remove from my .vimrc the line [`set paste`](https://github.com/davidhalter/jedi-vim/issues/484)
 * I ran the command from the [readme](https://github.com/davidhalter/jedi-vim#manual-installation): cd ~/.vim/bundle/ && git clone --recursive https://github.com/davidhalter/jedi-vim.git
 * I enabled the tab mode by adding this in my .vimrc: `let g:jedi#use_splits_not_buffers = "left"`

 To make sure that jedi-vim was installed without any problems, you can open vim and run `:help jedi-vim`.

## Usage

So, there are multiple way to use this plugin, which are all referenced in the [readme of the project](https://github.com/davidhalter/jedi-vim#features), so I will explain briefly the one I am using on a day to day basis:

PS: by default, `leader` is set to backslash `\` in VIM.

 * The most obvious one being auto-completion which is enabled by default. You can disable it and use `Ctrl + space` manually to trigger the auto-complete. It may as well open documentation in a split or a tab if available. This feature can be disabled if you don't want it.
 * Get a list of all the usage of the name your cursor is on (method, property, ...): `leader + n`
 * Open a module in a split (because I set the `use_splits_not_buffers` earlier): `:Pyimport module_name`
 * Got to the definition of the name your cursor is on: `leader + d`

 I encountered one problem with the last command, it sometimes opens a buffer instead of a split, I do not know the reason why and IF it should happen. As I was not used at all to buffers I had to learn how to use them, so here's a free crash course:

 * Buffers are 'windows' which cover your current window, if you type `:q` (like I did), you will not only close this new 'window' (a.k.a buffer), you will exit VIM completely.
 * To list all buffers type `:buffers`
 * To switch between buffers type `:b buffer_number`

## My two cents

Aside the "sometimes I get a buffer instead of a split" problem I explained earlier, which, again, may be normal but I have not figured out why, I think it's a pretty solid plugin with tons of feature, the autocompletion is pretty fast and the goto functions are very convenient.

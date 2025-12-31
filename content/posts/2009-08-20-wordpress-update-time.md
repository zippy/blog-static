---
title: "wordpress update time & syntax coloring"
date: 2009-08-20
categories: 
  - "geeky"
  - "solutions"
tags: 
  - "syntax-coloring"
  - "wordpress"
slug: "wordpress-update-time"
---

So I've just spent a couple hours updating wordpress to 2.8.4 (it's been a long time since I've done an upgrade) and I'm trying to pick from the myriad syntax coloring plugins.  I tried using [SyntaxHighlighter Plus](http://wordpress.org/extend/plugins/syntaxhighlighter-plus) which has nicer configuration options. But it doesn't look as good as [wp-syntax](http://wordpress.org/extend/plugins/wp-syntax/)

Note that to get the SyntaxHighlighter Plus configuration options to work on my php4 box (I was seeing this error: `Call to undefined function: scandir()`) I had to replace this call:

```
$themes = scandir(ABSPATH . PLUGINDIR . '/syntaxhighlighter-plus/syntaxhighlighter/styles/');

```

with this:

```
$dir = ABSPATH . PLUGINDIR . '/syntaxhighlighter-plus/syntaxhighlighter/styles/';
$dh = opendir($dir);
 while (false !== ($filename = readdir($dh))) {
$themes[] = $filename;
}

```

I actually like the way SyntaxHighlighter Plus works better than wp-syntax in that it uses a custom tag \[sourcecode\] rather than using <pre> which means that it handles embedded angle braces better. But I just think that it looks much worse than wp-syntax!

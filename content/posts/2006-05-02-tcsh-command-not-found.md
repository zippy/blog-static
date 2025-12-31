---
title: "tcsh: command not found"
date: 2006-05-02
categories: 
  - "solutions"
tags: 
  - "commands"
  - "executable"
  - "tcsh"
slug: "tcsh-command-not-found"
---

Have you ever gotten the `tcsh: Command not found.` error after installing some code? Well it happened to me today, and I couldn't figure out what the problem was. I had already added the commands directory into my PATH, and set it to executable with `chmod 755`, but still the error kept coming up. The answer turned out to be that the command file (a shell script) that I had download had DOS line endings. Which, I quicly fixed using my trusty [bbedit](http://barebones.com/products/bbedit/index.shtml) and bingo it worked fine.

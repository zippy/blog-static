---
title: "clojurescript syntax hilighting in emacs"
date: 2011-09-16
categories: 
  - "clojure"
  - "codingsoftware"
  - "solutions"
slug: "clojurescript-syntax-hilighting-in-emacs"
---

To get emacs to syntax color clojurescript files (cljs) add this to your .emacs (or other emacs config file):

```
 (setq auto-mode-alist (cons '("\.cljs" . clojure-mode) auto-mode-alist))
```

---
title: "A \"list items won't wrap\" Firefox css fix!"
date: 2007-04-15
categories: 
  - "codingsoftware"
  - "solutions"
slug: "a-list-items-wont-wrap-firefox-css-fix"
---

The last few days working on the [openmoney.info](http://openmoney.info) website, I've had a major hassle dealing with what appears to be a bug in the html renderer in Firefox.

The issue is that in Firefox, text in a list item won't wrap around a right floated image; like this:

![](/blog/images/eric.png)2. Lorem ipsum dolor sit amet, consectetur adipisicing elit,
3. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Code:

```
<ol style="border: 1px solid #cccccc; width: 300px">
  <img src="/blog/images/eric.png" style="float: right" />
  <li>Lorem ipsum dolor sit amet, consectetur adipisicing elit,</li>
  <li>sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
  ut aliquip ex ea commodo consequat.</li>
</ol>
```

In Safari & Opera the text in the second list item wraps just fine. After an hour of searching the web and trying various things with clear, and in-line, I discovered that the solution was to set the list item width to 100%. In other words, list items take on the width that they start at by default! Crazy. The solution:

```
<ol style="border: 1px solid #cccccc; width: 300px">
  <img src="/blog/images/eric.png" style="float: right" />
  <li>Lorem ipsum dolor sit amet, consectetur adipisicing elit,</li>
  <li style="width:100%">sed do eiusmod tempor incididunt ut labore et
  dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud exercitation
  ullamco laboris nisi ut aliquip ex ea commodo consequat.</li>
</ol>
```

yields nice wrapping text for the second list item:

![](/blog/images/eric.png)2. Lorem ipsum dolor sit amet, consectetur adipisicing elit,
3. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

If you aren't viewing this on Firefox, the above two may look identical. That's the whole point!

\[tags\]css,firefox,list item,wrap\[/tags\]

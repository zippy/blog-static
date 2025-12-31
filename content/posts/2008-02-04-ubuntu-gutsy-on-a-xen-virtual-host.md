---
title: "ubuntu gutsy on a xen virtual host"
date: 2008-02-04
categories: 
  - "codingsoftware"
  - "geeky"
  - "solutions"
slug: "ubuntu-gutsy-on-a-xen-virtual-host"
---

Hey googlers looking for tech-support:

I was trying to install various packages (emacs, etc) from universe on Ubuntu Gutsy (7.10), and I kept getting weird segmentation faults (`Setting up emacsen-common (1.4.17) Segmentation fault`). Turns out that the problem was that my server was being hosted on a VPS running XEN for virtualization, and you have to first install libc6-xen: `apt-get install libc6-xen`

Hope this saves someone the half day that it cost me...

---
title: "git me some solutions"
date: 2008-04-17
categories: 
  - "geeky"
  - "solutions"
slug: "git-me-some-solutions"
---

Well, git definitely takes some gitting used to.

My situation is using git with three team members and a private shared repository that we all pull from and push too.  Additionally our project has a submodule that lives on a public git-hub repository (metaform).

So here are some things I've learned:

- Use rebase. Here's how:
    1. Rebase doesn't work on "dirty" working tree. So you must, either:
        1. Add and commit all you changes.`git commit -a -m 'all my changes'` (assuming that your ok committing them in a single batch). or
        2. Stash your changes away`git stash` (But don't use stash if you have made changes in your submodule ! It'll stash the changes away, but it gets very grumpy when unstashing later.)
    2. Fetch the changes:`git fetch` this should copy the changes from the remote branch (I assume your tracking the defaults here from the clone origin)
    3. Now to rebase: `git rebase origin/master` If you do a git log you should now see your checked in changes at the top of the tree, not somewhere near the bottom where they would be if you had just done a pull.
    4. If you stashed above, then you need to unstash with `git stash apply`
- Submodules that are in active development can be a pain. Here's a gotcha that gotme: When you have made a change to a submodule, checked it in and pushed it, you still need to add this change into your containing repository and commit that, and then do a `git submodule update` This is all well documented, but lets take a concrete example. My submodule is a rails plugin. So just after committing the change in my submodlue `git status` shows that `vendor/plugins/myplugin` is modified. So I use my shell's file completion to add that folder. This gets me: `git add vendor/plugins/myplugin/` notice the trailing slash. This is the gotcha. That causes git add to add all of the contents of the directory as if you wanted to track them directly instead of through the submodule. Erase that trailing slash!

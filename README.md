# Eric's Blog (Static Hugo Site)

Migrated from WordPress at eric.harris-braun.com/blog to Hugo with the Congo theme.

## Local Development

Start the local server:
```bash
~/bin/hugo server -D
```
- Site available at: http://localhost:1313/blog/
- `-D` flag includes draft posts

## Adding a New Post

1. Create a new markdown file in `content/posts/`:
   ```bash
   ~/bin/hugo new posts/YYYY-MM-DD-your-post-slug.md
   ```
   Or manually create a file with this frontmatter:
   ```yaml
   ---
   title: "Your Post Title"
   date: YYYY-MM-DD
   categories:
     - "category-name"
   tags:
     - "tag-name"
   slug: "your-post-slug"
   draft: true
   ---

   Your content here...
   ```

2. Add images to `static/images/` and reference them as `(/blog/images/filename.png)`

3. Preview locally with `~/bin/hugo server -D`

4. When ready to publish, remove `draft: true` from frontmatter

5. Commit and push:
   ```bash
   git add .
   git commit -m "Add new post: your post title"
   git push
   ```

## Deployment

The site is deployed on Cloudflare Pages and auto-deploys when you push to the `main` branch.

### Cloudflare Pages Configuration

- **Build command:**
  ```
  hugo --gc --minify --baseURL https://blog-static-51h.pages.dev/blog/ -d public/blog && echo '/ /blog/ 307' > public/_redirects
  ```
- **Build output directory:** `public`
- **Environment variable:** `HUGO_VERSION` = `0.140.1`

### Key Deployment Notes

1. **URL Structure**: Posts are at `/blog/YYYY/MM/DD/slug/` to match original WordPress URLs

2. **baseURL**: Config has `baseURL = "https://eric.harris-braun.com/blog/"` for production. The Cloudflare build command overrides this for the pages.dev domain.

3. **Hugo outputs to subdirectory**: The `-d public/blog` flag puts all content in `public/blog/` so the site is served at `/blog/` path.

4. **Root redirect**: The `_redirects` file redirects `/` to `/blog/` (307 = temporary redirect).

5. **For production domain**: When setting up `eric.harris-braun.com`, update the build command's `--baseURL` to `https://eric.harris-braun.com/blog/`

## Comments

- Historical WordPress comments are embedded in posts as HTML
- New comments use Giscus (GitHub Discussions-based)
- Giscus config is in `layouts/_partials/comments.html`

## Theme

Using [Congo](https://github.com/jpanther/congo) theme as a git submodule.

To update the theme:
```bash
cd themes/congo
git pull origin main
cd ../..
git add themes/congo
git commit -m "Update Congo theme"
```

## Project Structure

```
blog-static/
├── config/_default/     # Hugo configuration
├── content/posts/       # Blog posts (markdown)
├── layouts/             # Custom layouts (overrides theme)
│   ├── _partials/       # Includes comments.html for Giscus
│   └── partials/        # Theme partial overrides
├── static/images/       # Blog images
└── themes/congo/        # Theme (git submodule)
```

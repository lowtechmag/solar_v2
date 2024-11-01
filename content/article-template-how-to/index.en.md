---
title: "Article Template: How to write articles and translations in Markdown for Hugo?"
date: ""
summary: "This page goes over the specific markdown syntax that should be used to write articles, add translations and comments in the new hugo solar web. "
lang: "en"
authors: ["Marie Verdeil"]
categories: [""]
tags: [""]
unlisted: true
draft: false
featured_image: "image.png"
---

{{% figure src="image.png" %}} 
A screenshot of the markdown file for this page.
{{% /figure %}}

## Table of Contents

- [Files](#files) 
    - [Structure](#structure)
     - [Creating a new article](#folder-name)
    - [Index](#index)
    - [Comments file](#comments-files)
- [Article Syntax](#syntax)
    - [Front Matter](#front-matter)
    - [Syntax rules](#rules)
    - [Main rules](#main-rules)
    - [Internal links](#internal-links)
- [Image shortcodes](#syntax-images)
- [Comments](#syntax-comments)
- [Translations](#translations)
    - [Translations front matter](#translations-front-matter)
    - [Translations internal links](#translations-internal-links)
    - [Translations of site metadata](#translations-meta)
    

## Files {#files}

Each articles lives in the folder `posts` on Gitlab, with the following structure. 

#### **Structure** {#structure}

Each post/article is a folder which contains: 

* the article in english (`index.md`) or (`index.en.md`) 
* the translations (`index.lang.md`)
* the images in the article (`images/`)
* dithered versions of the images (`images/dithers/`)
* comments in various languages (`comments.en.md`) 

Example:

```
how-to-build-a-low-tech-internet/
├── comments.en.md
├── images
│   ├── air-jaldi-epostman.png
│   ├── dithers
│   │   ├── air-jaldi-epostman_dithered.png
│   │   ├── freifunk-wifi-node_dithered.png
│   │   ├── node-air-jaldi-network_dithered.png
│   │   ├── node-spanish-guifi-network_dithered.png
│   │   ├── node-tegola_dithered.png
│   │   ├── sneakernet-on-rails_dithered.png
│   │   ├── tegola-project-low-tech-internet_dithered.png
│   │   ├── wifi-link_dithered.png
│   │   └── wireless-links-spanish-guifi-network_dithered.png
│   ├── freifunk-wifi-node.jpg
│   ├── node-air-jaldi-network.png
│   ├── node-spanish-guifi-network.png
│   ├── node-tegola.jpg
│   ├── sneakernet-on-rails.jpg
│   ├── tegola-project-low-tech-internet.png
│   ├── wifi-link.jpg
│   └── wireless-links-spanish-guifi-network.jpg
├── index.de.md
├── index.en.md
├── index.es.md
└── index.fr.md
```

#### **Folder Name** {#folder-name}

To create on new article, be sure to create a new folder in `posts/` with the name of the article, containing at least:
- 1 index file 
- 1 comments file (see below)
- 1 `images/` folder where your images will live. 


To create an new page that isn't an article, place the folder directly in `content/` or in `content/about/` for the about section. 

By default, your folder name is the article slug. The slug should match the title, but with the following rules. Use `"-"`instead of `" "` spaces and **don't** include special character (no `,=;/%?! &.@` etc.)

```
/posts/my-article-name/index.en.md
```
will become:
```
https://solar.lowtechmagazine.com/YYYY/MM/my-article-name/ 
```


### **Index** {#index}

The article content should be in a file named `index.lang.md`. For an english article it would be `index.en.md`, for french translation  `index.fr.md`, etc.


Regarding the syntax of the index files see the [Syntax section below](#syntax)..


### **Comments file** {#comments-files}

The comments should now be placed in a different file in the article folder. The different comments are separated by languages and will appear in the corresponding article version. Each comments files should be named "comments.lang.md". So for english it would be `comments.en.md`, for dutch  `comments.nl.md`, etc. 

The Comments will appear automatically at the end of the article, no need to add anything in the article file. 

Regarding the syntax of the comments files see the [Comments section below](#syntax-comments).


### **Output**

The folder should look like this at start: 
```
my-article-name/
├── comments.en.md
├── images/ 
│   └── images goes here. 
└── index.lang.md
```


## Syntax {#syntax}

The syntax of the markdown file has a few changes and additions in Hugo, which we will go over in this section. The specific changes related to Translations can be found in the[Translations section below](#translations).

## Front matter data {#front-matter}

The Front matter data at the top of each article should follow the following syntax:

```yaml
---
title: "Article Title"
date: "2015-10-26"
summary: "Article Summary"
lang: "en"
authors: ["Kris De Decker"]
categories: ["Low-tech Solutions"]
tags: ["tag", "tag2"]
translators: [""]
featured_image: "image.png"
draft: false
---
```

**_!Do not forget the `---` at the first and last line of the front matter!_**


- Date should use the following YYYY-MM-DD syntax.
```yaml
date: "2015-10-26"
```

- Language should be using on the following: en (english), nl (dutch), fr (french) pl (polish), pt (portuguese), es (spanish), de (german), it (italian ), vn (vietnamese), ar (arabic), ko (korean). 
To add a different language translations changes in the config file are necessary. 

```yaml
lang: "en"
```

- The authors, tags and translators fields support several entry, using this syntax:
```yaml
authors: ["Kris De Decker"]
authors: ["Kris De Decker", "Roel Roscam Abbing"]
tags: ["ICT", "transportation"] 
```
- The correct spelling for categories is:
 `"Low-tech Solutions"` (Blue), `"High-tech Problems"` (Red),  `"Obsolete Technology"` (Green),  `"About"` or `" "` (BW)



```yaml
categories: ["Low-tech Solutions"]
```

- The featured image will appear as a thumbnail on the category page. Make sure the image is placed inside the `images/` folder. Do not include the file path, just the image with the correct extension (.png, .jpg).
```yaml
featured_image: "image.png"
```
- `draft: false` is the default. Setting this to `draft: true` will not generate the article. It will not be visible on the site anymore, only on gitlab.
```yaml
draft: false
```

_**Always include at least:**_ `title: "", date: "", summary: "Article Summary", lang: "en"`

Other metadata fields are available: 



- `slug: ""` : By default, the slug is the filename but you can overwrite this by adding a slug.
```yaml
slug: "this-is-a-slug"
```

- `unlisted: true` : Include this field to mark the article as unlisted: it will still be accessible via the url but won't be listed in the index page.
```yaml
unlisted: true
```
- `translators: [""]` : see [Translations section below](#translations)
```yaml
translators: [""]
```
## Syntax Rules {#rules}

The rest of of the document uses [regular markdown syntax](https://www.markdownguide.org/cheat-sheet), with a few exception. Markup conventions as follows: 


### **Main rules**

- `## Big headers are h2` and render as:
## (Big headers are h2)

- `### Sub-header are h3` and render as:
### Sub-header are h3 

- `> Quotes` render as:
> Quotes

- `* Lists` /  ` - Lists` render as this list.


* _Footnote references_ use this syntax: `[^number]` and render as [^1]
* _Footnotes_ appear the bottom of the document. The syntax is `[^1]: text`

[^1]: Footnotes appear here the bottom of the document.

- `[Hyperlinks](url)` linking to other websites render as: [Hyperlinks](url)


### **Internal Links**

To link to other articles on the solar website, we use a hugo specific shortcode to call the article folder. This has several advantages: 
1. The url will not break if the article slug changes, since we are calling the file itself. 
2. We don't need to change the url when translating an article, it's automatic: see [translations section](#translations-internal-links). 

- _Shortcode is written as follow and looks like this:_ [Text](/).
```go
[Text]({{</* ref "/path-to-folder" /*>}})
``` 

The file path should start from within the content folder and link to the article or page folder, not the slug!

- _Examples:_
```go
[Donate]({{</* ref "/donate" */>}})
[here]({{</* ref "/posts/power-water-networks/" */>}})
```


* _To link to a section in the article_ (render as: [Link to section](#section).)
```go
[Link to Section](#section)

### Section Header{#section}
```




## Images shortcodes {#syntax-images}

Images now use specific shortcodes instead of the classic markdown syntax. This allows t include a toggle linking to the original images and to embed the caption within the image and better control its styling. 

The shortcode is written: 
``` go
{{%/* figure src="image-1.png" %}} 
Here goes the image caption. 
You can include footnotes [^1], 
[Hyperlinks](https://solar.lowtechmagazine.com), 
and *regular* __markdown__ syntax.
{{% /figure */%}}
```
and render as: 

{{% figure src="image-1.png" %}} 
This is an image of the shortcode that generated it. You can include footnotes [^1], 
[Hyperlinks](https://solar.lowtechmagazine.com), 
and *regular* __markdown__ syntax.
{{% /figure %}}

Captions are handy to include sources and additional info but are also useful for screen-readers users (people who cannot see images). Describing the image is thoughtful of them. 

To render uncompressed images (not dithered and not compressed in `.webp`), use the normal markdown syntax. This comes in handy for comic pages, for example. Please pre-compress the images to prevent overcrowding the server with big files. 
```markdown
![here goes your alt text](image-filename.png)
```


## Comments {#syntax-comments}
 
Comments are now added in a dedicated `comments.lang.md` file, as explained above. 
The file should start with the following lines:
```yaml
---
---
```
Each comment is then added: 
```go
{{</* comment name="Name" >}}

This is the comment text.

{{</ comment */>}}
```
Check out the result [at the bottom](#comments-title)

## Translations {#translations}

To translate an article in a different language, another `index.lang.md` file should be created in the article folder as detailed above. 

### **Front matter** {#translations-front-matter}

Not all front matter should be translated, or the website might give an error. 
- _Front-matter that should be translated:_

```yaml
---
title: "Translate the title"
date: "YYYY-MM-DD" #of the translation
summary: "Translate the Article Summary"
lang: "en" #add the language code (fr, nl, etc.)
translators: ["add translator name", "other translator"]
---
```

- _Front matter that shouldn't change, no matter the language:_
```yaml
---
authors: ["Kris De Decker"]
categories: ["Low-tech Solutions"]
tags: ["tag", "tag2"]
featured_image: "image.png"
draft: false
---
```

### **Internal Links** {#translations-internal-links}

When linking to articles on the website, the shortcode will handle directing to the correct translation automatically: 

On a french article `index.fr.md` the link will redirect to the french [donate](/fr/donate) page. 
```go
[Donate]({{</* ref "/donate" */>}})
```

Another example: this article [Bring back the Horses]({{< ref "/posts/bring-back-the-horses" >}})  isn't yet available in dutch. The shortcode below in a `index.nl.md_ file would lead to the english version, until the dutch translation is available:
```go
[Bring back the Horses]({{</* ref "/posts/bring-back-the-horses" */>}})
```


[^1]:  Footnote that are correctly linked appear here at the bottom of the document. You should use the following syntax for the footnotes: 


### **Translating Site Metadata** {#translations-meta}

Another thing that needs to be translated is the many metadata words used in the website. Such as:

- "Translated by"
- "Written by"
- "View Original Image / View Dithered Image"
- "Subscribe to our Newsletter"
- etc.

This metadata is stored in configuration files called `lang.toml` (`pl.toml`, `fr.toml`, etc.). Find this folder in `solar > i18n > lang.toml`

_The syntax is (here for `nl.toml`):_
```toml
[pagesize]
    other = 'Fill in here the word for page size'
[written_by]
	other = 'Door'
[translated_by]
	other = 'Vertaald door'
```
The `[key]` should not be changed and be the same in every language. 

The most complete files are the french (`fr.toml`) and dutch (`nl.toml`) one, refer to those to know what expressions need translation. Untranslated expressions will default back to english. 


Please reach out _marie @ verdeil . net_ if you have any remaining questions.


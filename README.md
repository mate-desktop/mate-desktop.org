# mate-desktop.org

This repository contains the [Nikola](http://getnikola.com) configuration and content
for <http://mate-desktop.org>.

# Contributing content

If you want to add or edit content on <http://mate-desktop.org> then please submit a
[pull-request](https://help.github.com/articles/using-pull-requests).

## Contributing a new post

The simplest way to contribute a new blog post to the mate-desktop.org
website is to:

  * [Fork](https://help.github.com/articles/fork-a-repo) this repository.
  
  * Copy `blog/20991231template-markdown.md` to a new file, for example:

    cp blog/20991231template-markdown.md blog/20131107my-cool-blog-post.md

  * Edit your new file making sure to change the meta data in the file header. The meta data fields are:
    * `link` is optional but should include the URL to the original article if there is one.
    * `description` is optional an should brefily describe the post.
    * `tags` any tags that are relevant. You **must include the `draft` tag**
    * `date is the intended publication date of the post in the format YYYY/MM/DD HH:MML:SS
    * `title` is the post title
    * `slug` is how the post name will be represented in the URL.
    * `author` is your full name.

  * Commit you changes, [submit a pull-request](https://help.github.com/articles/creating-a-pull-request)
  and one of the website maintainers will review your submission and
  publish it if it is suitable.

If you prefer ReStructuredText to Markdown, then follow the same process
as above but use `blog/20991231template-rest.rst` template file.

## Contributing a translation

To contribute a translated page or blog pot the mate-desktop.org website do the followingl::

  * [Fork](https://help.github.com/articles/fork-a-repo) this repository.

  * Copy the blog post or page you wish to translate to a new file
  with the same filename but ending with the short country code (see below).
  For example, if you want to translate the home page to German you would
  do the following:

    cp pages/index.md pages/index.md.de

  * Translate the meta data as well as the content. However, **do not change the date format**.

  * Commit your changes, [submit a pull-request](https://help.github.com/articles/creating-a-pull-request)
  and one of the website maintainers will review your submission.

Currently supported languages are:

  * bg     Bulgarian
  * ca     Catalan
  * de     German
  * el     Greek [NOT gr!]
  * en     English
  * eo     Esperanto
  * es     Spanish
  * fa     Persian
  * fr     French
  * hr     Croatian
  * it     Italian
  * jp     Japanese
  * nl     Dutch
  * pt_br  Portuguese (Brasil)
  * pl     Polish
  * ru     Russian
  * tr_tr  Turkish (Turkey)
  * zh_cn  Chinese (Simplified)


# The migration

For the benefit of the MATE developers and admins, here is a run down of how
the Wordpress site was migrated to Nikola.

## Python 2.7

Nikola is being power by Python 2.7 and some additional packages were required
on the server.

    sudo apt-get install python2.7-dev libfreetype6-dev libjpeg8-dev libxslt1-dev libxml2-dev libyaml-dev

### What are these requirements for?

  * `python2.7-dev` provides the header files for Python 2.7 so that Python modules 
  with C extensions can be built.

The following are required to build `pillow`, the Python imaging library.

  * libjpeg8-dev
  * libfreetype6-dev

The following are required to build `lxml`, a Python XML library.

  * libxml2-dev
  * libxslt1-dev

The following are required to build `python-coveralls`.

  * libyaml-dev

### virtualenv

[`virtualenv`](http://www.virtualenv.org/en/latest/) is used to create a sandboxed Python
environments, so you don't pollute the system Python. This is how a the `virtualenv` for
Nikola was created.

    cd ~
    curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.10.1.tar.gz
    tar xvfz virtualenv-1.10.1.tar.gz
    cd virtualenv-1.10.1
    sudo python setup.py install

### Install Nikola 6.2.1

Create an environment for Nikola.

    mkdir ~/PythonEnvs
    virtualenv -p python2.7 ~/PythonEnvs/nikola-621

Activate the environment.

    source ~/PythonEnvs/nikola-621/bin/activate

Download Nikola 6.2.1

    mkdir -p ${VIRTUAL_ENV}/src
    cd ${VIRTUAL_ENV}/src
    wget https://github.com/getnikola/nikola/archive/v6.2.1.tar.gz -O nikola-621.tar.gz
    tar zxvf nikola-621.tar.gz
    cd nikola-6.2.1

Install the Nikola requirements.

    pip install cython
    pip install -r requirements-full.txt

Actually install nikola.

    python setup.py install

## Migrate Wordpress to Nikola

Export the Wordpress content.

  * `Tools -> Export -> All Content`

Make sure the Nikola environment is activated.

    source ~/PythonEnvs/nikola-611/bin/activate

Clone the mate-desktop.org Git repository.

    cd ~/Websites
    git clone https://github.com/mate-desktop/mate-desktop.org

Run the migration.

    nikola import_wordpress ~/Downloads/mate.wordpress.2013-10-23.xml ~/Migration

The only interesting log entries form the migration were:

    [2013-10-23T15:26:02Z] WARNING: import_wordpress: Not going to import "Wiki" because it seems to contain no content.
    [2013-10-23T15:26:02Z] WARNING: import_wordpress: Not going to import "Forum" because it seems to contain no content.

`rsync` the migrated files to the git repository.

    rsync -av ~/Migration/ ~/Websites/mate-desktop.org/

Install [html2text](https://github.com/aaronsw/html2text).

    pip install https://github.com/aaronsw/html2text/archive/master.zip

Convert the Wordpress `.wp` faux HTML files to [Markdown](http://daringfireball.net/projects/markdown/)
and correct the image links.

    cd ~/Websites/mate-desktop.org/posts
    for FILE in *.wp; do html2text ${FILE} > `basename ${FILE} .wp`.md; done
    for FILE in *.md; do sed -i 's/\/martin\/Migration//g' ${FILE}; done
    rm *.wp
    cd ~/Websites/mate-desktop.org/stories
    for FILE in *.wp; do html2text ${FILE} > `basename ${FILE} .wp`.md; done
    for FILE in *.md; do sed -i 's/\/martin\/Migration//g' ${FILE}; done
    rm *.wp

The meta data and content were merged using `scripts/merge_meta.sh`.

# The clean up

At this point you have a basic Nikola site that preserves all the 
content (but not the comments) from the Wordpress site. Now the
hacking begins...

# Building and deploying the site

When the site cleanup is complete, Nikola will be integrated with
Git so that any new pushes to the mate-desktop.org Git repository
will automatically trigger a Nikola build and deploy.

In the meantime, here is how Nikola can be run manually. This
assumes you are running as me on the server however.

    source ~/PythonEnvs/nikola-611/bin/activate
    cd ~/Websites/mate-desktop.org
    nikola build
    nikola deploy

# TODO

  * Document how to create posts
  * ~~Clean all content.~~
    * ~~Improve some titles, but retain rediections to old slugs.~~
  * ~~Fix all broken images.~~
  * ~~Posted date on newline.~~
  * ~~Update donation page.~~
  * Add more text the homepage.
    * Floating MATE logo
    * ~~More background~~
    * ~~Recent accomplishments and future direction.~~
    * ~~Pronunciation.~~
    * All the applications, with improved layout.
    * ~~Update screenshot using MATE 1.6~~
  * ~~Navingation to include drop down on Blog for RSS, Tags and Archives and Planet.~~
  * ~~Community page needs link to IRC wiki and Planet.~~
  * ~~Development page needs links to additional resources.~~
  * ~~Add social media buttons.~~
  * Integrate SocialSharePrivacy
    * https://github.com/panzi/SocialSharePrivacy

# W.I.P

**Currently this migration is a work in progress!**

# mate-desktop.org

This repository contains the [Nikola](http://getnikola.com) configuration and content
for <http://mate-desktop.org>.

If you want to add or edit content on <http://mate-desktop.org> then please submit a
[pull-request](https://help.github.com/articles/using-pull-requests).

# The migration

For the benefit of the MATE developers and admins, here is a run down of how
the Wordpress site was migrated to Nikola.

## Python 2.7

Nikola is being power by Poython 2.7 and some additional packages were required
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

### Install Nikola 6.2.0

Create an environment for Nikola.

    mkdir ~/PythonEnvs
    virtualenv -p python2.7 ~/PythonEnvs/nikola-620

Activate the environment.

    source ~/PythonEnvs/nikola-620/bin/activate

Download Nikola 6.2.0

    mkdir -p ${VIRTUAL_ENV}/src
    wget https://github.com/getnikola/nikola/archive/v6.2.0.tar.gz -O ${VIRTUAL_ENV}/src/nikola-620.tar.gz
    cd ${VIRTUAL_ENV}/src
    tar zxvf nikola-620.tar.gz
    cd nikola-6.2.0/    

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
    * More background.
    * Recent accomplishments and future direction.
    * ~~Pronunciation.~~
    * All the applications, with improved layout.
    * ~~Update screenshot using MATE 1.6~~
  * Team links to social profiles
  * Navingation to include drop down on Blog for RSS, Tags and Archives and Planet.
  * ~~Community page needs link to IRC wiki and Planet.~~
  * ~~Development page needs links to additional resources.~~
  * ~~Add social media buttons.~~
  * Add footer with site links?

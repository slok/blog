Creating a blog with Pelican
############################

:date: 2012-10-15 18:00
:tags: howto, static, blog, pelican, python
:category: Blog
:author: Xabier Larrakoetxea
:slug: creating-a-blog-with-pelican

Like I said in my `first post <posts/2012/10/hello-world>`_, this blog is an static blog made with `Pelican <http://blog.getpelican.com/>`_
and `github pages <https://help.github.com/categories/20/articles/>`_. This is awesome, for various reasons, it's simple, tidy, easy, scalable and the best of all, is *funny*. Also Pelican uses `Pygments <http://pygments.org/>`_
for the syntax highlighting and as you know this will be a very techie blog,
so I need the perfect tool for this, and yes, it's Pygments.

To write the posts I use `reStructuredText <http://docutils.sourceforge.net/rst.html>`_, But I could do it in `Markdown <http://daringfireball.net/projects/markdown/>`_, that I love it too. 

And last but not least, the blog is hosted on github pages, so I can track all
the versions of each file, wich means that I have all the version of each post. 
Let's start!


Requirements
------------

- Github account
- Python (>= 2.6)
- Git


Github and GH-pages
-------------------

We need to make a respository. For example ``blog``, so our blog url will be
``user.github.com/blog`` If you want to set a custom domain see the optional_  
section.

The site content to render (HTML, CSS...) needs to be in the gh-pages branch.
This leads to a personal organization of the blog:


Organization
------------

I like to be tidy so the HTML and that stuff will be only in the place that is 
needed: ``gh-pages`` branch, in the master branch I will have all my other things:
settings, fabfile, requirements... 
About this I will talk later.

Right now my ``master`` branch is this::

    .
    |-- README.rst
    |-- fabfile.py
    |-- local_settings.py
    |-- requirements.txt
    |-- settings.py
    `-- src
        |-- images
        `-- posts
            `-- 2012
                `-- 10
                    |-- creating-a-blog-with-pelican.rst
                    `-- hello-world.rst

And only that, the automation, util, config files and the posts. In the other
hand gh-pages has all this, plus the generated html, but I'm not working in that
branch so it doesn't matter to be a mess :)

Installing Python tools
-----------------------

If you already have this tools you can go to the next section:

Install `pip <http://www.pip-installer.org/en/latest/>`_ for managing the python packages::

    $ easy_install pip

Install `Virtualenv <http://www.virtualenv.org/en/latest/>`_ to manage the virtual envs::

    $ pip install virtualenv

To manage easyly the virtualenvs is recommended to install `virtualenwrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_::

    $ pip install virtualenvwrapper

We need to configure virtualenvwrapper with some environment vars, so for example
in your user bashrc (``~/.bashrc``) add this (maybe ``virtualenvwrapper.sh`` is in other
location, change if necessary):

.. code-block:: bash

    #Virtualenvwrapper
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/bin/virtualenvwrapper.sh

After this, log again in a terminal and now you should be able to create a virtualenv. 
If you don't know what is a virtual env. In a few words: An isolated Python system. 
So Now you can install, uninstall and delete all the packages you 
want without messing up the systems Python installation. 
Also is a good choice for testing different versions of a project, Python 
versions included.

We create a virtualenv::

    $ mkvirtualenv blog

This will create and insert us in that virtualenv. After the creation if we 
want to enter in that virtualenv we use::

    $ workon blog

And to leave::
    
    $ deactivate


Installing pelican
------------------

Install pelican, this is obvious::

    $ pip install pelican

If you want to use markdown over reStructuredText, install it, reStructuredText
is installed by default::

    $ pip install markdown

Creating the blog
-----------------

Well we have pelican installed, we are in a virtualenv and now is time to create
the blog. But before start messing up with files. I will explain the steps to 
publish a post. Is very important to understand this flow. 
*In parenthesis is the git branch we are working on*:

- (``master``) Create the post in rst or md (rst and md are abbreviations for resTructuredText and markdown)
- (``master``) Generate the HTML
- (``master``) Check the post in a local server
- (``master``) We could delete the output but dones't matter if we don't because git will ignore with our gitignore file
- (``gh-pages``) Merge master branch
- (``gh-pages``) Generate the HTML
- (``gh-pages``) push all the files (normally all the new HTML)
- (``master``) push all the files (normally only one post)


The first thing is to create the git repository. So we clone the repo from the
first step and enter in the directory::

    $ git clone git@github.com:user/blog.git
    $ cd ./blog

Add this to your .gitignore file::
    
    #Custom
    local_settings.py
    output

If you don't have, create in the root folder a file named ``.gitignore`` file. This
file will ignore all the files that match with the names of the file::

    #Custom
    local_settings.py
    output

    #Python
    *.py[cod]

    # C extensions
    *.so

    # Packages
    *.egg
    *.egg-info
    dist
    build
    eggs
    parts
    bin
    var
    sdist
    develop-eggs
    .installed.cfg
    lib
    lib64

    # Installer logs
    pip-log.txt

    # Unit test / coverage reports
    .coverage
    .tox
    nosetests.xml

    # Translations
    *.mo

    # Mr Developer
    .mr.developer.cfg
    .project
    .pydevproject


Now we will create a pelican settings file called ``local_settings.py``, this file
will not be commited to the git repo, maybe has personal data. But we will upload
a blank template named ``settings.py``, so we create also this one, that has the 
same variables as ``local_settings.py`` but without
the vars data. Edit the data you need 
(You can store the ``local_settings.py`` data in a private gist manually):

.. code-block:: python

    # -*- coding: utf-8 -*-

    AUTHOR = "Chuck norris"
    SITENAME = "chuck's Blog"
    SITEURL = "http://blog.chucknorris.org"
    TIMEZONE = "Europe/Madrid"

    GITHUB_URL = "http://github.com/chucknorris/"
    DISQUS_SITENAME = "xxxxxxxxxxxxxxxxxxxxxx"
    PDF_GENERATOR = False
    REVERSE_CATEGORY_ORDER = True
    LOCALE = "en_US"
    DEFAULT_PAGINATION = 4

    #THEME = "mnmlist"

    FEED_RSS = "feeds/all.rss.xml"
    CATEGORY_FEED_RSS = "feeds/%s.rss.xml"

    LINKS = (("Stalone's blog", "http://stalone.com"),)

    SOCIAL = (("twitter", "http://twitter.com/chucknorris"),
              ("linkedin", "http://www.linkedin.com/in/chucknorris"),
              ("github", "http://github.com/chucknorris"),)

    OUTPUT_PATH = "output"
    PATH = "src/posts"

    ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
    ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

    # static paths will be copied under the same name
    STATIC_PATHS = ["src/images", ]

Now that we have our ``settings.py`` and ``local_settings.py``. 

To generate the static html we use::

    $ pelican -s ./local_settings.py

This will take all the settings and apply, but if we want to override some settings
we could do. For example to specify the ouput we use ``-o``::

    $ pelican -s ./local_settings.py -o /tmp/myBlog    

Creating a post
---------------

To be tidy we create a directory structure of ``/posts/{year}/{month}/`` where
the posts will be written::
    
    $ mkdir -p ./posts/2012/10

Create a post named ``hello-world.rst`` or ``hello-world.md``, that depends on your
preferences of syntax. Add This example and edit as you want, title, user... 
(is in rst)::

    Hello world!
    ##############

    :date: 2012-10-15 23:06
    :tags: helloworld, blog, first
    :category: Blog
    :author: Chuck Norris

    This is our first post!! A classic

    .. code-block:: python

        print("Hello world!")

    See you soon ;)

Save and generate the static blog. If all goes fine. Then we have a new
directory named ``output``, our blog is there, so, to test it , insert there and
run a simple server::

    $ cd ./output
    $ python -m SimpleHTTPServer

Point your browser to ``127.0.0.1:8000`` and you will see the blog. If all is
correct then is time to deploy.


Deploying the blog
------------------

In a previous section I explained the process to deploy, if you have understood
(you should ¬¬) this will be easy. We start the process in the ``master`` branch

Commit all changes in the master branch (the new post), this may vary depends
on the files you haven't commited yet (gitignore, settings...)::

    $ git add .
    $ git commit -m "First post: Hello world"

Push it to master (remember, this doesn't deploy the page, this is our source)::

    $ git push origin master

If we havent the ``gh-pages`` branch we create::

    $ git branch gh-pages

Change to ``gh-pages`` and merge the master branch::
    
    $ git checkout gh-pages
    $ git merge master

Now generate the HTML. But wait! github doesn't know that our webpage is in
``output`` dir, so we need to put our generated HTML in the root of the 
project, to do that we replace the settings outputdir in the command::

    $ pelican -s ./local_settings.py -o ./

We are ready to deploy, commit all and push::
    
    $ git add .
    $ git commit -m "Publish hello world post"
    $ git push origin gh-pages

We change again to our master branch and we are done :)::
    
    $ git checkout master

point your browser to ``you.github.com/blog`` , awesome!!
    
This could be tedious, so we can automate the process with `fabric <http://fabfile.org>`_. I have 
created a fabfile that automates it. See in optional_. section


.. _optional:

Optional
--------

Custom domain
~~~~~~~~~~~~~

If you want a custom domain you have to create in the gh-pages branch a file
called ``CNAME`` and put there your domain. For example::
    
    blog.chucknorris.com

In your domain provider point the domain to ``204.232.175.78`` with a record 
type of ``A``


Automation
~~~~~~~~~~

`Fabric <http://fabfile.org>`_ is a tool, an awesome tool! to automate things, is most used for remote
servers, but also works fine for local automation. put this script in the 
root path of the blog in the master branch. You need fabric installe to use it::

    $ pip install fabric

Now you can use like this:
    
    - fab generate: generates the html for developing (while writing)
    - fab serve: Serves the blog in local
    - fab publish: Does all the process of change, commit and publish gh-pages branch, needs to be in master branch while executing the command

The ``fabfile.py``:

.. code-block:: python
    
    import os
    import time

    from fabric.api import local, lcd, settings
    from fabric.utils import puts

    #If no local_settings.py then settings.py
    try:
        from local_settings import OUTPUT_PATH
        SETTINGS_FILE = "local_settings.py"
    except ImportError:
        from settings import OUTPUT_PATH
        SETTINGS_FILE = "settings.py"


    # Get directories
    ABS_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    ABS_SETTINGS_FILE = os.path.join(ABS_ROOT_DIR, SETTINGS_FILE)
    ABS_OUTPUT_PATH = os.path.join(ABS_ROOT_DIR, OUTPUT_PATH)


    # Commands
    def generate(output=None):
        """Generates the pelican static site"""

        if not output:
            cmd = "pelican -s {0}".format(ABS_SETTINGS_FILE)
        else:
            cmd = "pelican -s {0} -o {1}".format(ABS_SETTINGS_FILE, output)

        local(cmd)


    def destroy(output=None):
        """Destroys the pelican static site"""

        if not output:
            cmd = "rm -r {0}".format(os.path.join(ABS_ROOT_DIR, OUTPUT_PATH))
        else:
            cmd = "rm -r {0}".format(output)

        with settings(warn_only=True):
            result = local(cmd)
        if result.failed:
            puts("Already deleted")


    def serve():
        """Serves the site in the development webserver"""
        print(ABS_OUTPUT_PATH)
        with lcd(ABS_OUTPUT_PATH):
            local("python -m SimpleHTTPServer")


    def git_change_branch(branch):
        """Changes from one branch to other in a git repo"""
        local("git checkout {0}".format(branch))


    def git_merge_branch(branch):
        """Merges a branch in other branch"""
        local("git merge {0}".format(branch))


    def git_push(remote, branch):
        """Pushes the git changes to git remote repo"""
        local("git push {0} {1}".format(remote, branch))


    def git_commit_all(msg):
        """Commits all the changes"""
        local("git add .")
        local("git commit -m \"{0}\"".format(msg))


    def publish():
        """Generates and publish the new site in github pages"""
        master_branch = "master"
        publish_branch = "gh-pages"
        remote = "origin"

        # Push original changes to master
        #push(remote, master_branch)

        # Change to gh-pages branch
        git_change_branch(publish_branch)

        # Merge master into gh-pages
        git_merge_branch(master_branch)

        # Generate the html
        generate(ABS_ROOT_DIR)

        # Commit changes
        now = time.strftime("%d %b %Y %H:%M:%S", time.localtime())
        git_commit_all("Publication {0}".format(now))

        # Push to gh-pages branch
        git_push(remote, publish_branch)

        # go to master
        git_change_branch(master_branch)



I hope you enyoyed and liked doing an awesome static blog
Virtualenvwrapper in Arch Linux
###############################

:date: 2013-10-15 14:15
:tags: howto, python, arch, linux, virtualenv, virtualenvwrapper, pip
:category: Blog
:author: Xabier Larrakoetxea
:slug: Virtualenvwrapper-in-Arch-Linux

It's been almost a year since I wrote my last post, well I hope that the future
of this blog will be more updated :O

Today I pick up My arch linux laptop (I'm a long time user of Slackware) and
the problem basically is that Arch's default Python version is Python3, that's
fine because yo have also Python2 and they can use both at the same time. The 
problem appears when you start messing up with 
`Pip <http://www.pip-installer.org>`_, 
`Virtualenv <http://www.virtualenv.org/>`_ and
`Virtualenwrapper <http://virtualenvwrapper.readthedocs.org/>`_. So here is
this little receipe to get working in a fast and clean way.

Install all the stuff
---------------------

Install Python2 and python3 if you don't have it already::

    # pacman -Sy python2 python3

Install ``pip`` and ``virtualenv`` (for python2) with pacman::

    # pacman -Sy python2-pip python2-virtualenv

Install with pip ``virtualenvwrapper``::

    # pip2 install virtualenvwrapper


Configure virtualenvwrapper
---------------------------

We have installed all the neccessary things, So far so good... let's configure
our virtualenvwrapper adding to our ``/home/$USER/.bashrc`` some lines

.. code-block:: bash

    #Virtualenvwrapper
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Projects
    source /usr/bin/virtualenvwrapper.sh

Lets test it! Open a new console and... OOPS!

.. code-block:: bash
    /usr/bin/python: No module named 'virtualenvwrapper'
    virtualenvwrapper.sh: There was a problem running the initialization hooks. 

    If Python could not import the module virtualenvwrapper.hook_loader,
    check that virtualenv has been installed for
    VIRTUALENVWRAPPER_PYTHON=/usr/bin/python and that PATH is
    set properly.

Let's add the correct path to our Python in the ``bashrc`` before 
``source /usr/bin/virtualenvwrapper.sh`` line:

.. code-block:: bash

    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2

Open a console, and... no errors :D, lets test it::

    $ mkvirtualenv test
    which: no virtualenv in (/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/bin/core_perl)
    ERROR: virtualenvwrapper could not find virtualenv in your path

No problem, add the correct virtualenv to ``bashrc`` before 
``source /usr/bin/virtualenvwrapper.sh`` line:

.. code-block:: bash
    
    export VIRTUALENVWRAPPER_VIRTUALENV=virtualenv2


Last test::

    $ mkvirtualenv test
    New python executable in test/bin/python2
    Also creating executable in test/bin/python
    Installing Setuptools............done.
    Installing Pip...................done.
    (test)$ python --version
    Python 2.7.5

That's it :)

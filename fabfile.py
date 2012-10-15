import os

from fabric.api import local, lcd

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
def generate():
    """Generates the pelican static site"""
    local("pelican -s {0}".format(ABS_SETTINGS_FILE))


def destroy():
    """Destroys the pelican static site"""
    local("rm -r {0}".format(os.path.join(ABS_ROOT_DIR, OUTPUT_PATH)))


def serve():
    """Serves the site in the development webserver"""
    print(ABS_OUTPUT_PATH)
    with lcd(ABS_OUTPUT_PATH):
        local("python -m SimpleHTTPServer")


def git_change_branch(branch):
    """Changes from one branch to other in a git repo"""
    local("git checkout {0}".format(branch))


def git_push(remote, branch):
    """Pushes the git changes to git remote repo"""
    local("git push {0} {1}".format(remote, branch))

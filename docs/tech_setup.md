# Software, tools, etc.

This course requires a number of free services and tools available on Unix/Mac systems. If you're on Windows, see below for options.

> See the [Technical FAQ page](tech_faq.md) if you run into snags and/or [report an issue](https://github.com/stanfordjournalism/stanford-progj-2020/issues).

## Services/Platforms

* Slack: Join the **comm-177p-progj** channel in the [StanfordJournalism][] workspace.
* [GitHub](https://github.com/)

## Windows

Windows users should download the latest "LTS" desktop version from the [Ubuntu downloads page][] and then [install VirtualBox and Ubuntu Linux][].

Then perform the installations below *inside the Ubuntu virtual machine*.

[Ubuntu downloads page]: https://ubuntu.com/download/desktop
[install VirtualBox and Ubuntu Linux]: https://brb.nci.nih.gov/seqtools/installUbuntu.html



## Text Editor

You'll need a text editor designed for working with code. For beginners, we recommend [VSCode][] or [Atom][], although you're free to use other tools of your own choosing.

## Shell Terminal

Mac and Linux both come with terminal programs, which provide a text-based interface to your operating system and related command-line tools. 

On Mac, use `Command + spacebar` to perform a Spotlight search for "terminal".

For a more pleasant shell experience, we strongly recommend installing [iTerm2](https://iterm2.com/).

## Version control

[Git][] is a [version control][] system that we'll use to save and submit all the code and data related to class assignments, exercises and projects.

[version control]: https://en.wikipedia.org/wiki/Version_control

### Mac

For beginner Mac users, install [Homebrew][], a software package manager used on the command line. Then use Homebrew to install git.

Open a Terminal shell (see above) and then run the below commands. Along the way, you'll be prompted to agree to Apple licensing terms and to provide your laptop password.

> Note: The below commands are based on Steps 1-3 of [How to Install Xcode, Homebrew, Git etc.](https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/#laptop-script) See the blog post for more details.

```
xcode-select --install

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew doctor

brew update
brew install git
```

### Linux

Open a terminal shell and run: 

```
sudo apt install git-all
```

## Configure git

After installing [git][] (see above), open a Terminal shell and run the below git configuration commands (**make sure to replace name and email with your own**):

```
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

Use the below commands to ensure the configuration worked:

```
git config --global --get user.name
git config --global --get user.email
```

## Generate ssh keys

SSH keys are a best practice for secure network communications. In our case, we'll use them to more easily transfer code to and from GitHub. 

Follow the instructions under [Generating a new ssh key][]. Do **not set a passphrase** when prompted (just leave it blank). Also, you do **not** have to perform the steps in *Adding your SSH key to the ssh-agent*.


[Generating a new ssh key]: https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key

## Python

**Python 3.5 - 3.7**

Before installing Python, first open a shell and run: `python --version`.

If you have a version between Python 3.5 and 3.7, you're all set.

If you have an older Python version (e.g. 2.7), please follow the Hitchhiker's Guide to Python [install instructions][]. 

### Mac

Follow [these steps][] but skip the installation of Homebrew, which should have been installed earlier when we set up git (see above).

[install instructions]: https://docs.python-guide.org/starting/installation/
[these steps]: https://docs.python-guide.org/starting/install3/osx/#install3-osx



[Atom]: https://atom.io/
[Homebrew]: https://brew.sh/
[git]: https://git-scm.com/
[StanfordJournalism]: https://stanford-r8xo.slack.com/home
[VSCode]: https://code.visualstudio.com/
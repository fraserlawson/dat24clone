# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Installation Check (15 min)

## Part 1. Operating System

You can be a Data Scientist on any operating system. In general, most professionals choose a UNIX-type OS; typically Apple's OS X or a popular Linux distribution, such as Ubuntu. If you're already using Mac or Linux, great! Skip ahead to Part 2 and get started with your installs.

However, there is a growing need for (and interest in) Data Science in industries that traditionally use PCs. If you're on a Windows machine, that's OK too! You'll just need to install an additional piece of software to provide a development environment similar to OS X and Linux.

Click [here to download the Git Bash shell](https://gitforwindows.org/). This will allow you to emulate most of the common commands and functions native to OS and Linux systems.

## Part 2. Anaconda Installation

In this course, we'll be working closely with tools that utilize the Python programming language. Anaconda is a popular cross-platform tool that helps install and manage Python-related data science libraries.

1) [Download Anaconda](https://docs.anaconda.com/anaconda/install/) and follow the installation instructions package for your operating system. Please make sure that you're downloading the latest stable version for Python 3 (3.6)! <br>

2) Agree to the terms and let Anaconda complete its default installation. <br>

3) Once installed, navigate to your command line (on OS X, this is the terminal application; on Windows, use your new `Git Bash` shell) and confirm that it's installed by typing in the `which conda` command. <br>

You should see:

```bash
$ which conda
/Users/USERNAME/anaconda3/bin/conda
```
  - If the command line returns a file path (like in the example below), you've successfully installed Anaconda.
  - If the command line returns nothing (and sends you back to the prompt), check in with your instructor.
    - **Note**: Your file path may look different.
    - **Note**: You'll often see commands that look like: `$ which conda` above — when you see those, type in everything **except** the dollar sign. The dollar sign is used to denote a code prompt in your window.

4) Once installed, run the following command to ensure that some frequently used libraries are installed. Anaconda may also update your packages at this time (which is OK!). <br>

```bash
conda install jupyter notebook python matplotlib nltk numpy pip setuptools scikit-learn scipy statsmodels
```

## Part 3. Git Configuration

1) To check if your Git installation was successful, open a new terminal window and try to run Git from the command line: <br>

```bash
$ git --version
```

The output should be something like this:

```bash
$ git --version
git version 2.5.0
```

2) Next, you'll need to provide Git with your name and email. Make sure to use the same email address that you registered at [https://git.generalassemb.ly](https://git.generalassemb.ly): <br>

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email your.name@example.com
```

These identifiers will be added to your commits and show up when you push your changes to [GitHub](https://git.generalassemb.ly) from the command line!

### Optional: Set Up SSH for Easier Remote Connection

While you can connect your local repositories (the work on your laptop) to remote repositories (those stored on [GitHub](https://git.generalassemb.ly)) without much additional effort, this will prompt you to input your username and password quite  frequently. However, there's an alternative known as SSH, which will let you create a file on your computer that will authenticate you to [GitHub](https://git.generalassemb.ly) without entering your username and password over and over again. 

**Note**: Remember, these steps are optional. If you're having trouble, feel free to chat w your instructor!

#### Using SSH and SSH Agent (Recommended)

You can use these guides to get started:

- [Working with SSH Key Passphrases](https://help.github.com/articles/working-with-ssh-key-passphrases/)
- [Generating a New SSH Key and Adding it to the SSH Agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [Adding a New SSH Key to Your GitHub Account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)

#### What is Secure Shell (SSH)?

SSH, or Secure SHell, is a common means of adding an additional layer of security to a connection. It establishes authenticity between a client and a server. This can be useful for secure file sharing and remote application access.

#### How SSH Works

There are a couple of steps to the high-level SSH process:

- A client makes a request to the server.
- A server responds by asking for authentication.
- A client provides authentication.
- If authentication is correct, a connection is established.

+++
title = "the command line"
shorttitle = "command line"
subsections = ["introduction"]
subsections_weight = 2
date = "2016-12-28T03:15:42-06:02"
+++
Most of the programs you're used to running have graphical interfaces.
Take the file manager for example
(on Windows it used to be called Windows Explorer. I think now it's called
File Explorer):

![file manager](/media/prog/file_manager.png)

Information about your files is displayed to you visually. You can click on things
to interact with the program. But did you know there's another way to
get this information? You'll need to open a program that will let you
type commands instead of just using your mouse. It will depend on your
operating system.

**Windows**

The program you need is called the Command Prompt. Open the search bar
and type `cmd.exe`, then run the first one that comes up. On Windows 7
it looks like this (it won't be too much different on Windows 10):

![cmd.exe on Windows](/media/prog/windows_cmd2.png)

**Linux or Mac OS X**

Search or look for an application called Terminal. In Linux, it might
be in the Applications -> Accessories menu. It should look something
like this:

![Linux terminal](/media/prog/linux_terminal.png)

**Command line crash course**

Whatever your operating system, you should have a little box you can
type into now. I use Linux, so my examples will have Linux commands.
Often, the commands are the same for Windows and OS X. I'll tell you
if the commands are different.

In your little black box, type `ls` (on Windows, type `dir`). After
hitting enter, you'll get a list of files and folders (also called
directories):

```
jacob@ubuntu:~$ ls
archive  comp     family      misc   notes     Webcam
church   Desktop  learn_prog  music  pictures
```

In the file manager, you can double click on a folder to move into it.
Here, we use the `cd` (change directory) command. It's the same on
Windows too.

```
jacob@ubuntu:~$ cd music/
jacob@ubuntu:~/music$ ls
archive  guitar   m4a          originals  playlists  videos
dump     library  old_archive  phone      sheet
```

Notice how after we used `cd`, our new "current directory" is
displayed right before that dollar sign:

```
jacob@ubuntu:~/music$
```

This line is called a "prompt." It gives you some helpful
information and it indicates that the terminal is ready for you to
type a command. On windows, it looks something like this:

```
C:\Users\jacob\Music>
```

When you see my examples, anything after the prompt is what you should
type. Lines that don't have the prompt are the output from whatever
command you used.

You can `cd` into multiple directories by using a slash:

```
jacob@ubuntu:~$ cd music/library
jacob@ubuntu:~/music/library$
```

{{% tip %}}
You don't need to type out the entire directory name every time. Type a few
characters and then hit Tab. The rest of the word will be autocompleted for
you!
{{% /tip %}}

`cd ..` will change back to the "parent directory":

```
jacob@ubuntu:~/music/library$ cd ..
jacob@ubuntu:~/music$ 
```

There are many more commands, but this is enough to get you started.
On the next page, I'll show you how to run a Python program from this
command line interface.

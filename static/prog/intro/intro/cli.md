+++
title = "the command line"
shorttitle = "command line"
subsections = ["introduction"]
subsections_weight = 2
date = "2016-12-28T03:15:42-06:02"
draft = true
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


<a href="#lintut" class="btn btn-info" data-toggle="collapse">Show Linux/OS X
tutorial</a>
<div id="lintut" class="collapse">

Search or look for an application called Terminal. In Linux, it might
be in the Applications -> Accessories menu. It should look something
like this:

![Linux terminal](/media/prog/linux_terminal.png)

Type `ls`. After hitting enter, you'll get a list of files and folders
(also called directories):

<pre>
jacob@ubuntu:~$ <b>ls</b>
archive  comp     family      misc   notes     Webcam
church   Desktop  learn_prog  music  pictures
</pre>

In the file manager, you can double click on a folder to move into it.
In the command line, we use the `cd` (change directory) command.
After `cd` you type the name of the directory you want to move into,
e.g. `cd documents`.

Notice above that one of the directories shown by `ls` is the `music`
directory. I can move into it like so:

<pre>
jacob@ubuntu:~$ <b>cd music/</b>
jacob@ubuntu:~/music$ <b>ls</b>
archive  guitar   m4a          originals  playlists  videos
dump     library  old_archive  phone      sheet
</pre>

Try using `ls` and `cd` to move into a different directory on your
computer.

Notice that after I used `cd`, my new "current directory" is displayed
right before that dollar sign:

<pre>
jacob@ubuntu:~/music$
</pre>

This line is called a "prompt." It gives you some helpful
information and it indicates that the terminal is ready for you to
type a command.

If you want to get back to your starting directory, you can type `cd
..`.

<pre>
jacob@ubuntu:~/music$ <b>cd ..</b>
jacob@ubuntu:~$
</pre>

Try using `cd` to move around the directories on your computer.

There are many more commands, but this is enough to get you started.
On the next page, I'll show you how to run a Python program from this
command line interface.
</div>

<a href="#wintut" class="btn btn-info" data-toggle="collapse">Show
Windows tutorial</a>
<div id="wintut" class="collapse">

{{% note %}}
There is a video at the end of this tutorial that demonstrates the
following information. Try to understand the tutorial first, and then
use the video to clear up any questions you have.
{{% /note %}}

The program you need is called the Command Prompt. Open the search bar
and type `cmd.exe`, then run the first one that comes up. On Windows 7
it looks like this (it won't be too much different on Windows 10):

![cmd.exe on Windows](/media/prog/windows_cmd2.png)

In your little black box, type `dir`. After
hitting enter, you'll get a list of files and folders (also called
**dir**ectories):

<pre>
C:\users\jacob><b>dir</b>
Volume in drive C has no label.
Volume Serial Number is 0000-0000

Directory of C:\users\jacob

  4/7/2017  11:28 PM  &lt;DIR>         .
  5/8/2016   5:11 PM  &lt;DIR>         ..
  5/8/2016   5:11 PM  &lt;DIR>         AppData
  7/1/2016  10:24 PM  &lt;DIR>         Application Data
  5/8/2016   5:11 PM  &lt;DIR>         Contacts
 5/30/2016   3:29 PM  &lt;DIR>         Cookies
 2/14/2017   5:26 PM  &lt;DIR>         Desktop
  5/8/2016   5:11 PM  &lt;DIR>         Downloads
  5/8/2016   5:11 PM  &lt;DIR>         Favorites
  5/8/2016   5:11 PM  &lt;DIR>         Links
  5/8/2016   5:11 PM  &lt;DIR>         Local Settings
  5/8/2016   5:11 PM  &lt;DIR>         NetHood
  5/8/2016   5:11 PM  &lt;DIR>         PrintHood
  5/8/2016   5:11 PM  &lt;DIR>         Recent
  5/8/2016   5:11 PM  &lt;DIR>         Saved Games
  5/8/2016   5:11 PM  &lt;DIR>         Searches
  5/8/2016   5:11 PM  &lt;DIR>         SendTo
  5/8/2016   5:11 PM  &lt;DIR>         Start Menu
  4/7/2017  11:28 PM  &lt;DIR>         Temp
  5/8/2016   5:11 PM  &lt;DIR>         Templates
       0 files                        0 bytes
      20 directories     39,040,172,032 bytes free


C:\users\jacob>
</pre>

Each line in the output represents one file or directory. On the left
you can see what time the file or directory was created. On the right
you can see the name. If you opened Windows Explorer, you would
see some of these directories (but not all--some of them are hidden,
like Application Data). 

Do you see this line?
<pre>
C:\users\jacob>
</pre>

This line is called a "prompt." It indicates that the terminal is
ready for you to type a command. It also tells you your current
**location**. `C:\users\jacob` is my default directory.

In Windows Explorer, you can change your location by double clicking
on a directory. Observe:

![before](before.png)

I now double click on Downloads:

![after](after.png)

Nothing too earth shattering. But how do you change your location from
the command line? With the `cd` command:

<pre>
C:\users\jacob><b>cd Downloads</b>

C:\users\jacob\Downloads>
</pre>

`cd` is short for "change directory." After `cd` you type the name of
the directory that you want to move into. Notice that the prompt now
shows my new location. If I type `dir`, I'll see the contents of
the Downloads directory:

<pre>
C:\users\jacob\Downloads><b>dir</b>
Volume in drive C has no label.
Volume Serial Number is 0000-0000

Directory of C:\users\jacob\Downloads

  4/7/2017  11:40 PM  &lt;DIR>         .
  4/7/2017  11:28 PM  &lt;DIR>         ..
  4/7/2017  11:40 PM             0  burma_shave.pdf
       1 file                         0 bytes
       2 directories     39,039,877,120 bytes free


C:\users\jacob\Downloads>
</pre>

If I want to go back to where I was before, I can type `cd ..`:

<pre>
C:\users\jacob\Downloads><b>cd ..</b>

C:\users\jacob>
</pre>

Try it out on your own:

 1. Use `dir` to see what directories you have.
 2. Use `cd` to move into one of those directories.
 3. Use `dir` again to view the contents of the new directory.
 4. Use `cd ..` to move back to the first directory.

Stuck? Watch this video (I recommend full screen. And increase the
video quality if it's fuzzy):

<iframe width="560" height="315" src="https://www.youtube.com/embed/RWtUyzpBlHY" frameborder="0" allowfullscreen></iframe>

<br />
There are many more commands, but this is enough to get you started.
On the next page, I'll show you how to run a Python program from this
command line interface.

</div>

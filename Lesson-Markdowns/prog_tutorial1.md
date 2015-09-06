index:1
banner_title:Exploring the Terminal
banner_description: Use the terminal to navigate your file system and issue commands to your computer.
banner_img: terminal.png
default_code: bash


#Exploring the Terminal

##Why would we want to use the terminal?

Simply put, the terminal allows us to perform tasks that would be very difficult to do otherwise. The graphical user interface we are used to when we drag icons and windows is mostly limited to moving files and programs around as well as do some extra tasks based on the right click button. But even these simple tasks can be inefficient when you begin to have hundreds of files. What if you want to filter through these and take out only the ones you want? This would be extremely tedious in the Documents window, but is trivial using the terminal. In fact we can filter them, perform operations with them, change their names, move them around, put information on websites, and many other things just by using a combination of the terminal and your favorite programming language. Despite the terminal's imposing and slightly antiquated appearance, its grammar is very easy to understand. The first step for now is to get the terminal set up on our computers.

##What to Download:

If you are using Linux or Mac, then you are done! Go to your search pane and type **terminal**. Click on terminal to open it. A retro-looking window with a flashing cursor will pop up. You can get started by skipping to the next section.

Windows is slightly different in that it does not come with the type of terminal we want to use. Mac and Linux branched off from an operating system called Unix a long time ago. Consequently their terminals more or less speak the same language. Windows' terminal is actually called the Command Prompt and is very similar to the terminal. In fact many of its commands are the same. With some a little finessing and some perseverance you could do everything in the Command Prompt that you could do in the Mac and Linux terminal, but commands are just different enough to make this more difficult than is necessary. Rather we will force Windows to have the terminal by downloading it ourselves.

To do this we will install something called Git. It can [downloaded here](https://git-scm.com/). Git is a version control software invented by Linus Torvalds, the same person who is largely credited for the Linux operating system. Git for Windows comes with a piece of software called Git Bash, which mimics the terminal. Once you have installed Git, go to the Windows Start menu and type **Git Bash**. Just like for Mac and Linux, you should see a new window pop up with a blinking cursor.

##Getting to Your Home Directory:


We should now be on the same page, so from now on I will refer to both Git Bash and the terminal synonymously unless I indicate otherwise.

Go ahead and open your terminal. You may not know this yet, but within the terminal you are currently stationed in one of the folders in your computer. If you are using Linux or Mac this will put you into your **Home** directory. (Windows likes to use the term 'folder' and Linux likes to use 'directory'. These are the same thing.) Windows is a little different because there is no “Home” directory. Do you remember launching Windows for the first time and giving it a name? In my case I just used my first name. Windows takes this name and uses it to make your main account folder. This contains your Documents, Pictures, Music, and other primary folders. So whatever name you happened to give it, this is functionally the same as your **Home** directory.

If you do not remember the name of your “Home” directory in Windows, that is okay. There is a handy way to always jump to your home directory, no matter if you are on Linux, Mac, or Windows. Just type this into your terminal:

	cd ~

And then press the Enter key. This may look cryptic, but it is very simple. The terminal uses the same variation on a theme when you perform any operation. It goes like this:

	<command name> [arguments…]

In this case your command name is ‘cd’ and the argument we are passing to it is ‘~’. Think about functions in mathematics. ‘cd’ is the function name and we pass ‘~’ to that function. Informally we can think of this like cd(~) just as we would think about f(x) in mathematics. Spaces are used to separate arguments from each other so if we had some made up command called ‘do_this_thing’ and we pass a series of numbers to it, we would type it as

	do_this_thing 1 2 3 4 5

If we were to informally think about this mathematically we would just think about it as do_this_thing(1, 2, 3, 4, 5).

So back to **cd ~**. **cd** stands for Change-Directory and is a command used to move between different folders. We have to learn to crawl before we learn to walk and this is the general function we use to crawl through our folders. More on crawling later. The **~** is a little tricky in this circumstance because it has special meaning. In this case **~** means “Home folder”.  Putting this all together **cd ~** can be spoken informally as **Go to my home folder!**, and it will take you there. So if you happen to go exploring into the depths of your file system and you get lost, you can always jump back to familiar ground by using this command.

##Peeking inside folders:

Before we talk about cd more, another command should be introduced. Shifting between different folders does not help much if you don’t know what is actually inside those folders. The **ls** command helps with this. All you have to do is type:

	ls

And press enter. This will list all of the files and folders located in your current directory. If you just used the **cd ~** command, then this will be your Home directory. That way if you want to traverse somewhere in your file system, you actually have an idea where to go. ‘ls’ can be thought of as ‘**l**i**s**t’, ‘**l**ists **s**tuff’, ‘have a **l**ook **s**ee’, or whatever other mnemonic device you prefer.

One more thing. You might have noticed that this function does not seem to actually take any arguments like **cd** did. Although the default behavior of **ls** is to show you the files and directories in your current directory, this is not all you can do with it. For example if you are in folder1 and folder2 is in folder1, you can type:

	ls folder2

And the contents of folder2 will be returned even though you are in folder1. All of these functions that I describe will be able to do more than I have time to tell you. To learn more about what these functions can do you can Google something like ‘ls command linux’ and you will get some interesting information. Regardless we will try to present you with only what you need to know for this course.

##Crawling with cd:

So we are back to the cd command. Previously we used the ‘cd ~’ command to jump to your home directory. There are just two other variants that are crucial you to know for now. Imagine you are in folder1 and you want to tell the terminal to enter folder2. In this case folder2 is a folder within folder1. Since we are in folder1 we can just type:

	cd folder2

And we are taken to folder2. Now imagine we are back in folder1 and we want to navigate to folder3. This time, however, folder3 is not within folder1, it is somewhere else. If we try to type:

	cd folder3

We will get an error because this does not really make sense. We could hypothetically have many folders named folder3 scattered around our computer. Which folder3 do we mean?

Now say we were in folder1 and were able to enter folder2 using ‘cd folder2’. But now we want to go back to folder1. You might think we can just type:

	cd folder1

But this will not work. The cd command will only look for immediate child folders of the folder we are currently in. Instead we must type:

	cd ..

Which takes us back one folder. To be clear this is ‘cd<space>..’ with two dots. A hand-wavy explanation for the double-dot notation is that the single dot **.** represents the current director, so **..** turned into the parent of the current directory. Consequently you can type **cd .** and you will just wind up back in the same directory.

##Putting this all together:

So far we have learned the cd and ls command within the terminal. This may not seem like a lot, but with these you can now use the terminal to enter any directory on your system that you would like. These commands you will probably use the most. By stringing together commands,

	cd <folder name>

	cd ..

	cd ~

	ls

You will be able to explore all the folders on your computer.** Take a look at the figure below to put all of this information together.

![Directories Picture](img/directories.png "Exploring files with cd.")

Now go exploring and see where you can get in your file system using these commands. Try to enter your documents folder, desktop folder, or some other folder you have created for some school project. Once you feel comfortable navigating with these commands we can move on to the ssh command.

*This will also download some interesting software called Git, used in version control. Essentially Git provides easy backup-restore-merge features to programmers working on code, especially when there are many people working on different features that could break the whole program. Again we just care about Git Bash that comes with it.

**Well sort of. Sometimes folders are off limits and have been locked to keep you out.

index:6
banner_title:Creating, copying, and deleting.
banner_description: Make new folders, files, move them around, and destroy them.
banner_img: copy.jpg
default_code: bash

#Creating, copying, and deleting.


##Additional Functionality

At this point you might be frustrated because there are obviously some operations you cannot perform using the terminal that can can easily do in your file explorer. These include, creating folders, creating files, renaming files, moving files, and deleting them. This is quite the array of actions to get familiar with, but be assured that it is just a variation of the material you are already familiar with.


##Making directories

The command for making a directory is **mkdir**. Its usage is as follows

	mkdir directory-name

Pretty simple. This will create a directory called “directory-name” in your current working directory.

If we use the **ls** command we can verify that “directory-name” is indeed present in our current working directory.

Let's make a sample directory called “test-directory” right now.

	mkdir test-directory

##Creating files

We will now cd into our new “test-directory” using the command we are already familiar with.

	cd test-directory

Now we will want to create a file. We can call it “test-file”. We do this with the **touch** command, like so:

	touch test-file

Again using **ls** verifies that we have created our file.

Notice how this file doesn't have an extension. Normally we always thing of a file as ending with .txt, .exe, .jpg, .whatever. The terminal is general use, so it does not care that the extension is not there, but this is not good practice and we should include a file extension to tell other programs what they are for. In this case let's assume are just making a text file. Let's also assume that our file has something important in it. Right now it is just empty, but please indulge the hypothetical. What we want to do is take all of the contents of “test-file” and move it into a file called “test-file.txt”. We can do this simply with the **mv** command.

This command will take two arguments, the name of the file we keeping the contents of, followed by the name of the file we want to move all of the contents to. This is functionally the same as renaming a file.

	mv test-file test-file.txt

Be careful though. If test-file.txt already exists in your working directory, all of its contents will be overwritten by that of test-file following this command. You could inadvertently delete lots of important data!

One thing to notice is that the **mv** command can be more useful than just renaming files. It can be used, as you would expect, to move a file to another directory. For example if the parent directory of our current working directory had another directory called directory2, we could move test-file.txt to that directory like so.

	mv test-file.txt ../directory2/test-file.txt

So we take all of the contents of test-file.txt and then start traveling to our target destination for that content. First we go to the parent directory with **../**, then go into directory2, then create a new file with the same name as before and insert the contents of the previous file. Keep in mind that the first argument could be a “path” to a file relative to the current working directory, just like the second argument, not just a file that is within the current working directory.

Understanding how the path system works is important and will come back later. 

##Copying files

But what if you want to copy files, not just move them around. There is a command for that and it is simply **cp**. It does all of the same things that mv does, except It keeps the original file around instead of deleting it. If we had used **cp** instead of **mv** in the last section, we might have typed

	cp test-file test-file.txt

or

	cp test-file.txt ../directory2/test-file.txt

##Opening Files

Opening and editing files is somewhat involved because some of the most popular editors are used from within the terminal. For new terminal users, this can cause them to unnecessarily lose their bearings. I will give you one such example called nano. You can open and edit your file by typing

	nano test-file

This will open up the nano text editor where you can add text among other things. You save and exit nano by simple hitting CTRL+x and then pressing enter. You will be returned to the directory you were in previously. Two other popular terminal editors are vim and emacs. If you would like to start a fight on a 1990s looking programing forum, ask them if they prefer vim or emacs. This is the question that started some of the earliest Internet flame wars. The more you know.

Personally I prefer using some of the more user friendly text editors. I suggest downloading [Sublime Text 3](http://www.sublimetext.com/3), [Notepad++](https://notepad-plus-plus.org/), [textmate](https://macromates.com/), or the new [Atom](https://atom.io/) text [editor](https://youtu.be/Y7aEiVwBAdk). 

##Deleting files

Deleting files is simple. This is done with the rm command. Assuming test-file.txt is in our current directory, we could delete test-file by doing this

	rm test-file.txt

We could also delete one of the copies we made in another directory by either navigatign with cd to that directory or giving rm a relative path to that directory. Like:

	rm ../directory2/test-file.txt

Be careful though. The terminal will assume that you know what you are doing, so passing a file to rm will not send it to the trash bin, it will be deleted forever. Sometimes simple mistakes can lead to horrible consequences. One of these pitfalls is using rm with the \* symbol. The terminal has special meaning for the star meaning to match any text at any length. So the command 'rm \*' will go through and delete all of the files in your working directory. Pixar ran into this mistake as is [retold here](https://www.youtube.com/watch?v=8dhp_20j0Ys).

##Same functions with directories

All of these functions behave almost identically with directories except for two exception. If you try deleting or copying a directory like this

	rm directory-name
	cp directory-name ../new-directory/directory-name

It will complain that “directory-name” is not a file. The reason it does not just delete directories is because the terminal is worried that you will accidentally delete files in the directory you are trying to remove. Rather, you have to apply an argument to the rm command through what is called a flag. In this case we will have to pass **r** for “recursive to the **rm** command.

	rm -r direcotory-name
	cp -r directory-name ../new-directory/directory-name

This tells the terminal to go in and delete the folder and all of the files and folders that are children of “directory-name”.

##Recap

The commands we have learned in this lesson are:

- **mkdir [directory name]** = Creates a directory-name
- **touch [file name]** = Creates a file.
- **mv [file or directory name]** = moves contents of file or directory to a new file or directory
- **cp [file or directory name]** = Same thing as **mv** except it keeps the original file/directory. Include -r for directories.
- **rm [file or directory name]** = Deletes file. Include -r to delete a directory.

Try out these commands for yourself and become comfortable with them. We will apply these principles later as well to retrieve data from MSI computers.
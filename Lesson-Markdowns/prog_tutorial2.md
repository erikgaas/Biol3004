index: 2
banner_title: A tool for remote connection to other computers.
banner_description: The computer teloportation tool.
banner_img: ssh_logo.jpg
default_code: bash


#SSH

##What is this useful for?

Sometimes your computer will not have the files, hardware, or software to to the task you want to get done. In most cases you have no way to access other people's computers, but in some cases you can. For instance the Minnesota Supercomputing Institute (MSI) gives you a place to store files and allows you to perform computationally intensive operations. If we want to be able to take advantage of this additional storage and performance, we need to be able to get into the MSI files system. 

Besides MSI functionality, ssh gives you the ability to remotely access your own computer as well. We will not talk about how to do this, but it is something interesting to keep in mind.

##Getting a VPN Client

You will be able to ssh into MSI easily if you are already connected to the network at the UofM. However, if you are off campus, then ssh will not be able to connect you right away. In order to connect you will have to trick your computer into thinking it is at the UofM. This is what a VPN is for.

[Here is a link](https://it.umn.edu/services/resources/software-downloads?field_operating_system_tid%5B%5D=7681) to find VPNs that work with the University of Minnesota. There are buttons to toggle to find the right software for your system. Each has detailed installation instructions, so you may read up on that and come back. Once you have installed your VPN, open it up and try connecting. It should ask you for your UMN x500 and password. Once you submit this information it should connect you. You can now use ssh whenever you like.

##Connecting to MSI

By signing up for this course you should have gotten access to MSI. To ssh into MSI use this command:

	ssh <x500>.login.msi.umn.edu

After this command executes it will probably ask for your UMN password. Go ahead and type that in and press enter. Keep in mind it will not show any characters when you are typing your password. You might be used to seeing little circles in place for characters. This is not the case this time.

In step with our previous understanding of commands, ssh is our function name and “<x500>.longin.msi.umn.edu” is the argument we pass to that function. Wherever you happened to be in your local file system, you will be transferred to your directory in the MSI file system. All the rules are the same as your local file system. You can change directories using cd and list files and folders using ls. Try looking around. See if you can find everyone else’s directories on the MSI system.

If at any time you want to exit the MSI file system simply type:

	exit

And press enter. You will be returned to whatever directory you were working on in your local file system.

##Almost to usefulness

Nobody is going to give you a Nobel Prize for searching through directories, but we are very close to finding a tool that is useful to us. Let me briefly introduce you to a metagenomics package called QIIME. (Pronounced ‘chime’) If you are interested right now, go exploring at [http://qiime.org/](http://qiime.org/) . QIIME is a piece of software you could just as easily download on your own computer, but rather than going through that hassle, we will instead ssh intoMSI to use QIIME functionality.

Go ahead and ssh into MSI just as we did previously. Make sure you have your VPN connected if you are off campus. We have entered MSI, but what we want to do now is ssh into one of MSI’s specialized machines. In this case we want to ssh into a machine called Itasca. So at this point type:

	ssh itasca

They will again ask you to provide your password. Once you have done this, everything will be just as it was before. All of your files will be in the same place, but now you have the added benefit of using software that is already installed on the itasca machine. This is how we get to QIIME. Now we are not going to make this a QIIME lesson. Instead we will just load QIIME and run a quick test.

To load QIIME type:

	module load qiime/1.8.0

Think of all of the commands we have learned so far and consider the circumstance where we would want to get some additional commands that do not come with the default terminal settings. By loading QIIME, this is exactly what we are doing. This ‘module’ command has unlocked a whole bunch of new commands that we can use to perform complex operations pertinent to metagenomics research.

We will run one of these commands right now as a demonstration. Go ahead and type:

	print_qiime_config.py –t

And press Enter. If you see a whole bunch of text with specifics about different settings, then everything is ready to go and you can now use QIIME for metagenomics. The only problem is that you do not know how to use QIIME yet. We will cover that later. For now go back and get practice navigating directories and using ssh to enter MSI.

//TODO: We need to learn what commands in QIIME are important and how to move files between MSI and local file system. 
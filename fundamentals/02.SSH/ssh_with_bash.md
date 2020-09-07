# SSH initiation

## Learning Objectives

- To understand what is deployment
- To understand and use the right professional terminology.
- To become familiar with SSH and how it works, from the terminal.
- To be able to deploy a local file onto a remote computer via SSH.

## Introduction: the art of putting your files online

Since we are web builders, we must, of course, be able to actually "put online" the files we create with our lovely, full-of-cool-stickers development computer.  
To put something "Online" really means transfer it onto a computer that is configured to **serve** files to the connected masses. Most often, these **servers** (aka "computers that serve content") are provided by **Web hosting companies** such as [Gandi](https://gandi.net), [OVH](https://www.ovh.com/fr/), [siteground](https://www.siteground.com/), [AWS](https://aws.amazon.com/fr/), [DigitalOcean](https://www.digitalocean.com/)...

![](./assets/infographics_local_production.png)


This process of "putting files online" is called **deployment** : transfering files from your local machine (**the development environment**) to the remote hosting machine (**the production environment**).  
How do we do that, concretely ? There are many many ways, depending on your web hosting company. Perhaps you know a few of them...  

A really basic way to deploy files is to transfer them via **FTP** (Google to see what it means). FTP is not secure at all, so it's not advised. 

Some web hosting providers provide a web interface to upload and manage your files on their server. In that case, the method is based on simple **http** requests (hopefully, **https** requests, actually).

... And then, there is SSH. 

## What is SSH ?
SSH or *Secure Shell*, is a communication protocol allowing a "client" (your local development machine for example) to open a secure interactive session on a remote computer (the "server"), so as to execute commands, transfer files to/from it. Basically, take control of the remote computer. 

## Why SSH ?
 **SSH** is considered to be a really good professional deployment technique, because, among other reasons, it is **much more secure** than all the techniques mentioned before. 

## Why is it secure ?

- Contrary to FTP, the data sent between client and server are **encrypted**, ensuring their confidentiality (no one can read the information apart from the local and remote computers).
- The client and server **mutually authenticate themselves** : each verifies that the other machine is the authorized one. 

## How does it work ? 

For this exercise, we will use a BeCode laptop, already configured by your coach with two software : 

- a web server ([Apache](https://fr.wikipedia.org/wiki/Apache_HTTP_Server))
- an SSH server (OpenBSD Secure Shell server - google it)

To connect using SSH to a remote machine, you will need 3 things: 

- the `ssh` command
- parameters, such as `-p` to specify the port (by default: `22`)
- the username of the user we want to connect as;
- The server machine's network name or IP address

All combined, the syntax is : 

`ssh -p 22 user@machineIP`  
or  
`ssh -p 22 user@machineName`  
or simply, since 22 is the default SSH port  

`ssh user@machineIP` 

**Exercise**  

An ssh server is available on your WiFi under the name : `becode-server` at the address `xxx.xxx.xxx.xxx` 
(Ask your coach to find out the server's IP address, via the command  `hostname -I` on Linux ). The SSH port is, in this case, `1992`.

**Connect using the given IP address and port,  using the user `junior`, whose password is : `yolo`.**


**note** : another way to find the IP address of a machine is via the `arp -a` command. This one returns the IP address of all machines on the connected network. Useful!  
Yet another method is to use the "Fing" app on your mobile phone...

## Yeah! I'm connected... What can I do ?

Once you're connected to the remote host, you can do anything... allowed to the user you've used! (in this case : `junior`). In this case you're allowed a few stuff, but not "admin" commands, like `apt-get update`. Try, see what happens...

Here are a few commands that you can use : 

1. What is my Present Working Directory ?  ( `pwd`)
2. Create a file : `touch fichier.txt`
3. Observe the state of the machine in real time:  (`top` and [a few more](https://www.howtogeek.com/107217/how-to-manage-processes-from-the-linux-terminal-10-commands-you-need-to-know/))
4. Check the state of the hard drives' free space ([doc](https://askubuntu.com/questions/432836/how-can-i-check-disk-space-used-in-a-partition-using-the-terminal-in-ubuntu-12-0/432842))

## Transfer a file from your local machine to the remote machine

Classic scenario : you have a hosting contract on a VPS (Virtual Private Server). Usually they come blank, with not much installed. The only way to manipulate it is via SSH. Thus, via your terminal.

In this exercise, you will deploy an html file. Here is how to do it : 

1. Connect to the remote via SSH
2. Navigate to the folder served by Apache : `/var/www/html`
2. Create a folder using your first and last names without space nor special characters, all in lowercase: `your-firstname-lastname`
1. Exit your session using ... `exit`
1. Create an **index.html** file on your local computer. 
2. Edit it and add "Hello, I'm Firstname Lastname". Save then close it.
3. Open a new terminal window and access that file on your local drive : 
   - use this command: `cd ~` ( `~` is a shortcut to say "the current user's home folder").
   - List all the current folder's content via `ls -lh`. 
   - Navigate to the folder where you have saved the `index.html` file
1. Now that we are in the right folder, let's **transfer our html file onto the server. Remember: you created a folder using your first and last names? Let's put that html file inside, via the command :`scp` (Secure CoPy).  
2. Type this command: `scp -P 1992 ./index.html junior@adresseIP:/var/www/html/your-firstname-lastname/`

**scp syntax**  

```
scp : secure copy 
-P <portnumber> : port number
./index.html : the "source" to be transfered : a path leading to the file to transfer
junior : SSH username  
xxx.xxx.xxx.xxx : remote host IP address
:/var/www/html/your-firstname-lastname/ : the "target" folder, in which the file is to be transfered on the remote host. 
```

**IF YOU DID IT RIGHT, YOUR FILE SHOULD BE VISIBLE AT THIS ADDRESS**

http://{IP_ADDRESS}/{your-firstname-lastname}/index.html

## Going beyond...

At this point, you may wonder how really useful that is. Transfering one file at a time ? Yuk!   

1. In reality, what we do goes more like this : go on the remote host's destination folder (the "target" mentioned above), then from there, `git pull` to clone the repository of your project's master branch. Thus deploy every update via git. 
How about you try that with your peer ? Imagine the procedure, then try pulling a repository of yours into your own folder?
2. Done ? Okay, but that's still a bit tedious. Imagine you could simply do `git push` and it automatically deploys ? Find out how to do that [using that quick tutorial](https://dev.to/pixeline/deploy-an-application-automatically-using-github-hooks-50fd)!

All done? Well, hope you had fun and learned a ton!

![](./assets/redpill.gif)

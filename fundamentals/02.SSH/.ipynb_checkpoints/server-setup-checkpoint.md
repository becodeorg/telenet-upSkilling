# How to setup a local SSH/Apache Server for the exercise...


1. install openssh  + apache2 + git   
 `apt-get install openssh-server apache2 git`
2. edit ssh config to set port to 1992:
	1. `vi /etc/ssh/sshd_config`
	2. change "Port 22" to "Port 1992"
3. `sudo adduser telenet`  password: `learning`
You can press enter on names, room, tel,...
4. `sudo usermod -aG www-data telenet`
5. Change ownership of apache folders to `www-data`:  `sudo chown -R www-data:www-data /var/www/html` 
6. create a symbolic link from `/home/telenet/www` to `/var/www/html` : 
`ln -s /var/www/html /home/telenet/www`
7. to find the server's current IP address: 
 `hostname -I`


You are now ready to launch your server [for the exercise](./readme.md)...

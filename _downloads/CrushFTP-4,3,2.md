---
layout: downloadpage
permalink: /downloads/CrushFTP-4,3,2/
name: CrushFTP 4.3.2
file_type: download
title: CrushFTP 4.3.2
description: >-
  CrushFTP lets you serve files from your computer, or any other computer on the Internet that's running an FTP server , CrushFTP 3 allows you serve files from your computer, or any other computer on the Internet that's running an FTP server. 
tags: [Servers]
category: Internet
sort_order: 100
rating: 100
changefreq: monthly
priority: 0.5
published: false
create_date: 
modified_date: 03/11/2017
created_by: 
modified_by: 
comments: true
redirect_url: 
### 
version: 4.3.2
size: 6.23 MB
downloadurl: http://www.crushftp.com:81/crushftp4.zip
response: -1
by: 
by_link: 
licence: Shareware 
os: Windows
---

{% include download-header.html download=page%}

<p style="fix-download-text !important">
<p><font size="2">CrushFTP lets you serve files from your computer, or any other computer on the Internet that's running an FTP server <br />
CrushFTP 3 allows you serve files from your computer, or any other computer on the Internet that's running an FTP server. <br />
<br />
CrushFTP does this by treating your local machine as if its the same as any other machine. You drag and drop directories into CrushFTP 3's file system, and you also add servers into the file system. They look just like a directory, but CrushFTP will connect and return directory listings to a user when they are browsing them. It will also translate listings from non standard formats. <br />
<br />
When a user requests a file, CrushFTP tells the remote server to start sending the file to the user. The user never really knows the file didn't come from you. Of course they could check to see where the connection came from, but CrushFTP also allows you to tunnel the data through itself. While this doesn't distribute the load on the server, it does give a little more security. CrushFTP will also tunnel the data when its not possible to tell the server to transfer the data directly. <br />
<br />
This type of serving can be used to create redundant servers. One main CrushFTP server that transfers each incoming connection to a server in its list. If for some reason that connection times out, it quickly goes on to the next server in the list and so on. So if a server did happen to go down, or a config was changed on that server, CrushFTP transparently starts serving form the next in the list. The timeout value for the server can even be specified. This can also be used to create load balancing servers. <br />
<br />
The first connection goes to the first server in the list, and the next connection to the next. When its gets to the end, it wraps around to the beginning. As long as the data isn't being tunneled through CrushFTP, then the load is distributed. Its important to note that this isn't something that can only be done for just one directory, but can be done for multiple directories in one users <br />
virtual file system. <br />
<br />
A good use for something like this would be somebody running a mirror site. They could distribute the load coming in on their server over to other servers as well. <br />
<br />
CrushFTP also allows for switching servers once the Main server is reaching its max allowed bandwidth. So you can just have backup servers to take over the load when your main one starts to fill up. <br />
<br />
Here are some key features of "CrushFTP": <br />
<br />
· Complete GUI remote administration from any machine that can run CrushFTP. You can even launch the GUI from a web browser! <br />
· Multihoming support. Virtual servers for multiple IP's, or multiple ports on an IP, or both. <br />
· Resume supported on download and uploads. <br />
· Intuitive, built-in user manager for administering user and group accounts. <br />
· Built in log viewer is updated in real time as the server is running. <br />
· Directory permissions per directory. All directories can have different read/write/view/delete/resume/rename/make dir permissions/etc. <br />
· File permissions per file. All files can have different read/write/view/delete/resume/rename/etc. <br />
· Directory quotas. Every directory can have a quota applied to it, or inherit from the parent directory. <br />
· Virtual Directory support on any platform. Design your own directory structure for a user when they log in. <br />
· MacBinary III encoding on the fly when a user has turned on MacBinary (MACB E) and is downloading a file with a resource fork. Also, uploads that are MacBinary files are stored as Mac files. <br />
· Bandwidth limits on uploads per [user/group/server]. <br />
· Bandwidth limits on downloads per [user/group/server]. <br />
· Idle timeout for auto-disconnect per [user/group]. <br />
· Maximum login time allowed per [user/group]. <br />
· Maximum simultaneous logins allowed per [user/group]. <br />
· Maximum logins per IP for a [user/group]. (e.g. 100 anonymous logins, but only 2 from the same IP) <br />
· Allow/Deny IP restrictions for logins per [user/group/server]. Supports IP ranges for deny and allow. <br />
· Max download amount per [user/group] for each login session. (e.g. after 10mb's the user cannot download till they logout and then login again) <br />
· Server queuing for downloads/uploads. No other FTP server has this feature. <br />
· Day of week restrictions per [user/group/server] (e.g. Sun, Mon, Tues, etc.) <br />
· Time of day restrictions per [user/group/server] (e.g. login between 10 a.m. and 11 a.m. and between 4 p.m. to 10 p.m.) <br />
· Group inheriting for users, along with ability to override any part of a group setting for a particular user. <br />
· Spying on connected users. See their log, current dir, bytes sent/received, transfers speeds, login time, login IP, and estimated time left for a transfer. <br />
· Download ratio per [user/group]. Both can be temporary per session login or permanent. <br />
· Incredible server statistics, such as last login date, time, IP, current total server bandwidth usage (bytes in/out), files downloaded/uploaded, graphs for bandwidth utilization, etc. <br />
· SITE commands for remote administering from an FTP client. Each [user/group] can be limited to what commands they can issue. <br />
· All server messages are customizable, along with nearly everything else in the server. <br />
· Customizable logging options allow you to control what gets logged to both the server window and log file. <br />
· FXP protection just in case you don't want users doing FXP transfers. <br />
· Filtering of filenames for uploads, downloads, lists, and renames. <br />
· Temporary bans for users. <br />
· Hammering protection that will ban a user. <br />
· Temporary accounts that can be set to auto expire after so long, or be automatically deleted! <br />
· Users behind a router/firewall can have CrushFTP auto discover their real IP. <br />
· Log rolling allows logs to automatically be archived, or deleted. <br />
· Can listen on multiple ports. <br />
<br />
<br />
What's New in This Release: <br />
<br />
· supports mini URL's to redirect users to a specific file, folder, or website. They can be set to auto expire as well. Example:https://www.crushftp.com/d <br />
· supports PDF submissions from Acrobat. Have end users fill out an acrobat form, and submit it for storage on your server. <br />
· added feature to MagicDirectory plugin so you can set expiration dates for the MagicDirectory users. <br />
· added ability to set an extension to be applied to uploads that are in progress and removed when they finish. <br />
· added ability to tell a remote admin server to download and run a self update (OS X only) <br />
· added pattern matching to email events so you can generate an event when someone uploads a specific kind of file. Example: /uploads/*.mp3 <br />
· notifies you if you are using different CrushFTP versions for the server and remote admin client. <br />
· fixed bug with homedirectory plugin <br />
· fixed bugs with new caching mechanism <br />
· fixed bug with the UserFolderSizes report where it would report no data <br />
· fixed bug in Account Activity Summary where downloads were counted more than once. <br />
· fixed bug with localization.</font></p></p>

---
layout: downloadpage
permalink: /downloads/Everything/
name: Everything
file_type: download
title: Everything
description: >-
  Locate files and folders by name instantly.
tags: [Launchers]
category: System
sort_order: 100
rating: 100
changefreq: monthly
priority: 0.5
published: true
create_date:
modified_date: 03/11/2017
created_by:
modified_by:
comments: true
redirect_url:
###
version:  1.4.1
size: 1.4 MB
downloadurl: https://www.voidtools.com/Everything-1.4.1.877.x64.zip
response: 301
by: voidtools
by_link: https://www.voidtools.com
license: Freeware
os: Windows
---

{% include download-header.html download=page%}

Locate files and folders by name instantly.

- Small installation file
- Clean and simple user interface
- Quick file indexing
- Quick searching
- Minimal resource usage
- Share files with others easily
- Real-time updating

#### What is "Everything"?

"Everything" is search engine that locates files and folders by filename instantly for Windows.
Unlike Windows search "Everything" initially displays every file and folder on your computer (hence the name "Everything").
You type in a search filter to limit what files and folders are displayed.

#### How long will it take to index my files?

"Everything" only indexes file and folder names and generally takes a few seconds to build its database.
A fresh install of Windows 10 (about 120,000 files) will take about 1 second to index.
1,000,000 files will take about 1 minute.

#### Does Everything search file contents?

Yes, "Everything" can search file content with the content: search function.
File content is not indexed, searching content is slow.

#### Does "Everything" hog my system resources?

No, "Everything" uses very little system resources.
A fresh install of Windows 10 (about 120,000 files) will use about 14 MB of ram and less than 9 MB of disk space.
1,000,000 files will use about 75 MB of ram and 45 MB of disk space.

#### Does "Everything" monitor file system changes?

Yes, "Everything" does monitor file system changes.
Your search windows will reflect changes made to the file system.

#### Is "Everything" free?

Yes, "Everything" is Freeware.
Please consider donating.

#### Does "Everything" contain any malware, spyware or adware?

No, "Everything" does not contain any malware, spyware or adware.

#### Does "Everything" miss changes made to the file system if it is not running?

No, "Everything" can be closed and restarted without missing changes made to the file system (even across system restarts).
"Everything" updates the database when it is started.

#### What are the system requirements for "Everything"?

"Everything" will run on Windows XP, Vista, Windows 7, Windows 8 and Windows 10
NTFS indexing requires the Everything service or running "Everything" as administrator.

#### How do I convert a volume to NTFS?

Please backup anything important before converting a volume to NTFS.
Once a volume is converted to NTFS it can not be converted back to FAT or FAT32.
Please note that some devices may not be able to read NTFS volumes on USB disks / USB drives.

To convert a volume to NTFS:
From the Start menu, click Run.
Type in the following and press ENTER:
cmd
In the command prompt, type in the following and press ENTER:
convert D: /fs:ntfs
where D: is the drive to convert.

#### Can "Everything" index a mapped network drive?

Yes, please see Folder indexing for more information.

#### How do I install "Everything"?

Please see A basic guide to installing "Everything".

#### How do I use "Everything"?

Please see A basic guide to using "Everything".

#### Why is "Everything" 1.4 using more memory than 1.3?

"Everything" 1.4 indexes file sizes and dates and also stores extra information for faster sorting by default.
Please see Optimizing for smallest memory foot print to disable these changes.

#### How do I prevent the UAC prompt when running "Everything"?

"Everything" requires administrative privileges for low level read access to NTFS volumes for NTFS indexing.

The UAC prompt can be avoided by running "Everything" as a standard user and installing the "Everything" service or not using NTFS indexing.

To run "Everything" as a standard user and install the "Everything" service:
In "Everything", from the Tools menu, click Options.
Click the General tab.
Check Everything Service.
Uncheck Run as administrator.
Click OK.
Exit "Everything" (right click the Everything system tray icon and click Exit)
Restart Everything.



#### Searching

How do I search for a file or folder?

Type the partial file or folder name into the search edit, the results will appear instantly.

How do I use boolean operators?

AND is the default boolean operator.

For example, to search for abc and 123, search for:
abc 123

To search for either of two search terms, add a | between the terms.

For example, to search for .jpg or .bmp, search for:
.jpg | .bmp

To exclude something from the search include a ! at the front of the term.

For example, to search for everything except abc, search for:
!abc

To show the basic search syntax in Everything:
In "Everything", from the Help menu, click Search syntax.

How do I use wildcards?

Using a * in your search will match any number of any type of character.
For example, here is how to search for files and folders that start with e and end with g: e*g
Using a ? in your search will match one character.
For example, here is how to search for files that have a 2 letter file extension: \*.??

#### How do I include spaces in my search?

To include spaces in your search enclose your search in double quotes.
For example, here is how to search for foo<space>bar: "foo bar"

#### How do I search for a file type?

To search for a file type, type the file extension into the search edit,
eg: to search for the mp3 file type, type \*.mp3 into the search edit.
To search for more than one type of file type use a | to separate file types,
eg: \*.bmp|\*.jpg will search for files with the extension bmp or jpg.

#### How do I search for files and folders in a specific location?

To search for files and folders in a specific location include a \ in your search string.
For example, here is how to search for all your mp3s in a downloads folder: downloads\ .mp3
You could alternately enable Match Path in the Search menu and include the location in your search string.
For example, here is how to search for all your avis in a downloads folder with Match Path enabled: downloads .avi

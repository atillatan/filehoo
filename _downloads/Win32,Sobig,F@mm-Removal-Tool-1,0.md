---
layout: downloadpage
permalink: /downloads/Win32,Sobig,F@mm-Removal-Tool-1,0/
name: Win32.Sobig.F@mm Removal Tool 1.0
file_type: download
title: Win32.Sobig.F@mm Removal Tool 1.0
description: >-
  Win32.Sobig.F@mm FREE Removal Tool
tags: [null]
category: Antivirus
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
version:  1.0
size: 55 KB
downloadurl: http://www.bitdefender.com//bd/downloads/removaltools/Antisobig EN.exe
response: 301
by:
by_link:
licence: Freeware
os: Windows
---

{% include download-header.html download=page%}

<p style="fix-download-text !important">
<p><font size="2"><p><strong>Name:</strong> Win32.Sobig.F@mm <br />
<strong>Aliases:</strong> W32/Sobig.F@mm <br />
<strong>Type:</strong> Executable Mass Mailer <br />
<strong>Size:</strong> ~70 KB <br />
<strong>Discovered:</strong> 19.08.2000 <br />
<strong>Spreading:</strong> High <br />
<strong>Damage:</strong> Low <br />
<strong>In The Wild:</strong> Yes <br />
<br />
<strong>Symptoms:</strong><br />
Registry keys:<br />
HKLMSoftwareMicrosoftWindowsRunCurrentVersionTrayX with value:<br />
%WINDIR%winppr32.exe /sinc<br />
HKCUSoftwareMicrosoftWindowsRunCurrentVersionTrayX with value:<br />
%WINDIR%winppr32.exe /sinc<br />
<br />
Following files in the %WINDIR% folder:<br />
<br />
Winstt32.dat<br />
Winppr32.exe<br />
Winstf32.dll<br />
<br />
<strong>Technical description:</strong> <br />
<br />
It arrives in e-mail</a> in the following format:<br />
<br />
Subject:<br />
Randomly chosen from the following list:<br />
"Re: Wicked screensaver"<br />
"Re: That movie"<br />
"Re: Your application"<br />
"Re: Approved"<br />
"Re: Re: My details"<br />
"Re: Details"<br />
"Your details"<br />
"Thank you!"<br />
"Re: Thank you!"<br />
<br />
Body:<br />
Please see the attached file for details.<br />
Or<br />
See the attached file for details<br />
<br />
Attachment:<br />
Randomly chosen from the following list:<br />
“.movie0045.pif"<br />
"wicked_scr.scr"<br />
"application.pif"<br />
"document_9446.pif"<br />
"details.pif"<br />
"your_details.pif"<br />
"thank_you.pif"<br />
"document_all.pif"<br />
"your_document.pif “.<br />
<br />
After the user opens the attachment the worm copies in the following location:<br />
%WINDIR%winppr32.exe<br />
and adds the following registry keys:<br />
HKLMSoftwareMicrosoftWindowsRunCurrentVersionTrayX with value:<br />
%WINDIR%winppr32.exe /sinc<br />
<br />
HKCUSoftwareMicrosoftWindowsRunCurrentVersionTrayX with value:<br />
%WINDIR%winppr32.exe /sinc<br />
<br />
It searches for e-mails in the following file types:<br />
html, wab, mht, hlp, txt, eml, htm, dbx<br />
<br />
The worm also spreads trough network shares. <br />
After the 10.09.2003 it stops spreading<br />
<br />
<strong>Removal instructions:</strong> <br />
<br />
The BitDefender Virus Analyse Team has releasead a free removal tool for this particular virus.<br />
<br />
<strong>Important:</strong> You will have to close all applications beforerunning the tool (including the antivirus shields) and to restart thecomputer afterwards. Additionally you ll have to manually delete theinfected files located in archives and the infected messages from yourmail client. <br />
<br />
The BitDefender Antisobig-en.exe tool does the following:<br />
it detects all the known Sobig versions.<br />
it deletes the files infected with Sobig.<br />
it kills the process from memory.<br />
it repairs the Windows registry<br />
<br />
You may also need to restore the affected files.<br />
<br />
To prevent the virus from replicating itself from infected machines toclean machines, you should try to disinfect all computers in thenetwork before rebooting any of them, or unplug the netw</p></p></p>

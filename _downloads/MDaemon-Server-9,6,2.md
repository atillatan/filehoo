---
layout: downloadpage
permalink: /downloads/MDaemon-Server-9,6,2/
name: MDaemon Server 9.6.2
file_type: download
title: MDaemon Server 9.6.2
description: >-
  MDaemon Server - designed to meet all your LAN and Internet  
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
version:  9.6.2
size: 32.7 MB
downloadurl: http://files.altn.com/MDaemon/Release/md_en.exe
response: 302
by:
by_link:
licence: Trial
os: Windows
---

{% include download-header.html download=page%}

<p style="fix-download-text !important">
<p><font size="2"><p>MDaemon is a Windows-based email server</a> that provides full mail server functionality and control as well as a host of other features. <br />
<br />
MDaemon Server is an email server that allows you send and recive email messages.<br />
<br />
It includes anti-virus and anti-spam security features, seamless Webaccess to email via the integrated WorldClient component, can beadministered remotely through the web-based WebAdmin plug-in, and muchmore. <br />
<br />
MDaemon is proven as secure, dependable, and versatile.<br />
<br />
Alt-N Technologies offers the international marketplace innovativecommunications software with professional features and beginner levelease-of-use. MDaemon, provides a complete suite of secure andstandards-compliant messaging and collaborative capabilities.<br />
<br />
SyncML server for PIM data synchronization. <br />
Free/busy server for scheduling meetings. <br />
PocketPC access to groupware shared folders. <br />
Sender ID to fight spoofing and phishing. <br />
Multi-threading speed for IMAP, Content Filter. <br />
WorldClient UTF-8 output for easy language switching. <br />
Active Directory monitoring for account management. <br />
Active Directory access for building mailing lists. <br />
AntiSpam as a separate, substitutable daemon, accessible by TCP/IP.<br />
<br />
<span><strong>Here are some key features of "MDaemon Server":</strong></span><br />
<br />
Detect Spoofed Email Addresses <br />
Automatic Update Service <br />
Private White Lists <br />
Compose Messages in Rich Text (HTML) Format <br />
Spam Filter <br />
Collaboration and Contact Sharing <br />
Shared Calendaring and Scheduling <br />
Instant Messenger <br />
Contact Synchronization <br />
Message Folder Sharing <br />
Secure Socket Layer (SSL) Support <br />
IMAP Support <br />
Multiple Domain Support <br />
ODBC Support for Account Storage <br />
ODBC Support for Mailing Lists <br />
Performance Enhancements <br />
Strong Passwords<br />
Automatic IP Screening <br />
DomainPOP <br />
On-Demand Mail Relay (ODMR) <br />
SMTP Authentication <br />
Web-based email <br />
Spam Blocker <br />
Content Filtering <br />
Mailing Lists <br />
Easy to Backup and Restore <br />
Extensive and Versatile Interface <br />
Logging<br />
Mail Processing Scheduler <br />
Reverse Lookup <br />
IP and Host Screening, Address Suppression <br />
IP Shielding <br />
POP Before SMTP <br />
Control Relaying of Messages <br />
<br />
<br />
<span><strong>Requirements:</strong></span><br />
<br />
Computer with Pentium III 500 MHz (or higher) processor <br />
512 MB of memory (1 GB recommended) <br />
Typical Hard disk space required: 30MB, additional space for any mail to be stored <br />
Winsock 2 <br />
Internet Explorer 4.0 or higher <br />
Ethernet Network Card <br />
TCP/IP network protocol installed <br />
Internet or Intranet communication capabilities <br />
<br />
<strong>Note:</strong> MDaemon is no longer compatible with the original Windows95 release. MDaemon now requires Windows 95 OSR2 or higher. Windows 95installations require WinSock 2.0 to be installed. Like all mailservers MDaemon is heavily I/O bound - performance can be dramaticallyimproved with faster hard drives<br />
<br />
<br />
<span><strong>Limitations:</strong></span><br />
<br />
30 days trial</p>
<div class="celltext_big"><br />
<br />
<strong>What s New</strong> in This Release:<br />
<br />
[6434] Added a white list to the Backscatter Protection system. Thereis a new white list button on the UI. The white list allows you tospecify IP addresses and domain names. The white list is only employedwhen you have enabled Backscatter Protection s "reject" option.Connections from white listed IPs will not be rejected by BackscatterProtection. White listed domain names are matched against the PTRlookup results on the connecting IP. So, you must enable PTR lookups ifyou want to white list using domain names.<br />
[6551] Improved antispam s ability to detect PDF based spams.<br />
[6498] MDStats strips backscatter information from addresses it parses from log files<br />
[6524] Global and domain level admins will have star icon in account mgr. <br />
[6447] Midnight config file backup event now occurs in a separate thread. <br />
[6132] SMTP delivery to multiple RCPTs will bypass the SMTP basedspam scan if any one of the RCPTs has white listed the sender.Otherwise, the SMTP spam scan will take place.<br />
[6444] fix to Comagent crashes when clicking on Auto Update dialog box after another Comagent dialog box opens<br />
[6445] fix to possible Comagent crash on icon right-click<br />
[6449] fix to truncation on # in dat files <br />
[6452] fix to duplicate public contact when new account added with Configuration Session<br />
[6453] fix to "local mail only" restrictions not working correctly<br />
[6454] fix to default action "Refused" not being selected in "local mail only" restriction settings<br />
[6493] fix to $SENDER$ expanding to Return-Path header address ratherthan to the From header address within the content filter rules andnotification message processing systems. $SENDER$ should always be theaddress taken out of the From header.<br />
[6505] fix to the following problems when appending a ":port" to thesmart host value: a) if the smart host domain is down, an endlessdelivery loop results / b) port value is ignored and treated as part ofthe smart host domain name / c) use of default port when connection togive port failed <br />
[6499] fix to auto responders triggered by mail with NULL reverse path<br />
[6506] fix to spam filter address book white listing not working with DPOP<br />
[6416] fix to postmaster auth requirement not honored with wildcard aliases<br />
[6466] fix to WC error when attempting to create a folder that already exists<br />
[6470] fix to queue lock when using the option to send only X messages per thread<br />
[6463] fix to procnow.sem not working<br />
[6467] fix to DomainPOP real name matching feature not working with aliases<br />
[6474] fix to AntiSpam server missing from File menu<br />
[6576] fix to apply button not working right on spam filter heuristics tab<br />
[6482] fix to IP screen hits logging to system rather than screening log<br />
[6464] fix to MDStats not parsing Subject from SMTP-Out logs<br />
[6535] fix to certain Japanese characters preventing messages from being sent in WorldClient using the iso-2022-jp encoding<br />
[6538] fix to Minger authentication fails when verifying certain addresses<br />
[5545] fix to RTE files are orphaned when messages are deleted by WC<br />
[6526] fix to "update webadmin" program manager group item being created<br />
[6549] fix to possible crash when processing the local queue<br />
[6567] fix to "noreply@" being refused when referencing foreign domains... [</div></p></p>

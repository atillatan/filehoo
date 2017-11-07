---
layout: downloadpage
permalink: /downloads/Inno-Setup-5,1,14/
name: Inno Setup 5.1.14
file_type: download
title: Inno Setup 5.1.14
description: >-
  Inno Setup is a tool that helps you to create windows installers.
tags: [Setup creators]
category: Authoring tools
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
version:  5.1.14
size: 876 KB
downloadurl: http://files.jrsoftware.org/is/5/isetup 5.1.14.exe
response: 200
by:
by_link:
licence: Freeware
os: Windows
---

{% include download-header.html download=page%}

<p style="fix-download-text !important">
<p><font size="2"><p>InnoSetup is a free installer for Windows programs. First introduced in1997, Inno Setup today rivals and even surpasses many commercialinstallers in feature set and stability.<br />
<br />
Installations are created by means of scripts, which are ASCII textfiles with a format somewhat similar to .INI files. (No, it s not ascomplicated as you might be thinking!) <br />
<br />
Inno Setup is a tool that helps you to create windows installers.<br />
<br />
Scripts have an ".iss" (meaning Inno Setup Script) extension. Thescript controls every aspect of the installation. It specifies whichfiles are to be installed and where, what shortcuts are to be createdand what they are to be named, and so on. <br />
<br />
Script files are usually edited from inside the Setup Compiler program. After you have finishing writing the script , the next and final step is select "Compile" in the SetupCompiler. What this does is create a complete, ready-to-run Setupprogram based on your script. By default, this is created in adirectory named "Output" under the directory containing the script.<br />
<br />
To give you an idea of how this all works, start the Setup Compiler,click File | Open, and select one of the script files in the Samplessubdirectory located under the Inno Setup directory. (It may be helpfulto use the sample scripts as a template for your own scripts.)<br />
<br />
<span><strong>Here are some key features of "Inno Setup":</strong></span><br />
<br />
Support for all 32-bit Windows versions in use today -- Windows 95, 98, 2000, XP, Me, NT 4.0. <br />
Supports creation of a single EXE to install your program for easy online distribution. Disk spanning is also supported. <br />
Standard wizard interface, including support for the latest Windows 2000/XP wizard style. <br />
Customizable setup types, e.g. Full, Minimal, Custom. <br />
Complete uninstall capabilities. <br />
Installation of files:<br />
Includes integrated "deflate" file compression (the same compression.zip files use) and also supports bzip2 compression. The installer hasthe ability to compare file version info, replace in-use files, useshared file counting, register DLL/OCX s and type libraries, andinstall fonts. <br />
Creation of shortcuts anywhere, including in the Start Menu and on the desktop. <br />
Creation of registry and .INI entries. <br />
Silent install and uninstall. <br />
Full source code is available (Borland Delphi 2.0-5.0).<br />
</p>
<div class="celltext_big"><br />
<br />
<strong>What s New</strong> in This Release:<br />
<br />
Added new lzma/ultra64 compression level. Same as lzma/ultra, but uses a dictionary size that is twice as large (64 MB). <br />
Added new SetupLogging [Setup] section directive. If set to yes,Setup will always create a log file (equivalent to passing /LOG on thecommand line). <br />
Added new AppSupportPhone [Setup] section directive. <br />
Added new [Files] section flag: solidbreak. <br />
Added new [Run] and [UninstallRun] sections parameter: Verb. Whenused with the shellexec flag, specifies the action to be performed onthe file. <br />
When the shellexec flag is used in the [Run] and [UninstallRun]sections, it now uses the default verb for the file type instead ofhardcoding "open". (If necessary, you can override this by adding aVerb parameter.) <br />
Setup now supports a /TYPE parameter to override the default setup type. <br />
Components/tasks-related changes: /COMPONENTS &amp;. /TASKS: When aparent component/task is specified, it no longer automatically checksevery child component/task. To achieve the old behavior, prefix thename of the parent component/task with a "*" character, or list eachchild component/task individually. | /COMPONENTS: It is now possible toforce a child component to be deselected by including its name in thelist with a "!" prefix. (/TASKS already supports this.) | /COMPONENTSis now ignored if no custom type is defined. | /SAVEINF now writes theselected setup type in the INF file. Previously, using /LOADINF wouldalways select a custom type. | /SAVEINF now writes the selected tasksin the INF file. | When aMinVersion/OnlyBelowVersion/Languages/Check/Components parameter causesa parent component/task to be hidden from view, child items will now behidden as well. (Previously, it was necessary to include the sameconditions on every child item in order for them to be hidden alongwith the parent item.) | Fix: When new child components/tasks wereintroduced in a new install, they would always be selected by defaultif the parent component/task was selected in the previous installation.| Fix: /LOADINF would select child components that weren t selectedduring the initial install. | Fix: In a /COMPONENTS parameter, it is nolonger necessary to list fixed components in order for them to beselected.<br />
Pascal Scripting changes: FindFirst/FindNext: Add CreationTime,LastAccessTime, LastWriteTime, AlternateName fields to TFindRec. |TInputFileWizardPage: Added new IsSaveButton property. This can be usedto make a button open a Save As dialog instead of the default Opendialog. | TNewCheckListBox: Setting Checked[] to True will no longerautomatically check an item s child check boxes. To do that now, callthe new CheckItem method with coCheckWithChildren in the AOperationparameter. | ParamStr/ParamCount: Empty parameters ("") are no longerskipped. <br />
/LOG: Logged times now include milliseconds. <br />
Compiler IDE changes: During the compression phase of a compile, thestatus bar now shows the estimated time remaining and KBcompressed/second. | The Edit | Redo shortcut is now Ctrl+Y. Theprevious shortcut (Shift+Ctrl+Z) still works too. <br />
Fix: In the [INI] section, if Filename was blank, the uninsdelete* flags didn t actually delete anything. <br />
The uninstall program s version is now 51.47.0.0. <br />
Minor tweaks...</div></p></p>

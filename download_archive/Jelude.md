---
layout: downloadpage
permalink: /downloads/Jelude/
name: Jelude
file_type: download
title: Jelude
description: >-
  Jelude is a short NSIS script designed to allow JAR files to be wrapped in an EXE file so they can be made distributable to Windows users. The main advantage over distributing JAR files alone is that the end user is prompted when a Java Runtime ...
tags: [Debuggers-Decompilers-Dissasemblers]
category: Programming
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
version: 1.0
size: 249 KB
downloadurl: http://www.geocities.com/java_intro/jelude.zip
response: 302
by:
by_link:
license: Free
os: Windows
---

{% include download-header.html download=page%}

<p style="fix-download-text !important">
<p><font size="2">What is Jelude?</font></p>
<div class="chapter">
<p><font size="2">Jelude is a short NSIS</acronym> script designed to allow JAR files to be wrapped in an EXE</abbr> file so they can be made distributable to Windows users. The main advantage over distributing JAR files alone is that the end user is prompted when a Java Runtime Environment (JRE</acronym>) is not found on the computer and an option is provided to download it.</font></p>
<p><font size="2">Other features include:</font></p>
<ul>
    <li><font size="2">A single distributable with no floating files.</font></li>
    <li><font size="2">Support for multiple JAR files.</font></li>
    <li><font size="2">Runtime parameters are transferred to the Java application.</font></li>
    <li><font size="2">An optional splash screen can be shown at startup.</font></li>
    <li><font size="2">Free</font></li>
</ul>
<p><font size="2">Note that Jelude does not convert your actual Java code into a native application. Also, Jelude does not replace the role of a Java Virtual Machine (JVM</acronym>). </font></p>
</div>
<h2 class="instructions"><font size="2">How do I use Jelude?</font></h2>
<div class="chapter">
<ol>
    <li>
    <p><font size="2">First <strong>download</strong> the </font><font size="2">script and NSIS compiler</font><font size="2">.</font></p>
    </li>
    <li>
    <p><font size="2">Then <strong>open</strong> the script file using a text editor (like Notepad) and <strong>edit</strong> the first 2 lines to specify your application name and JAR filename. i.e.,</font></p>
    <p class="indented"><code><font size="2">!define APPNAME "<strong>Synergy Easter Egg Demo</strong>" <br />
    !define JARFILE "<strong>Egglet.jar</strong>" </font></code></p>
    <p class="diagrams"><font size="2"><img height="132" alt="A screenshot of the script file opened using notepad." width="491" src="http://www.geocities.com/java_intro/notepad.gif" /></font></p>
    </li>
    <li>
    <p><font size="2">Then <strong>compile</strong> the script using the NSIS compiler by running the following instruction at the command prompt. (In the same way you compile Java code):</font></p>
    <p class="indented"><code><font size="2">makensis.exe script.nsi</font></code></p>
    <p class="diagrams"><font size="2"><img height="108" alt="A screenshot of the command prompt entering the said commands." width="526" src="http://www.geocities.com/java_intro/cmd.gif" /></font></p>
    </li>
    <li>
    <p><font size="2">An EXE</abbr> file named launch.exe should be produced in the same directory. You can now <strong>distribute</strong> that <abbr>EXE</abbr> file to anyone.</font></p>
    </li>
</ol>
</div>
<h2 class="instructions"><font size="2">How does it work?</font></h2>
<div class="chapter">
<p><font size="2">When you execute the compiled program, the program will search the system registry and environment variables for a <acronym class="spelt">JRE</acronym> and if it exists, it will extract the JAR file to a temporary folder and execute it with the <acronym class="spelt">JRE</acronym>. Any parameters sent to the <abbr>EXE</abbr> would be passed along to the JAR file. The program will also register a <abbr title="MUTual EXclusion lock">mutex</abbr> with Windows for 5 seconds to prevent the same program from being executed multiple times if, for example, the user double clicks on the icon several times while the <acronym class="spelt" title="Java Virtual Machine">JVM</acronym> is still loading. If a splash screen is specified, it will be displayed for 4 seconds. </font></p>
<p><font size="2">However, if no <acronym class="spelt">JRE</acronym> is found, it will display an error message.</font></p>
<p class="diagrams"><font size="2"><img height="139" alt="A screenshot of the popup dialog shown when a Java Runtime Environment is not found." width="519" src="http://www.geocities.com/java_intro/popup.gif" /></font></p>
<p><font size="2">If the user clicks on the "Yes" button on the error message dialog box, they would be directed to the Sun website to download the <acronym class="spelt">JRE</acronym>. If the user clicks "no", the application exits.</font></p>
</div>
<h2 class="instructions"><font size="2">License?</font></h2>
<div class="chapter">
<p><font size="2">This script is license free and is considered a part of the </font><font color="#0000ff" size="2">public domain</font><font size="2">. Feel free to use it or add on to it. The NSIS compiler, however, is distributed by </font><font color="#0000ff" size="2">Nullsoft</font><font size="2"> and is subject to </font><font color="#0000ff" size="2">their license</font><font size="2">.</font></p>
</div>
<h2 class="instructions">
<p>&#160;</p>
<font size="2">Here is an inline copy of the script in it's entirety with nice formatting: <br />
</font></h2>
<div class="chapter">
<pre id="entirecode"><code><font face="Courier New"><font size="2"><span class="codecomment">;--------- CONFIGURATION ---------</span>

<span class="codecommand">!define</span> <span class="codevariable">APPNAME</span> <span class="codestring">"Synergy Easter Egg Demo"</span>
<span class="codecommand">!define</span> <span class="codevariable">JARFILE</span> <span class="codestring">"Egglet.jar"</span>

<span class="codecomment">;Uncomment the next line to specify an icon for the EXE.</span>
<span class="codecomment">;Icon "test.ico"</span>

<span class="codecomment">;Uncomment the next line to specify a splash screen bitmap.</span>
<span class="codecomment">;!define SPLASH_IMAGE "splash.bmp"</span>

<span class="codecomment">;---------------------------------</span>

<span class="codecommand">Name</span> <span class="codestring">"Jelude"</span>
<span class="codecommand">Caption</span> <span class="codestring">"${<span class="codevariable">APPNAME</span>}"</span>
<span class="codecommand">OutFile</span> <span class="codestring">"launch.exe"</span>

<span class="codecommand">SilentInstall</span> silent
<span class="codecommand">XPStyle</span> on

<span class="codecommand">!addplugindir</span> .

<span class="codecommand">Section</span> <span class="codestring">""</span>
  <span class="codecommand">System::Call</span> <span class="codestring">"kernel32::CreateMutexA(i 0, i 0, t 'jelude') i .r1 ?e"</span>
  <span class="codecommand">Pop</span> <span class="codevariable">$R0</span>
  <span class="codecommand">StrCmp</span> <span class="codevariable">$R0</span> 0 +2
  <span class="codecommand">Quit</span>

  <span class="codecommand">ClearErrors</span>
  <span class="codecommand">ReadRegStr</span> <span class="codevariable">$R0</span> HKLM <span class="codestring">"SOFTWARE\JavaSoft\Java Runtime Environment" "CurrentVersion"</span>
  <span class="codecommand">ReadRegStr</span> <span class="codevariable">$R0</span> HKLM <span class="codestring">"SOFTWARE\JavaSoft\Java Runtime Environment\<span class="codevariable">$R0</span>" "JavaHome"</span>
  <span class="codecommand">IfErrors</span> 0 FoundVM

  <span class="codecommand">ClearErrors</span>
  <span class="codecommand">ReadRegStr</span> <span class="codevariable">$R0</span> HKLM <span class="codestring">"SOFTWARE\JavaSoft\Java Development Kit" "CurrentVersion"</span>
  <span class="codecommand">ReadRegStr</span> <span class="codevariable">$R0</span> HKLM <span class="codestring">"SOFTWARE\JavaSoft\Java Development Kit\<span class="codevariable">$R0</span>" "JavaHome"</span>
  <span class="codecommand">IfErrors</span> 0 FoundVM

  <span class="codecommand">ClearErrors</span>
  <span class="codecommand">ReadEnvStr</span> <span class="codevariable">$R0</span> <span class="codestring">"JAVA_HOME"</span>
  <span class="codecommand">IfErrors</span> NotFound 0

  FoundVM:
  <span class="codecommand">StrCpy</span> <span class="codevariable">$R0</span> <span class="codestring">"<span class="codevariable">$R0</span>\bin\javaw.exe"</span>
  <span class="codecommand">IfFileExists</span> <span class="codevariable">$R0</span> 0 NotFound

  <span class="codecommand">StrCpy</span> <span class="codevariable">$R1</span> <span class="codestring">""</span>
  <span class="codecommand">Call</span> GetParameters
  <span class="codecommand">Pop</span> <span class="codevariable">$R1</span>

  <span class="codecommand">SetOverwrite</span> ifdiff
  <span class="codecommand">SetOutPath</span> <span class="codevariable">$TEMP</span>
  <span class="codecommand">File</span> <span class="codestring">"${<span class="codevariable">JARFILE</span>}"</span>
  <span class="codecommand">StrCpy</span> <span class="codevariable">$R0</span> <span class="codestring">'<span class="codevariable">$R0</span> -jar "${<span class="codevariable">JARFILE</span>}" <span class="codevariable">$R1</span>'</span>
  <span class="codecommand">Exec</span> <span class="codestring">"<span class="codevariable">$R0</span>"</span>

  <span class="codecommand">!ifdef</span> <span class="codevariable">SPLASH_IMAGE</span>
    <span class="codecommand">SetOutPath</span> <span class="codevariable">$TEMP</span>
    <span class="codecommand">File</span> /oname=spltmp.bmp <span class="codestring">"${<span class="codevariable">SPLASH_IMAGE</span>}"</span>
    <span class="codecommand">Splash::show</span> 4000 <span class="codestring">"<span class="codevariable">$TEMP</span>\spltmp"</span>
    <span class="codecommand">Delete</span> <span class="codestring">"<span class="codevariable">$TEMP</span>\spltmp.bmp"</span>
  <span class="codecommand">!endif</span>

  <span class="codecommand">Sleep</span> 5000
  <span class="codecommand">Quit</span>

  NotFound:
  <span class="codecommand">Sleep</span> 800
  <span class="codecommand">MessageBox</span> MB_ICONEXCLAMATION|MB_YESNO           </font></font><font face="Courier New"><font size="2"><span class="codestring">'Could not find a Java Runtime Environment installed on your computer.           <span class="codevariable">$\n</span>Without it you cannot run "${<span class="codevariable">APPNAME</span>}".           <span class="codevariable">$\n$\n</span>Would you like to visit the Java website to download it?'</span>           IDNO +2
  <span class="codecommand">ExecShell</span> open <span class="codestring">"http://java.sun.com/getjava"</span>
  <span class="codecommand">Quit</span>
<span class="codecommand">SectionEnd</span>

<span class="codecommand">Function GetParameters</span>
  <span class="codecommand">Push</span> <span class="codevariable">$R0</span>
  <span class="codecommand">Push</span> <span class="codevariable">$R1</span>
  <span class="codecommand">Push</span> <span class="codevariable">$R2</span>
  <span class="codecommand">StrCpy</span> <span class="codevariable">$R0 $CMDLINE</span> 1
  <span class="codecommand">StrCpy</span> <span class="codevariable">$R1</span> <span class="codestring">'"'</span>
  <span class="codecommand">StrCpy</span> <span class="codevariable">$R2</span> 1
  <span class="codecommand">StrCmp</span> <span class="codevariable">$R0</span> <span class="codestring">'"'</span> loop
  <span class="codecommand">StrCpy</span> <span class="codevariable">$R1</span> <span class="codestring">' '</span>
  loop:
    <span class="codecommand">StrCpy</span> <span class="codevariable">$R0 $CMDLINE</span> 1 <span class="codevariable">$R2</span>
    <span class="codecommand">StrCmp</span> <span class="codevariable">$R0 $R1</span> loop2
    <span class="codecommand">StrCmp</span> <span class="codevariable">$R0</span> <span class="codestring">""</span> loop2
    <span class="codecommand">IntOp</span> <span class="codevariable">$R2 $R2</span> + 1
    <span class="codecommand">Goto</span> loop
  loop2:
    <span class="codecommand">IntOp</span> <span class="codevariable">$R2 $R2</span> + 1
    <span class="codecommand">StrCpy</span> <span class="codevariable">$R0 $CMDLINE</span> 1 <span class="codevariable">$R2</span>
    <span class="codecommand">StrCmp</span> <span class="codevariable">$R0</span> <span class="codestring">" "</span> loop2
  <span class="codecommand">StrCpy</span> <span class="codevariable">$R0 $CMDLINE</span> <span class="codestring">""</span> <span class="codevariable">$R2</span>
  <span class="codecommand">Pop</span> <span class="codevariable">$R2</span>
  <span class="codecommand">Pop</span> <span class="codevariable">$R1</span>
  <span class="codecommand">Exch</span> <span class="codevariable">$R0</span>
<span class="codecommand">FunctionEnd</span></font></font></code></pre>
</div>
<h2><font size="2">Why did I create Jelude?</font></h2>
<div class="chapter">
<p><font size="2">It's because I wanted to experiment with </font><font size="2">NSIS</font><font size="2"> before I do any real work with it. NSIS stands for, Nullsoft Scriptable Installation System, and is created by the same people who brought you, </font><font size="2">Winamp</font><font size="2">. Since I am a Java programmer, I decided to create a JAR distribution program.</font></p>
</div>
<h2><font size="2">The script is indeed really short!?</font></h2>
<div class="chapter">
<p><font size="2">Yes it is. It shows how powerful NSIS can be with just a few lines of code. (See below for an inline version of the NSIS script.) I decided to keep the script short but simple rather than long but powerful because that was what I wanted. As long as it gets it's job done. Note that because of this, it will only run the JRE if it is version <code>1.2.X</code> and above and was produced by Sun. If you want fine tuned version checking, you will have to do it from within your Java application.</font></p>
<p><font size="2">Note: Jelude uses the "System" plugin by Nik Medved, the "Splash" plugin by Justin &amp; Amir Szekely and the "GetParameters" code by Sunjammer.</font></p>
</div>
<h2><font size="2">Why name such a short program?</font></h2>
<div class="chapter">
<p><font size="2">I felt that quite a few Java programmers could benefit from this tool so I decided to give it a name so that others could find it easily via search engines. The name Jelude comes from the letter "J" and the word "elude" which is meant to show how easily Java applications could be designed to mimic native Windows applications.</font></p>
</div>
<h2 class="troubleshooter"><font size="2">How can I show the text console for my application?</font></h2>
<div class="chapter">
<p><font size="2">You can show the text console by editing the following line in the script to use <code>java.exe</code> instead of <code>javaw.exe</code> to launch the Java application:</font></p>
<p class="indented"><code><font size="2">StrCpy $R0 "$R0\bin\<strong class="codeimportant">javaw</strong>.exe" </font></code></p>
<font size="2">change to </font>
<p class="indented"><code><font size="2">StrCpy $R0 "$R0\bin\java.exe" </font></code></p>
</div>
<h2 class="troubleshooter"><font size="2">How can I specify more than one JAR file?</font></h2>
<div class="chapter">
<p><font size="2">If you want to specify more JAR files to extract, simply edit the following line to include a reference to your jar files.</font></p>
<p class="indented"><code><font size="2">SetOutPath $TEMP <br />
File "${JARFILE}" <br />
</font><font size="2"><strong class="codeimportant">File "second.jar" <br />
File "third.jar"</strong> <br />
StrCpy $R0 '$R0 -jar "${JARFILE}" $R1' </font></code></p>
<p><font size="2">The additional files will automatically be included when you compile the script. If you do decide to use multiple JAR files, don't forget to include the <strong>classpath</strong> information within the main JAR file's <strong>MANIFEST</strong> file. For more information on how to do this, read the JAR file documentation below.</font></p>
</div>
<h2 class="troubleshooter"><font size="2">How can I modify where the JAR file is extracted?</font></h2>
<div class="chapter">
<p><font size="2">By default, the JAR file is extracted to the computer's default temporary folder. This is usually located in "C:\Windows\Temp" and is represented by the </font><font color="#000000" size="2">symbolic constant</font><font size="2">, "<code>$TEMP</code>". You can change the output folder to the folder where the <abbr>EXE</abbr> file is currently residing by editing the following line in the script:</font></p>
<p class="indented"><code><font size="2">SetOutPath $TEMP </font></code></p>
<font size="2">change to </font>
<p class="indented"><code><font size="2">SetOutPath <strong class="codeimportant">$EXEDIR</strong> </font></code></p>
</div>
<h2 class="troubleshooter"><font size="2">How can I locate the directory of the <abbr>EXE</abbr> file in the Java application?</font></h2>
<div class="chapter">
<p><font size="2">You can explicitly pass the <abbr>EXE</abbr> file's directory information to the Java application by using Java's </font><font color="#000000" size="2">System Properties</font><font size="2"> facility. You can do this by editing the following line in the script:</font></p>
<p class="indented"><code><font size="2">StrCpy $R0 '$R0 -jar "${JARFILE}" $R1' </font></code></p>
<font size="2">change to </font>
<p class="indented"><code><font size="2">StrCpy $R0 '$R0 <strong class="codeimportant">-Dexe.dir="$EXEDIR"</strong> -jar "${JARFILE}" $R1' </font></code></p>
<p><font size="2">Then when you need to locate the directory information inside your Java application, simply call, <code>System.getProperty("exe.dir")</code> which returns a <code>String</code>. This feature may be useful if the <abbr>EXE</abbr> file is accompanied with other files in the same directory. </font></p>
</div>
<h2 class="troubleshooter"><font size="2">How can I make it delete the JAR file after it exits?</font></h2>
<div class="chapter">
<p><font size="2">You can specify that the <abbr>EXE</abbr> file deletes the JAR file from the temporary folder after it exits, by editing the following line in the script. If left unchanged, the default configuration is to leave the JAR file in the temporary folder so that on subsequent launches the JAR does not have to be extracted everytime.</font></p>
<p class="indented"><code><font size="2">Exec "$R0" </font></code></p>
<font size="2">change to </font>
<p class="indented"><code><font size="2">Exec<strong class="codeimportant">Wait</strong> "$R0" <br />
<strong class="codeimportant">Delete "${JARFILE}"</strong> </font></code></p>
<p><font size="2">If you do modify the code, the <abbr>EXE</abbr> file will then persist in memory until the Java application exits whereafter the <abbr>EXE</abbr> file will delete the JAR file and exit itself.</font></p>
<p><font size="2">It is <strong>important</strong> to note that the splash screen is shown <em>after</em> the call to start the <acronym class="spelt" title="Java Virtual Machine">JVM</acronym>. If you make the above changes, the program will pause until the <acronym class="spelt" title="Java Virtual Machine">JVM</acronym> exits which therefore prevents the splash screen from being shown beforehand.</font></p>
</div>
<h2 class="instructions"><font size="2">What are JAR files?</font></h2>
<div class="chapter">
<p><font color="#000000" size="2">JAR files</font><font size="2"> are the distribution format recommended for Java applications. You can use the JAR tool provided by Sun to store all your CLASS files, image files and data files <font color="#000000">into one JAR file for easy transportation. JAR files are by default compressed files. For more information and instructions for producing and using JAR files, read the </font></font><font color="#000000" size="2">JAR Tutorial</font><font size="2"><font color="#000000">.</font>&#160;</font></p>
</div></p>

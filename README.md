# SPPU_DS_IT_Practical
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>

<h1>Assignment Readme</h1>

<p>This repository contains assignments and associated instructions for various tasks and projects.</p>

<h2>Pre-requisites</h2>

<p>Before running any of the assignments, ensure you have JDK 8 installed:</p>

<pre><code>sudo apt-get remove openjdk*
sudo apt update
sudo apt install openjdk-8-jdk openjdk-8-jre
</code></pre>

<h2>Assignment Instructions</h2>

<h3>Assignment 1</h3>

<ol>
<li><strong>Terminal 1:</strong></li>
<pre><code>javac Client/.java &amp;&amp; javac Server/.java
rmiregistry 5000
</code></pre>

<li><strong>Terminal 2:</strong></li>
<pre><code>java Server.ServerMain
</code></pre>

<li><strong>Terminal 3:</strong></li>
<pre><code>java Client.ClientMain
</code></pre>
</ol>

<h3>Assignment 2 (Calculator)</h3>

<ol>
<li><strong>Terminal 1:</strong></li>
<pre><code>idlj -fall Calc.idl
sudo apt install openjdk-8-jdk-headless
sudo apt update
</code></pre>

<li><strong>Terminal 2:</strong></li>
<pre><code>javac CalcApp/.java CalcApp/CalcPackage/.java CalcClient.java CalcServer.java
orbd -ORBInitialPort 1050 -ORBInitialHost localhost &amp;
</code></pre>

<li><strong>Terminal 3:</strong></li>
<pre><code>java -cp .:target/dependency/* CalcServer -ORBInitialPort 1050 -ORBInitialHost localhost
</code></pre>

<li><strong>Terminal 4:</strong></li>
<pre><code>java -cp .:target/dependency/* CalcClient -ORBInitialPort 1050 -ORBInitialHost localhost
</code></pre>
</ol>

<h3>Assignment 2 (Reverse String)</h3>

<ol>
<li><strong>Terminal 1:</strong></li>
<pre><code>idlj -fall ReverseModule.idl
javac .java ReverseModule/.java
orbd -ORBInitialPort 1056&amp;
java ReverseServer -ORBInitialPort 1056&amp;
</code></pre>

<li><strong>Terminal 2:</strong></li>
<pre><code>java ReverseClient -ORBInitialPort 1056 -ORBInitialHost localhost
</code></pre>
</ol>

<h3>Assignment 3</h3>

<ol>
<li><strong>Download MPJ from <a href="https://sourceforge.net/projects/mpjexpress/files/releases/mpj-v0_44.tar.gz/download">here</a></strong></li>

<li><strong>Set MPJ_HOME:</strong></li>
<pre><code>export MPJ_HOME=(Copy path from bin of extracted mpj directory)
</code></pre>

<li><strong>Compile and run:</strong></li>
<pre><code>javac -cp $MPJ_HOME/lib/mpj.jar ArrSum.java
$MPJ_HOME/bin/mpjrun.sh -np 4 ArrSum
</code></pre>
</ol>

<h3>Assignment 3 (Classroom)</h3>

<ol>
<li><strong>Setup:</strong></li>
<pre><code>sudo apt update
sudo apt install python3-pip
sudo apt-get install mpich # for MPICH
pip install mpi4py --upgrade
</code></pre>

<li><strong>Run:</strong></li>
<pre><code>python3 filename.py
</code></pre>
</ol>

<h3>Assignment 4</h3>

<ol>
<li><strong>Terminal 1:</strong></li>
<pre><code>python3 server.py
</code></pre>

<li><strong>Terminal 2:</strong></li>
<pre><code>python3 client.py
</code></pre>
</ol>

<h3>Assignment 4 (Classroom)</h3>

<ol>
<li><strong>Setup:</strong></li>
<pre><code>sudo apt install openjdk-11-jre-headless
</code></pre>

<li><strong>Run:</strong></li>
<pre><code>java assignment4.java
</code></pre>
</ol>

<h3>Assignment 5</h3>

<pre><code>javac Tring.java
java Tring
</code></pre>

<h3>Assignment 6</h3>

<pre><code>javac Bully.java
java Bully

javac Ring.java
java Ring
</code></pre>

<h3>Assignment 7</h3>

<ol>
<li><strong>Step 1:</strong></li>
<pre><code>pip install flask
</code></pre>

<li><strong>Step 2 (Terminal 1):</strong></li>
<pre><code>python3 app.py
</code></pre>

<li><strong>Step 3 (Terminal 2):</strong></li>
<pre><code>python3 distributed_app.py
</code></pre>

<li><strong>Step 4:</strong></li>
<p>Open <a href="http://localhost:5000/hello">http://localhost:5000/hello</a> for output.</p>
</ol>

<h3>Assignment 9 (Content Beyond Syllabus)</h3>

<ol>
<li><strong>Terminal 1:</strong></li>
<pre><code>javac *.java
java Server
</code></pre>

<li><strong>Terminal 2:</strong></li>
<pre><code>java Client
</code></pre>
</ol>

<!-- Add other assignments here -->

</body>
</html>

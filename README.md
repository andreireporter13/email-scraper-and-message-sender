<h1>Email Scraper and Message Sender</h1>
<br>
<p><strong>This is a portofolio script, but it works perfectly. This include the following functional libraries: </strong></p>
<br>
<ol>
  <li>googlesearch-python</li>
  <li>playwright</li>
  <li>re</li>
  <li>smtplib</li>
</ol>
<br>
<p>This script works with google smtp server. If you have 2factor authentification, you need create a password to <br>
conect your email without any errors and problems. </p>

<br> 
<p> In this tutorial you will see how to generate an app password: </p><a href="https://support.teamgate.com/hc/en-us/articles/115002064229-How-to-create-a-password-to-connect-email-while-using-2-step-verification-in-Gmail-">Gmail 2F auth app password</a>
<br> 
<h2> This is a portofolio app, take care with GDPR. </h2>
<p> It my another portofolio app. This script didn't work with Proxy or VPN. Even if it would work with <br>
Proxy or VPN, you send with your email adress. So... be careful. If you send many emails <br> 
and didn't respect GDPR policy, you may have problems. You can find many information about email sender strategy <br> 
in internet. This script works for RO_ro Google Search area. </p>
<br> 
<p> You have a 2f auth password. Its great. Now, you need find a folder with name: "email_sender", <br>
in this folder, you will find a config.py file. Great! You need do complete variable email and password <br>
with your data. </p>
<br>
<pre><code>
email = ''      # here input your email adress
password= ''    # here input your password or 2F auth password
</code></pre>
<br> 
<p> If you want to customize the Plain text messages or edit the HTML template, <br>
you can also find the text_data.py file in this folder.
<br>
<h2> How install this script? </h2>
<p> You cand download this script with command: </p>
<pre><code>git clone https://github.com/andreireporter13/email_scraper_and_message_sender.git
</code></pre>
<br> 
<p> After this, you need create special virtual environments. A show how install it on Linux: </p>
<pre><code>python3 -m venv venv_name
</code></pre>
<br>
<p> After installing venv, you need install libraries: </p>
<pre><code>pip3 install -r requirements.txt
</code></pre>
<br> 
<p> If you want to use this CLI app, you must insert this command: </p>
<pre><code>python3 email_finder_sender_main.py
</code></pre>
<br> 
<p> If you run this script, the questions that you will have to fill in with the necessary data will begin to flow.</p>
<h3>Thank you for yout atention. If you need something else, you cand find me on my website: </h3>
<a href="https://webautomation.ro"></strong>Web Automation RO_ro</strong></a>


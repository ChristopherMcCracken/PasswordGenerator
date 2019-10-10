# PythonProject

**1 Objective:** 

The objective of this project is to create a password
manager similar to LastPass. However, instead of 
storing the user’s passwords, a unique password 
would be generated consistently using an algorithm 
that generates the password based on some data 
provided by the user and the site’s URL. 
 
**2 Approach:** 

We plan to initially have the user provide a master 
password. This password will be used alongside a 
provided URL to send into an algorithm in order to 
create a unique password for each site. 
After the basic algorithm for the password generation 
is created, we will then focus on getting URL fetching
to work. By URL fetching we mean we would like to 
grab the URL of a login page, and then using this 
as a unique string to allow for unique passwords 
between each website our application is used for. 
We want to have it work for Chrome on Windows 
initially, and support different browsers and 
platforms if time permits. 
Once URL fetching has been completed. We want to move
onto making the passwords more secure. The first 
step to making the passwords more secure is to take
the master password and URL and send it into an 
algorithm which will obfuscate this data into a 
much more secure, difficult to predict password. 
It is important to note that this algorithm is the
key principle behind this application. This 
algorithm will consistently generate the same 
password given same master password and URL. Next
to make our program more secure we hope to use 
facial recognition, where we will get a master 
scan of the user’s face and use that in place of 
the master password. We will then use this image 
whenever we verify the user. With Python, we can 
either use simpleCV or openCV tools to help scan
faces for the password. We are leaning more 
towards simpleCV as it was built directly for 
Python. We will determine the facial scan by 
either using a combination of height/width or
by using specific features from an individual's
face(i.e. Moles, scars). The scan will be 
stored in a data set and be compared to the
scan before it will either allow access or 
deny the user access.

**3 Possible Issues:** 

One of the biggest issues that we believe we will 
face is getting the user’s biometrics to work. We 
intend to use facial recognition as a means to 
generate a unique string. It may be difficult to use 
facial recognition to generate a consistent unique 
string. As a backup we plan to use a user memorized 
password as the unique string as opposed to facial 
recognition. Although this provides a minor 
inconvenience of having to remember a password, 
the application will still perform its main purpose; 
Allowing for strong, unique passwords across multiple 
websites without the need to remember numerous 
passwords, while storing no passwords 
directly anywhere.

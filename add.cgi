#!/usr/bin/python
import os

qs = os.environ['QUERY_STRING']

if(qs):
        user = qs.split('=')[1]
        print ("Set-Cookie: usename =" + str(user))


print ("Content-Type: text/html")     
print ("")


print ("""
<html>
    <head>
        <meta charset="utf-8">
        <title>A2Q1</title>
        <link rel="stylesheet" type="text/css" href="index2.css" />
    </head>

    <body> """)
print("<h1>Add a task for: %s</h1>") %user

print("""
        <form action="welcomeNewSignUp.cgi" method="get">

            <div>
                <label for="Id">User</label> 
                <input type="text" id="id" name="user_id">
            </div>

            <div>
                <label for="Id">Action:</label> 
                <input type="text" id="id" name="user_id">
            </div>
            <div>
                <label for="password">Description</label> 
                <input type="password" id="password" name="user_password">
            </div>
            <div>
                <input type="radio" id="contactChoice1"
                name="contact" value="email">
                <label for="contactChoice1">Medium</label>

                <input type="radio" id="contactChoice2"
                name="contact" value="phone">
                <label for="contactChoice2">Low</label>

                <input type="radio" id="contactChoice3"
                name="contact" value="mail">
                <label for="contactChoice3">High</label>
            </div>
            <div class="button">
                <button type="submit">Add</button>
            </div>
        </form>
    </body>
</html>
""")

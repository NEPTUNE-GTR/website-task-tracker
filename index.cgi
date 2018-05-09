#!/usr/bin/python
import os
import json


obj  = json.load(open("users.json"))
ActionToDelete = ""

possibleUser   = ""

if 'HTTP_COOKIE' in os.environ:  
    possibleUser = os.environ["HTTP_COOKIE"].split("=")[1]

print ("Content-Type: text/html")     
print ("")

print ("""
<html>
    <head>
        <meta charset="utf-8">
        <title>A2Q2 dropdown menu</title>
        <link rel="stylesheet" type="text/css" href="index2.css" />
    </head>

    <body>
        <form action="add.cgi" method="get">
            <select id="sel" name="name" onchange="show(this.value);">
                <option value="">-- Select a user --</option>
            </select>

            <input type="submit"  value="Add action" />
        </form>
        <p id="demo"></p>

        <script type="text/javascript" language="JavaScript">
            window.onload = populateSelect();

            function populateSelect() 
            {
                // CREATE AN XMLHttpRequest OBJECT, WITH GET METHOD.
                var xhr = new XMLHttpRequest(), 
                    method = 'GET',
                    overrideMimeType = 'application/json',
                    url = 'users.json';        // ADD THE URL OF THE FILE.

                xhr.onreadystatechange = function () 
                {
                    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) 
                    {
                        // PARSE JSON DATA.
                        var users = JSON.parse(xhr.responseText);
                        var ele = document.getElementById('sel');
                        for (var i = 0; i < users.length; i++) 
                        {
                            if(users[i].name.localeCompare("%s") == 0)
                            {
                                ele.innerHTML = ele.innerHTML + '<option value="' + users[i].name + '" selected = "selected">' + users[i].name + '</option>';
                            }
                            else
                            {
                                // BIND DATA TO <select> ELEMENT.
                                ele.innerHTML = ele.innerHTML + '<option value="' + users[i].name + '">' + users[i].name + '</option>';
                            }
                        }
                    }
                };
                xhr.open(method, url, true);
                xhr.send();
            }
            function show(ele) 
            {
                var obj; 
                var dbParam; 
                var xmlhttp;
                var myObj;
                var x;
                var txt  = '';

                obj = { "form":sel, "limit":55 };
                dbParam = JSON.stringify(obj);
                xmlhttp = new XMLHttpRequest();
                xmlhttp.onreadystatechange = function() 
                {
                    if (this.readyState == 4 && this.status == 200) 
                    {
                        myObj = JSON.parse(this.responseText);

                        txt += '<form>'
                        for (var i=0; i < myObj.length; i++) 
                        {
                            if(ele.localeCompare(myObj[i].name) == 0)
                            {
                                txt += "<h1>" + myObj[i].name + "</h1>"
                                for (var j=0; j < myObj[i].actions.length; j++) 
                                {
                                    txt += '<p> Action:' + j + '- ' + myObj[i].actions[j] + '</br>' + 'Priority: ' + myObj[i].priorities[j] +
                                    '</br>' + 'Description: ' + myObj[i].descriptions[j] + '</br> ' +
                                    ' <input type = "button" value="delete" onclick = "deleteFunction('+ i +' , '+ myObj[i].actionIndex[j] +' , ele)"></p>'
                                    txt += '<hr>';
                                }
                            }
                        }
                        txt += '</form>'
                        document.getElementById("demo").innerHTML = txt;
                    }
                };
                xmlhttp.open("POST", "users.json", true);
                xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xmlhttp.send("x=" + dbParam);
            }
            function deleteFunction(index, actionIndex, ele)
            {
                var xmlhttp;
                var myObj;

                xmlhttp=new XMLHttpRequest();
            
                xmlhttp.onreadystatechange = function() 
                {
                    if (this.readyState == 4 && this.status == 200) 
                    {
                        document.getElementById("demo").innerHTML = xmlhttp.responseText;
                    }
                };
                var url =  "delete.cgi?index=" + index.toString() + "&actionIndex=" + actionIndex.toString();
                xmlhttp.open("GET",url, true);
                xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xmlhttp.send();
                show(ele);
            }
        </script>
    </body>
</html>
""" % possibleUser)



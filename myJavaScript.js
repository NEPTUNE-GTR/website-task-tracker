

window.onload = loadJSON();

function loadJSON() {   

    //making an XMLHttpRequest object, with the get method
    var xobj = new XMLHttpRequest();
    
    xobj.overrideMimeType("application/json");
    xobj.open('GET', 'users.json', true); 
    xobj.onreadystatechange = function () {
        if (xobj.readyState == 4 && xobj.status == "200") 
        {
            //Parsing the JSON data

            //first convert JSON string into object
            var users = JSON.parse(xobj.responseText);

            var elements = document.getElementById('sel');
            
            for(var i = 0; i < Users.length; i ++)
            {
                //bind data to <select> element

                ele.innterHTML = ele.innterHTML + '<option value=">' + Users[i].name + '</option>';

            }
        }
    };
    xobj.send();  
 }
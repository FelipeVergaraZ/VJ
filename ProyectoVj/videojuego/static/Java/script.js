function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function validar() {
    var a = document.forms["myForm"]["username"].value;
    if (a == "") {
        alert("Falta llenar el Usuario,\n ");
        return false;
    }
    var b = document.forms["myForm"]["email"].value;
    if (b == "") {
        alert("Falta llenar el Email");
        return false;
    }
    var c = document.forms["myForm"]["phone"].value;
    if (c == "") {
        alert("Falta llenar el numero");
        return false;
    }
    var d = document.forms["myForm"]["message"].value;
    if (d == "") {
        alert("Falta llenar el mensaje");
        return false;
    }
    console.log (email, 'hola');
    email.send({
        
    })


    



}

function iniciarMap() {
    var coord = { lat: -32.7723101, lng: -71.5333 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}

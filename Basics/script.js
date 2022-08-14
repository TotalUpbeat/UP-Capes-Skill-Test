function validate(event){
    var username=document.getElementById("username").value;
    var password=document.getElementById("password").value;
    if (username=='admin' && password=='123'){
        alert('login succesfully')
    } else{
        alert('invalid credentials')
    }
}
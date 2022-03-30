const ValidateLogin = () =>{
    let useremail = document.getElementById("useremail");
    let password = document.getElementById("password");
    let rememberme = document.getElementById("rememberme");
    if(useremail.value.trim() === '' || password.value.trim() === ''){
        if(useremail.value.trim() === ''){
            useremail.style.borderColor = "red";
            return false;
        }else{
            password.style.borderColor = "red";
            return false;
        }
    }else{
        if(rememberme.checked){
            localStorage.setItem("useremail", useremail.value.trim())
            localStorage.setItem("password", password.value.trim())
        }else{
            alert("not checked");
            return false;
        }
    }
}

const removeError = (clicked_id) =>{
    document.getElementById(clicked_id).style.borderColor = "#868E27";
}

const ShowHidePassword = () =>{
    let target = document.getElementById("password");
    if(target.type == "password"){
        target.type = "text";
    }else{
        target.type="password";
    }
}

const getdetails = () =>{
    let uname = localStorage.getItem("useremail");
    let pname = localStorage.getItem("password");
    if(uname != ''){
        document.getElementById("useremail").value= uname;
        document.getElementById("password").value = pname;
    }
setTimeout("getdetails", 1000);
}
window.onload = getdetails;



const resetShowHidePassword = () =>{
    let target = document.getElementById("passwords");
    if(target.type == "password"){
        target.type = "text";
    }else{
        target.type="password";
    }
}


const confShowHidePassword = () =>{
    let target = document.getElementById("cpasspassword");
    if(target.type == "password"){
        target.type = "text";
    }else{
        target.type="password";
    }
}


const ValidateReset = () =>{
    let useremail = document.getElementById("useremails");
    let password = document.getElementById("passwords");
    let confirmpass = document.getElementById("cpasspassword");
    if(useremail.value.trim() === '' || password.value.trim() === '' || confirmpass.value.trim() === ''){
        if(useremail.value.trim() === ''){
            useremail.style.borderColor = "red";
            return false;
        }else if(password.value.trim() === ''){
            password.style.borderColor = "red";
            return false;
        }else{
            confirmpass.style.borderColor = "red";
            return false;
        }
    }else{
        if(password.value.trim() != confirmpass.value.trim()){
            password.style.borderColor = "red";
            confirmpass.style.borderColor = "red";
            return false;
        }
    }
}
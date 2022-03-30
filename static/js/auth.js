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
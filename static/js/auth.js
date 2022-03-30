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
            alert("checked");
            return false;
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
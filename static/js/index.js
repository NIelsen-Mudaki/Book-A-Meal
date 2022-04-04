const ValidateSignup = () =>{
    let fullname = document.getElementById("fullnames");
    let email = document.getElementById("emailadress");
    let phone = document.getElementById("phonenumber");
    let password = document.getElementById("userpassword");
    if(fullname.value.trim() === '' || email.value.trim() === '' || phone.value.trim() === '' || password.value.trim() ===''){
        if(fullname.value.trim() === ''){
            fullname.style.borderColor = "red";
            return false;
        }else if( email.value.trim() === ''){
            email.style.borderColor = "red";
            return false;
        }else if(phone.value.trim() === ''){
            phone.style.borderColor = "red";
            return false;
        }else{
            password.style.borderColor = "red";
            return false;
        }
    }else{
        let phonestr = String(phone.value.trim())
        if(phonestr.length > 9 && phonestr.length < 15){

        }else{
            alert("The contact provided is not a valid number")
            phone.style.borderColor = "red";
            return false;
        }
    }
}


const removeError = (clicked_id) =>{
    document.getElementById(clicked_id).style.borderColor = "#868E27";
}

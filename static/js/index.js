const HideShowItems = () =>{
    let tartget = document.getElementsByClassName("items");
    if(tartget.style.display == 'none'){
        tartget.style.display = 'block';
    }else{
        tartget.style.display = 'none'
    }
}
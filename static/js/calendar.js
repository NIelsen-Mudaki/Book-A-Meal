const callendar = ()=>{


let date = new Date()
let dates = date.getDate()
let months = date.getMonth()
let year = date.getFullYear()
let day = date.getDay()
let days = ['SUN','MON','TUE','WED','THUR','FRI','SAT']
let currrent_date = days[day] + "," + dates + "/" + (months + 1) + "/" + year
document.getElementById("calendarheader").innerHTML = currrent_date;
setTimeout("callendar", 1000)

//months
let months_array = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];
let months_current = months + 1;
let days_array = [31,28,31,30,30,31,31,31,31,31,30,31];
let target = document.getElementById("weeks");
for(let i = 0; i < days.length; i ++){
   let buttons =  document.createElement("BUTTON");
   buttons.innerText = days[i];
   buttons.setAttribute("id", days[i]);
   buttons.setAttribute("title", days[i]);
   buttons.setAttribute("class", "allbuttons");
   target.appendChild(buttons);

}
let targets = document.getElementById("days");
for(let m = 0; m < days_array[months_current]; m ++){
    let daysbtn = document.createElement("BUTTON");
    let ids = "day" + (m + 1);
    daysbtn.setAttribute("id", ids);
    daysbtn.setAttribute("title", m +1);
    daysbtn.setAttribute("class", "allbuttons");
    daysbtn.innerText = m + 1;
    targets.appendChild(daysbtn);
}
document.getElementById(days[day]).style.color = "#FFFFFF";
document.getElementById(days[day]).style.backgroundColor = "#868E27";
let ids = "day" + dates;
document.getElementById(ids).style.color = "#FFFFFF";
document.getElementById(ids).style.backgroundColor = "#868E27";
}
window.onload = callendar
let date = new Date()
let dates = date.getDate()
let months = date.getMonth()
let year = date.getFullYear()
let day = date.getDay()
let days = ['SUN','MON','TUE','WED','THUR','FRI','SAT']
console.log(days[day] + "," + dates + "/" + (months + 1) + "/" + year)
document.getElementById("calendar_header").innerHTML = "dates";
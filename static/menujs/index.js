$(() => {
  let active_date = $("#menudate").val();
  document.cookie = `activedate=${active_date}`;
  $("#menudate").on("change", (event) => {
    console.log("date changed");
    var selected_date = $("#menudate").val();
    document.cookie = "activedate= ; expires = Thu, 01 Jan 1970 00:00:00 GMT";
    document.cookie = `activedate=${selected_date}`;
    localStorage.setItem("activedate", selected_date);
    $("#menudatepicker").submit();
  });

$('#notify').click((e)=>{
  e.preventDefault()
  $.ajax(
    {
      url:"/menu/notify",
      success:(()=>{alert('email notification sent');})
    }
  );
  return
})


});


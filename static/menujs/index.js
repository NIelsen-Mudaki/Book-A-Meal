// document.cookie='activedate=2022-04-06'
$(()=>{


$('#menudate').on('change',(event)=>{
  console.log('date changed');
  var selected_date=$('#menudate').val();
  document.cookie = "activedate= ; expires = Thu, 01 Jan 1970 00:00:00 GMT"
  document.cookie=`activedate=${selected_date}`;
  localStorage.setItem('activedate',selected_date);
  $('#menudatepicker').submit()
});


});
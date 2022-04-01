document.cookie='activedate=2022-04-06'
$(()=>{


$('#menudate').on('change',(event)=>{
  console.log('date changed');
  var selected_date=$('#menudate').val();
  document.cookie=`activedate=${selected_date}`
  $('#menudatepicker').submit()
});


});
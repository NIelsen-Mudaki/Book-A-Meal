// $(()=>{

//   $('#menuform').submit((e)=>{
//     e.preventDefault()
//     form=$('#menuform')
//     console.log('menu submitted');
//     // project=$('#targetproject').val()

//     // design_rating=$('input[name=designoptions]:checked')
//     // console.log(design_rating.val())
//     $.ajax({
//       'url':'/menu/create',
//       'type':'POST',
//       'data':form.serialize(),
//       'dataType':'json',
//       'success':(data)=>{
//         alert(data['success']);
//         window.location.reload()
      
//     },
//     })
//     // $('#ratingModal').modal('hide');
    
//    return false;
//   });

//   console.log('page loaded');
// })

$(()=>{


$('#menudate').on('change',(event)=>{
  console.log('date changed');
  console.log($('#menudate').val());
  $('#menudatepicker').submit()
});


});
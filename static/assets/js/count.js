// function state(){
//     var countDownDate = new Date("Jan 5, 2024 15:37:25").getTime();
//     var menu = document.getElementById("change");
//     var selected = menu.addEventListener("change", generateData);
//     var test = document.getElementById("demo");
//     function generateData(event){
//         if (menu.value == '1'){
//           var x = setInterval(function() {
//         var now = new Date().getTime();
//         var distance = countDownDate - now;
  
//         var minutes = Math.floor((distance % (1000 * 60)) / (1000 * 60));
//         var seconds = Math.floor((distance % (1000 * 60)) / 1000);
         
//         test.innerHTML = minutes + "m " + seconds + "s ";
//         if (distance < 0) {
//       clearInterval(x);
//       test.innerHTML = "EXPIRED";
//     }
// }, 1000);
// }

//  else if (menu.value == '2'){
//     var x = setInterval(function() {
//   var now = new Date().getTime();
//   var distance = countDownDate - now;

//   var minutes = Math.floor((distance % (1000 * 60 * 30)) / (1000 * 60));
//   var seconds = Math.floor((distance % (1000 * 60)) / 1000);
   
//   document.getElementById("demo").innerHTML = minutes + "m " + seconds + "s ";
//   if (distance < 0) {
// clearInterval(x);
// document.getElementById("demo").innerHTML = "EXPIRED";
// }
// }, 1000);
//   }
//   else if(menu.value == '3'){
//     var x = setInterval(function() {
//   var now = new Date().getTime();
//   var distance = countDownDate - now;

//   var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
//   var seconds = Math.floor((distance % (1000 * 60)) / 1000);
   
//   document.getElementById("demo").innerHTML = minutes + "m " + seconds + "s ";
//  if (distance < 0) {
// clearInterval(x);
// document.getElementById("demo").innerHTML = "EXPIRED";
// }
// }, 1000);
//   }
//   else if(menu.value == '4'){
//     var x = setInterval(function() {
//   var now = new Date().getTime();
//   var distance = countDownDate - now;

//   var minutes = Math.floor((distance % (1000 * 60 * 80)) / (1000 * 60));
//   var seconds = Math.floor((distance % (1000 * 60)) / 1000);
   
//   document.getElementById("demo").innerHTML = minutes + "m " + seconds + "s ";
//   if (distance < 0) {
// clearInterval(x);
// document.getElementById("demo").innerHTML = "EXPIRED";
// }
// }, 1000);
//   }
//   else if(menu.value == '5'){
//     var x = setInterval(function() {
//   var now = new Date().getTime();
//   var distance = countDownDate - now;
//   var hours = Math.floor((distance % (1000 * 60 * 60 * 5)) / (1000 * 60 * 60));
//   var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
//   var seconds = Math.floor((distance % (1000 * 60)) / 1000);
   
//   document.getElementById("demo").innerHTML =hours+"h"+ minutes + "m " + seconds + "s ";
//   if (distance < 0) {
// clearInterval(x);
// document.getElementById("demo").innerHTML = "EXPIRED";
// }
// }, 1000);
//   }
  
//   else if (menu.value == '6'){
//     var x = setInterval(function() {
//   var now = new Date().getTime();
//   var distance = countDownDate - now;
//   var hours = Math.floor((distance % (1000 * 60 * 60 * 7)) / (1000 * 60 * 60));
//   var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
//   var seconds = Math.floor((distance % (1000 * 60)) / 1000);
   
//   document.getElementById("demo").innerHTML =hours+"h"+ minutes + "m " + seconds + "s ";
//   if (distance < 0) {
// clearInterval(x);
// document.getElementById("demo").innerHTML = "EXPIRED";
// }
// }, 1000);
//   }
//     }


// }

const getOption= ()=>{
  selectElement = document.querySelector('#change');
  output = selectElement.value;
  getTimer(output)
}   

let getTimer = (input)=>{
  let min =  input - 1
  let sec = 60
  setInterval(()=>{
      sec--;
      if(sec === 00){
          min--;
          if(min < 0 && sec == 0 ){
              min = 0
              sec = 0  
          }
          
      }
      clearInterval(sec)
      
      document.getElementById('demo').innerHTML = min + " : " + sec;
      
  },1000)

}
function Run(){
 
  var two = document.getElementsByClassName("two")
  var five = document.getElementsByClassName("five")
  var twenty = document.getElementsByClassName("twenty")
  var thirty = document.getElementsByClassName("thirty")
  var one = document.getElementsByClassName("one")
  var twox = document.getElementsByClassName("twox")






















function timer(){
// Set the date we're counting down to
var countDownDate = new Date("Jan 5, 2024 15:37:25").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds

  // var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (2000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("demo").innerHTML =  hours + "h "
  + minutes + "m " + seconds + "s ";

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "EXPIRED";
  }
}, 1000);


}


























//   if (s == two){
//     var end = new Date('02/25/2021 00:00 AM' );

//   }else if(s == five ){
//     var end = new Date('02/22/2021 6:30 AM');
//   }else if(s == twenty ){
//     var end = new Date('02/20/2021 9:30 AM');
//   }else if(s == thirty ){
//     var end = new Date('02/19/2021 12:30 AM');
//   }else if(s == one ){
//     var end = new Date('02/15/2021 2:30 AM');
//   }
//   else if(s == twox ){
//     var end = new Date('02/10/2021 5:30 AM');
//   }

// var _second = 1000
// var _minute = _second * 60;
// var _hour = _minute *60;
// var timer;

// function showRemaining(){
//   var now = new Date();
//   var distance = end - now;
   
//   if (distance < 0){
//     clearInterval(timer);
//     document.getElementById("demo").innerHTML= "its out already";
//     return;
//   }
//   var hour = Math.floor((distance % _hour) / _hour);
//   var minutes = Math.floor((distance % _hour) / _minute);
//   var seconds = Math.floor((distance % _minute)/ _second);
  

//   document.getElementById('demo').innerHTML = hour +'hour,'+ minutes + 'minutes,' + seconds + 'seconds.';
// }
// timer = setInterval(showRemaining, 1000);
// if ( s == 1){
//   document.getElementById('demo').innerHTML= "Dont select nothing";
//   end;
// }

}
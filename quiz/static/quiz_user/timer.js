//     var deadline = new Date("mar 03, 2022 16:25:00").getTime();
    function timer(){
  
    var minutes_from_user = 10
    var add = 60000*minutes_from_user
    var deadline = new Date().getTime();
    deadline += add
    
    var x = setInterval(function() {
    var now = new Date().getTime();
//     var deadline = new Date().getTime();
    console.log(deadline)
    var t = deadline - now;
  
    var hours = Math.floor((t%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
    var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((t % (1000 * 60)) / 1000);
 
    document.getElementById("hour").innerHTML =hours;
    document.getElementById("minute").innerHTML = minutes;
    document.getElementById("second").innerHTML =seconds;
    if (t < 0) {
            clearInterval(x);
            document.getElementById("demo").innerHTML = "TIME UP";
            document.getElementById("hour").innerHTML ='0';
            document.getElementById("minute").innerHTML ='0' ;
            document.getElementById("second").innerHTML = '0'; }
    }, 1000);

    }
    

  
    
    
   
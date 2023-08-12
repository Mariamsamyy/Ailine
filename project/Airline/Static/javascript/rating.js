
let buttons = document.getElementsByClassName("numberButton");
let chosen = "";

for(let btn of buttons) {
   btn.addEventListener("mouseover",function handleHover(event) {
      event.target.style.backgroundColor = 'rgb(251,116,19)';
      event.target.style.color = 'white';
   })
}

for(let btn of buttons) {
   btn.addEventListener("mouseout",function handleHoverOut(event) {
      event.target.style.backgroundColor = 'rgb(43,52,64)';
      event.target.style.color = 'rgb(149,158,172)';
      document.getElementById(chosen).style.backgroundColor = 'rgb(149,158,172)';
      document.getElementById(chosen).style.color = 'white';
   })
}

for(let btn of buttons) {
   btn.addEventListener("click",function handleClick(event) {

      for(let btn2 of buttons) {
         btn2.style.backgroundColor = 'rgb(43,52,64)';
         btn2.style.color = 'rgb(149,158,172)';
      }

      event.target.style.backgroundColor = 'rgb(149,158,172)';
      event.target.style.color = 'white';
      chosen = event.target.id;
   });
}

let btnSubmit = document.getElementById("submitButton");

btnSubmit.addEventListener("click",function handleSubmit(event) {
   
   if(chosen=="") {
      window.alert("Choose a rating first!");
      return;
   }

   let ratingElements = document.getElementsByClassName("ratingState");
   for(let el of ratingElements) {
      el.style.display = 'none';
   }

   let thankYouElements = document.getElementsByClassName("thankYouState");
   for(let el of thankYouElements) {
      el.style.display = 'block';
   }
   let spanEls = document.getElementsByTagName("span");
   spanEls[0].style.display = 'inline';
   spanEls[0].innerHTML = document.getElementById(chosen).innerHTML;
   // document.getElementsByTagName("span")[0].style.display = 'inline';
   document.getElementsByTagName("main")[0].style.alignItems = "center";
});
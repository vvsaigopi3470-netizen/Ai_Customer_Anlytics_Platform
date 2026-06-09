// =====================================
// LOADER
// =====================================

window.addEventListener(
"load",
function(){

const loader =
document.getElementById(
"loader"
);

if(loader){

loader.style.transition =
"0.5s";

loader.style.opacity =
"0";

setTimeout(()=>{

loader.style.display =
"none";

},500);

}

}
);


// =====================================
// DARK MODE
// =====================================

function toggleDarkMode(){

document.body.classList.toggle(
"dark-mode"
);

const enabled =
document.body.classList.contains(
"dark-mode"
);

localStorage.setItem(
"darkMode",
enabled
);

}

window.addEventListener(
"DOMContentLoaded",
function(){

const darkMode =
localStorage.getItem(
"darkMode"
);

if(darkMode === "true"){

document.body.classList.add(
"dark-mode"
);

}

}
);


// =====================================
// NAVBAR SCROLL EFFECT
// =====================================

window.addEventListener(
"scroll",
function(){

const navbar =
document.querySelector(
".custom-navbar"
);

if(!navbar) return;

if(window.scrollY > 50){

navbar.style.background =
"#020617";

navbar.style.boxShadow =
"0 4px 20px rgba(0,0,0,.25)";

}
else{

navbar.style.background =
"#0f172a";

navbar.style.boxShadow =
"none";

}

}
);


// =====================================
// CARD ANIMATION
// =====================================

document.addEventListener(
"DOMContentLoaded",
function(){

const cards =
document.querySelectorAll(

".feature-card," +
".stat-card," +
".segment-card," +
".prediction-card," +
".recommendation-card," +
".analytics-box," +
".glass-card"

);

cards.forEach(
(card,index)=>{

card.style.opacity = "0";
card.style.transform =
"translateY(30px)";

setTimeout(()=>{

card.style.transition =
"all .7s ease";

card.style.opacity =
"1";

card.style.transform =
"translateY(0px)";

}, index * 100);

}
);

}
);


// =====================================
// COUNTER ANIMATION
// =====================================

document.addEventListener(
"DOMContentLoaded",
function(){

const counters =
document.querySelectorAll(
".counter"
);

counters.forEach(counter=>{

let target =
parseInt(
counter.innerText
.replace(/\D/g,'')
);

if(isNaN(target))
return;

let count = 0;

let speed =
Math.max(
1,
Math.floor(target / 100)
);

const updateCounter = ()=>{

if(count < target){

count += speed;

counter.innerText =
count + "+";

requestAnimationFrame(
updateCounter
);

}
else{

counter.innerText =
target + "+";

}

};

updateCounter();

});

}
);


// =====================================
// CUSTOMER SEARCH TABLE
// =====================================

document.addEventListener(
"DOMContentLoaded",
function(){

const searchInput =
document.getElementById(
"searchInput"
);

if(!searchInput)
return;

searchInput.addEventListener(
"keyup",
function(){

const filter =
this.value.toUpperCase();

const rows =
document.querySelectorAll(
"#customerTable tbody tr"
);

rows.forEach(row=>{

const firstColumn =
row.cells[0];

if(!firstColumn)
return;

const text =
firstColumn.innerText
.toUpperCase();

row.style.display =
text.includes(filter)
? ""
: "none";

});

}
);

}
);


// =====================================
// SCROLL TO TOP BUTTON
// =====================================

document.addEventListener(
"DOMContentLoaded",
function(){

const btn =
document.createElement(
"button"
);

btn.innerHTML =
"⬆";

btn.id =
"scrollTopBtn";

document.body.appendChild(
btn
);

btn.style.position =
"fixed";

btn.style.bottom =
"20px";

btn.style.right =
"20px";

btn.style.padding =
"12px 15px";

btn.style.border =
"none";

btn.style.borderRadius =
"50%";

btn.style.fontSize =
"18px";

btn.style.cursor =
"pointer";

btn.style.display =
"none";

btn.style.zIndex =
"999";

btn.style.background =
"#4f46e5";

btn.style.color =
"white";

window.addEventListener(
"scroll",
function(){

btn.style.display =
window.scrollY > 300
? "block"
: "none";

}
);

btn.addEventListener(
"click",
function(){

window.scrollTo({

top:0,
behavior:"smooth"

});

}
);

}
);


// =====================================
// BUTTON RIPPLE EFFECT
// =====================================

document.addEventListener(
"DOMContentLoaded",
function(){

const buttons =
document.querySelectorAll(
".btn"
);

buttons.forEach(btn=>{

btn.addEventListener(
"click",
function(e){

const circle =
document.createElement(
"span"
);

const diameter =
Math.max(
btn.clientWidth,
btn.clientHeight
);

const radius =
diameter / 2;

circle.style.width =
circle.style.height =
`${diameter}px`;

circle.style.left =
`${e.clientX -
btn.offsetLeft -
radius}px`;

circle.style.top =
`${e.clientY -
btn.offsetTop -
radius}px`;

circle.classList.add(
"ripple"
);

const ripple =
btn.getElementsByClassName(
"ripple"
)[0];

if(ripple){

ripple.remove();

}

btn.appendChild(
circle
);

}
);

});

}
);


// =====================================
// SMOOTH SCROLL LINKS
// =====================================

document.querySelectorAll(
'a[href^="#"]'
).forEach(anchor=>{

anchor.addEventListener(
"click",
function(e){

e.preventDefault();

const target =
document.querySelector(
this.getAttribute(
"href"
)
);

if(target){

target.scrollIntoView({

behavior:"smooth"

});

}

}
);

});


// =====================================
// AI STATUS SIMULATION
// =====================================

document.addEventListener(
"DOMContentLoaded",
function(){

const status =
document.getElementById(
"ai-status"
);

if(status){

const states = [

"Analyzing...",
"Processing...",
"Generating Insights...",
"AI Active"

];

let index = 0;

setInterval(()=>{

status.innerText =
states[index];

index++;

if(index >= states.length){

index = 0;

}

},2000);

}

});


// =====================================
// PAGE TRANSITION
// =====================================

document.addEventListener(
"DOMContentLoaded",
function(){

document.body.style.opacity =
"0";

setTimeout(()=>{

document.body.style.transition =
"opacity .6s ease";

document.body.style.opacity =
"1";

},100);

}
);


// =====================================
// CONSOLE MESSAGE
// =====================================

console.log(
"%cAI Customer Analytics Platform Loaded Successfully",
"color:#4f46e5;font-size:16px;font-weight:bold;"
);
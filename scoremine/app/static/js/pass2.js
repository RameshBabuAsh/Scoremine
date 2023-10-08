function loco() {
    gsap.registerPlugin(ScrollTrigger);

// Using Locomotive Scroll from Locomotive https://github.com/locomotivemtl/locomotive-scroll

const locoScroll = new LocomotiveScroll({
  el: document.querySelector("#main"),
  smooth: true
});
// each time Locomotive Scroll updates, tell ScrollTrigger to update too (sync positioning)
locoScroll.on("scroll", ScrollTrigger.update);

// tell ScrollTrigger to use these proxy methods for the ".smooth-scroll" element since Locomotive Scroll is hijacking things
ScrollTrigger.scrollerProxy("#main", {
  scrollTop(value) {
    return arguments.length ? locoScroll.scrollTo(value, 0, 0) : locoScroll.scroll.instance.scroll.y;
  }, // we don't have to define a scrollLeft because we're only scrolling vertically.
  getBoundingClientRect() {
    return {top: 0, left: 0, width: window.innerWidth, height: window.innerHeight};
  },
  // LocomotiveScroll handles things completely differently on mobile devices - it doesn't even transform the container at all! So to get the correct behavior and avoid jitters, we should pin things with position: fixed on mobile. We sense it by checking to see if there's a transform applied to the container (the LocomotiveScroll-controlled element).
  pinType: document.querySelector("#main").style.transform ? "transform" : "fixed"
});



// each time the window updates, we should refresh ScrollTrigger and then update LocomotiveScroll. 
ScrollTrigger.addEventListener("refresh", () => locoScroll.update());

// after everything is set up, refresh() ScrollTrigger and update LocomotiveScroll because padding may have been added for pinning, etc.
ScrollTrigger.refresh();

}

loco()


var word = "";

document.querySelector(".page2>h2").textContent.split(' ').forEach(function (dets)
{
    word += `<span> ${dets} </span>`;
    document.querySelector(".page2>h2").innerHTML = word;
})

gsap.to(".page2>h2>span", {
    scrollTrigger: {
        trigger: `.page2>h2>span`,
        start: `top bottom`,
        end: `bottom top`,
        scroller: `#main`,
        scrub: .5,
        markers: false
    },
    stagger: .2,
    color: `#fff`
})


function rotate() {
         var lastChild = $(".slider div:last-child").clone()

          $(".slider div").removeClass(".firstSlide");

          $(".slider div:last-child").remove();

          $(".slider").prepend(lastChild);
          
          $(lastChild).addClass("firstChild");
}

window.setInterval(function() {
       rotate()
}, 5000);

const h3Element = document.getElementById('slider-detail');

const texts = ["Soccer conducted in Noida",
    "Yoga Fest conducted at Banaras",
    "Soccer tournament in NYC",
    "Batminton tounament in Yale",
    "Athletics in Beijing",
    "Batminton tournament in Prince State",
    "Volley ball tournament in Jabalpur"];
let currentIndex = 4;

function updateH3Content() {
    h3Element.textContent = texts[currentIndex];
    currentIndex = (currentIndex + 1) % texts.length;
}

setInterval(updateH3Content, 5000);



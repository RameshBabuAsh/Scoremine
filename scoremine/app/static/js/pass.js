

function passShowHideLog() {
    let x = document.getElementById("log-pass")
    let y = document.getElementById("log-pass-slash")
    let z = document.getElementById("log-pass-input")
    if (z.type === "password") {
        z.type = "text"
        x.style.display = "block"
        y.style.display ="none"
    }
    else {
        z.type = "password"
        x.style.display = "none"
        y.style.display ="block"
    }
}

function passShowHideReg1() {
    let x = document.getElementById("reg-pass-1")
    let y = document.getElementById("reg-pass-slash-1")
    let z = document.getElementById("reg-pass-input-1")
    if (z.type === "password") {
        z.type = "text"
        x.style.display = "block"
        y.style.display ="none"
    }
    else {
        z.type = "password"
        x.style.display = "none"
        y.style.display ="block"
    }
}

function passShowHideReg2() {
    let x = document.getElementById("reg-pass-2")
    let y = document.getElementById("reg-pass-slash-2")
    let z = document.getElementById("reg-pass-input-2")
    if (z.type === "password") {
        z.type = "text"
        x.style.display = "block"
        y.style.display ="none"
    }
    else {
        z.type = "password"
        x.style.display = "none"
        y.style.display ="block"
    }
}
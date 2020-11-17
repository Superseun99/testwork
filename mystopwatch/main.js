
    var interval;
    var seconds = 00;
    var tens = 00;
    var minutes = 00;
    var start = document.getElementById("button-start");
    var stop = document.getElementById("button-stop");
    var reset = document.getElementById("button-reset");
    var showMinutes = document.getElementById("minutes");
    var showSeconds = document.getElementById("seconds");
    var showTens = document.getElementById("tens");
    var colonImp = document.getElementById("colon");

    start.onclick = function () {
        clearInterval(interval);
        interval = setInterval(startTimer, 10);
        stop.style.display = "inline-block";
        reset.style.display = "inline-block";
        start.style.display = "none";
    }

    stop.onclick = function () {
        clearInterval(interval);
        start.style.display = "inline-block";
        stop.style.display = "none";
    }

    reset.onclick = function () {
        clearInterval(interval);
        seconds = 00;
        tens = 00;
        minutes = 0;
        showMinutes.innerHTML = "0" + minutes;
        showSeconds.innerHTML = "0" + seconds;
        showTens.innerHTML = "0" + tens;
        start.style.display = "inline-block";
        stop.style.display = "none";
        reset.style.display = "none";
    }

    function startTimer() {
        tens++;
        if (tens <= 9) {
            showTens.innerHTML = "0" + tens;
        }
        if (tens > 9) {
            showTens.innerHTML = tens;
        }
        if (tens > 99) {
            seconds++;
            tens = 0;
            showTens.innerHTML = "0" + 0;
            showSeconds.innerHTML = seconds;
        }
        if (seconds <= 9) {
            showSeconds.innerHTML = "0" + seconds;
        }
        if (seconds > 9) {
            showSeconds.innerHTML = seconds;
        }
        if (seconds % 60 == 0 && seconds > 0) {
            seconds = 00;
            showSeconds.innerHTML = seconds;
            minutes++;
            colonImp.style.display = "inline-block";
            showMinutes.style.display = "inline-block";
            showMinutes.innerHTML = " " + minutes;
        }

    }

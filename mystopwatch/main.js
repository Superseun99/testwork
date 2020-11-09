test=0;
a=0;
function aut(){
    if(test<1){
        a=setInterval(function() {
            add();
        },10);
        test++;
    }
}
ms = 0;
s = 0;
min =0;
function add() {
    ++ms;
    if (ms>=100) {ms-=100; ++s;}
    if (ms<10) ms = "0"+ms;
    if (s<10&&ms==0||s==0&&ms==1) s = "0"+s;
    if (s>=60) {s-=60;s=String(s).slice(0,1);  ++min}
    if (min<10&&s<1&&ms==1) min = "0"+min;
    $(".end").text(min+" : "+s+" : "+ms);
}
function stop_aut() {
    clearInterval(a);
    test=0;
}
function reset(){
    clearInterval(a);
    ms=0;
    s=0; 
    min=0;
    $(".end").text("0"+min+" : 0"+s+" : 0"+ms);
    test=0;
    $("#lapEnd").children().remove();
}
function lap(){
    lapVal=min+":"+s+":"+ms;
    $("#lapEnd").append($("<li></li>").text(lapVal));
}
// paste all the code into the browser console
// alter the numbers below to the time you wish to leave
// right now it is set to 20:28:00
// hit enter

var leaveHour = 20;
var leaveMinute = 28;

var leaveSecond = 0;

var now = new Date();

var leaveTime = new Date();
leaveTime.setHours(leaveHour);
leaveTime.setMinutes(leaveMinute);
leaveTime.setSeconds(leaveSecond);

var deltaT = (leaveTime.getTime() - now.getTime())/1000;
console.log('leaving in ' + deltaT + ' seconds (' + (deltaT/60) + ') Minutes');

function timeout() {
    // avoid "do you really want to leave" popup
    document.getElementsByTagName('html')[0].innerHTML = '';
    location.href = 'https://google.com';
}
window.setTimeout(timeout, deltaT*1000);

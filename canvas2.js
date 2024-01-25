var canvas = document.querySelector('canvas');


canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var c = canvas.getContext('2d');


// var x = Math.random() * innerWidth;
// var y = Math.random() * innerHeight;
// var dx = 4;
// var dy = 4;
// var radius = 30;

var x = 100;

function animate() {
    requestAnimationFrame(animate);
    c.clearRect(0, 0, innerWidth, innerHeight);
    c.beginPath();
    c.arc(x, 200, 30, 0, Math.PI * 2, false);
    c.strokeStyle = 'blue';
    c.stroke();

    x += 1;

    // if (x + radius > innerWidth || x - radius < 0) {
    //     dx = -dx;
    // }

    // if (y + radius > innerHeight || y - radius < 0){
    //     dy = -dy;
    // }
}

animate();
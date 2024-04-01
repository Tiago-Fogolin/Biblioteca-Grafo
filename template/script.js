var circle;
var isDragging = false;
var previousX, previousY;

function moveCircle(dx, dy) {
    var cx = parseFloat(circle.getAttribute('cx'));
    var cy = parseFloat(circle.getAttribute('cy'));
    circle.setAttribute('cx', cx + dx);
    circle.setAttribute('cy', cy + dy);
}

function onMouseMove(event) {
    if (isDragging) {
        var mouseX = event.clientX;
        var mouseY = event.clientY;
        var dx = mouseX - previousX;
        var dy = mouseY - previousY;
        moveCircle(dx, dy);
        previousX = mouseX;
        previousY = mouseY;
    }
}

function onMouseDown(event) {
    if (event.target instanceof SVGCircleElement) {
        isDragging = true;
        previousX = event.clientX;
        previousY = event.clientY;
        circle = event.target;
    }
}

function onMouseUp() {
    isDragging = false;
}

document.addEventListener('mousemove', onMouseMove);
document.addEventListener('mousedown', onMouseDown);
document.addEventListener('mouseup', onMouseUp);
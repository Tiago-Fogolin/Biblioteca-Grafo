var canvas = document.getElementById('lineCanvas');
var ctx = canvas.getContext('2d');

nodes = ESCAPE_NODES

connections = ESCAPE_CONNECTIONS

positions = {}

container = document.getElementById('container')

for(let i = 0; i < nodes.length; i++){
    let div = document.createElement('div')
    let label = document.createElement('label')
    label.innerText = nodes[i]
    div.classList.add('box')

    positionX = Math.floor(Math.random() * 250)
    positionY = Math.floor(Math.random() * 250)

    div.style.left = positionX + 'px'
    div.style.top = positionY + 'px'


    container.appendChild(div)
    

    rect = div.getBoundingClientRect()

    centerX = rect.left + rect.width / 2
    centerY = rect.top + rect.height / 2
    
    label.style.position = 'absolute'
    label.style.top = rect.bottom - 10 + 'px'
    label.style.left = rect.left + 'px'
    container.appendChild(label)

    node_label = nodes[i]
    positions[node_label] = [centerX, centerY]
}

canvas.width = document.getElementById('container').offsetWidth;
canvas.height = document.getElementById('container').offsetHeight;


for (let i = 0 ; i < connections.length; i++){
    ctx.beginPath();

    from_node = connections[i].from;
    to_node = connections[i].to;

    ctx.moveTo(positions[from_node][0], positions[from_node][1]);
    ctx.lineTo(positions[to_node][0], positions[to_node][1]);
    ctx.strokeStyle = '#000';
    ctx.stroke();   

    var arrowSize = 10;
    var endY = positions[to_node][1];
    var startY = positions[from_node][1];
    var endX = positions[to_node][0];
    var startX = positions[from_node][0]

    var angle = Math.atan2(endY - startY, endX - startX);
    ctx.beginPath();
    ctx.moveTo(endX, endY);
    ctx.lineTo(endX - arrowSize * Math.cos(angle - Math.PI / 6), endY - arrowSize * Math.sin(angle - Math.PI / 6));
    ctx.lineTo(endX - arrowSize * Math.cos(angle + Math.PI / 6), endY - arrowSize * Math.sin(angle + Math.PI / 6));
    ctx.closePath();
    ctx.fill();
}


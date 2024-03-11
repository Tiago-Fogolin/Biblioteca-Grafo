var canvas = document.getElementById('lineCanvas');
var ctx = canvas.getContext('2d');

nos = ['teste', 'teste2', 'teste3', 'teste4']

centers = []

container = document.getElementById('container')

for(let i = 0; i < nos.length; i++){
    let div = document.createElement('div')
    let label = document.createElement('label')
    label.innerText = nos[i]
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
    label.style.top = rect.bottom
    label.style.left = rect.left
    container.appendChild(label)
    centers.push([centerX, centerY])
}

canvas.width = document.getElementById('container').offsetWidth;
canvas.height = document.getElementById('container').offsetHeight;


for (let i = 0 ; i < nos.length; i+= 2){
    ctx.beginPath();
    ctx.moveTo(centers[i][0], centers[i][1]);
    ctx.lineTo(centers[i+1][0], centers[i+1][1]);
    ctx.strokeStyle = '#000';
    ctx.stroke();   
}


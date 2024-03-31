class NodeConnections{

    constructor(node_labels, connections, container){
        this.nodes = node_labels
        this.connections = connections
        this.container = container
        this.centerPositions = []
    }

    createRandomX(){
        return Math.floor(Math.random() * (window.innerWidth - 150))
    }

    createRandomY(){
        return Math.floor(Math.random() * (window.innerHeight - 150))
    }

    createNodeLabel(node_label, node_rect){
        let label = document.createElement('label')
        label.innerText = node_label


        label.classList.add('label');
        label.style.top = node_rect.bottom - 10 + 'px'
        label.style.left = node_rect.left + 'px'

        return label
    }

    createNode(){
        let node = document.createElement('div')
        node.classList.add('node')
        
        let positionX = this.createRandomX()
        let positionY = this.createRandomY()

        node.style.left = positionX + 'px'
        node.style.top = positionY + 'px'

        return node
    }

    getNodeCenters(node_rect){
        let containerRect = this.container.getBoundingClientRect()
        let centerX = node_rect.left - containerRect.left + node_rect.width / 2
        let centerY = node_rect.top - containerRect.top + node_rect.height / 2

        return [centerX, centerY]
    }

    drawNodes(){
        for(let i = 0; i < this.nodes.length; i++){
            let node = this.createNode()

            this.container.appendChild(node)

            let nodeRect = node.getBoundingClientRect()

            let label = this.createNodeLabel(this.nodes[i], nodeRect)
                    
            this.container.appendChild(label)
        
            this.centerPositions[this.nodes[i]] = this.getNodeCenters(nodeRect)
        }
    }

    getXPosition(node){
        return this.centerPositions[node][0]
    }

    getYPosition(node){
        return this.centerPositions[node][1]
    }

    drawLine(ctx, startX, endX, startY, endY){
        ctx.beginPath();
        ctx.moveTo(startX, startY);
        ctx.lineTo(endX, endY);
        ctx.strokeStyle = '#000';
        ctx.stroke();
    }

    drawArrow(ctx, startX, endX, startY, endY){
        this.drawLine(ctx, startX, endX, startY, endY)
        let arrowSize = 10
        let angle = Math.atan2(endY - startY, endX - startX)
        let midX = ((startX + endX) / 2)
        let midY = ((startY + endY) / 2)
        ctx.beginPath()
        ctx.moveTo(midX, midY)
        ctx.lineTo(midX - arrowSize * Math.cos(angle - Math.PI / 6), midY - arrowSize * Math.sin(angle - Math.PI / 6))
        ctx.lineTo(midX - arrowSize * Math.cos(angle + Math.PI / 6), midY - arrowSize * Math.sin(angle + Math.PI / 6))
        ctx.closePath()
        ctx.fill()
    }

    drawConnections(ctx){
        for (let i = 0 ; i < this.connections.length; i++){
            
    
            let from_node = this.connections[i].from
            let to_node = this.connections[i].to
        
            var startX = this.getXPosition(from_node)
            var endX = this.getXPosition(to_node)
            var startY = this.getYPosition(from_node)
            var endY = this.getYPosition(to_node)

            this.drawLine(ctx, startX, endX, startY, endY)
            this.drawArrow(ctx, startX, endX, startY, endY)
        }
    }
}

var canvas = document.getElementById('lineCanvas');
var ctx = canvas.getContext('2d');

nodes = ESCAPE_NODES

connections = ESCAPE_CONNECTIONS

positions = {}

container = document.getElementById('container')

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let node_connections = new NodeConnections(nodes, connections, container)

node_connections.drawNodes()
node_connections.drawConnections(ctx)
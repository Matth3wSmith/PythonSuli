function onload(){
    const c =document.getElementById("muszer")
    const ctx = c.getContext("2d");
    c.width=1000
    c.height=600
    sebessegMero(ctx)

}
function sebessegMero(ctx){
    ctx.beginPath()
    ctx.arc(400,200,100,0,2*Math.PI/20)
    ctx.rotate(90*(Math.PI/180))
    ctx.lineTo(100,100)


    ctx.stroke()
    ctx.closePath()

}

function korRajz(x,y,r){
    ctx.beginPath()
    ctx.arc(x,y,r,0,2*Math.PI)
    ctx.stroke()
    ctx.closePath()

}
let szog = 1;
let ctx;
function szogvaltoztatas(e){
    if (e.wheelDeltaY<0){
        szog-=5
    }
    else{
        szog+=5;
    }
    ctx.clearRect(0,0,1000,700)

	sebessegMero(ctx,szog);
}

function onload(){

	const c = document.getElementById("muszer");
	ctx = c.getContext("2d");
	c.width=1000;
	c.height=700;
    c.addEventListener("wheel",szogvaltoztatas);

	sebessegMero(ctx,szog);
}

function sebessegMero(ctx,szog){
	let x = 200;
	let y = 200;
	let r = 100;
	let kezdoSzog=20*(Math.PI/180);

	//Körvonal
	ctx.beginPath();
	ctx.arc(x+r,y,r,0,Math.PI*2);
	ctx.stroke();
	ctx.closePath();

	//r=√((x−u)**2+(y−v)**2)
    let a;
    let b;
    console.log(szog)
    if (szog<-90 || szog > 90){
        if (szog > 360 || szog<-360){
            szog=360-szog
        }
        szog = szog * (Math.PI/180);
        b = y - Math.sin(szog)*r;
        a = x + Math.sqrt(r**2-(y-b)**2);
    }
    else{
        szog = szog * (Math.PI/180);
        b = y - Math.sin(szog)*r;
        a = x - Math.sqrt(r**2-(y-b)**2);
    }

    /*if (szog > 90 && szog <= 180){

        szog = szog * (Math.PI/180);
        b = y - Math.sin(szog)*r;
        a = x + Math.sqrt(r**2-(y-b)**2);
    }
    else if (szog>180 && szog<=270) {
        szog = szog * (Math.PI/180);
        b = y + Math.sin(szog)*r;
        a = x + Math.sqrt(r**2-(y-b)**2);
    }*/

/*
	ctx.beginPath()
	ctx.fillStyle="black"
	ctx.arc(x+r,y,1,0,Math.PI*2)
	ctx.stroke()*/
	
	ctx.moveTo(x+r,y);
	ctx.lineTo(a+r,b);
	ctx.stroke();


	

}
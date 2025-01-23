let szog = 0;
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
    //c.addEventListener("wheel",szogvaltoztatas);

	sebessegMero(ctx);
}

function sebessegMero(ctx){
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
    
    let a2;
    let b2;

    let sebesseg = 0;
    for (let i = 11; i >= -2; i--){
        let szog = i*20
        console.log(szog)
        if (szog<-90 || (szog > 90)){
            if (szog > 360 || szog<-360){
                szog=360-szog
            }
            szog = szog * (Math.PI/180);
            b = y - Math.sin(szog)*r;
            a = x + Math.sqrt(r**2-(y-b)**2);
            
            b2 = b + Math.sin(szog)*(1/6*r);
            a2 = a - Math.sqrt((1/6*r)**2-(b2-b)**2);
        }
        else{
            szog = szog * (Math.PI/180);
            b = y - Math.sin(szog)*r;
            a = x - Math.sqrt(r**2-(y-b)**2);
            
            b2 = b + Math.sin(szog)*(1/6*r);
            a2 = a + Math.sqrt((1/6*r)**2-(b2-b)**2);
        }
        ctx.beginPath();
        ctx.moveTo(a2+r,b2);
        ctx.lineTo(a+r,b);
        ctx.stroke();
        ctx.closePath();

        //
        ctx.beginPath();
        ctx.moveTo(x+r,y);
        ctx.lineTo(a+r,b);
        ctx.stroke();
        ctx.closePath();
    }/*
    for (let i = 11; i >= -2; i--){
        let szog = i*20
        console.log(szog)
        if (szog<-90 || (szog > 90)){
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
        ctx.beginPath();
        ctx.moveTo(x+r,y);
        ctx.lineTo(a+r,b);
        ctx.stroke();
        ctx.closePath();
    }*/


	

}
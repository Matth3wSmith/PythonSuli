let szog = 0;
let ctx;
function szogvaltoztatas(e){
    if (e.wheelDeltaY<0){
        szog-=5
    }
    else{
        szog+=5;
    }
    torles(ctx)
	sebessegMero(ctx);
}

function torles(ctx){
    ctx.clearRect(0,0,1000,700)
}

function onload(){

	const c = document.getElementById("muszer");
	ctx = c.getContext("2d");
	c.width=1000;
	c.height=700;
    //c.addEventListener("wheel",szogvaltoztatas);

	sebessegMero(ctx);
}
let sebesseg = 0
function sebessegNov(){
    sebesseg+=20
    if (sebesseg<=260){
        torles(ctx)
        sebessegMero(ctx,sebesseg,20)
    }
}
function sebessegMero(ctx,sebesseg=0,noveles=0){
    //Sebességmérő óra x,y koordinátája és sugrának beállítása
	let x = 200;
	let y = 200;
	let r = 100;

	//Körvonal
	ctx.beginPath();
	ctx.arc(x+r,y,r,0,Math.PI*2);
	ctx.stroke();
	ctx.closePath();

    //Beosztás körvonalon lévő pontjának koordinátája
    let a;
    let b;
    //Beosztás körben lévő pontjának koordinátája
    let a2;
    let b2;

    //A Sebességmérő óra beosztásai, -2-től rajzolj (-40 fok) 11-ig (220 fok)
    for (let i = -2; i <= 11; i++){
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

    }
    
    //Sebességmérő óra mutató
    /*let sebessegSzog = sebesseg-40;

    if (sebessegSzog<-90 || (sebessegSzog > 90)){
        if (sebessegSzog > 360 || sebessegSzog<-360){
            sebessegSzog=360-sebessegSzog
        }
        sebessegSzog = sebessegSzog * (Math.PI/180);
        b = y - Math.sin(sebessegSzog)*r;
        a = x + Math.sqrt(r**2-(y-b)**2);
    }
    else{
        sebessegSzog = sebessegSzog * (Math.PI/180);
        b = y - Math.sin(sebessegSzog)*r;
        a = x - Math.sqrt(r**2-(y-b)**2);
        
    }
    ctx.beginPath();
    ctx.lineWidth = 10;
    ctx.moveTo(x+r,y);
    ctx.lineTo(a+r,b);
    ctx.stroke();
    ctx.lineWidth = 1;
    ctx.closePath();*/


    
    let i =0;
    setInterval(function() {
        let szog = i+sebesseg-noveles-40;
        console.log(szog);
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
            
        
        ctx.beginPath();
        ctx.moveTo(x+r,y);
        ctx.lineTo(a+r,b);
        ctx.stroke();
        ctx.closePath();
        i++;
        torles(ctx)
    }
    },1000)
        

	

}
var nrow = 8;
var ncell = 8;
var tt = new Array(nrow);
var babuk = ["V", "B", "b", "bb"]

var newrow;

var kiJon=0;//0: világos, 1:sötét
var pontok=[0,0];
var figuraErtek={G:1,F:2,H:2,K:2,B:3,V:5};
figuraErtek={o:1,v:2,m:2,l:2,t:3,w:5};

function init()
{
	for(var i=0;i<nrow;i++){
		tt[i] = new Array(ncell);
		newrow=document.getElementById("palya").insertRow(i);
		for(var j=0;j<ncell;j++){
			tt[i][j]=newrow.insertCell(j);
			tt[i][j].id=i*ncell+j;
			tt[i][j].onclick=function(){cellClicked(this);};
			tt[i][j].style.width="50px";
			tt[i][j].style.height="50px";
			tt[i][j].style.color="white";
			tt[i][j].style.background="red";
			tt[i][j].innerHTML="";
		}
	}
}    

function cellClicked(obj)
		{
			var row = parseInt(obj.id/ncell);
			var column = obj.id%ncell;
			console.log("row",row,"column",column)
				//üres
				let i = 1;
				if(tt[row][column].innerHTML=="" && i < 3)
				{
					tt[row][column].innerHTML=babuk[i];
					i+=1
					console.log("row",row,"column",column)
				}
				/*tt[row][column].innerHTML=tt[babu[0]][babu[1]].innerHTML;
				tt[row][column].dataset.szin=tt[babu[0]][babu[1]].dataset.szin;
				tt[row][column].dataset.irany=tt[babu[0]][babu[1]].dataset.irany;
				tt[row][column].style.color=tt[babu[0]][babu[1]].style.color;
				tt[row][column].style.textShadow=tt[babu[0]][babu[1]].style.textShadow;

				tt[babu[0]][babu[1]].innerHTML="";
				tt[babu[0]][babu[1]].dataset.szin="";
				tt[babu[0]][babu[1]].dataset.irany="";
				tt[babu[0]][babu[1]].style.color="";
				//tt[babu[0]][babu[1]].style.textShadow="";

				//ha gyalog beér, akkor megfordul
				if(tt[row][column].innerHTML=="o" 
					&& (row==0 || row==nrow-1))
				{
					tt[row][column].dataset.irany*=-1;s
				}
				//ha gyalog, akkor merre is megy
				if(tt[row][column].innerHTML=="o")
				{
					if(tt[row][column].dataset.irany==1) {tt[row][column].style.textDecoration="underline";}
					if(tt[row][column].dataset.irany==-1) {tt[row][column].style.textDecoration="overline";}
				}
				else
				{
					tt[row][column].style.textDecoration="";
				}*/
			
		}
	
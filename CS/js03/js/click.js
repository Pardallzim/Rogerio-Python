var contador = 0;
var bt = document.getElementById('btCont');
var btL = document.getElementById('btLimpa');
var btZ = document.getElementById('btZero');
bt.onclick=()=>{
    contador++;
    var el = document.getElementById('cont');
    el.innerHTML = contador;
}
btL.onclick=()=>{
    contador--;
    var el = document.getElementById('cont');
    el.innerHTML = contador;
}
btZ.onclick=()=>{
    contador = 0;
    var el = document.getElementById('cont');
    el.innerHTML = contador;
}
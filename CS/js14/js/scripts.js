var num1 = document.getElementById('num1').value;
var num2 = document.getElementById('num2').value;

function somar(){
    var num1 = document.getElementById('num1').value;
    var num2 = document.getElementById('num2').value;
    if(isNaN(num1) || num1 == ""){
        alert("Valor inválido para o número 1"); 
    }else if(isNaN(num2) || num2 == ""){
        alert("Valor inválido para o número 2");
    }else{
        var somar = parseInt(num1) + parseInt(num2);
        document.getElementById('resultado').innerHTML = somar;   
    }
}
function subtrair(){
    var num1 = document.getElementById('num1').value;
    var num2 = document.getElementById('num2').value;
    if(isNaN(num1) || num1 == ""){
        alert("Valor inválido para o número 1"); 
    }else if(isNaN(num2) || num2 == ""){
        alert("Valor inválido para o número 2");
    }else{
        var subtrair = parseInt(num1) - parseInt(num2);
        document.getElementById('resultado').innerHTML = subtrair;
    }
}
function multiplicar(){
    var num1 = document.getElementById('num1').value;
    var num2 = document.getElementById('num2').value;
    if(isNaN(num1) || num1 == ""){
        alert("Valor inválido para o número 1"); 
    }else if(isNaN(num2) || num2 == ""){
        alert("Valor inválido para o número 2");
    }else{
        var multiplicar = parseInt(num1) * parseInt(num2);
        document.getElementById('resultado').innerHTML = multiplicar;
    }
}
function dividir(){
    var num1 = document.getElementById('num1').value;
    var num2 = document.getElementById('num2').value;
    if(isNaN(num1) || num1 == ""){
        alert("Valor inválido para o número 1"); 
    }else if(isNaN(num2) || num2 == ""){
        alert("Valor inválido para o número 2");
    }else{
        var dividir = parseInt(num1) / parseInt(num2);
        document.getElementById('resultado').innerHTML = dividir;
    }
}
function limpar(){
    var limpar = null;
    document.getElementById('resultado').innerHTML = limpar;
}

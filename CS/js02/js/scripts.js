// função 
liga_desliga = true
function mostrarParagrafo(){
    if (liga_desliga == true){
        document.getElementById('p1').style.visibility = 'visible';
        liga_desliga = false
    }else{
        document.getElementById('p1').style.visibility = 'hidden';
        liga_desliga = true
    }
}
function alteraConteudo(){
    document.getElementsByTagName("p")[2].innerHTML = "Texto modificado por JS!";
}
liga_desliga_Name = true
function alteraBotao(){
    var x = document.getElementsByName('btRed');
    if (liga_desliga_Name == true){
        alert('Existe(m)' + x.length + 'elemento(s) <btRed> nesta pagina.');
        document.getElementsByName('btRed')[0].style.backgroundColor = 'red';
        liga_desliga_Name = false
    }else{
        document.getElementsByName('btRed')[0].style.backgroundColor = '#47817f';
        liga_desliga_Name = true
    }
}
liga_desliga_Class = true
function alteraCor(){
    var y = document.getElementsByClassName('divAlterada');
    var i; 
    if (liga_desliga_Class == true){
        for(i = 0; i < y.length; i++){
            y[i].style.backgroundColor = '#837744';
        };
        liga_desliga_Class = false
    }else{
        for(i = 0; i < y.length; i++){
            y[i].style.backgroundColor = '#47817f';
        };
        liga_desliga_Class = true
    }
}
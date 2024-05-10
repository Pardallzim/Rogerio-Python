// 01 - fução insere item no final
function insereItemFinal(){
    // cria novo objeto item a ser inserido
    var novo = document.createElement('li');
    // cria objeto com itens da lista
    var els = document.getElementsByTagName('ul');
    // cria novo item após o elemento[0]
    els[0].appendChild(novo);
    // insere conteúdo no novo elemento
    novo.innerHTML = "Binômio de Newton";
}
// 02 - função insere item antes de...
function insereItemBefore(){
    // cria  novo objeto - item a ser incluído
    var item = document.createElement('li');
    // insere conteúdo na Item
    item.innerHTML = "Binômio de Newton";
    // cria objeto com itens da lista
    var lista = document.getElementById('mat');
    // insere o item antes da posição definida
    lista.insertBefore(item, lista.childNodes[2]);
}
// 03 - subistitui item especificado
function substituiItem(){
    // cria objeto com os itens da lista
    var els = document.getElementsByTagName('li');
    // define o número de itens
    var tamanho = els.length -1;
    // define a posição para a substituição
    var pos = prompt('Informe a posição do item a ser substituido [0 a ' + tamanho + ']');
    // substitui o conteúdo do elemento escolhido
    els[pos].innerHTML = prompt('Informe a matéria:')
}
// 04 - exclui item específicado
function excluiItem(){
    // cria objeto com a lista de Matemática
    var lista = document.getElementById('mat');
    // cria objeto com itens da lista
    var els = document.getElementsByTagName('li');
    // remove o primeiro elemento da lista
    lista.removeChild(els[0]);
}
// 05 - exclui item na lista de Português
function excluiPortugues(){
    // cria objeto com a lista de Matemática
    var listap = document.getElementById('port');
    // cria objeto com itens da lista
    var elsp = listap.getElementsByTagName('li');
    // remove o primeiro elemento da lista
    listap.removeChild(elsp[0]);
}
// 06 - exclui item na lista de Geografia
function excluiGeografia(){
    // cria objeto com a lista de Matemática
    var listag = document.getElementById('geo');
    // cria objeto com itens da lista
    var elsg = listag.getElementsByTagName('li');
    // remove o primeiro elemento da lista
    listag.removeChild(elsg[0]);
}
// 07 - insere imagem da pagina
function insereImagem(){
    var img = document.createElement('img');
    img.src = './img/rio.jpg';
    item = document.createElement('h3');
    item.innerHTML = 'Foto tirada por Florencia Potter';
    teste = document.getElementById('imagem');
    imagem.appendChild(img, item);
    teste.appendChild(item);
}
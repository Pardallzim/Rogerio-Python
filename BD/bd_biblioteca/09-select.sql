/*
9 - Listar todos os Livros em que seu títulosomente tenham as vogais ‘a’ e ‘i’
*/
SELECT l.idlivros, l.titulo, l.isbn
	FROM livros as l
WHERE l.titulo NOT LIKE '%E%' 
  AND l.titulo NOT LIKE '%O%'
  AND l.titulo NOT LIKE '%U%';
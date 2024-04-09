/*
08 - Listar todos os Livros dos Autores quecontenham a letra 
‘u’ em seu nome

SELECT l.idlivros, l.titulo, l.isbn,
	   a.idautores, a.nome
	FROM livros AS l
INNER JOIN autores AS a
	ON l.autores_idautores = a.idautores
		AND a.nome LIKE '%u%';
*/
SELECT l.idlivros, l.titulo, l.isbn,
	   a.idautores, a.nome
	FROM livros AS l, autores AS a
WHERE l.autores_idautores = a.idautores 
	AND a.nome LIKE '%u%';        
/*
13 - Listar todos os Livros que em seu ISBNcontenham os números ‘123’ nesta sequência
*/
SELECT l.idlivros, l.titulo, l.isbn
	FROM livros AS l
WHERE l.isbn LIKE '%123%';
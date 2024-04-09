/*
19 - Listar os autores que não tiveram livrosemprestados
*/
SELECT l.idlivros, l.titulo, l.isbn,
       e.idemprestimos, e.livros_idlivros,
       a.nome
	FROM livros AS l
INNER JOIN autores AS a
	ON l.autores_idautores = a.idautores
LEFT JOIN emprestimos AS e
	ON l.idlivros = e.livros_idlivros
WHERE e.idemprestimos IS NULL;
    
/*
(l) livros -> autores e empréstimos (d)
INNER: deve existir nas duas tabelas
LEFT : deve existir na tabela à "esquerda"
RIGHT: deve existir na tabela à "direita"
FULL
OUTER
*/
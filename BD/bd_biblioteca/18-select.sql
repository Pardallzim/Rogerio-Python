/*
18 - Listar os livros que não foram emprestados
*/
SELECT l.idlivros, l.titulo, l.isbn,
       e.idemprestimos, e.livros_idlivros
	FROM livros AS l
LEFT JOIN emprestimos AS e
	ON l.idlivros = e.livros_idlivros
WHERE e.idemprestimos IS NULL;
    
/*
(l) livros -> empréstimos (d)
INNER: deve existir nas duas tabelas
LEFT : deve existir na tabela à "esquerda"
RIGHT: deve existir na tabela à "direita"
FULL
OUTER
*/
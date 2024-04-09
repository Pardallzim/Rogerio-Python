/*
16 - Listar quantos livros foram emprestados porautor
*/

SELECT a.idautores, a.nome, count(e.idemprestimos) as qtde
   FROM livros AS l 
INNER JOIN autores AS a
	ON l.autores_idautores = a.idautores
INNER JOIN emprestimos AS e
   ON l.idlivros = e.livros_idlivros  
GROUP BY a.idautores
ORDER BY a.nome;
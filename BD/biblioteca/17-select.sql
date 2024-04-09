/*
17 - Listar quantos livros foram emprestados porusuário
*/
SELECT u.idusuarios, u.nome, 
    COUNT(e.idemprestimos) AS qtde,	
    COUNT(e.idemprestimos) * 12 AS valor
	FROM usuarios AS u
INNER JOIN emprestimos AS e
	ON u.idusuarios = e.usuarios_idusuarios
GROUP BY u.nome;
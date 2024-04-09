/*
20 - Listar o usuário com o maior número deempréstimo
*/
SELECT u.idusuarios, u.nome, 
	COUNT(e.idemprestimos) AS emprestimos
	FROM usuarios AS u, emprestimos AS e
WHERE u.idusuarios = e.usuarios_idusuarios
	GROUP BY u.nome
    ORDER BY emprestimos DESC LIMIT 1;
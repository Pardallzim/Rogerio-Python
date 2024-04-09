/*
12 - Listar a quantidade de usuários por cidadeem ordem alfabética decrescente 
*/
SELECT u.cidade, COUNT(u.idusuarios) AS Quantidade
	FROM usuarios AS u
    GROUP BY u.cidade
    ORDER BY u.cidade;
    
/*
10 - Listar todos os usuários da cidade deDescoberto
*/
SELECT u.idusuarios, u.nome, u.endereco, 
       u.cidade, u.cep, u.fone
	FROM usuarios as u
WHERE u.cidade = "Descoberto";

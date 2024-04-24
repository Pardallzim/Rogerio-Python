DELIMITER $$
CREATE PROCEDURE `InsertMecanicos`(nomeInsert VARCHAR(45), cpfInsert VARCHAR(11), telefoneInsert VARCHAR(11), cidadeInsert VARCHAR(45), ufInsert VARCHAR(2), enderecoInsert VARCHAR(45), bairroInsert VARCHAR(45), cepInsert VARCHAR(9))
BEGIN
INSERT INTO `mecanicos`(`nome`,`cpf`,`telefone`,`cidade`,`uf`,`endereco`,`bairro`,`cep`)
VALUE(nomeInsert, cpfInsert, telefoneInsert, cidadeInsert, ufInsert, enderecoInsert, bairroInsert, cepInsert);
END $$
DELIMITER ;


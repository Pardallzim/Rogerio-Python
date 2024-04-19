/* Criação de Store Procedure para inclusão de Dados */

DELIMITER $
CREATE PROCEDURE `InserirVenda`(`venda` INT,`prod` VARCHAR(3),`qtde` INT)
BEGIN 
	INSERT INTO `ItensVendas`(`Venda`,`Produto`, `Quantidade`)
    VALUES (`venda`,`prod`,`qtde`);
END
$
DELIMITER ;
ALTER TABLE `Aluno`
	ADD UNIQUE INDEX `fx_nome_decrescente`(`nome` DESC, `idAluno` DESC);
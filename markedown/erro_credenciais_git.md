# Resolver Problema de Credenciais no GitHub

Às vezes, ao trabalhar com repositórios do GitHub via HTTPS no Windows, pode ser necessário limpar ou atualizar as credenciais armazenadas. Abaixo estão os passos para fazer isso utilizando comandos do CMD.

## Verificar Credenciais Armazenadas

Para verificar as credenciais armazenadas para conexões HTTPS do GitHub, execute o seguinte comando no prompt de comando (CMD):

```bash
cmdkey /list

## Excluir Credenciais

Se você identificar uma entrada que precisa ser removida (por exemplo, uma entrada legada ou incorreta), utilize o comando cmdkey com a opção /delete. Substitua LegacyGeneric:target=git:https://github.com pelo nome da entrada que deseja excluir:

```bash
cmdkey /delete:LegacyGeneric:target=git:https://github.com



---
nav_title: Diferença entre lista de bloqueio e exclusão
article_title: Diferença entre lista de bloqueio e exclusão
page_order: 2

page_type: solution
description: "Este artigo de ajuda explica a diferença entre colocar dados personalizados na lista de bloqueio e excluí-los."
---

# Diferença entre lista de bloqueio e exclusão {#difference-between-blocklisting-and-deleting}

Para entender a diferença entre colocar na lista de bloqueio e excluir dados personalizados na Braze, veja os resultados de cada ação:

- **Lista de bloqueio:** Se atributos personalizados, eventos ou compras forem colocados na lista de bloqueio, eles permanecerão nos perfis de usuário, mas a Braze não processará mais novos dados para esses objetos.
- **Exclusão:** Se atributos personalizados, eventos ou compras forem excluídos, a Braze removerá esses dados dos perfis de usuário. Atributos personalizados e eventos excluídos são movidos para `Trashed` por sete dias, período em que você pode restaurá-los. Após sete dias, a Braze os exclui permanentemente. A exclusão também não impede a entrada de novos dados, então certifique-se de que os dados não estão mais sendo enviados pelo SDK, API ou importações de CSV antes de excluí-los.

## O que devo fazer? {#which-should-i-do}

Para realizar a lista de bloqueio, a Braze terá que enviar as informações de bloqueio para o dispositivo de cada usuário, e essa será uma operação com uso intensivo de dados, o que idealmente tentamos evitar. Além disso, se a lista for muito grande (> 100 atributos, eventos ou compras), seu app pode começar a ficar lento.

Se você não planeja mais enviar atributos para a Braze, a exclusão seria a abordagem recomendada.

Independentemente da rota escolhida, os atributos personalizados, eventos e compras que você remover não aparecerão mais na página **Manage Workspace**, o que os remove como filtros de segmento. Se você excluir dados personalizados, a Braze removerá esses dados de nível de usuário dos perfis.
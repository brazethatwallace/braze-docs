---
nav_title: Exemplo de solicitação de produto
hidden: true
alias: /product_request/

page_type: reference
description: "Este artigo de referência mostra um exemplo de uma solicitação de produto."
---

# Exemplo de solicitação de produto {#product-request-example}

Aqui está um exemplo de uma boa solicitação de produto enviada por um cliente. Ela define claramente a solicitação e detalha o caso de uso do recurso.

## Exemplo de solicitação do Skyscanner {#example-request-from-skyscanner}

### Que problema você está tentando resolver? {#what-problem-are-you-trying-to-solve}
O Skyscanner gostaria de poder indicar a prioridade de determinadas tags em relação a outras, no contexto do limite de frequência.

### Exemplifique alguns casos de uso. {#what-are-some-specific-use-cases}
_É aqui que os links para Campaigns e Canvas podem ajudar, bem como uma descrição_

Como lançaremos cada vez mais campanhas disparadas, com base no comportamento dos usuários, há uma chance de que alguns e-mails acabem se sobrepondo uns aos outros e que os programados para envio no início do dia tenham precedência sobre os da tarde, já que temos um limite de um e-mail por dia. Isso não é ideal. Por exemplo, os e-mails referentes ao fundo do funil (redirecionamento) geram mais resultados do que seus equivalentes TOFU (por exemplo, newsletter), e gostaríamos de poder priorizá-los.

Por exemplo, gostaríamos de poder definir que o limite de frequência é de, no máximo, um dia, mas que todas as Campaigns e Canvas marcadas com redirecionamento são P0, todas as de inspiração são P3, todo redirecionamento para pesquisas seria P2, Xsell pode ser P1 etc.

Como ilustração, o resultado seria definir as tags em ordem de prioridade.

### Você tem algum insight adicional? {#do-you-have-any-additional-insight}
_Como isso beneficiaria você e suas equipes de forma mais ampla do que "isso é o que poderíamos fazer"._

Isso nos ajudaria a criar nossos e-mails e campanhas como um ecossistema e a integrá-los em uma experiência abrangente para os usuários, eliminando a complicação dos horários de envio para garantir que o TOFU não tenha prioridade indevida.
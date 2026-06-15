---
nav_title: Usar o ID externo da Braze
article_title: Usar o ID externo da Braze
page_order: 5
page_type: reference
description: "Este artigo de referência explica por que o Decisioning Studio usa o ID externo da Braze como unidade de identidade do cliente e o que acontece se uma estrutura de identificador diferente for usada."
---

# Usar o ID externo da Braze {#use-braze-external-id}

> O Decisioning Studio requer um identificador de cliente único e estável, consistente em todos os ativos de dados. A recomendação é usar o ID externo da Braze como esse identificador. Este artigo explica o motivo e quais riscos surgem quando outras estruturas de identificador são usadas.

## Por que usar o ID externo da Braze? {#why-use-braze-external-id}

O Decisioning Studio opera exclusivamente usando o ID externo da Braze como sua unidade de identidade do cliente. Todos os ativos de dados (perfis de clientes, features, ativações, engajamentos, conversões) devem referenciar o ID externo da Braze como o identificador principal do cliente.

Além de atender a um requisito técnico, exigir o ID externo da Braze é uma escolha de design deliberada que protege a confiabilidade do treinamento e das recomendações do modelo.

### Desafios de outros identificadores {#challenges-of-other-identifiers}

Muitas organizações mantêm dois sistemas diferentes de identificação de clientes:

- **Um ID de warehouse ou sistema de registro** (às vezes chamado de "ID canônico" ou "ID físico"): a fonte de verdade para métricas como lifetime value, devoluções e fidelidade. Reside no seu data warehouse ou ERP.
- **Um ID de plataforma:** o identificador usado por ferramentas como a Braze, normalmente vinculado a um endereço de e-mail, token de dispositivo ou canal de ativação semelhante.

A tentação é usar o ID do warehouse para construir features de clientes (já que é lá que os dados residem) e o ID da Braze para ativação (já que é o que a Braze usa). Mas isso requer uma camada de tradução entre os dois sistemas, e essa camada de tradução introduz fragilidade.

#### Desvio de identidade {#identity-drift}

Mesmo que o mapeamento entre o ID do seu warehouse e o ID da Braze seja atualmente de um-para-muitos (um cliente físico mapeia para múltiplos perfis na Braze), esse mapeamento pode se desestabilizar ao longo do tempo para muitos-para-muitos. Se um único ID de warehouse for reatribuído a diferentes clientes ao longo do tempo, ou se o mesmo perfil da Braze se tornar associado a múltiplos IDs de warehouse, o resultado é **desvio de identidade**.

O desvio de identidade causa:

- **Falhas no treinamento do modelo:** se o cliente para quem o modelo pensava estar recomendando é na verdade uma pessoa diferente, o sinal de treinamento fica corrompido.
- **Imprecisões nos relatórios:** as métricas perdem o sentido quando o mapeamento de identidade subjacente é instável.
- **Erros de atribuição:** as conversões são associadas às recomendações erradas.

### Como o ID externo da Braze resolve esses riscos {#how-braze-external-id-addresses-these-risks}

#### Pronto para ativação por design {#activation-ready-by-design}

Recomendações geradas com base em um ID externo da Braze podem ser injetadas diretamente em mensagens por meio de Liquid ou Conteúdo conectado, sem nenhuma etapa de tradução de ID. Eliminar a camada de tradução remove uma fonte significativa de complexidade operacional e falhas.

#### Isolado de mudanças upstream {#isolated-from-upstream-changes}

Ao operar com o ID externo da Braze, o Decisioning Studio fica isolado de mudanças nos seus sistemas upstream. Se o ID interno do seu warehouse mudar devido a uma migração de sistema, uma correção de qualidade de dados ou uma atualização de ERP, o ID externo da Braze — e tudo associado a ele — permanece estável.

#### Separação limpa de canais {#clean-channel-separation}

Na Braze, um perfil de usuário corresponde a um canal de comunicação alcançável. Se um cliente registra dois endereços de e-mail, ele tem dois perfis distintos na Braze com dois IDs externos distintos. O Decisioning Studio trata esses como duas entidades separadas, o que significa que recomendações e histórico de eventos de um e-mail não são contaminados pela atividade associada ao outro.

Isso evita o que pode ser chamado de "contaminação de contexto". O mecanismo de recomendação não misturaria, por exemplo, comportamento de compra relacionado ao trabalho em recomendações enviadas para uma conta de e-mail pessoal.

## Considerações sobre múltiplas entidades {#multi-entity-considerations}

### Negócios com múltiplas lojas ou hierárquicos {#multi-store-or-hierarchical-businesses}

Para negócios que operam múltiplas lojas ou submarcas (por exemplo, um franqueador com muitos franqueados), o conceito de "cliente" pode ser ambíguo. Um cliente que compra em múltiplas localidades pode ter registros separados em cada local, mas deve ser tratado como uma única pessoa para fins de recomendação.

Se o seu negócio tem essa estrutura, discuta com a equipe do Decisioning Studio como modelar a hierarquia de clientes antes de finalizar sua estratégia de identificadores.

### Fragmentação de identidade B2C {#b2c-identity-fragmentation}

Uma única pessoa física pode acumular múltiplos perfis na Braze ao longo do tempo, como ao se registrar com diferentes endereços de e-mail ou fazer login em diferentes dispositivos antes da unificação de contas. O Decisioning Studio trata cada ID externo da Braze como um cliente distinto.

Isso é intencional: cada perfil representa um canal de ativação distinto. No entanto, isso significa que a qualidade das suas recomendações depende da qualidade da resolução de identidade na Braze. Se a sua implementação da Braze não unifica perfis duplicados de forma confiável, alguns clientes podem receber personalização de menor qualidade porque o histórico deles está fragmentado em múltiplos perfis.
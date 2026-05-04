---
nav_title: Otimizador de conteúdo
article_title: Otimizador de conteúdo
alias: "/content_optimizer/"
description: "O Otimizador de Conteúdo é um agente que ajuda você a testar e otimizar o conteúdo das mensagens em grande escala, usando IA para gerar e avaliar automaticamente altos volumes de variantes de conteúdo."
page_type: reference
page_order: 3
---

# Otimizador de conteúdo

> O Otimizador de Conteúdo é um agente que ajuda você a testar e otimizar o conteúdo das mensagens em grande escala, usando IA para gerar e avaliar automaticamente altos volumes de variantes de conteúdo.

{% alert important %}
O Otimizador de Conteúdo está atualmente em beta e disponível apenas para estes canais: e-mail e notificações por push. Para começar, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Sobre o Otimizador de Conteúdo

O Otimizador de Conteúdo é um agente que funciona em uma etapa do Canvas. Ele ajuda você a definir os componentes da mensagem a serem testados, gerar variantes usando IA Generativa ou entrada manual, e otimizar automaticamente quais combinações de conteúdo são enviadas aos usuários. Este recurso ajuda você a:

- Otimizar linhas de assunto, cabeçalho do corpo, conteúdo do corpo ou CTA principal para e-mails.
- Otimizar títulos e mensagens para notificações por push.
- Melhorar continuamente a performance das mensagens sem a configuração manual de testes A/B.
- Testar rapidamente altos volumes de variantes de conteúdo, aproveitando a IA para ideação.
- Descontinuar automaticamente conteúdos com baixa performance e escalar os vencedores.

Saiba como criar uma [etapa do Otimizador de Conteúdo]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step/).

## Casos de uso

### E-mail

| Caso de uso de otimização | Objetivo | Descrição |
| --- | --- | --- |
| Variações de linha de assunto | Aumentar a taxa de abertura | Testar tom, urgência, personalização e uso de emojis. |
| Estilos de mensagens de cabeçalho | Aumentar o engajamento | Comparar mensagens emocionais, orientadas a valor e claras no cabeçalho do corpo. | 
| Formato do conteúdo do corpo | Melhorar a legibilidade e o engajamento | Testar narrativas versus listas de recursos, marcadores versus parágrafos e comprimento do conteúdo. |
| Tom e texto do CTA | Aumentar os cliques | Comparar frases de CTA focadas em ação, em benefícios e em primeira pessoa. |
| Combinações de conteúdo temático | Descobrir combinações de alta performance | Misturar e combinar componentes de assunto, corpo e CTA temáticos para encontrar a melhor combinação geral. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Notificações por push

| Caso de uso de otimização | Objetivo | Descrição |
| --- | --- | --- |
| Variações de título | Aumentar a taxa de abertura | Testar clareza, urgência, personalização e tom no título da notificação por push. |
| Estilos de texto do corpo | Melhorar o engajamento | Comparar mensagens concisas, orientadas a benefícios e voltadas para ação no corpo da notificação por push. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Como funciona

O Otimizador de Conteúdo usa um algoritmo [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) não contextual para alocar mais envios a variantes de alta performance e reduzir a alocação para as de baixa performance. Com o tempo, isso resulta em uma melhoria contínua do conteúdo da sua mensagem, com mínima intervenção manual.

O algoritmo de otimização proprietário da Braze é construído especificamente para a natureza combinatória da etapa do Otimizador de Conteúdo. Como cada mensagem é composta por vários componentes, o bandit aprende simultaneamente sobre a performance de cada componente (como a linha de assunto, corpo, CTA) e sobre suas interações quando combinados em uma mensagem. Mais concretamente, quando uma determinada combinação é enviada, todas as combinações que compartilham os mesmos componentes se beneficiam dos dados desse envio. Isso permite que o bandit aprenda muito mais rápido com a mesma quantidade de dados, em comparação com um algoritmo bandit padrão.

Quando a etapa é lançada pela primeira vez, o Otimizador de Conteúdo envia variantes aleatoriamente para coletar dados de performance iniciais. Após esse período inicial de exploração, o algoritmo começa a direcionar o tráfego para combinações de conteúdo de maior performance, reduzindo gradualmente a alocação para opções de baixa performance. Durante o período de exploração, o tráfego é geralmente distribuído entre as variantes disponíveis para permitir que o algoritmo aprenda com a performance relativa delas.

O Otimizador de Conteúdo é semelhante à etapa de Mensagem no Canvas, com recursos como horário de silêncio, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) e registro de eventos. Você pode configurar uma etapa do Otimizador de Conteúdo criando uma mensagem base e definindo quais componentes de conteúdo (como linha de assunto, texto do corpo ou chamada para ação) otimizar. As variantes de cada componente podem ser geradas com IA ou inseridas manualmente, e Liquid tags devem ser adicionadas à mensagem base para mapear os componentes no conteúdo da mensagem.

Cada usuário recebe uma mensagem por entrada na etapa do Otimizador de Conteúdo. Reentradas são tratadas como novas, sem memória de variantes anteriores.

## Configuração de entrada no Canvas

Para melhores resultados, use o Otimizador de Conteúdo em Canvas onde os usuários entram na etapa gradualmente e regularmente ao longo do tempo, como em Canvas recorrentes ou sempre ativos com volume diário consistente. Se todos os usuários entrarem na etapa de uma vez, o agente não terá tempo para aprender com os resultados iniciais. Nesse caso, a etapa se comportará mais como um teste A/B estático do que como um motor de otimização ao vivo.

O Otimizador de Conteúdo funciona melhor em Canvas de entrada recorrente diária, bem como em Canvas disparados por eventos e por API com volume diário de usuários relativamente consistente. Se você usar o Otimizador de Conteúdo em Canvas de envio único ou Canvas com entradas "em picos" (como recorrentes mensais), considere usar [Controles de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#selecting-entry-controls) para distribuir as entradas dos usuários ao longo de vários dias.

### Conceitos-chave

| Termo                    | Descrição |
|-------------------------|-------------|
| Mensagem base   | O modelo de mensagem principal a partir do qual as variantes são construídas, incluindo todas as configurações de envio. |
| Componentes de conteúdo  | Elementos dentro de uma mensagem (por exemplo, linha de assunto ou CTA principal) que podem ser testados e otimizados. Os profissionais de marketing devem inserir a Liquid tag relevante na mensagem onde o componente deve aparecer. |
| Variantes de conteúdo    | Os diferentes valores que um componente de conteúdo pode assumir. |
| Combinações de conteúdo| Mensagens únicas criadas pela mistura e combinação de variantes de conteúdo. |
| Evento de otimização       | Determina como o Otimizador de Conteúdo avalia a performance e aloca tráfego para combinações de conteúdo ao longo do tempo, como cliques ou aberturas de e-mail. Aplica-se a todos os componentes de conteúdo em uma etapa. O Otimizador de Conteúdo aprende continuamente com esse evento e redireciona automaticamente a entrega para combinações de conteúdo de melhor performance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Considerações

- O Otimizador de Conteúdo está atualmente em beta e disponível apenas para estes canais: e-mail e notificações por push.
- Para e-mail, o agente pode gerar até 125 combinações por etapa:
   - Até 3 componentes por etapa
   - Até 5 variantes para cada componente
- Para notificações por push, o agente pode gerar até 25 combinações por etapa:
   - Até 2 componentes por etapa
   - Até 5 variantes para cada componente
- Apenas uma mensagem é enviada por usuário por entrada. Não há memória de envios anteriores para reentradas.
- Os profissionais de marketing devem inserir manualmente as Liquid tags para cada componente no criador de mensagens onde as variantes do componente de conteúdo definido devem ser exibidas.

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Próximos passos

- Entre em contato com seu gerente de sucesso do cliente para participar da versão beta ou para suporte na integração.
- Saiba como criar uma [etapa do Otimizador de Conteúdo]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step/).
---
nav_title: Otimizador de Conteúdo
article_title: Otimizador de Conteúdo
alias: "/content_optimizer/"
description: "O Otimizador de Conteúdo ajuda você a testar e otimizar o conteúdo das mensagens em grande escala, usando IA para gerar e avaliar automaticamente altos volumes de variantes de conteúdo."
page_type: reference
page_order: 3
---

# Otimizador de Conteúdo {#content-optimizer}

> O Otimizador de Conteúdo ajuda você a testar e otimizar o conteúdo das mensagens em grande escala, usando IA para gerar e avaliar automaticamente altos volumes de variantes de conteúdo.

{% alert important %}
O Otimizador de Conteúdo está atualmente em beta e disponível apenas para estes canais: e-mail, notificações por push e mensagens SMS/MMS/RCS. Para começar, entre em contato com seu CSM.
{% endalert %}

## Sobre o Otimizador de Conteúdo {#about-content-optimizer}

O Otimizador de Conteúdo funciona em uma etapa do Canvas. Ele ajuda você a definir componentes de mensagem para testar, gerar variantes usando IA generativa ou entrada manual e otimizar automaticamente quais combinações de conteúdo são enviadas aos usuários. Esse recurso ajuda você a:

- Otimizar linhas de assunto, cabeçalho do corpo, conteúdo do corpo ou CTA principal para e-mails.
- Otimizar títulos e mensagens para notificações por push.
- Otimizar ganchos, corpos e CTAs para mensagens SMS, MMS e RCS.
- Melhorar continuamente o desempenho das mensagens sem a necessidade de configurar testes A/B manualmente.
- Testar grandes volumes de variantes de conteúdo rapidamente, aproveitando a IA para ideação.
- Eliminar automaticamente conteúdos com baixo desempenho e escalar os vencedores.

Saiba como criar uma [etapa do Otimizador de Conteúdo]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).

{% multi_lang_include brazeai/generative_ai/policy.md %}

### OpenAI e o Otimizador de Conteúdo {#openai-and-content-optimizer}

O Otimizador de Conteúdo usa a OpenAI apenas quando você solicita explicitamente sugestões de variantes geradas por IA. Ele não usa a OpenAI para escolher qual variante cada usuário recebe nem para alocar o tráfego de envio.

- **Usa a OpenAI:** Quando você seleciona **Gerar sugestões de IA** para um componente de conteúdo, a Braze envia sua variante semente, instruções, [diretriz da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) opcional e (para etapas lançadas com dados de envio suficientes) contexto agregado de desempenho para a OpenAI gerar ideias de variantes.
- **Otimização bandit:** O algoritmo proprietário de multi-armed bandit da Braze lida com a alocação de tráfego, a seleção de variantes no momento do envio e a otimização baseada em desempenho. Consulte [Como funciona](#how-it-works).
- **Entrada manual:** Você pode definir variantes digitando-as por conta própria, sem enviar conteúdo para a OpenAI.

## Casos de uso {#use-cases}

### E-mail {#email}

| Caso de uso de otimização | Objetivo | Descrição |
| --- | --- | --- |
| Variações de linha de assunto | Aumentar a taxa de abertura | Teste tom, urgência, personalização e uso de emojis. |
| Estilos de mensagem no cabeçalho | Melhorar o engajamento | Compare mensagens emocionais, focadas em valor e diretas no cabeçalho do corpo do e-mail. |
| Formato do conteúdo do corpo | Melhorar a legibilidade e o engajamento | Teste narrativa versus listas de recursos, marcadores versus parágrafos e comprimento do conteúdo. |
| Texto e tom do CTA | Aumentar os cliques | Compare fraseados de CTA orientados à ação, focados em benefícios e em primeira pessoa. |
| Combinações de conteúdo temático | Descobrir combinações de alto desempenho | Misture e combine componentes temáticos de assunto, corpo e CTA para encontrar a melhor combinação geral. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="E-mail" }

### Notificações por push {#push-notifications}

| Caso de uso de otimização | Objetivo | Descrição |
| --- | --- | --- |
| Variações de título | Aumentar a taxa de abertura | Teste clareza, urgência, personalização e tom no título da notificação por push. |
| Estilos de texto do corpo | Melhorar o engajamento | Compare mensagens concisas, focadas em benefícios e orientadas à ação no corpo da notificação por push. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Notificações por push" }

### Mensagens SMS, MMS e RCS {#sms-mms-and-rcs-messages}

| Caso de uso de otimização | Objetivo | Descrição |
| --- | --- | --- |
| Variações de gancho | Aumentar o engajamento | Teste urgência, personalização e tom na primeira linha exibida nas prévias de SMS, legendas de MMS ou introduções de RCS. |
| Estilos de texto do corpo | Melhorar o engajamento | Compare mensagens concisas e orientadas à ação no corpo, incluindo o texto que acompanha a mídia em MMS e RCS. |
| Variações de texto do CTA | Aumentar os cliques | Compare fraseados de CTA orientados à ação e conversacionais para links e chamadas de próxima etapa em SMS, MMS e RCS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensagens SMS, MMS e RCS" }

## Como funciona {#how-it-works}

O algoritmo bandit da Braze lida com a otimização descrita nesta seção.

O Otimizador de Conteúdo usa um algoritmo [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) não contextual para alocar mais envios a variantes de alto desempenho e reduzir a alocação para as de baixo desempenho. Com o tempo, isso resulta em uma melhoria contínua do conteúdo da sua mensagem, com mínima intervenção manual.

O algoritmo de otimização bandit proprietário da Braze é construído especificamente para a natureza combinatória da etapa do Otimizador de Conteúdo. Como cada mensagem é composta por vários componentes, o bandit aprende simultaneamente sobre o desempenho de cada componente (como a linha de assunto, corpo, CTA) e sobre suas interações quando combinados em uma mensagem. Mais concretamente, quando uma determinada combinação é enviada, todas as combinações que compartilham os mesmos componentes se beneficiam dos dados desse envio. Isso permite que o bandit aprenda muito mais rápido com a mesma quantidade de dados, em comparação com um algoritmo bandit padrão.

Quando a etapa é lançada pela primeira vez, o Otimizador de Conteúdo envia variantes aleatoriamente para coletar dados de desempenho iniciais. Após esse período inicial de exploração, o algoritmo começa a direcionar o tráfego para combinações de conteúdo de maior desempenho, reduzindo gradualmente a alocação para opções de baixo desempenho. Durante o período de exploração, o tráfego é geralmente distribuído entre as variantes disponíveis para permitir que o algoritmo aprenda com o desempenho relativo delas.

O Otimizador de Conteúdo é semelhante à etapa de Mensagem no Canvas, com recursos como horário de silêncio, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) e registro de eventos. Você pode configurar uma etapa do Otimizador de Conteúdo criando uma mensagem base e definindo quais componentes de conteúdo (como linha de assunto, texto do corpo ou chamada para ação) otimizar. As variantes de cada componente podem ser geradas com IA ou inseridas manualmente, e Liquid tags devem ser adicionadas à mensagem base para mapear os componentes no conteúdo da mensagem.

Cada usuário recebe uma mensagem por entrada na etapa do Otimizador de Conteúdo. Reentradas são tratadas como novas, sem memória de variantes anteriores.

Para atribuir comportamentos posteriores nas suas próprias ferramentas de análise de dados, adicione uma Liquid tag à sua mensagem que registre qual combinação cada usuário recebeu. Para saber mais, consulte [Token de combinação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step#combination-token).

## Configuração de entrada do Canvas {#canvas-entry-setup}

Para obter os melhores resultados, use o Otimizador de Conteúdo em Canvas onde os usuários entram na etapa gradualmente e de forma regular ao longo do tempo, como em Canvas recorrentes ou sempre ativos com volume diário consistente. Se todos os usuários entrarem na etapa de uma vez, o Otimizador de Conteúdo não terá tempo para aprender com os resultados iniciais. A etapa se comportará mais como um teste A/B estático do que como um mecanismo de otimização em tempo real.

O melhor cenário para o Otimizador de Conteúdo é em Canvas de entrada recorrente diária, bem como Canvas disparados por eventos e disparados por API com entradas de usuários diárias relativamente consistentes. Se você usar o Otimizador de Conteúdo em Canvas de envio único ou Canvas com entradas "em picos" (como recorrentes mensais), considere usar [Controles de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) para distribuir as entradas dos usuários ao longo de vários dias.

### Conceitos-chave {#key-concepts}

| Termo                    | Descrição |
|-------------------------|-------------|
| Mensagem base   | O modelo de mensagem principal a partir do qual as variantes são criadas, incluindo todas as configurações de envio. |
| Componentes de conteúdo  | Elementos dentro de uma mensagem (por exemplo, linha de assunto ou CTA principal) que podem ser testados e otimizados. Os profissionais de marketing devem inserir a Liquid tag relevante na mensagem onde o componente deve aparecer. |
| Variantes de conteúdo    | Os diferentes valores que um componente de conteúdo pode assumir. |
| Combinações de conteúdo | Mensagens únicas criadas pela mistura e combinação de variantes de conteúdo. |
| Evento de otimização       | Determina como o Otimizador de Conteúdo avalia o desempenho e distribui o tráfego entre as combinações de conteúdo ao longo do tempo, como cliques ou aberturas para e-mail. Aplica-se a todos os componentes de conteúdo em uma etapa. O Otimizador de Conteúdo aprende continuamente com esse evento e direciona automaticamente a entrega para as combinações de conteúdo com melhor desempenho. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conceitos-chave" }

## Considerações {#considerations}

- O Otimizador de Conteúdo está atualmente em beta e disponível apenas para estes canais: e-mail, notificações por push e mensagens SMS/MMS/RCS.
- Para e-mail, o Otimizador de Conteúdo pode gerar até 125 combinações por etapa:
   - Até 3 componentes por etapa
   - Até 5 variantes para cada componente
- Para notificações por push, o Otimizador de Conteúdo pode gerar até 25 combinações por etapa:
   - Até 2 componentes por etapa
   - Até 5 variantes para cada componente
- Para mensagens SMS, MMS e RCS, o Otimizador de Conteúdo pode gerar até 25 combinações por etapa:
   - Até 2 componentes por etapa
   - Até 5 variantes para cada componente
- Apenas uma mensagem é enviada por usuário por entrada. Não há memória de envios anteriores para reentradas.
- Os profissionais de marketing devem inserir manualmente as Liquid tags para cada componente no criador de mensagem onde as variantes do componente de conteúdo definido devem ser renderizadas.

## Próximos passos {#next-steps}

- Entre em contato com seu CSM para participar do beta ou obter suporte de integração.
- Saiba como criar uma [etapa do Otimizador de Conteúdo]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).
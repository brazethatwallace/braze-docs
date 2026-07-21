---
nav_title: Exemplos
article_title: Exemplos para Decisioning Studio Go
page_order: 5
page_type: reference
description: "Analise tipos comuns de programas de e-mail para determinar se o Decisioning Studio Go é uma boa opção para o seu cenário."
---

# Exemplos para Decisioning Studio Go {#examples-for-decisioning-studio-go}

> O Decisioning Studio Go funciona melhor para programas de e-mail recorrentes em que o agente tem tempo para aprender com o engajamento e em que seu conteúdo inclui opções de variantes suficientes para uma personalização significativa. Esta página agrupa casos de uso comuns de e-mail por nível de adequação, com exemplos e orientações para cada um.

Para uma visão geral de como o Decisioning Studio Go funciona, consulte [BrazeAI Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go).

Cada exemplo neste guia é rotulado com um dos seguintes níveis de adequação:

| Nível de adequação | Descrição |
|---|---|
| **Melhor adequação** | O agente tem tempo suficiente para aprender, seu público é estável o bastante para mostrar aumento, e a personalização pode afetar significativamente o engajamento. Comece por aqui. |
| **Compatível** | O exemplo pode funcionar bem, mas o sucesso depende do timing, do tamanho do público ou do sequenciamento. Analise as considerações antes de se comprometer. |
| **Não recomendado** | O exemplo entra em conflito com a forma como o agente aprende. Escolha um tipo de programa diferente ou converse com seu gerente de sucesso do cliente ou consultor de soluções sobre uma configuração diferente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Níveis de adequação" }

{% alert note %}
Em todos os níveis de adequação, o agente aprende melhor quando seu público gera sinal de engajamento suficiente para que o algoritmo detecte padrões. Como regra prática, direcione públicos na casa das dezenas de milhares de usuários ou mais, com volume de envio semanal consistente. O agente pode funcionar com públicos menores, mas espere um período de aprendizado mais longo e um aumento menos confiável. Seu gerente de sucesso do cliente ou consultor de soluções pode ajudar a confirmar se um determinado público tem o tamanho adequado.
{% endalert %}

## Melhor adequação {#best-fit}

### Campaigns calendárias contínuas {#always-on-calendared-campaigns}

| Tópico | Detalhes |
|---|---|
| Como se apresenta | Um calendário de marketing que funciona por vários meses ou mais, com conteúdo sendo trocado ao longo do tempo — por exemplo, um calendário de membros de recompensas, um cronograma de lançamento de conteúdo ou um calendário de estilo de vida ou inspiração. |
| Por que se encaixa | Programas de longa duração dão ao agente tempo para aprender o que funciona para diferentes usuários. O público é estável, o conteúdo é atualizado regularmente e os cliques geralmente são um indicador significativo de engajamento. |
| O que preparar | Múltiplos criativos base ou conjuntos de variantes que você se sinta confortável em rotacionar. O agente seleciona qual versão funciona para cada usuário, mas precisa de variedade suficiente nas opções que você fornece. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns calendárias contínuas" }

### Programas perenes {#evergreen-programs}

| Tópico | Detalhes |
|---|---|
| Como se apresenta | Campaigns contínuas que não estão vinculadas a datas ou eventos específicos — reconquista, programas de reengajamento, estímulos para contas inativas ou celebrações de marcos. |
| Por que se encaixa | Assim como as Campaigns calendárias, o público é dinâmico, mas o programa funciona indefinidamente. O agente tem tempo para aprender, o conteúdo tem flexibilidade e os cliques são um indicador antecipado contra o qual o agente pode otimizar. |
| O que preparar | Opções de variantes para linha de assunto e CTA que enquadrem a mensagem para diferentes motivações. Variantes de imagem ajudam se você as tiver. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Programas perenes" }

## Casos de uso compatíveis {#supported-use-cases}

### Promoções com múltiplos e-mails {#multi-email-promotions}

| Tópico | Detalhes |
|---|---|
| Como se apresenta | Um conjunto de e-mails enviados ao longo de várias semanas sob o mesmo tema promocional — por exemplo, uma série de volta às aulas ou uma promoção de categoria com várias semanas de duração. |
| Por que funciona | Se a promoção durar tempo suficiente — pelo menos várias semanas — o agente tem margem para aprender dentro da promoção. Os cliques geralmente são um forte indicador antecipado de engajamento promocional. |
| Considerações | Para promoções mais curtas, o agente pode não ter dias de dados suficientes para aprender antes do programa terminar. Como diretriz geral, o agente precisa de pelo menos 10 dias de Campaign para desenvolver recomendações sólidas. Se sua promoção for mais curta que isso, considere se um programa perene poderia conduzir o aprendizado, e então aplique o que aprender na próxima promoção. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Promoções com múltiplos e-mails" }

### Jornadas baseadas em ações ou eventos {#action-or-event-driven-journeys}

| Tópico | Detalhes |
|---|---|
| Como se apresenta | Um único e-mail ou sequência disparada por uma ação do cliente — abandono de carrinho, abandono de navegação ou acompanhamento pós-compra. |
| Por que funciona | Os disparadores criam um ponto de entrada limpo. Se a jornada for recorrente e o volume do público for consistente, o agente pode aprender qual conteúdo funciona para quais usuários. |
| Considerações | O timing importa. Se o e-mail precisa ser enviado em minutos após o evento-gatilho, trabalhe com seu gerente de sucesso do cliente ou consultor de soluções para confirmar se o cronograma de envio do agente é compatível. Se os usuários precisam receber e-mails em uma ordem específica (e-mail A antes do e-mail B), você precisa orquestrar as movimentações de público por conta própria — o agente não sequencia envios para um único usuário ao longo de uma jornada com múltiplos e-mails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Jornadas baseadas em ações ou eventos" }

## Não recomendado {#not-recommended}

### Sequências drip {#drip-sequences}

| Tópico | Detalhes |
|---|---|
| Como se apresenta | Uma sequência de múltiplos e-mails — por exemplo, um tutorial de integração — em que os usuários devem receber o e-mail A, depois o e-mail B, depois o e-mail C em ordem. |
| Por que não se encaixa | O agente seleciona o que enviar para cada usuário com base no que tem mais probabilidade de gerar um clique para aquele usuário. Ele não modela requisitos de sequência. Se você precisa impor uma ordem específica, deve orquestrar o público por conta própria (movendo usuários de Segment para Segment após cada e-mail), o que reduz a maior parte do benefício de usar o agente. O agente também não consegue confirmar de forma independente que o e-mail A foi bem-sucedido antes de enviar o e-mail B. |
| O que fazer em vez disso | Use o [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) para orquestrar a sequência drip. Se você deseja otimização por IA dentro de uma sequência drip, converse com seu gerente de sucesso do cliente ou consultor de soluções sobre se o [Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/get_started) é uma opção melhor. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sequências drip" }

### Envios únicos de e-mail em massa {#one-time-email-blasts}

| Tópico | Detalhes |
|---|---|
| Como se apresenta | Um único e-mail enviado de uma só vez — um anúncio de Black Friday, o lançamento de um novo produto ou uma comunicação corporativa pontual. |
| Por que não se encaixa | O agente precisa de tempo para aprender. Um único envio não dá a ele nenhuma oportunidade de melhorar as decisões antes da Campaign terminar. Quando ele tiver sinal de engajamento suficiente para fazer escolhas melhores, o programa já terá acabado. |
| O que fazer em vez disso | Se você tem um programa perene com conteúdo semelhante — por exemplo, um programa de anúncio de produtos durante o ano todo — use o Decisioning Studio Go nele e aplique o que aprender nos envios únicos. Para um envio verdadeiramente pontual, [testes A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) ou [seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) são opções mais adequadas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Envios únicos de e-mail em massa" }

## Resumo rápido {#at-a-glance}

| Cenário | Adequação | Consideração principal |
|---|---|---|
| Campaigns calendárias contínuas | Melhor adequação | Forneça múltiplos criativos base ou conjuntos de variantes para atualizar ao longo do tempo. |
| Programas perenes (reconquista, reengajamento) | Melhor adequação | Forneça opções de variantes que enquadrem a mesma mensagem para diferentes motivações. |
| Promoções com múltiplos e-mails | Compatível | Busque pelo menos 10 dias de Campaign de margem; promoções mais curtas limitam o aprendizado. |
| Jornadas baseadas em ações ou eventos | Compatível | Confirme os requisitos de timing de envio; você é responsável pela imposição da sequência. |
| Sequências drip (tutoriais de integração) | Não recomendado | Use Canvas para sequenciamento; considere o Decisioning Studio Pro para otimização dentro da sequência drip. |
| Envios únicos de e-mail em massa | Não recomendado | Use testes A/B ou seleção inteligente em vez disso. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tabela resumo de exemplos" }

## Próximas etapas {#next-steps}

Entre em contato com seu gerente de sucesso do cliente ou consultor de soluções da Braze se não tiver certeza se seu programa é adequado. Sinais fortes incluem:

- O público recebe e-mails regularmente — pelo menos semanalmente — ao longo de uma janela de um mês ou mais.
- O público é grande o suficiente para gerar sinal de engajamento consistente (dezenas de milhares de usuários é um ponto de partida útil).
- Você tem pelo menos duas ou três opções de variantes significativas para oferecer (linhas de assunto, CTAs ou imagens que enquadrem a mensagem de forma diferente).
- Os cliques são um indicador antecipado de valor de negócio para este programa, não apenas uma métrica de vaidade.
- O Segment não está sendo usado ativamente por outro Canvas ou Campaign que competiria pelo engajamento dos mesmos usuários.
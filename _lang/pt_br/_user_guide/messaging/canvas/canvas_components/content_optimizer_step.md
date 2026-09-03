---
nav_title: Otimizador de Conteúdo
article_title: Etapa do Otimizador de Conteúdo
alias: "/content_optimizer_step/"
page_order: 5
description: "A etapa do Otimizador de Conteúdo permite configurar e testar múltiplas versões de componentes de conteúdo em uma única etapa. Ela ajuda você a experimentar variações de conteúdo e otimiza automaticamente em direção às combinações com melhor desempenho ao longo do tempo."
page_type: reference

---

# Etapa do Otimizador de Conteúdo {#content-optimizer-step}

> A etapa do Otimizador de Conteúdo permite configurar e testar múltiplas versões de componentes de conteúdo em uma única etapa. Ela ajuda você a experimentar variações de conteúdo e otimiza automaticamente em direção às combinações com melhor desempenho ao longo do tempo. Para uma introdução, consulte [Otimizador de Conteúdo]({{site.baseurl}}/user_guide/brazeai/content_optimizer).

{% alert important %}
O Otimizador de Conteúdo está atualmente em beta. Para começar, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Criar uma etapa do Otimizador de Conteúdo {#create-a-content-optimizer-step}

Para melhores resultados, use o Otimizador de Conteúdo em Canvas onde os usuários entram na etapa gradualmente ao longo do tempo. Se todos os usuários entrarem na etapa de uma só vez, o Otimizador de Conteúdo não terá tempo de aprender com os resultados iniciais.

### Etapa 1: Adicionar uma etapa {#step-1-add-a-step}

Arraste e solte o componente **Otimizador de Conteúdo** da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Otimizador de Conteúdo**.

### Etapa 2: Criar sua mensagem base {#step-2-create-your-base-message}

A mensagem base é o ponto de partida da sua etapa. As variantes de cada componente de conteúdo são inseridas dinamicamente com base nas combinações definidas na guia **Configurações do Otimizador de Conteúdo**.

{% alert note %}
Durante o período beta, os canais compatíveis são e-mail, notificações por push e SMS/MMS/RCS.
{% endalert %}

{% tabs local %}
{% tab E-mail %}

Na guia **Canais de envio de mensagens**, selecione **E-mail** e crie sua mensagem de e-mail base. Consulte nossa seção dedicada de [E-mail]({{site.baseurl}}/user_guide/channels/email) para obter ajuda.

O Otimizador de Conteúdo usa as configurações de envio (como o domínio de e-mail e o endereço de resposta) especificadas nesta variante para enviar todas as mensagens. Você pode começar com um novo design ou selecionar um modelo existente para esta mensagem. Nesta etapa, considere quais componentes da mensagem você deseja otimizar. Você os define na [etapa 4](#step-4).

Os componentes compatíveis para otimização incluem:

- Assunto
- Cabeçalho do corpo
- Conteúdo do corpo
- CTA principal

{% endtab %}
{% tab Notificações por push %}

Na guia **Canais de envio de mensagens**, selecione **Notificações por push** e crie sua notificação por push base. Consulte nossa seção dedicada de [Push]({{site.baseurl}}/user_guide/channels/push) para obter ajuda.

O Otimizador de Conteúdo usa as plataformas de push selecionadas especificadas nesta variante para enviar todas as mensagens. Você pode começar com um novo design ou selecionar um modelo existente para esta mensagem. Nesta etapa, considere quais componentes da mensagem você deseja otimizar. Você os define na [etapa 4](#step-4).

Os componentes compatíveis para otimização incluem:

- Título
- Mensagem

{% endtab %}
{% tab SMS/MMS/RCS %}

Na guia **Canais de envio de mensagens**, selecione **SMS/MMS/RCS** e crie sua mensagem base. Consulte nossa seção dedicada de [SMS/MMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) para obter ajuda.

O Otimizador de Conteúdo usa os detalhes de **Conteúdo** e **Mensagem** especificados nesta variante para enviar todas as mensagens. Você pode começar com um novo design ou selecionar um modelo existente para esta mensagem. Nesta etapa, considere quais componentes da mensagem você deseja otimizar. Você os define na [etapa 4](#step-4).

Os componentes compatíveis para otimização incluem:

- Gancho
- Corpo
- CTA

{% endtab %}
{% endtabs %}

### Etapa 3: Especificar configurações de entrega {#step-3-specify-delivery-settings}

Na guia **Configurações de entrega**, você pode especificar se a etapa deve usar Intelligent Timing ou validações de entrega. Para saber mais, consulte [Editar configurações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings) em Etapa de mensagem.

### Etapa 4: Adicionar componentes de conteúdo e variantes {#step-4}

Os componentes de conteúdo são os elementos individuais da sua mensagem que você deseja testar, como diferentes linhas de assunto ou títulos. Esses componentes permitem que você gere múltiplas versões de uma mensagem e otimize automaticamente com base no desempenho ao longo do tempo.

- **E-mail:** Você pode adicionar até três componentes de conteúdo por etapa e até cinco variantes por componente, totalizando 125 combinações únicas de conteúdo.
- **Notificações por push:** Você pode adicionar até dois componentes por etapa e até cinco variantes por componente, totalizando 25 combinações únicas de conteúdo.
- **SMS/MMS/RCS:** Você pode adicionar até dois componentes de conteúdo por etapa e até cinco variantes por componente, totalizando 25 combinações únicas de conteúdo.

Quando você usa **Gerar sugestões com IA**, a Braze envia conteúdo ao OpenAI para gerar ideias de variantes. A alocação de tráfego no momento do envio não usa OpenAI. Para saber mais sobre quais dados são enviados e como são utilizados, consulte [OpenAI e Otimizador de Conteúdo]({{site.baseurl}}/user_guide/brazeai/content_optimizer#openai-and-content-optimizer).

![Opções para adicionar e configurar componentes de conteúdo na interface do Otimizador de Conteúdo. A interface exibe componentes selecionáveis como Assunto, Cabeçalho do corpo, Conteúdo do corpo e CTA principal, cada um com campos para inserir diferentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Etapa 4.1: Configurar componentes de conteúdo {#step-41-configure-content-components}

Para configurar componentes, acesse a guia **Configurações do Otimizador de Conteúdo**.

{% tabs local %}
{% tab E-mail %}

Escolha quais componentes você deseja otimizar para mensagens de e-mail. As opções compatíveis são:

- Assunto
- Cabeçalho do corpo
- Conteúdo do corpo
- CTA principal

Para cada componente selecionado, defina um conjunto de versões alternativas desse conteúdo (variantes). Use variantes claras e distintas que difiram em tom, estrutura ou conteúdo. Isso ajuda o Otimizador de Conteúdo a identificar os melhores desempenhos de forma mais eficaz. Você pode:
  - Escrever suas próprias variantes manualmente.
  - Usar sugestões geradas por IA para explorar novas opções rapidamente.

![Interface de Configurações do Otimizador de Conteúdo mostrando opções para adicionar e configurar componentes de conteúdo para otimização de e-mail. Cada componente tem campos de entrada para inserir diferentes variantes. O texto visível inclui nomes de componentes e campos para inserir o texto das variantes.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Notificações por push %}

Escolha quais componentes você deseja otimizar para notificações por push. As opções compatíveis são:
- Título
- Mensagem

Para cada componente selecionado, defina um conjunto de versões alternativas desse conteúdo (variantes). Use variantes claras e distintas que difiram em tom, estrutura ou conteúdo. Isso ajuda o Otimizador de Conteúdo a identificar os melhores desempenhos de forma mais eficaz. Você pode:
  - Escrever suas próprias variantes manualmente.
  - Usar sugestões geradas por IA para explorar novas opções rapidamente.

![Configurações do Otimizador de Conteúdo mostrando opções para adicionar e configurar componentes de conteúdo para otimização de push.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% tab SMS/MMS/RCS %}

Após selecionar seu grupo de inscrições e tipo de mensagem (se aplicável), escolha quais componentes você deseja otimizar para SMS/MMS/RCS. As opções compatíveis são:
- Gancho
- Corpo
- CTA
{% alert note %}
Após o lançamento de uma etapa do Otimizador de Conteúdo para SMS/MMS/RCS, não é possível atualizar o grupo de inscrições ou o tipo de mensagem.
{% endalert %}
Para cada componente selecionado, defina um conjunto de versões alternativas desse conteúdo (variantes). Use variantes claras e distintas que difiram em tom, estrutura ou conteúdo. Isso ajuda o Otimizador de Conteúdo a identificar os melhores desempenhos de forma mais eficaz. Você pode:
  - Escrever suas próprias variantes manualmente.
  - Usar sugestões geradas por IA para explorar novas opções rapidamente.

![Configurações do Otimizador de Conteúdo mostrando opções para adicionar e configurar componentes de conteúdo para otimização de SMS/MMS/RCS.]({% image_buster /assets/img/content_optimizer/add_content_components_sms_rcs_mms.png %})

{% endtab %}
{% endtabs %}

#### Etapa 4.2: Adicionar Liquid à sua mensagem {#step-42-add-liquid-to-your-message}

Após definir pelo menos duas variantes para cada componente, copie a Liquid tag associada a cada um e cole-a no local correspondente na sua mensagem base.

- Por exemplo, se você está otimizando a linha de assunto, cole a tag {% raw %}`{% message_component "Subject" %}`{% endraw %} no campo de assunto do criador de e-mail.
- Você também pode incluir tags de componente dentro de textos mais longos para testar apenas uma parte do componente. Por exemplo: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Opções para adicionar e configurar componentes de conteúdo como Assunto, Cabeçalho do corpo, Conteúdo do corpo e CTA principal. Cada componente tem campos para inserir diferentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Se você não adicionar uma Liquid tag para um componente de conteúdo selecionado, verá um aviso na guia **Configurações do Otimizador de Conteúdo** e um erro na guia **Canais de envio de mensagens**. O Canvas não pode ser lançado até que todos os componentes selecionados sejam adicionados corretamente à sua mensagem base.

Conforme o Canvas é executado, o Otimizador de Conteúdo combina e mistura variantes entre componentes para gerar diferentes combinações de conteúdo. Com o tempo, as combinações de melhor desempenho são priorizadas para entrega, ajudando você a melhorar o desempenho sem intervenção manual.

#### Referências de Liquid {#liquid-references}

| Canal | Componente | Snippet de Liquid |
| --- | --- | --- |
| E-mail | Assunto | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| E-mail | Cabeçalho do corpo | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| E-mail | Conteúdo do corpo | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| E-mail | CTA principal | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| Push | Título | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| Push | Mensagem | {% raw %}`{% message_component "Message" %}`{% endraw %} |
| SMS/MMS/RCS | Gancho | {% raw %}`{% message_component "Hook" %}`{% endraw %} |
| SMS/MMS/RCS | Corpo | {% raw %}`{% message_component "Body" %}`{% endraw %} |
| SMS/MMS/RCS | CTA | {% raw %}`{% message_component "CTA" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Referências de Liquid" }

#### Token de combinação {#combination-token}

Use o token de combinação para registrar qual combinação de variantes um usuário recebeu. Adicione a Liquid tag {% raw %}`{{component_combination_token}}`{% endraw %} a um link na sua mensagem base e, em seguida, use o valor nas suas próprias ferramentas de análise de dados para atribuir comportamentos posteriores a uma combinação específica.

Por exemplo, adicione o token a um link como parâmetro UTM:

{% raw %}
```liquid
https://www.example.com/summer-sale?utm_content={{component_combination_token}}
```
{% endraw %}

A tag renderiza uma string de números separados por underscores, como `3_2_8`:

- Cada posição corresponde a um componente de conteúdo, na ordem em que os componentes aparecem na guia **Configurações do Otimizador de Conteúdo**.
- Cada número é o índice da variante que o usuário recebeu para aquele componente. Os índices começam em 0, então `0` é a primeira variante criada para aquele componente, `1` é a segunda, e assim por diante.

A Braze atribui um índice a uma variante quando você a cria e mantém esse índice durante toda a vida útil da etapa. Você pode desativar uma variante, mas não pode excluí-la, e os índices nunca são reutilizados ou renumerados. Um índice não reflete a posição da variante entre as variantes ativas no momento.

Por isso, os índices podem subir além do que o limite de cinco variantes por componente sugere. Esse limite se aplica apenas às variantes ativas. Então, se você desativar várias variantes e adicionar novas, as novas variantes podem ter índices como 5, 6, 7 e 8.

Por exemplo, uma etapa de e-mail otimiza uma linha de assunto e um CTA principal. O componente de assunto foi lançado com cinco variantes. Três foram desativadas posteriormente e três novas foram adicionadas:

| Variante de assunto | Índice | Status |
| --- | --- | --- |
| Your summer sale starts now | 0 | Desativada |
| Summer sale: 20% off | 1 | Desativada |
| 20% off, this week only | 2 | Desativada |
| Save 20% on summer picks | 3 | Ativa |
| Your 20% off code is inside | 4 | Ativa |
| Summer picks, 20% off | 5 | Ativa |
| Don't miss 20% off | 6 | Ativa |
| Last chance: 20% off summer | 7 | Ativa |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Índices de variantes de assunto" }

O componente de CTA principal tem duas variantes, com índices 0 e 1. Nesta etapa, um token de `6_1` significa que o usuário recebeu a variante de assunto com índice 6 ("Don't miss 20% off") e a variante de CTA principal com índice 1.

### Etapa 5: Selecionar evento de otimização {#step-5-select-optimization-event}

O evento de otimização determina como o Otimizador de Conteúdo avalia o desempenho e aloca tráfego para as combinações de conteúdo ao longo do tempo.

O evento de otimização selecionado se aplica a todos os componentes de conteúdo nesta etapa.

{% tabs local %}
{% tab E-mail %}

Para e-mail, você pode otimizar para um dos eventos a seguir. O Otimizador de Conteúdo usa aberturas e cliques registrados dentro de 7 dias após o envio de uma mensagem para direcionar a entrega para combinações de conteúdo de melhor desempenho.

| Evento | Descrição | Casos de uso |
| --- | --- | --- |
| Aberturas | Otimiza para combinações que levam os destinatários a abrir o e-mail. | Testar linhas de assunto ou aumentar a visibilidade |
| Cliques | Otimiza para combinações que geram engajamento com links. Não inclui cliques de bots ou cliques de cancelamento de inscrição reconhecidos pela Braze. | Gerar tráfego, engajamento ou conversão a partir de links |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 5: Selecionar evento de otimização" }

#### Excluir links da otimização {#exclude-links-from-optimization}

Quando você otimiza para cliques, é possível excluir um ou mais links da otimização. Use isso para links que não sinalizam engajamento com o conteúdo que você está testando, como uma Central de Preferências ou um localizador de lojas.

Para excluir um link, acesse a guia **Configurações do Otimizador de Conteúdo** e adicione a URL do link. A Braze faz a correspondência pelo prefixo, então um clique em qualquer URL na sua mensagem que comece com a URL especificada será excluído.

Os cliques excluídos não contam para o evento de otimização, então não influenciam quais combinações o Otimizador de Conteúdo favorece. Eles ainda são contabilizados na análise de dados total da etapa e não são contados nas tabelas de [Desempenho por componente](#performance-by-component) ou [Desempenho por combinação](#performance-by-combination).

{% endtab %}
{% tab Notificações por push %}

Para notificações por push, você pode otimizar **Aberturas**. Isso otimiza as combinações que levam os destinatários a abrir a notificação por push. Você pode usar esse evento de otimização para testar variações no título ou no texto da mensagem.

{% endtab %}
{% tab SMS/MMS/RCS %}

Para mensagens SMS e MMS, você pode otimizar **Cliques**. Para mensagens RCS, você pode otimizar **Leituras** ou **Cliques**.

Para que a etapa tenha um evento para otimizar:
- Mensagens SMS e MMS devem conter um link.
- Mensagens RCS devem conter um link ou uma resposta sugerida.

{% alert note %}
No momento, o envio de mensagens RCS com o Otimizador de Conteúdo não é compatível com fallbacks de SMS.
{% endalert %}
{% endtab %}
{% endtabs %}

## Estados da etapa {#step-states}

Conforme uma etapa do Otimizador de Conteúdo é executada, a Braze avalia o desempenho das variantes de conteúdo e atribui à etapa um dos três estados, visíveis no Canvas.

| Estado | O que significa |
| --- | --- |
| Learning | O Otimizador de Conteúdo ainda está coletando dados de desempenho das suas variantes de conteúdo e ainda não encontrou um vencedor consistente e confiável. |
| Optimizing | O Otimizador de Conteúdo encontrou variantes que superam consistentemente as outras e está direcionando a entrega para as combinações vencedoras. |
| Action Recommended | A etapa está em execução há algum tempo sem que um vencedor claro tenha surgido. Revise a configuração da sua etapa para ajudar o Otimizador de Conteúdo a encontrar um. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados da etapa do Otimizador de Conteúdo" }

### Ações a considerar {#actions-to-consider}

Se a sua etapa entrar no estado Action Recommended, considere o seguinte:

- Aumente o número de usuários que entram no Canvas, se possível. Mais envios fornecem ao Otimizador de Conteúdo mais dados para aprender.
- De modo geral, teste mais combinações em vez de menos (consulte [Práticas recomendadas](#best-practices)). Isso dá ao Otimizador de Conteúdo um sinal mais claro sobre o que está funcionando melhor. Se o volume do seu público for baixo (com média inferior a aproximadamente 3.000 envios por dia), considere reduzir um pouco o número de variantes, já que combinações demais em relação ao seu volume podem desacelerar o aprendizado.
- Torne as variantes de conteúdo mais claramente distintas entre si em tom, estrutura ou conteúdo.
- Se você não puder aumentar o público e a quantidade de variantes e a diversidade de conteúdo já parecerem adequadas, talvez a sua etapa simplesmente precise de mais tempo para encontrar vencedores.

## Editar uma etapa lançada {#edit-a-launched-step}

Depois que o Canvas for lançado, você pode atualizar uma etapa do Otimizador de Conteúdo em execução abrindo-a no editor do Canvas. Você pode:

{% multi_lang_include messaging/canvas/content_optimizer_launched_step_actions.md %}

{% alert note %}
A Braze atribui a cada usuário uma combinação de conteúdo quando ele entra na etapa do Otimizador de Conteúdo. Se o envio for postergado por controles de entrega, como limite de frequência, Intelligent Timing ou horário de silêncio, o usuário ainda poderá receber uma variante que você desativou. Para interromper esses envios com urgência, siga as mesmas etapas de uma etapa de Mensagem. Para saber mais, consulte [Interromper Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases).
{% endalert %}

Quando você publica alterações, o otimizador é redefinido e começa a realocar o tráfego do zero entre todas as variantes e combinações ativas. Evite atualizar variantes enquanto a etapa estiver no estado de Aprendizado. Os dados históricos anteriores à edição são mantidos e podem ser visualizados na guia **Content Analytics**.

As configurações a seguir não podem ser alteradas após o lançamento:

- O conteúdo das variantes ativas existentes
- Quais componentes estão sendo testados
- O evento de otimização

Para etapas de SMS/MMS/RCS, o grupo de inscrições e o tipo de mensagem também não podem ser alterados após o lançamento.

## Práticas recomendadas {#best-practices}

- De modo geral, teste mais componentes em vez de menos na etapa do Otimizador de Conteúdo. Por exemplo, em vez de testar dois componentes para e-mail, teste três.
- Testar pelo menos 10 combinações no total geralmente produz melhores resultados.
- Para e-mail, etapas que otimizam para cliques tendem a ter um desempenho melhor do que etapas que otimizam para aberturas. Quando os cliques se encaixam no seu caso de uso, escolha cliques como seu evento de otimização.
- Se esta é a primeira vez que você usa o Otimizador de Conteúdo, considere usar uma etapa de [jornadas experimentais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que apenas parte do seu público entre na ramificação que contém a etapa do Otimizador de Conteúdo. Por exemplo, você poderia enviar metade dos seus usuários por uma jornada com a etapa do Otimizador de Conteúdo e enviar a outra metade por uma jornada de controle com a etapa de mensagem contendo seu conteúdo padrão atual. Em seguida, colete dados por 2 a 3 semanas e compare quaisquer indicadores chave de desempenho (KPIs) ou contra-métricas antes de aumentar o tráfego para as jornadas com etapas do Otimizador de Conteúdo.
  - Para uma comparação direta eficaz, inclua seu conteúdo padrão atual como uma das variantes para cada componente na sua etapa do Otimizador de Conteúdo.
- Quando estiver pronto para atualizar depois que sua etapa do Otimizador de Conteúdo estiver no estado Otimizando por algum tempo, desative as variantes com baixo desempenho e adicione novas que se baseiem nas características das suas variantes de melhor desempenho.

## Considerações {#considerations}

- As configurações de vários idiomas não são compatíveis com as etapas do Otimizador de Conteúdo. Em vez disso, use uma etapa do Otimizador de Conteúdo por idioma e ramifique as jornadas individualmente.
- As Liquid tags para componentes do Otimizador de Conteúdo não são compatíveis com etapas de Mensagem, então o Liquid é interrompido nas etapas de Mensagem.
- Após o lançamento de uma etapa do Otimizador de Conteúdo, não é possível alterar quais componentes estão sendo testados, o conteúdo das variantes ativas existentes nem o evento de otimização. Para etapas de SMS/MMS/RCS, o grupo de inscrições e o tipo de mensagem também não podem ser alterados.

## Análise de dados {#analytics}

Para revisar o desempenho, abra o painel de análise de dados no nível da etapa para ver métricas por variante de conteúdo e desempenho geral da combinação. A etapa do Otimizador de Conteúdo usa a [mesma análise de dados da etapa de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#analytics).

Se você atualizou a etapa após o lançamento, o gráfico de alocação de envios marca quando cada edição de conteúdo ocorreu. Os dados de variantes desativadas são retidos e permanecem visíveis no painel de análise de dados, para que você possa comparar o desempenho ao longo de toda a vida útil da etapa.

![Análise de dados do Otimizador de Conteúdo para três botões e a porcentagem de alocação de envios, que apresenta tendência de alta.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Desempenho por componente {#performance-by-component}

A seção **Desempenho por componente** exibe o desempenho de cada componente na etapa do Otimizador de Conteúdo. A coluna **Componente** corresponde ao componente de conteúdo que você está testando (por exemplo, **Linha de assunto** ou **CTA principal**). A coluna **Identificador** corresponde ao identificador dessa variante na guia **Configurações do Otimizador de Conteúdo**.

As aberturas e cliques únicos são capturados dentro de sete dias após o envio de uma mensagem. As colunas exibidas dependem do seu canal e do evento de otimização selecionado.

| Métrica | Descrição |
| --- | --- |
| Envios | O número de envios atribuídos a essa variante para aquele componente nesta etapa, usando a mesma contagem de envios no nível da etapa que [*Envios*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends) na tabela [Desempenho por combinação](#performance-by-combination). |
| Aberturas | Quando esta coluna aparece para o seu canal, o número de aberturas **únicas** para essa variante dentro de sete dias após o envio. Consulte [*Aberturas únicas*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Taxa de abertura | Quando esta coluna aparece, a porcentagem de envios para essa variante que registraram pelo menos uma abertura única qualificada dentro de sete dias. |
| Cliques | O número de cliques **únicos** para essa variante dentro de sete dias após o envio. Consulte [*Total de cliques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks), [*Cliques únicos*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks) e [Etapa 5: Selecionar evento de otimização](#step-5-select-optimization-event). |
| Taxa de cliques | A porcentagem de envios para essa variante que registraram pelo menos um clique único qualificado dentro de sete dias, usando a mesma janela da etapa que a tabela [Desempenho por combinação](#performance-by-combination). Para saber mais, consulte [Por que a análise de dados da etapa difere da análise geral](#why-step-analytics-differ-from-general-analytics). |
| Leituras | Quando esta coluna aparece (por exemplo, para RCS quando você otimiza para leituras), conta quando um consumidor lê a mensagem com confirmações de leitura ativadas. Consulte [*Leituras*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads). |
| Taxa de leitura | A porcentagem de envios para essa variante que resultaram em uma leitura entre usuários com confirmações de leitura ativadas. Consulte [*Taxa de leitura*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de desempenho por componente" }

![Análise de dados do Otimizador de Conteúdo — Desempenho por componente, com tabelas separadas por componente, listando envios, cliques e taxa de cliques para cada variante.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_component.png %})

### Desempenho por combinação {#performance-by-combination}

A seção **Desempenho por combinação** exibe o desempenho de cada combinação na etapa do Otimizador de Conteúdo. Combinações são a mistura de variantes que definem essa linha — uma variante selecionada de cada componente de conteúdo que você está testando (por exemplo, uma linha de assunto associada a um CTA principal).

As aberturas e cliques únicos são capturados dentro de sete dias após o envio de uma mensagem. As colunas exibidas dependem do seu canal e do evento de otimização selecionado.

| Métrica | Descrição |
| --- | --- |
| Envios | O número total de mensagens enviadas a partir desta etapa usando essa combinação. A contagem segue o mesmo significado geral de [*Envios*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends), delimitado a cada combinação. |
| Aberturas | O número de aberturas únicas para essa combinação dentro de sete dias após o envio. Para saber como aberturas únicas são definidas para e-mail, consulte [*Aberturas únicas*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Taxa de abertura | A porcentagem de envios para essa combinação que registraram pelo menos uma abertura única qualificada dentro de sete dias. |
| Cliques | O número de cliques únicos para essa combinação dentro de sete dias após o envio. Para saber como a Braze define cliques por canal, consulte [*Total de cliques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks) e [*Cliques únicos*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks). |
| Taxa de cliques | A porcentagem de envios para essa combinação que registraram pelo menos um clique único qualificado dentro de sete dias. Como o Otimizador de Conteúdo usa contagens deduplicadas de sete dias da etapa, essa taxa pode não corresponder às taxas de cliques na análise geral de Campaign. Para saber mais, consulte [Por que a análise de dados da etapa difere da análise geral](#why-step-analytics-differ-from-general-analytics). |
| [Leituras]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads) | Quando esta coluna aparece (por exemplo, para RCS quando você otimiza para leituras), conta quando um consumidor lê a mensagem com confirmações de leitura ativadas. |
| [Taxa de leitura]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate) | Quando esta coluna aparece, a porcentagem de envios para essa combinação que resultaram em uma leitura entre usuários com confirmações de leitura ativadas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de desempenho por combinação" }

![Tabela de análise de dados do Otimizador de Conteúdo — Desempenho por combinação, com envios, cliques e taxa de cliques para cada combinação de conteúdo.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_combination.png %})

### Por que a análise de dados da etapa difere da análise geral {#why-step-analytics-differ-from-general-analytics}

Os motivos pelos quais a análise de dados na etapa do Otimizador de Conteúdo difere da seção **Analytics** incluem:

- Os envios de push são deduplicados para envios ao mesmo usuário em dispositivos diferentes.
- De modo geral, cliques e aberturas são deduplicados para serem únicos por usuário.
- Apenas cliques e aberturas que ocorrem dentro de sete dias após o envio de uma mensagem são contabilizados na etapa do Otimizador de Conteúdo.
- Cliques em links excluídos são contabilizados na análise total da etapa, mas não nas tabelas **Desempenho por componente** ou **Desempenho por combinação**. Para saber mais, consulte [Excluir links da otimização](#exclude-links-from-optimization).

### Visualizar variantes no perfil de usuário {#view-variants-on-a-user-profile}

Para ver quais variantes um usuário individual recebeu, abra o perfil do usuário e acesse a guia **Histórico de mensagens**. Na linha do evento de envio de uma etapa do Otimizador de Conteúdo, a tabela mostra as variantes de componente que foram enviadas para aquele usuário. Para saber mais, consulte [Guia Histórico de mensagens]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab).

### Comparar etapas no Report Builder {#compare-steps-in-report-builder}

Para comparar o desempenho entre mais de uma etapa do Otimizador de Conteúdo, crie um relatório e selecione **Canvas Step with Canvas Optimizer**. O relatório mostra o desempenho da etapa por componente e por combinação para as etapas que você incluir, estejam elas no mesmo Canvas ou em Canvas diferentes. Para saber mais, consulte [Report Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

## Solução de problemas {#troubleshooting}

| Problema | Descrição | Solução |
| --- | --- | --- |
| Tags Liquid ausentes | Se você adicionar um componente de conteúdo (como Assunto ou CTA) mas não inserir a tag Liquid correspondente na sua mensagem base, você verá: <br>- Um alerta na guia **Configurações do Otimizador de Conteúdo** <br>- Um erro na guia **Canais de envio de mensagens** | Copie o snippet Liquid exibido abaixo de cada componente na guia **Configurações do Otimizador de Conteúdo** e cole-o na parte apropriada da sua mensagem. |
| Tags Liquid órfãs | Se você excluir um componente de conteúdo, mas deixar a tag Liquid dele na mensagem base, a mensagem pode não ser renderizada conforme esperado ao ser enviada. | Remova todas as tags `message_component` não utilizadas da sua mensagem base antes de lançar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Solução de problemas" }
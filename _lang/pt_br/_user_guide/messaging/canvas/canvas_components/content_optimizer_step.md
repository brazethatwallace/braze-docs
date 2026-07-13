---
nav_title: Otimizador de Conteúdo
article_title: Etapa do agente Otimizador de Conteúdo
alias: "/content_optimizer_step/"
page_order: 5
description: "A etapa do agente Otimizador de Conteúdo permite configurar e testar múltiplas versões de componentes de conteúdo em uma única etapa. Ela ajuda você a experimentar variações de conteúdo e otimiza automaticamente em direção às combinações com melhor desempenho ao longo do tempo."
page_type: reference

---

# Etapa do agente Otimizador de Conteúdo {#content-optimizer-agent-step}

> A etapa do agente Otimizador de Conteúdo permite configurar e testar múltiplas versões de componentes de conteúdo em uma única etapa. Ela ajuda você a experimentar variações de conteúdo e otimiza automaticamente em direção às combinações com melhor desempenho ao longo do tempo. Para uma introdução, consulte [Otimizador de Conteúdo]({{site.baseurl}}/user_guide/brazeai/content_optimizer).

{% alert important %}
O Otimizador de Conteúdo está atualmente em beta. Para começar, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Criar uma etapa do Otimizador de Conteúdo {#create-a-content-optimizer-step}

Para melhores resultados, use o agente Otimizador de Conteúdo em Canvas onde os usuários entram na etapa gradualmente ao longo do tempo. Se todos os usuários entrarem na etapa de uma vez, o agente não terá tempo para aprender com os resultados iniciais.

### Etapa 1: Adicionar uma etapa {#step-1-add-a-step}

Arraste e solte o componente **Otimizador de Conteúdo** da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Otimizador de Conteúdo**.

### Etapa 2: Criar sua mensagem base {#step-2-create-your-base-message}

A mensagem base é o ponto de partida da sua etapa. As variantes de cada componente de conteúdo são inseridas dinamicamente com base nas combinações definidas na guia **Configurações do Otimizador de Conteúdo**.

{% alert note %}
Durante o período beta, os canais suportados são e-mail, notificações por push e SMS/MMS/RCS.
{% endalert %}

{% tabs local %}
{% tab E-mail %}

Na guia **Canais de envio de mensagens**, selecione **E-mail** e crie sua mensagem de e-mail base. Consulte nossa seção dedicada de [E-mail]({{site.baseurl}}/user_guide/channels/email) para obter ajuda.

O agente Otimizador de Conteúdo usa as configurações de envio (como o domínio de e-mail e o endereço de resposta) especificadas nesta variante para enviar todas as mensagens. Você pode começar com um novo design ou selecionar um modelo existente para esta mensagem. Nesta etapa, considere quais componentes da mensagem você deseja otimizar. Você os define na [etapa 4](#step-4).

Os componentes suportados para otimização incluem:

- Subject
- Body Header
- Body Content
- Primary CTA

{% endtab %}
{% tab Notificações por push %}

Na guia **Canais de envio de mensagens**, selecione **Notificações por push** e crie sua notificação por push base. Consulte nossa seção dedicada de [Push]({{site.baseurl}}/user_guide/channels/push) para obter ajuda.

O agente Otimizador de Conteúdo usa as plataformas de push selecionadas nesta variante para enviar todas as mensagens. Você pode começar com um novo design ou selecionar um modelo existente para esta mensagem. Nesta etapa, considere quais componentes da mensagem você deseja otimizar. Você os define na [etapa 4](#step-4).

Os componentes suportados para otimização incluem:

- Title
- Message

{% endtab %}
{% tab SMS/MMS/RCS %}

Na guia **Canais de envio de mensagens**, selecione **SMS/MMS/RCS** e crie sua mensagem base. Consulte nossa seção dedicada de [SMS/MMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) para obter ajuda.

O agente Otimizador de Conteúdo usa os detalhes de **Content** e **Message** especificados nesta variante para enviar todas as mensagens. Você pode começar com um novo design ou selecionar um modelo existente para esta mensagem. Nesta etapa, considere quais componentes da mensagem você deseja otimizar. Você os define na [etapa 4](#step-4).

Os componentes suportados para otimização incluem:

- Hook
- Body
- CTA

{% endtab %}
{% endtabs %}

### Etapa 3: Especificar configurações de entrega {#step-3-specify-delivery-settings}

Na guia **Configurações de entrega**, você pode especificar se a etapa deve usar Intelligent Timing ou validações de entrega. Para mais detalhes, consulte [Editar configurações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings) na etapa Mensagem.

### Etapa 4: Adicionar componentes de conteúdo e variantes {#step-4}

Componentes de conteúdo são os elementos individuais da sua mensagem que você deseja testar, como diferentes linhas de assunto ou títulos. Esses componentes permitem gerar múltiplas versões de uma mensagem e otimizar automaticamente com base no desempenho ao longo do tempo.

- **E-mail:** Você pode adicionar até três componentes de conteúdo por etapa e até cinco variantes por componente, totalizando 125 combinações únicas de conteúdo.
- **Notificações por push:** Você pode adicionar até dois componentes por etapa e até cinco variantes por componente, totalizando 25 combinações únicas de conteúdo.
- **SMS/MMS/RCS:** Você pode adicionar até dois componentes de conteúdo por etapa e até cinco variantes por componente, totalizando 25 combinações únicas de conteúdo.

![Opções para adicionar e configurar componentes de conteúdo na interface do Otimizador de Conteúdo. A interface exibe componentes selecionáveis como Subject, Body Header, Body Content e Primary CTA, cada um com campos para inserir diferentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Etapa 4.1: Configurar componentes de conteúdo {#step-41-configure-content-components}

Para configurar componentes, acesse a guia **Configurações do Otimizador de Conteúdo**.

{% tabs local %}
{% tab E-mail %}

Escolha quais componentes você deseja otimizar para mensagens de e-mail. As opções suportadas são:

- Subject
- Body Header
- Body Content
- Primary CTA

Para cada componente selecionado, defina um conjunto de versões alternativas desse conteúdo (variantes). Use variantes claras e distintas que difiram em tom, estrutura ou conteúdo. Isso ajuda o Otimizador de Conteúdo a identificar os melhores desempenhos de forma mais eficaz. Você pode:
  - Escrever suas próprias variantes manualmente.
  - Usar sugestões geradas por IA para explorar novas opções rapidamente.

![Interface de configurações do Otimizador de Conteúdo mostrando opções para adicionar e configurar componentes de conteúdo para otimização de e-mail. Cada componente tem campos de entrada para inserir diferentes variantes. O texto visível inclui nomes de componentes e campos para inserir texto de variantes.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Notificações por push %}

Escolha quais componentes você deseja otimizar para notificações por push. As opções suportadas são:
- Title
- Message

Para cada componente selecionado, defina um conjunto de versões alternativas desse conteúdo (variantes). Use variantes claras e distintas que difiram em tom, estrutura ou conteúdo. Isso ajuda o Otimizador de Conteúdo a identificar os melhores desempenhos de forma mais eficaz. Você pode:
  - Escrever suas próprias variantes manualmente.
  - Usar sugestões geradas por IA para explorar novas opções rapidamente.

![Configurações do Otimizador de Conteúdo mostrando opções para adicionar e configurar componentes de conteúdo para otimização de push.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% tab SMS/MMS/RCS %}

Após selecionar seu grupo de inscrições e tipo de mensagem (se aplicável), escolha quais componentes você deseja otimizar para SMS/MMS/RCS. As opções suportadas são:
- Hook
- Body
- CTA
{% alert note %}
Após uma etapa do Otimizador de Conteúdo para SMS/MMS/RCS ser lançada, você não pode atualizar o grupo de inscrições ou o tipo de mensagem.
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

![Opções para adicionar e configurar componentes de conteúdo como Subject, Body Header, Body Content e Primary CTA. Cada componente tem campos para inserir diferentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Se você não adicionar uma Liquid tag para um componente de conteúdo selecionado, verá um aviso na guia **Configurações do Otimizador de Conteúdo** e um erro na guia **Canais de envio de mensagens**. O Canvas não pode ser lançado até que todos os componentes selecionados sejam adicionados corretamente à sua mensagem base.

Conforme o Canvas é executado, o agente combina e alterna variantes entre componentes para gerar diferentes combinações de conteúdo. Com o tempo, as combinações com melhor desempenho são priorizadas para entrega, ajudando você a melhorar o desempenho sem intervenção manual.

#### Referências de Liquid {#liquid-references}

| Canal | Componente | Trecho Liquid |
| --- | --- | --- |
| E-mail | Subject | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| E-mail | Body Header | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| E-mail | Body Content | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| E-mail | Primary CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| Push | Title | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| Push | Message | {% raw %}`{% message_component "Message" %}`{% endraw %} |
| SMS/MMS/RCS | Hook | {% raw %}`{% message_component "Hook" %}`{% endraw %} |
| SMS/MMS/RCS | Body | {% raw %}`{% message_component "Body" %}`{% endraw %} |
| SMS/MMS/RCS | CTA | {% raw %}`{% message_component "CTA" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Referências de Liquid" }

### Etapa 5: Selecionar evento de otimização {#step-5-select-optimization-event}

O evento de otimização determina como o agente Otimizador de Conteúdo avalia o desempenho e distribui o tráfego para as combinações de conteúdo ao longo do tempo.

O evento de otimização selecionado se aplica a todos os componentes de conteúdo nesta etapa.

{% tabs local %}
{% tab E-mail %}

Para e-mail, você pode otimizar para um dos seguintes eventos. O agente usa aberturas e cliques registrados dentro de 7 dias após o envio de uma mensagem para direcionar a entrega para combinações de conteúdo com melhor desempenho.

| Evento | Descrição | Casos de uso |
| --- | --- | --- |
| Aberturas | Otimiza para combinações que levam os destinatários a abrir o e-mail. | Testar linhas de assunto ou aumentar a visibilidade |
| Cliques | Otimiza para combinações que geram engajamento com links. Não inclui cliques de bots ou cliques de cancelamento de inscrição reconhecidos pela Braze. | Gerar tráfego, engajamento ou conversão a partir de links |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 5: Selecionar evento de otimização" }

{% endtab %}
{% tab Notificações por push %}

Para notificações por push, você pode otimizar **Aberturas**. Isso otimiza combinações que levam os destinatários a abrir a notificação por push. Você pode usar este evento de otimização para testar variações no título ou no texto da mensagem.

{% endtab %}
{% tab SMS/MMS/RCS %}

Para mensagens SMS e MMS, você pode otimizar **Cliques**. Para mensagens RCS, você pode otimizar **Leituras** ou **Cliques**.

Para que a etapa tenha um evento para otimizar:
- Mensagens SMS e MMS devem conter um link.
- Mensagens RCS devem conter um link ou uma resposta sugerida.

{% alert note %}
No momento, o envio de mensagens RCS com o Otimizador de Conteúdo não suporta fallbacks de SMS.
{% endalert %}
{% endtab %}
{% endtabs %}

## Editar uma etapa lançada {#edit-a-launched-step}

Após o lançamento do seu Canvas, você pode atualizar uma etapa do Otimizador de Conteúdo em execução abrindo-a no editor de Canvas. Você pode:

- Adicionar novas variantes a qualquer componente existente, manualmente ou usando sugestões geradas por IA, até o limite de cinco variantes por componente.
- Desativar variantes para parar de enviá-las aos usuários.
- Reativar variantes previamente desativadas, desde que isso mantenha o componente dentro do limite de cinco variantes.

Quando você publica as alterações, o otimizador é reiniciado e começa a redistribuir o tráfego do zero entre todas as variantes e combinações ativas. Os dados históricos anteriores à edição são mantidos e podem ser visualizados na guia **Análise de conteúdo**.

As seguintes configurações não podem ser alteradas após o lançamento:

- O conteúdo de variantes ativas existentes
- Quais componentes estão sendo testados
- O evento de otimização

Para etapas de SMS/MMS/RCS, o grupo de inscrições e o tipo de mensagem também não podem ser alterados após o lançamento.

## Práticas recomendadas {#best-practices}

- Em geral, recomendamos testar mais componentes em vez de menos na etapa do Otimizador de Conteúdo. Por exemplo, em vez de testar dois componentes para e-mail, teste três.
- Teste pelo menos 10 combinações no total para obter melhores resultados.
- Se você está otimizando para cliques, inclua linhas de assunto nos seus testes, pois linhas de assunto mais fortes podem contribuir para mais aberturas e criar mais oportunidades de cliques.
- Se você está otimizando para aberturas, mantenha seus testes focados na linha de assunto.
- Se esta é a primeira vez que você usa o Otimizador de Conteúdo, considere usar uma etapa de [Jornadas do experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que apenas parte do seu público entre no ramo que contém a etapa do Otimizador de Conteúdo. Por exemplo, você pode enviar metade dos seus usuários por uma jornada com a etapa do Otimizador de Conteúdo e a outra metade por uma jornada de controle que envia a etapa Mensagem com o conteúdo habitual do seu negócio. Então, colete dados por 2 a 3 semanas e compare quaisquer indicadores-chave de desempenho (KPIs) ou contra-métricas antes de aumentar o tráfego para as jornadas com etapas do Otimizador de Conteúdo.
  - Para uma comparação eficaz um a um, recomendamos que sua etapa do Otimizador de Conteúdo contenha o conteúdo habitual do seu negócio como uma das variantes para cada componente.
- Antes de atualizar uma etapa em execução, aguarde até que os rankings de desempenho de todas as variantes dos componentes se estabilizem — ou seja, as mesmas variantes estejam consistentemente ganhando e perdendo por três a quatro dias seguidos. Isso normalmente leva cerca de sete dias, e um número maior de eventos de otimização produz um sinal mais forte e preciso.
- Evite atualizar cedo demais. Cada vez que você publica alterações, o otimizador é reiniciado. Se você atualizar antes que a etapa tenha tempo de identificar o que está funcionando, você impede que ela capitalize suas descobertas — e a etapa nunca tem a oportunidade de direcionar tráfego significativo para as combinações com melhor desempenho.
- Quando estiver pronto para atualizar, a abordagem recomendada é desativar variantes com baixo desempenho e adicionar novas que se baseiem nas características das suas melhores variantes.

## Considerações {#considerations}

- As configurações de múltiplos idiomas não são suportadas nas etapas do Otimizador de Conteúdo. Em vez disso, recomendamos usar uma etapa do Otimizador de Conteúdo por idioma e ramificar as jornadas individualmente.
- As Liquid tags para componentes do Otimizador de Conteúdo não são suportadas em etapas Mensagem, então o Liquid é abortado em etapas Mensagem.
- Após uma etapa do Otimizador de Conteúdo ser lançada, você não pode alterar quais componentes estão sendo testados, o conteúdo de variantes ativas existentes ou o evento de otimização. Para etapas de SMS/MMS/RCS, o grupo de inscrições e o tipo de mensagem também não podem ser alterados.

## Análise de dados {#analytics}

Para revisar o desempenho, abra o painel de análise de dados no nível da etapa para ver métricas por variante de conteúdo e desempenho geral das combinações. A etapa do Otimizador de Conteúdo usa a [mesma análise de dados da etapa Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#analytics).

Se você atualizou a etapa após o lançamento, o gráfico de alocação de envios marca quando cada edição de conteúdo ocorreu. Os dados de variantes desativadas são mantidos e permanecem visíveis no painel de análise de dados, para que você possa comparar o desempenho ao longo de toda a vida útil da etapa.

![Análise de dados do Otimizador de Conteúdo para três botões e a porcentagem de alocação de envios, que apresenta tendência de alta.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Desempenho por componente {#performance-by-component}

A seção **Desempenho por componente** exibe o desempenho de cada componente na etapa do Otimizador de Conteúdo. A coluna **Componente** corresponde ao componente de conteúdo que você está testando (por exemplo, **Subject line** ou **Primary CTA**). A coluna **Identificador** corresponde ao identificador dessa variante na guia **Configurações do Otimizador de Conteúdo**.

As aberturas e cliques únicos são capturados dentro de sete dias após o envio de uma mensagem. As colunas exibidas dependem do seu canal e do evento de otimização selecionado.

| Métrica | Descrição |
| --- | --- |
| Envios | O número de envios atribuídos a esta variante para esse componente nesta etapa, usando a mesma contagem de envios no nível da etapa que [*Envios*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends) na tabela [Desempenho por combinação](#performance-by-combination). |
| Aberturas | Quando esta coluna aparece para o seu canal, o número de aberturas **únicas** para esta variante dentro de sete dias após o envio. Consulte [*Aberturas únicas*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Taxa de abertura | Quando esta coluna aparece, a porcentagem de envios para esta variante que registraram pelo menos uma abertura única qualificada dentro de sete dias. |
| Cliques | O número de cliques **únicos** para esta variante dentro de sete dias após o envio. Consulte [*Total de cliques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks), [*Cliques únicos*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks) e [Etapa 5: Selecionar evento de otimização](#step-5-select-optimization-event). |
| Taxa de cliques | A porcentagem de envios para esta variante que registraram pelo menos um clique único qualificado dentro de sete dias, usando a mesma janela da etapa que a tabela [Desempenho por combinação](#performance-by-combination). Para saber mais, consulte [Por que a análise de dados da etapa difere da análise geral](#why-step-analytics-differ-from-general-analytics). |
| Leituras | Quando esta coluna aparece (por exemplo, para RCS quando você otimiza para leituras), conta quando um consumidor lê a mensagem com confirmações de leitura ativadas. Consulte [*Leituras*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads). |
| Taxa de leitura | A porcentagem de envios para esta variante que resultaram em uma leitura entre usuários com confirmações de leitura ativadas. Consulte [*Taxa de leitura*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de desempenho por componente" }

![Análise de desempenho por componente do Otimizador de Conteúdo com tabelas separadas por componente, listando envios, cliques e taxa de cliques para cada variante.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_component.png %})

### Desempenho por combinação {#performance-by-combination}

A seção **Desempenho por combinação** exibe o desempenho de cada combinação na etapa do Otimizador de Conteúdo. Combinações são a mistura de variantes que definem esta linha — uma variante selecionada de cada componente de conteúdo que você está testando (por exemplo, uma linha de assunto combinada com um CTA principal).

As aberturas e cliques únicos são capturados dentro de sete dias após o envio de uma mensagem. As colunas exibidas dependem do seu canal e do evento de otimização selecionado.

| Métrica | Descrição |
| --- | --- |
| Envios | O número total de mensagens enviadas a partir desta etapa usando esta combinação. A contagem segue o mesmo significado geral de [*Envios*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends), com escopo para cada combinação. |
| Aberturas | O número de aberturas únicas para esta combinação dentro de sete dias após o envio. Para saber como aberturas únicas são definidas para e-mail, consulte [*Aberturas únicas*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Taxa de abertura | A porcentagem de envios para esta combinação que registraram pelo menos uma abertura única qualificada dentro de sete dias. |
| Cliques | O número de cliques únicos para esta combinação dentro de sete dias após o envio. Para saber como a Braze define cliques por canal, consulte [*Total de cliques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks) e [*Cliques únicos*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks). |
| Taxa de cliques | A porcentagem de envios para esta combinação que registraram pelo menos um clique único qualificado dentro de sete dias. Como o Otimizador de Conteúdo usa as contagens deduplicadas de sete dias da etapa, essa taxa pode não corresponder às taxas de cliques na análise geral de Campaign. Para saber mais, consulte [Por que a análise de dados da etapa difere da análise geral](#why-step-analytics-differ-from-general-analytics). |
| [Leituras]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads) | Quando esta coluna aparece (por exemplo, para RCS quando você otimiza para leituras), conta quando um consumidor lê a mensagem com confirmações de leitura ativadas. |
| [Taxa de leitura]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate) | Quando esta coluna aparece, a porcentagem de envios para esta combinação que resultaram em uma leitura entre usuários com confirmações de leitura ativadas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de desempenho por combinação" }

![Tabela de análise de desempenho por combinação do Otimizador de Conteúdo com envios, cliques e taxa de cliques para cada combinação de conteúdo.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_combination.png %})

### Por que a análise de dados da etapa difere da análise geral {#why-step-analytics-differ-from-general-analytics}

Razões pelas quais a análise de dados na etapa do Otimizador de Conteúdo difere da seção **Analytics** incluem:

- Os envios de push são deduplicados para envios ao mesmo usuário em dispositivos diferentes.
- Em geral, cliques e aberturas são deduplicados para serem únicos por usuário.
- Apenas cliques e aberturas que ocorrem dentro de sete dias após o envio de uma mensagem são contabilizados na etapa do Otimizador de Conteúdo.

## Solução de problemas {#troubleshooting}

| Problema | Descrição | Solução |
| --- | --- | --- |
| Liquid tags ausentes | Se você adicionar um componente de conteúdo (como Subject ou CTA) mas não inserir a Liquid tag correspondente na sua mensagem base, você verá: <br>- Um aviso na guia **Configurações do Otimizador de Conteúdo** <br>- Um erro na guia **Canais de envio de mensagens** | Copie o trecho Liquid mostrado abaixo de cada componente na guia **Configurações do Otimizador de Conteúdo** e cole-o na parte apropriada da sua mensagem. |
| Liquid tags órfãs | Se você excluir um componente de conteúdo mas deixar sua Liquid tag na mensagem base, a mensagem pode não ser renderizada como esperado ao ser enviada. | Remova quaisquer tags `message_component` não utilizadas da sua mensagem base antes de lançar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Solução de problemas" }
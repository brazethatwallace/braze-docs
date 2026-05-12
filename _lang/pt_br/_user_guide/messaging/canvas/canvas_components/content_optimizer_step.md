---
nav_title: Otimizador de conteúdo
article_title: Etapa do agente Otimizador de conteúdo
alias: "/content_optimizer_step/"
page_order: 5
description: "A etapa do agente Otimizador de conteúdo permite configurar e testar múltiplas versões de componentes de conteúdo em uma única etapa. Ela ajuda você a experimentar variações de conteúdo e otimiza automaticamente em direção às combinações com melhor desempenho ao longo do tempo."
page_type: reference

---

# Etapa do agente Otimizador de conteúdo {#content-optimizer-agent-step}

> A etapa do agente Otimizador de conteúdo permite configurar e testar múltiplas versões de componentes de conteúdo em uma única etapa. Ela ajuda você a experimentar variações de conteúdo e otimiza automaticamente em direção às combinações com melhor desempenho ao longo do tempo. Para uma introdução, consulte [Otimizador de conteúdo]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
O Otimizador de conteúdo está atualmente em beta. Para começar, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Criando uma etapa do Otimizador de conteúdo {#creating-a-content-optimizer-step}

Para melhores resultados, use o agente Otimizador de conteúdo em Canvas onde os usuários entram na etapa gradualmente ao longo do tempo. Se todos os usuários entrarem na etapa de uma vez, o agente não terá tempo para aprender com os resultados iniciais.

### Etapa 1: Adicionar uma etapa {#step-1-add-a-step}

Arraste e solte o componente **Otimizador de conteúdo** da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Otimizador de conteúdo**.

### Etapa 2: Criar sua mensagem base {#step-2-create-your-base-message}

A mensagem base é o ponto de partida da sua etapa. As variantes de cada componente de conteúdo são inseridas dinamicamente com base nas combinações definidas na guia **Configurações do Otimizador de conteúdo**.

{% alert note %}
Durante o período beta, os canais suportados são e-mail e notificações por push.
{% endalert %}

{% tabs local %}
{% tab E-mail %}

Na guia **Canais de envio de mensagens**, selecione **E-mail** e crie sua mensagem de e-mail base. Consulte nossa seção dedicada de [E-mail]({{site.baseurl}}/user_guide/channels/email/) para obter ajuda.

O agente Otimizador de conteúdo usa as configurações de envio (como o domínio de e-mail e o endereço de resposta) especificadas nesta variante para enviar todas as mensagens. Você pode começar com um novo design ou selecionar um modelo existente para esta mensagem. Nesta etapa, considere quais componentes da mensagem você deseja otimizar. Você os define na [etapa 4](#step-4).

Os componentes suportados para otimização incluem:

- Assunto
- Cabeçalho do corpo
- Conteúdo do corpo
- CTA principal

{% endtab %}
{% tab Notificações por push %}

Na guia **Canais de envio de mensagens**, selecione **Notificações por push** e crie sua notificação por push base. Consulte nossa seção dedicada de [Push]({{site.baseurl}}/user_guide/channels/push/) para obter ajuda.

O agente Otimizador de conteúdo usa as plataformas de push selecionadas nesta variante para enviar todas as mensagens. Você pode começar com um novo design ou selecionar um modelo existente para esta mensagem. Nesta etapa, considere quais componentes da mensagem você deseja otimizar. Você os define na [etapa 4](#step-4).

Os componentes suportados para otimização incluem:

- Título
- Mensagem

{% endtab %}
{% endtabs %}

### Etapa 3: Especificar configurações de entrega {#step-3-specify-delivery-settings}

Na guia **Configurações de entrega**, você pode especificar se a etapa deve usar Intelligent Timing ou validações de entrega. Para mais detalhes, consulte [Editar configurações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) na etapa Mensagem.

### Etapa 4: Adicionar componentes de conteúdo e variantes {#step-4}

Componentes de conteúdo são os elementos individuais da sua mensagem que você deseja testar, como diferentes linhas de assunto ou títulos. Esses componentes permitem gerar múltiplas versões de uma mensagem e otimizar automaticamente com base no desempenho ao longo do tempo.

- **E-mail:** Você pode adicionar até três componentes de conteúdo por etapa e até cinco variantes por componente, totalizando 125 combinações únicas de conteúdo.
- **Notificações por push:** Você pode adicionar até dois componentes por etapa e até cinco variantes por componente, totalizando 25 combinações únicas de conteúdo.

![Opções para adicionar e configurar componentes de conteúdo na interface do Otimizador de conteúdo. A interface exibe componentes selecionáveis como Assunto, Cabeçalho do corpo, Conteúdo do corpo e CTA principal, cada um com campos para inserir diferentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Etapa 4.1: Configurar componentes de conteúdo {#step-41-configure-content-components}

Para configurar componentes, acesse a guia **Configurações do Otimizador de conteúdo**.

{% tabs local %}
{% tab E-mail %}

Escolha quais componentes você deseja otimizar para mensagens de e-mail. As opções suportadas são:

- Assunto
- Cabeçalho do corpo
- Conteúdo do corpo
- CTA principal

Para cada componente selecionado, defina um conjunto de versões alternativas desse conteúdo (variantes). Use variantes claras e distintas que difiram em tom, estrutura ou conteúdo. Isso ajuda o Otimizador de conteúdo a identificar os melhores desempenhos de forma mais eficaz. Você pode:
  - Escrever suas próprias variantes manualmente.
  - Usar sugestões geradas por IA para explorar novas opções rapidamente.

![Interface de Configurações do Otimizador de conteúdo mostrando opções para adicionar e configurar componentes de conteúdo para otimização de e-mail. Cada componente tem campos de entrada para inserir diferentes variantes. O texto visível inclui nomes de componentes e campos para inserir texto de variantes.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Notificações por push %}

Escolha quais componentes você deseja otimizar para notificações por push. As opções suportadas são:
- Título
- Mensagem

Para cada componente selecionado, defina um conjunto de versões alternativas desse conteúdo (variantes). Use variantes claras e distintas que difiram em tom, estrutura ou conteúdo. Isso ajuda o Otimizador de conteúdo a identificar os melhores desempenhos de forma mais eficaz. Você pode:
  - Escrever suas próprias variantes manualmente.
  - Usar sugestões geradas por IA para explorar novas opções rapidamente.

![Configurações do Otimizador de conteúdo mostrando opções para adicionar e configurar componentes de conteúdo para otimização de push.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% endtabs %}

#### Etapa 4.2: Adicionar Liquid à sua mensagem {#step-42-add-liquid-to-your-message}

Após definir pelo menos duas variantes para cada componente, copie a Liquid tag associada a cada um e cole-a no local correspondente na sua mensagem base.

- Por exemplo, se você está otimizando a linha de assunto, cole a tag {% raw %}`{% message_component "Subject" %}`{% endraw %} no campo de assunto do criador de e-mail.
- Você também pode incluir tags de componente dentro de textos mais longos para testar apenas uma parte do componente. Por exemplo: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Opções para adicionar e configurar componentes de conteúdo como Assunto, Cabeçalho do corpo, Conteúdo do corpo e CTA principal. Cada componente tem campos para inserir diferentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Se você não adicionar uma Liquid tag para um componente de conteúdo selecionado, verá um aviso na guia **Configurações do Otimizador de conteúdo** e um erro na guia **Canais de envio de mensagens**. O Canvas não pode ser lançado até que todos os componentes selecionados sejam adicionados corretamente à sua mensagem base.

Conforme o Canvas é executado, o agente combina e alterna variantes entre componentes para gerar diferentes combinações de conteúdo. Com o tempo, as combinações com melhor desempenho são priorizadas para entrega, ajudando você a melhorar o desempenho sem intervenção manual.

#### Referências de Liquid {#liquid-references}

| Canal | Componente | Trecho Liquid |
| --- | --- | --- |
| E-mail | Assunto | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| E-mail | Cabeçalho do corpo | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| E-mail | Conteúdo do corpo | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| E-mail | CTA principal | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| Push | Título | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| Push | Mensagem | {% raw %}`{% message_component "Message" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Referências de Liquid" }

### Etapa 5: Selecionar evento de otimização {#step-5-select-optimization-event}

O evento de otimização determina como o agente Otimizador de conteúdo avalia o desempenho e distribui o tráfego para as combinações de conteúdo ao longo do tempo.

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
{% endtabs %}

## Práticas recomendadas {#best-practices}

- Em geral, recomendamos testar mais de um componente na etapa do Otimizador de conteúdo.
- Se você está otimizando para cliques, inclua linhas de assunto nos seus testes, pois linhas de assunto mais fortes podem contribuir para mais aberturas e criar mais oportunidades de cliques.
- Se você está otimizando para aberturas, mantenha seus testes focados na linha de assunto.

## Análise de dados {#analytics}

Para revisar o desempenho, abra o painel de análise de dados no nível da etapa para ver métricas por variante de conteúdo e desempenho geral das combinações. A etapa do Otimizador de conteúdo usa a [mesma análise de dados da etapa Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#analytics).

![Análise de dados do Otimizador de conteúdo para três botões e a porcentagem de alocação de envios, que apresenta tendência de alta.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Por que a análise de dados da etapa difere da análise geral {#why-step-analytics-differ-from-general-analytics}

Razões pelas quais a análise de dados na etapa do Otimizador de conteúdo difere da seção **Analytics** incluem:

- Os envios de push são deduplicados para envios ao mesmo usuário em dispositivos diferentes.
- Em geral, cliques e aberturas são deduplicados para serem únicos por usuário.
- Apenas cliques e aberturas que ocorrem dentro de sete dias após o envio de uma mensagem são contabilizados na etapa do Otimizador de conteúdo.

## Solução de problemas {#troubleshooting}

| Problema | Descrição | Solução |
| --- | --- | --- |
| Liquid tags ausentes | Se você adicionar um componente de conteúdo (como Assunto ou CTA) mas não inserir a Liquid tag correspondente na sua mensagem base, você verá: <br>- Um aviso na guia **Configurações do Otimizador de conteúdo** <br>- Um erro na guia **Canais de envio de mensagens** | Copie o trecho Liquid mostrado abaixo de cada componente na guia **Configurações do Otimizador de conteúdo** e cole-o na parte apropriada da sua mensagem. |
| Liquid tags órfãs | Se você excluir um componente de conteúdo mas deixar sua Liquid tag na mensagem base, a mensagem pode não ser renderizada como esperado ao ser enviada. | Remova quaisquer tags `message_component` não utilizadas da sua mensagem base antes de lançar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Solução de problemas" }
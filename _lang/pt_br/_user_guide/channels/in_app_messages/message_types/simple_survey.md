---
nav_title: "Pesquisa simples"
article_title: Mensagem no app de pesquisa simples
page_order: 6
page_type: reference
description: "Este artigo de referência aborda como coletar atributos de usuário, insights e preferências para impulsionar sua estratégia de Campaign usando pesquisas de mensagem no app."
channel:
  - in-app messages
tool:
  - Templates
---

# Pesquisa simples {#simple-survey}

> Use o modelo de mensagem no app **Simple Survey** para coletar atributos de usuário, insights e preferências que impulsionam sua estratégia de Campaign.

Esse tipo de mensagem está disponível no [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

Casos de uso comuns de pesquisa incluem perguntar aos usuários como gostariam de usar seu app, saber mais sobre suas preferências pessoais ou perguntar sobre a satisfação com um recurso específico.

![Três mensagens de pesquisa simples: preferências de notificação, preferências alimentares e uma pesquisa de satisfação do cliente. As opções selecionadas nas pesquisas correspondem a atributos personalizados que serão registrados para aquele usuário.]({% image_buster /assets/img/iam/iam-survey.png %})

## Requisitos do SDK or kit de desenvolvimento de software {#supported-sdk-versions}

Essa mensagem no app só será entregue a dispositivos que suportem [Flex CSS](https://caniuse.com/flexbox) e deve ter pelo menos as seguintes [versões do SDK or kit de desenvolvimento de software]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Para ativar mensagens no app em HTML pelo SDK or kit de desenvolvimento de software Web, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` à Braze.
{% endalert %}

## Criando uma pesquisa {#create}

Ao criar uma [mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional), selecione **Simple Survey** como seu **Message Type**.

Esse modelo de pesquisa é compatível com apps mobile e navegadores web. Lembre-se de verificar se seus SDKs estão nas [versões mínimas do SDK or kit de desenvolvimento de software](#supported-sdk-versions) necessárias para esse recurso.

### Etapa 1: Adicione sua pergunta da pesquisa {#step-1-add-your-survey-question}

Para começar a criar sua pesquisa, adicione sua pergunta no campo **Header** da pesquisa. Se desejar, você pode adicionar uma mensagem opcional no **Body** que aparecerá abaixo da sua pergunta.

![Guia Redigir do editor de pesquisa simples, com campos para cabeçalho, corpo opcional e texto auxiliar opcional.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
Esses campos podem incluir tanto Liquid quanto emojis, então capriche!
{% endalert %}

### Etapa 2: Configure as opções {#single-multiple-choice}

Você pode adicionar até 12 opções em uma pesquisa.

Selecione **Single-choice selection** ou **Multiple-choice selection**. O **Helper text** será atualizado automaticamente quando você alternar entre as duas opções para informar aos usuários quantas opções eles podem selecionar.

Em seguida, determine se você vai [coletar atributos personalizados](#custom-attributes) ou [registrar apenas as respostas](#no-attributes).

![Menu suspenso de opções com "Log attributes upon submission" selecionado.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Coletar atributos personalizados {#custom-attributes}

Selecione **Log attributes upon submission** para coletar atributos com base na resposta do usuário. Você pode usar essa opção para criar novos segmentos e Campaigns de redirecionamento. Por exemplo, em uma [pesquisa de satisfação](#user-satisfaction), você poderia enviar um e-mail de acompanhamento para todos os usuários que não ficaram satisfeitos.

Para adicionar um atributo personalizado a cada opção, selecione um nome de atributo personalizado no menu suspenso (ou crie um novo) e insira o valor a ser definido quando essa opção for enviada. Você também pode criar um novo atributo personalizado na sua [página de configurações]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data).

O tipo de dados dos seus atributos personalizados é importante dependendo de como você configurou sua pesquisa.

- **Seleção de múltipla escolha:** O tipo de dados do atributo personalizado deve ser um array. Se o atributo personalizado estiver definido com um tipo de dados diferente, as respostas não serão registradas.
- **Seleção de escolha única:** O tipo de dados do atributo personalizado deve ser uma string. Atributos personalizados que não são do tipo string não aparecerão no menu suspenso, e as respostas não serão registradas.

{% alert important %}
Quando a coleta de atributos personalizados está ativada, opções que compartilham o mesmo nome de atributo personalizado serão combinadas em um array.
{% endalert %}

##### Exemplo {#example}

Por exemplo, em uma [pesquisa de preferências de notificação](#notification-preferences), você pode tornar cada opção um atributo booleano (verdadeiro/falso) para permitir que os usuários selecionem quais tópicos lhes interessam. Se um usuário marcar a opção "Promoções", isso atualizará seu [perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) com o atributo personalizado `Promotions Topic` definido como `true`. Se ele deixar a opção desmarcada, esse mesmo atributo permanecerá inalterado.

Você pode então usar o filtro `Custom Attribute` para criar um Segment or segmento para usuários com o atributo personalizado `Promotions Topic` `is` `true` para garantir que apenas os usuários interessados em suas promoções recebam as Campaigns relevantes.

#### Registrar apenas as respostas {#no-attributes}

Alternativamente, você pode escolher **Log responses only (no attributes)**. Quando essa opção é selecionada, as respostas da pesquisa são registradas como cliques em botões, mas os atributos personalizados não são registrados no perfil do usuário. Isso significa que você ainda pode visualizar as métricas de clique para cada opção da pesquisa (veja [Análise de dados](#analytics)), mas essa escolha não será refletida no perfil do usuário.

Essas métricas de clique não estão disponíveis para redirecionamento.

### Etapa 4: Escolha o comportamento de envio {#step-4-choose-submission-behavior}

Depois que um usuário enviar sua resposta, você pode opcionalmente exibir uma página de confirmação ou simplesmente fechar a mensagem.

Uma página de confirmação é um ótimo lugar para agradecer aos usuários pelo tempo dedicado ou fornecer informações adicionais. Você pode personalizar a chamada para ação nessa página para direcionar os usuários a outra página do seu app ou website.

{% alert note %}
Ao usar uma página de confirmação, o campo **Header** é obrigatório. Se você vir a mensagem "Composer has validation errors" ao tentar salvar sua Campaign, adicione um cabeçalho à sua página de confirmação.
{% endalert %}

Edite o texto do botão e o comportamento ao clicar na seção **Submit Button** na parte inferior da guia **Survey**:

![Comportamento ao clicar definido como "Submit responses and display confirmation page".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Se você optar por adicionar uma página de confirmação, mude para a guia **Confirmation Page** para personalizar sua mensagem:

![Guia Confirmation Page do editor de pesquisa simples. Os campos disponíveis são cabeçalho, corpo opcional, texto do botão e comportamento ao clicar do botão.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

Se você quiser direcionar os usuários a outra página do seu app ou website, altere o **On-click behavior** do botão.

### Etapa 5: Estilize sua mensagem (opcional) {#styling}

Você pode personalizar a cor da fonte e a cor de destaque da mensagem usando o seletor **Color Theme**.

![Guia Redigir do editor de pesquisa simples com o seletor Color Theme expandido após o usuário clicar na paleta de cores.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analisar resultados {#analytics}

Depois que sua Campaign for lançada, você pode analisar os resultados em tempo real para ver o detalhamento de cada opção selecionada. Se você ativou a [coleta de atributos personalizados](#custom-attributes), também poderá criar novos segmentos ou Campaigns de acompanhamento para os usuários que responderam à pesquisa.

{% alert note %}
Opções de pesquisa excluídas ainda aparecerão na análise de dados, mas não serão exibidas como opção para novos usuários.
{% endalert %}

Você pode encontrar as métricas de desempenho da sua pesquisa expandindo o menu suspenso **Results** para uma variante específica na seção **In-App Message Performance** da análise de dados. Veja o que você encontrará:

- **Engajamento da pesquisa** mostra como os usuários interagiram com a pesquisa de forma geral, incluindo total de envios, dispensas e cliques no corpo da mensagem.
- **Resultados da pesquisa** exibem um detalhamento de quantos usuários selecionaram cada opção de resposta, junto com a porcentagem do total de envios que cada opção representa.
- **Métricas da página de confirmação** (se ativada) incluem quantos usuários visualizaram a tela de confirmação, clicaram no botão ou dispensaram sem interagir.

Para definições das métricas de pesquisa, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary) e filtre por "In-App Message".

Confira [Relatórios de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) para um detalhamento das métricas da sua Campaign.

### Currents {#currents}

As opções selecionadas fluirão automaticamente para o Currents, no campo `button_id` de [**In-App Message Click Events**]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#in-app-message-click-events). Cada opção será enviada com seu identificador universalmente único (UUID).

## Casos de uso {#use-cases}

{% tabs %}
{% tab Satisfação do usuário %}

### Satisfação do usuário {#user-satisfaction}

**Objetivo:** Medir a satisfação do cliente e enviar campanhas de recuperação para usuários que deixaram pontuações baixas.

Para configurar isso, use uma pesquisa de seleção de escolha única com cinco opções, variando de "😡 Muito Insatisfeito" a "😍 Muito Satisfeito". Cada escolha é mapeada para o atributo personalizado `customer_satisfaction`, com um valor numérico de 1 a 5, em que 1 indica o menos satisfeito e 5 o mais satisfeito. Esses valores numéricos são armazenados como strings, já que atributos personalizados do tipo string são obrigatórios para seleção de escolha única.

| Escolha                                    | Atributo               | Valor |
|--------------------------------------------|------------------------|-------|
| 😡 Muito Insatisfeito                      | `customer_satisfaction` | 1     |
| 😟 Insatisfeito                            | `customer_satisfaction` | 2     |
| 🙂 Nem Satisfeito nem Insatisfeito        | `customer_satisfaction` | 3     |
| 😊 Satisfeito                              | `customer_satisfaction` | 4     |
| 😍 Muito Satisfeito                        | `customer_satisfaction` | 5     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Satisfação do usuário" }

Quando um usuário envia a pesquisa, o valor selecionado é registrado como um atributo personalizado. Você pode então criar campanhas de acompanhamento usando filtros de público. Por exemplo, direcione mensagens de recuperação para usuários cujo atributo `customer_satisfaction` seja "1" ou "2".

{% endtab %}
{% tab Preferências de notificação %}

### Preferências de notificação {#notification-preferences}

**Objetivo:** Permitir que os usuários optem por tipos específicos de notificações.

Para configurar isso, use uma pesquisa de seleção de múltipla escolha em que cada opção representa um tópico de notificação. Em vez de atribuir o mesmo atributo com valores diferentes, cada escolha é mapeada para um atributo booleano distinto que reflete o interesse do usuário naquele tópico. Se um usuário selecionar uma escolha, o atributo correspondente é definido como `true`. Se não for selecionado, o atributo permanece inalterado.

| Escolha                  | Atributo               | Valor  |
|--------------------------|------------------------|--------|
| Atualizações de produto  | `wants_product_updates`| `true` |
| Promoções                | `wants_promotions`     | `true` |
| Convites para eventos    | `wants_event_invites`  | `true` |
| Pesquisas e feedback     | `wants_surveys`        | `true` |
| Dicas e tutoriais        | `wants_tips`           | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Preferências de notificação" }

{% endtab %}
{% tab Identificar objetivos do cliente %}

### Identificar objetivos do cliente {#identify-customer-goals}

**Objetivo:** Identificar os principais motivos pelos quais os usuários visitam seu app.

Para configurar isso, use uma pesquisa de seleção de escolha única com cada opção representando um objetivo ou intenção comum. Cada escolha é mapeada para o atributo personalizado `product_goal` com um valor correspondente à intenção do usuário selecionada.

| Escolha                    | Atributo         | Valor     |
|----------------------------|------------------|-----------|
| Verificar status           | `product_goal`   | `status`  |
| Fazer upgrade da conta     | `product_goal`   | `upgrade` |
| Agendar um compromisso     | `product_goal`   | `schedule`|
| Suporte ao cliente         | `product_goal`   | `support` |
| Apenas navegando           | `product_goal`   | `browse`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Identificar objetivos do cliente" }

Quando um usuário envia a pesquisa, o valor selecionado é registrado como um atributo personalizado no perfil dele. Você pode então usar esses dados para personalizar experiências futuras ou segmentar usuários com base no objetivo principal deles.

{% endtab %}
{% tab Melhorar taxas de conversão %}

### Melhorar taxas de conversão {#improve-conversion-rates}

**Objetivo:** Entender por que os clientes não estão fazendo upgrade ou comprando.

Para configurar isso, use uma pesquisa de seleção de escolha única com cada opção representando uma barreira comum para fazer upgrade. Cada escolha é mapeada para o atributo personalizado `upgrade_reason` com um valor correspondente que reflete a seleção do usuário.

| Escolha                  | Atributo         | Valor       |
|--------------------------|------------------|-------------|
| Muito caro               | `upgrade_reason` | `expensive` |
| Sem valor                | `upgrade_reason` | `value`     |
| Difícil de usar          | `upgrade_reason` | `difficult` |
| Usando um concorrente    | `upgrade_reason` | `competitor`|
| Outro motivo             | `upgrade_reason` | `other`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Melhorar taxas de conversão" }

Quando um usuário envia a pesquisa, o valor selecionado é salvo no perfil dele. Você pode então direcionar esses usuários com campanhas adaptadas à objeção específica deles, como ofertas de desconto ou melhorias de usabilidade.

{% endtab %}
{% tab Recursos favoritos %}

### Recursos favoritos {#favorite-features}

**Objetivo:** Entender quais recursos os clientes gostam de usar.

Para configurar isso, use uma pesquisa de seleção de múltipla escolha em que cada opção representa um recurso do seu app. Cada escolha é mapeada para o atributo personalizado `favorite_features` e, quando o usuário envia a pesquisa, o atributo é definido como um array dos valores selecionados.

| Escolha              | Atributo           | Valor        |
|----------------------|--------------------|--------------|
| Favoritos            | `favorite_features`| `bookmarks`  |
| App móvel            | `favorite_features`| `mobile`     |
| Compartilhar posts   | `favorite_features`| `sharing`    |
| Suporte ao cliente   | `favorite_features`| `support`    |
| Personalização       | `favorite_features`| `custom`     |
| Preço / Valor        | `favorite_features`| `value`      |
| Comunidade           | `favorite_features`| `community`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Recursos favoritos" }

Como essa pesquisa usa seleção de múltipla escolha, o perfil do usuário será atualizado com uma lista de todos os valores de recursos selecionados.

{% endtab %}
{% endtabs %}
---
nav_title: Eventos de conversão
article_title: Eventos de conversão
page_order: 3
page_type: reference
description: "Este artigo de referência define eventos de conversão, como usá-los para definir suas métricas de sucesso na Braze e como usar esses eventos para ver o nível de engajamento dos seus usuários."
tool:
    - Campaigns
    - Canvas
---

# Eventos de conversão {#conversion-events}

> Um evento de conversão é um tipo de métrica de sucesso que rastreia se um destinatário das suas mensagens realiza uma ação de alto valor em um período definido após receber seu engajamento. Use esses eventos para garantir que você está coletando informações relevantes e úteis que poderá usar posteriormente para obter insights sobre sua Campaign ou Canvas.

## Como funciona {#how-it-works}

Para uma Campaign personalizada de feriado direcionada a usuários ativos, um evento de conversão de **Iniciar uma sessão** dentro de dois ou três dias pode ser apropriado, pois permite que você tenha uma noção do engajamento do usuário ao receber sua mensagem. Você também pode selecionar eventos adicionais como **Realiza pedido**, **Faz upgrade do app** ou qualquer um dos seus eventos personalizados como eventos de conversão.

### Quando o rastreamento de conversão começa? {#when-does-conversion-tracking-begin}

{% tabs %}
{% tab Campaign %}

O rastreamento de conversão começa quando um usuário recebe a Campaign ou entra no grupo de controle da Campaign. Receber uma mensagem e ser atribuído a uma variante geralmente acontecem ao mesmo tempo. Para Campaigns de mensagem no app, o rastreamento de conversão começa quando a Braze registra uma impressão.

{% endtab %}
{% tab Canvas %}

O rastreamento de conversão começa quando um usuário entra no Canvas. Para etapas do Canvas, as conversões são atribuídas enquanto o usuário está ativo naquela etapa. Quando o usuário avança para outra etapa, o rastreamento de conversão para a etapa anterior é interrompido e começa para a próxima etapa.

Enquanto um usuário está em uma etapa de postergação ou outra etapa sem mensagem, as conversões que ocorrem durante essa espera ainda são atribuídas à última etapa de mensagem recebida até que o usuário receba outra etapa de mensagem. Após o usuário receber a última etapa de mensagem em sua jornada, as conversões ainda podem ser registradas até o prazo de conversão (contado a partir da entrada no Canvas), mesmo que não haja mais etapas de mensagem.

{% endtab %}
{% endtabs %}

{% alert tip %}
Para saber mais sobre conversões, confira nosso [curso do Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuração de Campaigns.
{% endalert %}

### Regras de rastreamento de conversão {#conversion-tracking-rules}

Os eventos de conversão atribuem ações do usuário a um ponto de engajamento. De modo geral, enquanto uma janela de conversão está aberta, um usuário converte no máximo uma vez por evento de conversão para aquela Campaign ou Canvas. Se ele realizar a mesma ação de conversão mais de uma vez antes do prazo (por exemplo, duas compras), a Braze ainda conta apenas uma conversão para aquele evento. Campaigns multicanal podem registrar uma oportunidade de conversão separada para cada canal de envio de mensagens, o que pode produzir taxas de conversão acima de 100% quando você compara contagens de conversão com destinatários únicos (veja abaixo).

Observe o seguinte sobre como a Braze lida com múltiplas conversões:

- **Campaigns de canal único**: As conversões ocorrem por usuário, não por dispositivo. Dentro de um único canal, um usuário converte apenas uma vez por evento de conversão, mesmo que uma mensagem seja enviada para vários dispositivos. Por exemplo, se uma Campaign tem apenas um evento de conversão definido como "Realiza qualquer compra" e um usuário faz duas compras separadas dentro do prazo de conversão, a Braze conta apenas uma conversão.
- **Campaigns multicanal**: Para Campaigns multicanal, cada canal tem sua própria oportunidade de conversão. Um usuário pode converter uma vez por canal após receber uma mensagem naquele canal. Isso significa que, se um usuário receber mensagens em vários canais (por exemplo, e-mail e push) e realizar a ação de conversão, a Braze conta uma conversão para cada canal, o que pode resultar em taxas de conversão superiores a 100%.
- **Etapas de mensagem do Canvas**: A Braze atribui conversões que ocorrem dentro do prazo de conversão à última etapa de mensagem do Canvas que o usuário recebeu. Após receber a próxima etapa de mensagem, a atribuição passa para essa etapa. A Braze mede esse período a partir de quando o usuário entra no Canvas, não a partir de cada mensagem individualmente. Conversões que acontecem durante postergações entre etapas de mensagem contam para a atribuição da etapa de mensagem anterior até que o usuário avance; conversões após a última etapa de mensagem ainda contam até o prazo de conversão do Canvas.
- Se um usuário realizar um evento de conversão dentro dos prazos de conversão de duas Campaigns ou Canvas separados que recebeu, a conversão é registrada em ambos.
- Um usuário é contado como convertido se realizou o evento de conversão específico dentro do período, mesmo que não tenha aberto ou clicado na mensagem.

### Evento de conversão primária {#primary-conversion-event}

O evento de conversão primária é o primeiro evento que você adiciona durante a criação da Campaign ou Canvas. Esse evento tem o maior impacto no seu engajamento e relatórios. A Braze usa seu evento de conversão primária para:

- Calcular a variante de mensagem vencedora em Campaigns ou Canvas [multivariantes]({{site.baseurl}}/user_guide/messaging/ab_testing#multivariate-and-ab-testing).
- Determinar o período em que a receita é calculada para a Campaign ou Canvas.
- Ajustar as distribuições de mensagens para Campaigns e Canvas usando a [Seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection).

A contagem do evento de conversão primária é o número de eventos de conversão que ocorreram. Para Campaigns multicanal, a Braze conta conversões por canal (conforme descrito em [Regras de rastreamento de conversão](#conversion-tracking-rules)), o que significa que a contagem de conversões pode exceder o número de usuários únicos e resultar em taxas de conversão superiores a 100%. A Braze calcula a taxa do evento de conversão primária dividindo essa contagem pelo número de destinatários únicos. A Braze considera um usuário como destinatário quando a mensagem é enviada ou exibida, dependendo do canal. Por exemplo, em push ou e-mail, um usuário se torna destinatário após a Braze enviar a mensagem. Para mensagens no app ou Content Cards, o usuário precisa visualizar a mensagem para ser considerado destinatário.

{% alert note %}
Se você abortar mensagens usando a tag Liquid `abort`, a Braze aborta mensagens apenas para usuários que passam por variantes. Mensagens para usuários no grupo de controle não são abortadas, o que pode levar a porcentagens de conversão distorcidas entre variantes e grupos de controle. Como alternativa, use a [segmentação]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para direcionar seus usuários na entrada da Campaign e do Canvas.
{% endalert %}

## Criando uma Campaign com rastreamento de conversão {#creating-a-campaign-with-conversion-tracking}

### Etapa 1: Configure sua Campaign {#step-1-set-up-your-campaign}

[Crie uma Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign) para o canal de envio de mensagens desejado. Após configurar as mensagens e a programação da sua Campaign, você pode adicionar até quatro eventos de conversão para rastreamento.

Use quantos eventos de conversão forem necessários. Adicionar um segundo ou terceiro evento de conversão enriquece significativamente seus relatórios. Por exemplo, para uma Campaign direcionada a usuários inativos, adicionar um evento de conversão secundário junto com o evento de conversão primária **Inicia sessão** ajuda a entender a eficácia da sua Campaign em trazer os usuários de volta ao seu aplicativo.

### Etapa 2: Adicione os eventos de conversão {#step-2-add-the-conversion-events}

Primeiro, selecione o tipo geral de evento que você deseja usar:

| Tipo de evento de conversão | Descrição |
|-------------------------|----------------------------|
| **Inicia sessão** | Um usuário é contado como convertido quando abre qualquer um dos apps que você especificar (o padrão é todos os apps no espaço de trabalho). |
| **Realiza compra** | Um usuário é contado como convertido quando registra um [evento de compra]({{site.baseurl}}/api/objects_filters/purchase_object). Isso rastreia qualquer compra por padrão, ou você pode especificar um produto específico. |
| **Realiza pedido** | Um usuário é contado como convertido quando aciona o [evento recomendado de eCommerce Pedido realizado]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#ecommerce-recommended-events?tab=ecommerce.order_placed). Isso rastreia qualquer pedido por padrão, ou você pode filtrar por um produto específico.<br><br>O evento "Realiza pedido" está atualmente em acesso antecipado. Entre em contato com seu gerente de conta da Braze se tiver interesse em participar deste acesso antecipado. |
| **Realiza evento personalizado** | Um usuário é contado como convertido quando realiza um dos seus eventos personalizados existentes (sem padrão, você deve especificar o evento). |
| **Faz upgrade do app** | Um usuário é contado como convertido quando faz upgrade da versão do app em qualquer um dos apps que você especificar (o padrão é todos os apps no espaço de trabalho). A Braze realiza uma comparação numérica de melhor esforço para determinar se a alteração foi um upgrade. Versões não numéricas são contadas como conversões se a versão mudar. |
| **Abre e-mail** | Um usuário é contado como convertido quando abre o e-mail (apenas para Campaigns de e-mail). |
| **Clica no e-mail** | Um usuário é contado como convertido quando clica em um link dentro do e-mail (apenas para Campaigns de e-mail). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Adicione os eventos de conversão" }

{% alert important %}
**Propriedades aninhadas não são suportadas em eventos de conversão**. Você não pode usar propriedades aninhadas em eventos de conversão. Por exemplo, se `product_code` ou `product_name` são propriedades aninhadas dentro de um array `products` (como `products[].product_code`), você não pode usá-las para verificar se uma compra de produto específico foi realizada em um evento de conversão.
{% endalert %}

Defina seu prazo de conversão. Este é o tempo máximo que pode passar antes que a Braze considere uma conversão. Você pode definir um período de até 30 dias durante o qual a Braze conta a conversão se o usuário realizar a ação especificada.

![O tipo de evento de conversão "Realiza compra" como exemplo para registrar conversões de usuários que realizam qualquer compra. Este tem um prazo de conversão de 12 horas.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Após selecionar seus eventos de conversão, continue o processo de criação da Campaign e comece a enviá-la.

### Etapa 3: Visualize seus resultados {#step-3-view-your-results}

Acesse a página **Informações** para ver os detalhes de cada evento de conversão associado à Campaign que você criou. Independentemente dos eventos de conversão selecionados, você também pode ver a receita total atribuída a essa Campaign específica, bem como variantes específicas, durante o período do evento de conversão primária.

{% alert note %}
Se você não selecionar nenhum evento de conversão durante a criação da Campaign, o tempo padrão será de três dias.
{% endalert %}

Além disso, para mensagens multivariantes, você pode ver o número de conversões e as porcentagens de conversão para seu grupo de controle e cada variante.

![Quatro eventos de conversão que rastreiam conversões com base em quando uma compra foi realizada dentro de três horas, realizou uma compra dentro de duas horas, iniciou uma sessão dentro de 30 minutos e iniciou uma sessão dentro de 25 minutos.]({% image_buster /assets/img_archive/conversion_event_details.png %})
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

Para uma campanha de feriado personalizada direcionada a usuários ativos, um evento de conversão de **Iniciar uma Sessão** dentro de dois ou três dias pode ser apropriado, pois permite que você tenha uma noção do engajamento do usuário ao receber sua mensagem. Você também pode selecionar eventos adicionais como **Fazer Pedido**, **Fazer Upgrade do App** ou qualquer um dos seus eventos personalizados como eventos de conversão.

### Quando o rastreamento de conversão começa? {#when-does-conversion-tracking-begin}

{% tabs %}
{% tab Campaign %}

O rastreamento de conversão começa quando um usuário recebe a Campaign ou entra no grupo de controle da Campaign. O recebimento de uma mensagem e a atribuição a uma variante geralmente acontecem ao mesmo tempo. Para Campaigns de mensagem no app, o rastreamento de conversão começa quando a Braze registra uma impressão.

{% endtab %}
{% tab Canvas %}

O rastreamento de conversão começa quando um usuário entra no Canvas. Para etapas do Canvas, as conversões são atribuídas enquanto o usuário está ativo naquela etapa. Quando o usuário avança para outra etapa, o rastreamento de conversão para a etapa anterior é interrompido e começa para a próxima etapa.

Enquanto um usuário está em uma etapa de Postergação ou outra etapa sem mensagem, as conversões que ocorrem durante essa espera ainda são atribuídas à última etapa de mensagem recebida, até que o usuário receba outra etapa de mensagem. Depois que o usuário recebe a última etapa de mensagem em sua jornada, as conversões ainda podem ser registradas até o prazo de conversão (contado a partir da entrada no Canvas), mesmo que não haja mais etapas de mensagem.

{% endtab %}
{% endtabs %}

{% alert tip %}
Para saber mais sobre conversões, confira nosso [curso do Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuração de Campaigns.
{% endalert %}

### Regras de rastreamento de conversão {#conversion-tracking-rules}

Os eventos de conversão atribuem ações do usuário a um ponto de engajamento. De modo geral, enquanto uma janela de conversão está aberta, um usuário converte no máximo uma vez por evento de conversão para aquela Campaign ou Canvas. Se ele realizar a mesma ação de conversão mais de uma vez antes do prazo (por exemplo, duas compras), a Braze ainda conta apenas uma conversão para aquele evento. Campaigns multicanal podem registrar uma oportunidade de conversão separada para cada canal de envio de mensagens, o que pode produzir taxas de conversão superiores a 100% quando você compara contagens de conversão com destinatários únicos (conforme descrito nos itens a seguir).

Observe o seguinte sobre como a Braze lida com múltiplas conversões:

- **Campaigns de canal único:** As conversões ocorrem por usuário, não por dispositivo. Dentro de um único canal, um usuário converte apenas uma vez por evento de conversão, mesmo que uma mensagem seja enviada para vários dispositivos. Por exemplo, se uma Campaign tem apenas um evento de conversão definido como "Faz qualquer compra" e um usuário faz duas compras separadas dentro do prazo de conversão, a Braze conta apenas uma conversão. No entanto, quando a [reelegibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) está ativada, os usuários que receberem a Campaign várias vezes podem converter novamente a cada envio. Em Campaigns com reelegibilidade, o mecanismo de conversão é uma vez por usuário por envio de Campaign, o que pode resultar em contagens de conversão mais altas quando os usuários recebem e convertem a partir da mesma Campaign várias vezes.
- **Campaigns multicanal:** Para Campaigns multicanal, cada canal tem sua própria oportunidade de conversão. Um usuário pode converter uma vez por canal após receber uma mensagem naquele canal. Isso significa que, se um usuário recebe mensagens em vários canais (por exemplo, e-mail e push) e realiza a ação de conversão, a Braze conta uma conversão para cada canal, o que pode resultar em taxas de conversão superiores a 100%.
- **Etapas de Mensagem do Canvas:** A Braze atribui as conversões que ocorrem dentro do prazo de conversão à última etapa de Mensagem do Canvas que o usuário recebeu. Depois que ele recebe a próxima etapa de Mensagem, a atribuição passa para essa etapa. A Braze mede essa janela a partir de quando o usuário entra no Canvas, não a partir de cada mensagem individualmente. As conversões que acontecem durante postergações entre etapas de Mensagem contam para a atribuição da etapa de Mensagem anterior até que o usuário avance; as conversões após a última etapa de Mensagem ainda contam até o prazo de conversão do Canvas.
- **Retenção de eventos históricos:** O rastreamento de conversão nos dashboards de Campaign e Canvas mede ações históricas, não perfis de usuário atuais. Quando um usuário atende a uma regra de conversão dentro da janela designada, a Braze registra uma conversão na análise de dados e não a remove, mesmo que o perfil desse usuário seja posteriormente excluído, mesclado ou arquivado durante a manutenção rotineira de dados ou varreduras de conformidade com o GDPR. As contagens de Segments em tempo real podem ser naturalmente menores que os registros permanentes de eventos do dashboard, pois os Segments dinâmicos filtram apenas perfis ativos que existem atualmente no banco de dados.
- Se um usuário realiza um evento de conversão dentro dos prazos de conversão de duas Campaigns ou Canvas separados que ele recebeu, a conversão é registrada em ambos.
- Um usuário é considerado convertido se realizou o evento de conversão específico dentro da janela, mesmo que não tenha aberto ou clicado na mensagem.

### Evento de conversão primária {#primary-conversion-event}

O evento de conversão primária é o primeiro evento que você adiciona durante a criação da Campaign ou do Canvas. Esse evento tem o maior impacto no seu engajamento e relatórios. A Braze usa o evento de conversão primária para:

- Selecionar a variação de mensagem com melhor desempenho em [Campaigns multivariantes]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) ou Canvas.
- Determinar a janela em que a receita é calculada para a Campaign ou o Canvas.
- Ajustar as distribuições de mensagens para Campaigns e Canvas usando [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

A contagem de eventos de conversão primária é o número de eventos de conversão que ocorreram. Para Campaigns multicanal, a Braze conta conversões por canal (conforme descrito em [Regras de rastreamento de conversão](#conversion-tracking-rules)), o que significa que a contagem de conversões pode exceder o número de usuários únicos e resultar em taxas de conversão superiores a 100%. A Braze calcula a taxa do evento de conversão primária dividindo essa contagem pelo número de destinatários únicos. A Braze considera um usuário como destinatário quando a mensagem é enviada ou exibida, dependendo do canal. Por exemplo, em push ou e-mail, um usuário se torna destinatário depois que a Braze envia a mensagem. Para mensagens no app ou Content Cards, o usuário precisa visualizar a mensagem para ser considerado destinatário.

{% alert note %}
Se você interromper mensagens usando a tag Liquid `abort`, a Braze interrompe mensagens apenas para os usuários que passam pelas variantes. As mensagens para os usuários no grupo de controle não são interrompidas, o que pode levar a porcentagens de conversão distorcidas entre variantes e grupos de controle. Como alternativa, use a [segmentação]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para direcionar seus usuários na entrada da Campaign e do Canvas.
{% endalert %}

## Criando uma campanha com rastreamento de conversão {#creating-a-campaign-with-conversion-tracking}

### Etapa 1: Configure sua campanha {#step-1-set-up-your-campaign}

[Crie uma campanha]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign) para o canal de envio de mensagens desejado. Depois de configurar as mensagens e o cronograma da sua campanha, você pode adicionar até quatro eventos de conversão para rastreamento.

Use quantos eventos de conversão forem necessários. Adicionar um segundo ou terceiro evento de conversão enriquece significativamente seus relatórios. Por exemplo, para uma campanha direcionada a usuários inativos, adicionar um evento de conversão secundário junto com o evento de conversão primário **Starts Session** ajuda você a entender o quão eficaz sua campanha é em trazer os usuários de volta ao seu aplicativo.

### Etapa 2: Adicione os eventos de conversão {#step-2-add-the-conversion-events}

Primeiro, selecione o tipo geral de evento que você deseja usar:

| Tipo de evento de conversão | Descrição |
|-------------------------|----------------------------|
| **Starts Session** | Um usuário é contabilizado como convertido quando abre qualquer um dos apps que você especificar (o padrão são todos os apps no espaço de trabalho).|
| **Makes Purchase** | Um usuário é contabilizado como convertido quando registra um [evento de compra]({{site.baseurl}}/api/objects_filters/purchase_object). Isso rastreia qualquer compra por padrão, ou você pode especificar um produto específico.|
| **Places Order** | Um usuário é contabilizado como convertido quando dispara o [evento recomendado de e-commerce Order Placed]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#ecommerce-recommended-events?tab=ecommerce.order_placed). Isso rastreia qualquer pedido por padrão, ou você pode filtrar por um produto específico.<br><br>O evento "Places Order" está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze se tiver interesse em participar desse acesso antecipado. |
| **Performs Custom Event** | Um usuário é contabilizado como convertido quando realiza um dos seus eventos personalizados existentes (não há padrão, você precisa especificar o evento).|
| **Upgrade App** | Um usuário é contabilizado como convertido quando faz upgrade da versão do app em qualquer um dos apps que você especificar (o padrão são todos os apps no espaço de trabalho). A Braze realiza uma comparação numérica de melhor esforço para determinar se a alteração foi um upgrade. Versões não numéricas são contabilizadas como conversões se a versão mudar.|
| **Opens email** | Um usuário é contabilizado como convertido quando abre o e-mail (apenas para campanhas de e-mail).|
| **Clicks email** | Um usuário é contabilizado como convertido quando clica em um link no e-mail (apenas para campanhas de e-mail).|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Adicione os eventos de conversão" }

{% alert important %}
**Propriedades aninhadas não são compatíveis com eventos de conversão**. Você não pode usar propriedades aninhadas em eventos de conversão. Por exemplo, se `product_code` ou `product_name` são propriedades aninhadas dentro de um array `products` (como `products[].product_code`), você não pode usá-las para verificar se uma compra de produto específico foi feita em um evento de conversão.
{% endalert %}

Defina o prazo de conversão. Esse é o tempo máximo que pode passar antes que a Braze considere uma conversão. Você pode definir uma janela de até 30 dias durante a qual a Braze contabiliza a conversão se o usuário realizar a ação especificada.

![O tipo de evento de conversão "Makes Purchase" como exemplo para registrar conversões de usuários que fazem qualquer compra. O prazo de conversão é de 12 horas.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Depois de selecionar seus eventos de conversão, continue o processo de criação da campanha e comece a enviar sua campanha.

### Etapa 3: Visualize seus resultados {#step-3-view-your-results}

Acesse a página **Details** para visualizar os detalhes de cada evento de conversão associado à campanha que você criou. Independentemente dos eventos de conversão selecionados, você também pode ver a receita total atribuída a essa campanha específica, bem como a variantes específicas, durante a janela do evento de conversão primária.

{% alert note %}
Se você não selecionar nenhum evento de conversão durante a criação da campanha, o tempo padrão será de três dias.
{% endalert %}

Além disso, para mensagens multivariantes, você pode ver o número de conversões e os percentuais de conversão do seu grupo de controle e de cada variante.

![Quatro eventos de conversão que rastreiam conversões com base em quando uma compra foi feita dentro de três horas, compra feita dentro de duas horas, sessão iniciada dentro de 30 minutos e sessão iniciada dentro de 25 minutos.]({% image_buster /assets/img_archive/conversion_event_details.png %})

## Taxas de conversão de etapa do Canvas versus variante {#canvas-step-versus-variant-conversion-rates}

É comum que a contagem total de conversões de uma variante do Canvas seja maior que a soma das conversões de suas etapas individuais. Isso acontece porque as conversões são rastreadas de forma diferente no nível da variante e no nível da etapa:

- As conversões de variante são contabilizadas assim que o usuário entra na variante.
- As conversões de etapa são contabilizadas somente após a mensagem da etapa ser enviada ao usuário.

Isso significa que qualquer usuário que entra no Canvas e realiza o evento de conversão antes de receber uma etapa é contabilizado no total da variante, mas não em nenhuma etapa.

Os seguintes cenários também podem causar essa discrepância:

- **O usuário sai do Canvas antes de receber qualquer etapa.** Se um usuário entra no Canvas mas sai (por exemplo, devido a um filtro ou incompatibilidade de público) antes de qualquer mensagem ser enviada, uma conversão que ele realize ainda é contabilizada no nível da variante, mas não no nível de nenhuma etapa.
- **A etapa é direcionada a um subconjunto de usuários.** Se uma etapa está configurada para enviar apenas para uma plataforma específica (como mobile), os usuários em outras plataformas (como web) ainda podem entrar no Canvas e converter. Como esses usuários nunca recebem a mensagem da etapa, a conversão não é contabilizada no nível da etapa — somente no nível da variante.

Para saber mais sobre análise de dados do Canvas, consulte [Medindo e testando com análise de dados do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).
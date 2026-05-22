---
nav_title: Swym
article_title: Swym
description: "Este artigo de referência descreve a parceria entre a Braze e a Swym, que permite que os compradores salvem produtos e continuem sua jornada sem problemas em sites, apps móveis e lojas de varejo."
alias: /partners/swym/
page_type: partner
search_tag: Partner
---

# Swym

> [A Swym](https://getswym.com/) ajuda as marcas de comércio eletrônico a capturar a intenção de compra com Wishlists, Save for Later, Gift Registry e alertas de Back-in-Stock. Usando dados avançados e baseados em permissões, você pode criar campanhas hiperdirecionadas e oferecer experiências de compras personalizadas que impulsionam o engajamento, aumentam as conversões e a fidelidade.

*Essa integração é mantida pela Swym.*

## Sobre a integração {#about-the-integration}

A integração da Swym com a Braze permite que você entregue campanhas de marketing personalizadas e orientadas por eventos que convertem a intenção do comprador em vendas. Use a integração para que os compradores possam continuar de onde pararam, colaborar com outras pessoas durante toda a jornada de compras e receber campanhas de redirecionamento de alto desempenho.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Pré-requisito          | Descrição                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Swym  | Os apps Swym Wishlist Plus, Back in Stock ou ambos devem estar instalados em sua plataforma de comércio eletrônico (Shopify ou BigCommerce), e você deve estar no plano Enterprise.       |
| Uma chave da API REST da Braze  | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Settings** > **API Keys**. |
| Um endpoint REST da Braze | [Seu URL de endpoint REST]({{site.baseurl}}/api/basics/#endpoints). Seu endpoint dependerá do URL da Braze para sua instância.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso {#use-cases}

Ao conectar os apps Wishlist Plus e Back in Stock Alerts da Swym com a Braze, você pode enviar automaticamente eventos de atividade do comprador, como adições à lista de desejos, inscrições de volta ao estoque, alertas de queda de preço e lembretes, para a Braze como eventos personalizados. Esses eventos podem ser usados para disparar mensagens automatizadas na Braze, facilitando a comunicação oportuna, relevante e engajadora que leva os compradores a voltar para fazer uma compra.

## Integração da Swym {#integrating-swym}

### Etapa 1: Conecte seu app Swym à Braze {#step-1-connect-your-swym-app-to-braze}

Atualmente, a integração da Braze com a Swym é uma integração gerenciada e não é de autoatendimento. Para começar, entre em contato com a equipe de suporte da Swym em [support@getswym.com](mailto:support@getswym.com) e forneça as seguintes informações para que a Swym possa configurar a integração em seu nome:

1. Gere uma [chave da API REST]({{site.baseurl}}/api/basics/#about-rest-api-keys) no dashboard da Braze com a permissão `users.track`.

![Gerando uma chave de API na Braze.]({% image_buster /assets/img/swym/braze-api-key.png %})

{% alert important %}
Para proteger suas chaves de API, a Swym recomenda que você compartilhe credenciais com segurança usando uma ferramenta de link único e autodestrutivo (por exemplo, [OneTimeSecret](https://onetimesecret.com/)).
{% endalert %}

{: start="2"}
2. A Braze gerencia várias instâncias para seu dashboard e endpoints REST. Forneça o [endpoint REST]({{site.baseurl}}/api/basics/#endpoints) para a instância que está sendo provisionada.

3. Depois que a chave de API e o URL da instância forem compartilhados com a equipe de suporte da Swym, eles configurarão a integração para você e responderão com uma confirmação.

4. Após a conclusão da configuração, os eventos personalizados da Swym serão registrados automaticamente na Braze. Você pode visualizar a lista de eventos Swym registrados no dashboard da Braze acessando **Configurações de dados** > **Eventos personalizados**.

5. Visualize as propriedades de cada evento Swym selecionando **Manage Properties** para o evento personalizado correspondente. Essas propriedades contêm os valores de eventos que podem ser usados para personalizar suas mensagens.

![Propriedades personalizadas na Braze.]({% image_buster /assets/img/swym/braze-custom-properties.png %})

### Etapa 2: Assine os eventos que você deseja enviar para a Braze {#step-2-subscribe-to-events-you-want-to-send-to-braze}

No app Wishlist Plus, acesse a guia **Marketing** e encontre a seção **Automations**. Aqui, você pode selecionar os eventos que deseja assinar.

![Eventos a serem assinados.]({% image_buster /assets/img/swym/braze-event-subscription.png %})

#### Eventos do app Swym Wishlist Plus {#swym-wishlist-plus-app-events}

| Nome do evento | Quando esse evento é disparado |
|------------|------------------------------|
| Share Wishlist | Quando um comprador compartilha uma lista de desejos com outra pessoa |
| Add to Wishlist | Quando um comprador adiciona um item à sua lista de desejos |
| Wishlist Reminder | Lembrete sobre itens na lista de desejos de um comprador |
| Saved for Later Reminder | Lembrete sobre os itens salvos para depois de um comprador |
| Price Drop alert | O produto em uma lista de desejos é colocado à venda |
| Low Stock alert | O produto em uma lista de desejos está ficando sem estoque |
| Back in Stock alert | O produto em uma lista de desejos é reabastecido |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Eventos do app Swym Back in Stock Alerts {#swym-back-in-stock-alerts-app-events}

| Nome do evento | Quando esse evento é disparado |
|------------|------------------------------|
| Back in Stock Acknowledgment | O comprador se inscreve para ser notificado quando um produto estiver novamente em estoque |
| Restock Alert | O produto para o qual um comprador solicitou um alerta de volta ao estoque é reabastecido |
| Restock Reminder | Alerta de acompanhamento (geralmente cerca de 24 horas após o primeiro alerta de reabastecimento, configurável) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 3: Crie uma Campaign ou um Canvas na Braze {#step-3-create-a-braze-campaign-or-canvas}

Para automatizar o envio de mensagens personalizadas para seus compradores, é necessário criar uma Campaign ou um Canvas separado na Braze para cada evento em que você se inscreveu. Cada Campaign ou Canvas deve ser configurado para disparar com base no evento específico e usar as propriedades do evento correspondente para preencher o conteúdo dinâmico em suas mensagens. Para orientações passo a passo, consulte [Primeiros passos: Campaigns e Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases/).

![Um evento baseado em ações.]({% image_buster /assets/img/swym/braze-canvas-setup.png %})

Para detalhes adicionais, consulte a [central de ajuda da Swym](https://help.getswym.com/en/articles/12344153-braze-integration) ou entre em contato com a equipe de suporte da Swym em [support@getswym.com](mailto:support@getswym.com).
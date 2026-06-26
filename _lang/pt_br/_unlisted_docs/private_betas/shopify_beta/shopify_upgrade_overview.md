---
nav_title: Visão geral do upgrade do Shopify
article_title: Visão geral do upgrade do Shopify
description: "Este artigo de referência descreve como fazer upgrade da sua integração com o Shopify para a versão mais recente."
page_type: partner
search_tag: Partner
permalink: "/shopify_upgrade_overview/"
hidden: true
---

# Visão geral do upgrade do Shopify {#shopify-upgrade-overview}

> Como parte do nosso compromisso em oferecer a melhor experiência possível, estamos exigindo que todas as integrações com o Shopify façam [upgrade]({{site.baseurl}}/shopify/) para a versão mais recente até 28 de agosto de 2025. Esse upgrade é essencial porque mudanças significativas na tecnologia do Shopify vão impactar o funcionamento da nossa integração.

## Datas importantes {#key-dates}

- **Final de fevereiro até abril:** Você receberá notificações sobre quando o seu grupo específico (coorte) estará pronto para o upgrade. Fique atento a essa informação importante.
- **Prazo para o upgrade:** Todos os clientes devem concluir o upgrade até **28 de agosto de 2025**.

{% multi_lang_include shopify_alerts.md alert='breaking' %}

## O que está mudando na integração com o Shopify? {#whats-changing-in-the-shopify-integration}

Como parte dos planos do Shopify para aprimorar a extensibilidade do checkout, mudanças significativas estão chegando à integração com a Braze. Veja o que você precisa saber:

- **Descontinuação de Script Tags e `checkout.liquid`:** O Shopify está eliminando gradualmente os Script Tags e o `checkout.liquid`. Após agosto de 2025, o SDK para Web da Braze não carregará mais nas páginas de checkout por meio de Script Tags, a menos que você migre para a versão mais recente da integração.
- **Melhorias gerais na integração:**
    - **Introdução de eventos recomendados:** Estamos adicionando eventos de eCommerce recomendados à integração, o que simplifica casos de uso comuns de eCommerce por meio de modelos pré-construídos na Braze.
    - **Gerenciamento de identidade simplificado:** Estamos aprimorando nossa abordagem para gerenciar identidades de usuários, o que vai melhorar o rastreamento e a atribuição de dados de usuários anônimos. Para saber mais sobre como o gerenciamento de identidade será processado, consulte [Sincronização de usuários e dados]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#user-and-data-syncing).
    - **Listas de inscritos de e-mail e SMS:** Se você está coletando inscritos de e-mail e SMS atualmente, grupos de inscrições padrão para cada canal serão criados automaticamente como parte do upgrade. Quando a Braze sincronizar os opt-ins de e-mail e SMS, a Braze não substituirá mais o estado de inscrição global no perfil de usuário e apenas atualizará o opt-in do grupo de inscrições.
    - Para ver todos os detalhes sobre as mudanças da versão atual para a nova versão, consulte o [changelog](#full-changelog).

{% alert important %}
Esse upgrade é essencial para manter a funcionalidade da sua integração entre o Shopify e a Braze. Recomendamos colaborar de perto com sua equipe de desenvolvimento para avaliar o escopo e as implicações dessas mudanças e facilitar uma transição tranquila.
{% endalert %}

## Requisitos para o upgrade {#upgrade-requirements}

Antes de iniciar o processo de upgrade na página de integração do Shopify, conclua os seguintes requisitos com sua equipe de engenharia:

- **Verifique personalizações do SDK:** Se você personalizou sua integração entre a Braze e o Shopify (por exemplo, registrando eventos personalizados ou atributos personalizados), certifique-se de que essas personalizações funcionarão corretamente após o upgrade. Se você criou seus próprios eventos de navegador para ações como "produto visualizado" ou "carrinho atualizado", coordene com seus desenvolvedores para removê-los antes do upgrade, pois eles duplicarão a funcionalidade fornecida pelo novo conector.

{% alert important %}
Se você tem uma loja online no Shopify e seus desenvolvedores implementaram os SDKs da Braze diretamente no seu site Shopify, ou por meio do Google Tag Manager ou de uma plataforma de dados do cliente, você deve planejar parar de usá-los ao fazer upgrade para o novo conector do Shopify.
{% endalert %}

- **Revise o gerenciamento de identidade:** Se você está usando um ID externo da Braze, trabalhe com sua equipe de desenvolvimento para garantir que ele seja compatível com a nova integração. Se você define o ID externo dentro da experiência da sua loja Shopify, peça aos seus desenvolvedores para ajustá-lo e evitar conflitos com o [novo processo de gerenciamento de identidade]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing).
- **Prepare Campaigns, Canvas e Segments impactados:** Durante o processo de upgrade guiado, você pode visualizar e exportar quaisquer Campaigns, Canvas e Segments que dependem de dados do Shopify. Recomendamos adicionar os novos eventos e atributos obrigatórios do Shopify usando um operador "OR" para facilitar um upgrade tranquilo para suas mensagens ativas.
- **Crie jornadas de usuário de carrinho e checkout abandonados:** A jornada de usuário de carrinho abandonado agora deve usar o gatilho "Performed Cart Updated" como parte dos critérios de entrada no seu Canvas. Além disso, você precisa usar a nova Liquid tag de carrinho de compras para as jornadas de usuário de carrinho abandonado e checkout abandonado. Você pode usar nossos novos [modelos de Canvas]({{site.baseurl}}/using_shopify_with_braze/#create-your-canvas-user-journeys) para começar.

Concluir essas etapas ajudará a facilitar um upgrade bem-sucedido para a versão mais recente da integração com o Shopify.

## Opções de integração {#integration-options}

A Braze oferece duas opções de integração para lojistas do Shopify, projetadas para atender às diversas necessidades de negócios de eCommerce: **Integração padrão** e **Integração personalizada**.

{% tabs local %}
{% tab Padrão %}
A integração padrão é feita sob medida para lojas online do Shopify, oferecendo um processo de configuração simples e direto. Essa opção permite que você conecte rapidamente sua loja Shopify à Braze, possibilitando o uso de ferramentas poderosas de engajamento de clientes sem necessidade de conhecimento técnico avançado. Com essa opção de integração, você pode sincronizar dados de clientes, automatizar o envio de mensagens personalizadas e aprimorar seus esforços de marketing por meio dos recursos abrangentes da Braze.

Para fazer upgrade da sua integração existente com o Shopify pela jornada de upgrade padrão, consulte [Fazendo upgrade da sua integração com o Shopify (padrão)]({{site.baseurl}}/shopify_standard_upgrade/).
{% endtab %}

{% tab Personalizada %}
A integração personalizada oferece uma solução mais flexível e modular se você usa o Shopify Hydrogen ou tem uma loja headless. Essa opção permite que você implemente os SDKs da Braze diretamente no seu ambiente Shopify, possibilitando uma integração mais profunda e funcionalidades sob medida. Seja para criar experiências únicas para os clientes ou otimizar fluxos de trabalho específicos, a integração personalizada fornece as ferramentas necessárias para aproveitar ao máximo os recursos da Braze em uma configuração headless.

Para fazer upgrade da sua integração existente com o Shopify pela jornada de upgrade personalizada, consulte [Fazendo upgrade da sua integração com o Shopify (personalizada)]({{site.baseurl}}/shopify_custom_upgrade/).
{% endtab %}
{% endtabs %}

## Changelog

{% alert important %}
Essa integração usa o Shopify como fonte de verdade para atributos e eventos suportados. Como resultado, o Shopify pode substituir valores pré-existentes, como atributos padrão ou personalizados, em um perfil de usuário quando os dados são sincronizados.
{% endalert %}

### Integração padrão {#standard-integration}

| Versão anterior | Versão mais recente |
| --- | --- |
| {::nomarkdown}<ul><li>Script Tag support</li><li>Braze Web SDK only</li><li>Shopify webhooks for events and products</li></ul>{:/} | {::nomarkdown}<ul><li>Web Pixel API support</li><li>New Braze app embed</li><li>Braze Web SDK & JavaScript SDK</li><li>Shopify webhooks for events and products</ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integração padrão" }

### Identificadores de usuário suportados pela integração {#user-identifiers-supported-by-the-integration}

| Identificadores de usuário | Versão anterior | Versão mais recente |
| --- | --- | --- |
| ID de dispositivo da Braze |  {::nomarkdown}<ul><li>A randomly generated ID that is stored on the browser</li></ul>{:/} | {::nomarkdown} <ul><li>A randomly generated ID that is stored on the browser</li></ul>{:/}|
| Aliases da Braze | {::nomarkdown}<ul><li>Shopify customer ID</li><li>Shopify email</li></ul>{:/} | {::nomarkdown}<ul><li>Shopify cart token</li><li>Shopify checkout token</li></ul>{:/}|
| ID externo da Braze | {::nomarkdown}<ul><li>N/A</li></ul>{:/}| {::nomarkdown}<ul><li>Shopify customer ID</li><li>Email</li><li>Hashed email (SHA-256, SHA-1, MD5)</li><li>Custom external ID</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Identificadores de usuário suportados pela integração" }

Para mais detalhes sobre sincronização de usuários e gerenciamento de IDs, consulte [Dados de usuários e sincronização]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing).

{% alert note %}
Por padrão, a Braze converte automaticamente os e-mails do Shopify para letras minúsculas antes de usá-los como ID externo. Se você está usando e-mail ou e-mail com hash como seu ID externo, confirme que seus endereços de e-mail também são convertidos para letras minúsculas antes de atribuí-los como seu ID externo ou antes de aplicar o hash a partir de outras fontes de dados. Isso ajudará a evitar discrepâncias nos IDs externos e a criação de perfis de usuário duplicados na Braze.
{% endalert %}

### Eventos do Shopify suportados {#supported-shopify-events}

| Eventos ou atributos | Versão anterior | Versão mais recente |
| --- | --- | --- |
| Eventos |  {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=product%20viewed">shopify_product_viewed</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=product%20viewed">ecommerce.product_viewed</a></li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-browse">abandoned browse Canvas template</a></li></ul>{:/} |
| Eventos |  {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?tab=example%20payload">shopify_product_clicked</a></li></ul>{:/} | {::nomarkdown}<ul><li>Deprecated event</li></ul>{:/} |
| Eventos | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20cart&tab=example%20payload">shopify_abandoned_cart</a></li><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Abandoned cart timer setting</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=cart%20updated">ecommerce.cart_updated</a></li><li>Deprecated abandoned cart timer setting</li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-cart">abandoned cart Canvas template</a></li></ul>{:/} |
| Eventos | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20checkout&tab=example%20payload">shopify_abandoned_checkout</a></li><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Abandoned cart timer setting</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=checkout%20started">ecommerce.checkout_started</a></li><li>Deprecated abandoned checkout timer setting</li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-checkout">abandoned checkout Canvas template</a></li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20order&tab=example%20payload">shopify_created_order</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a></li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#order-confirmation-and-feedback-survey">order confirmation & post-purchase survey Canvas template</a></li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="https://braze.com/unlisted_docs/using_shopify_with_braze/?tab=order%20confirmation">Braze purchase event</a></li></ul>{:/}| {::nomarkdown}<ul><li>Deprecated event. Use <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a>.</li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=paid%20order&tab=example%20payload">shopify_paid_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=partially%20fulfilled%20order&tab=example%20payload">shopify_partially_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=fulfilled%20order&tab=example%20payload">shopify_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=cancelled%20order&tab=example%20payload">shopify_cancelled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20cancelled">ecommerce.order_cancelled</a></li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20refund&tab=example%20payload">shopify_created_refund</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20refunded">ecommerce.order_refunded</a></li></ul>{:/}|
| Eventos| {::nomarkdown}<ul><li>No Shopify account login event</li></ul>{:/}| {::nomarkdown}<ul><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=account%20login#tracked-shopify-events">shopify_account_login</a></li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_total_spent</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_order_count</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_last_order_id</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_last_order_name</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_zipcode</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_province</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Eventos do Shopify suportados" }

### Coleta de inscritos {#subscriber-collection}

| Tipo de coleta | Versão anterior | Versão mais recente |
| --- | --- | --- |
| Coleta de inscritos de e-mail |  {::nomarkdown}<ul><li>Override for global email subscription state</li><li>Ability to assign one or more subscription groups</li><li>No default subscription group for the integration for the connected Shopify store</li></ul>{:/} | {::nomarkdown}<ul><li>Deprecated override functionality</li><li>A default subscription group will be created as part of the upgrade</li><li>Ability to assign additional subscription groups</li></ul>{:/} |
| Coleta de inscritos de SMS |  {::nomarkdown}<ul><li>Required to assign one or more subscription groups</li><li>No default subscription group for the integration for the connected Shopify store</li></ul>{:/} | {::nomarkdown}<ul><li>A default subscription group will be created as part of the upgrade</li><li>Ability to assign additional subscription groups</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Coleta de inscritos" }

{% alert note %}
Se você está coletando inscritos de e-mail ou SMS atualmente, um novo grupo de inscrições padrão será criado após a conclusão do upgrade. O grupo de inscrições padrão terá o nome da sua vitrine do Shopify. Esse processo pode levar até 5 horas. <br><br>Depois que os grupos de inscrições estiverem disponíveis, certifique-se de incluí-los nas suas Campaigns, Segments ou Canvas ativos para alcançar efetivamente seus compradores inscritos.
{% endalert %}

### Sincronização de produtos {#product-sync}

| Tipo de sincronização | Versão anterior | Versão mais recente |
| --- | --- | --- |
| Sincronização inicial de produtos | {::nomarkdown}<ul><li>If product syncing is enabled, initial import of all products in your storefront</li><li>Ability to only import active products</li></ul>{:/} | {::nomarkdown}<ul><li>No&nbsp;changes</li></ul>{:/} |
| Sincronização de produtos em tempo real | {::nomarkdown}<ul><li>Real-time syncs when products are created, updated, or deleted from your store</li></ul>{:/} | {::nomarkdown}<ul><li>No&nbsp;changes</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sincronização de produtos" }

### Canais {#channels}

| Canal | Versão anterior | Versão mais recente |
| --- | --- | --- |
| In-App Messages |  {::nomarkdown}<ul><li>Included within standard integrations for Shopify online stores</li></ul>{:/} | {::nomarkdown}<ul><li>No changes</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canais" }
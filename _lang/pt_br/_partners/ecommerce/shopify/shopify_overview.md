---
nav_title: Visão geral do Shopify
article_title: Visão geral do Shopify
description: "Este artigo de referência descreve a parceria entre a Braze e a Shopify, uma empresa de comércio global que permite conectar sua loja da Shopify com a Braze para passar webhooks selecionados da Shopify para a Braze. Aproveite as estratégias de mensagens integradas entre canais da Braze e o Canvas para incentivar os clientes a completarem suas compras ou redirecionar os usuários com base nas compras anteriores."
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Visão geral do Shopify {#shopify-overview}

> [A Shopify](https://www.shopify.com/) é uma empresa líder em comércio global que fornece ferramentas confiáveis para iniciar, crescer, comercializar e gerenciar negócios de qualquer tamanho. A Shopify torna o comércio melhor para todo mundo com uma plataforma e serviços projetados para confiabilidade, enquanto oferece uma melhor experiência de compra para consumidores em todos os lugares.

A integração da Braze com a Shopify fornece uma solução poderosa para empresas de eCommerce que buscam aprimorar o engajamento do cliente e impulsionar esforços de marketing personalizados. Essa integração conecta perfeitamente as robustas capacidades de eCommerce da Shopify com nossa avançada plataforma de engajamento com clientes, permitindo que você envie mensagens direcionadas, relevantes e oportunas aos seus usuários com base em comportamentos de compra em tempo real e dados transacionais.

## Requisitos {#requirements}

| Requisito | Descrição |
| --- | --- |
| Loja Shopify | Você tem uma loja Shopify ativa. |
| Permissões de proprietário ou membro da equipe da loja Shopify | {::nomarkdown}<ul><li>Acesso a todas as configurações Gerais e da Loja Online.</li><li> Permissões adicionais de administrador:<ul><li>Pedidos: Visualizar</li><li>Cliente: Leitura e gravação</li><li>Visualizar eventos de clientes (Web Pixels)</li><li>Gerenciar configurações</li><li>Visualizar apps desenvolvidos por funcionários/colaboradores</li><li>Gerenciar/instalar apps e canais</li><li>Gerenciar/adicionar pixels personalizados</li></ul></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Como integrar {#how-to-integrate}

A Braze oferece duas opções de integração para comerciantes do Shopify, projetadas para atender às diversas necessidades de negócios de eCommerce: **Integração padrão** e **Integração personalizada**.

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

## Como a integração funciona {#how-the-integration-works}

Se você já configurou e ativou o [preenchimento de dados históricos]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill) nas suas configurações, a sincronização inicial dos dados começará imediatamente.

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

Após a sincronização inicial dos dados, a Braze rastreará continuamente novos dados e atualizações, diretamente do Shopify e dos SDKs da Braze.

{% alert note %}
Se você já é cliente da Braze com Campaigns ou Canvas ativos, consulte [Preenchimento de dados históricos do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill) para informações importantes. Para ver quais dados de clientes estão sendo preenchidos, consulte [Recursos do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).
{% endalert %}

### Sincronização de usuários e dados {#user-and-data-syncing}

Após a integração estar ativa, a Braze coletará dados de usuários de duas fontes principais por meio da integração com o Shopify:
- **API or interface de programação do aplicativo (API) Shopify Web Pixel e app embeds:** Isso alimenta o SDK or kit de desenvolvimento de software web da Braze e o SDK or kit de desenvolvimento de software JavaScript para oferecer suporte ao rastreamento no site, gerenciamento de identidade, dados comportamentais de eCommerce e canais de envio de mensagens como In-App Messages.
- **Webhooks do Shopify:** dados comportamentais de eCommerce, sincronização de produtos e coleta de inscritos

Durante a integração, você precisará selecionar quando os SDKs da Braze inicializam e carregam no seu site Shopify:
- Ao visitar o site (como início de sessão)
    - **O que faz:** Rastreia usuários anônimos — como visitantes — para acessar mais dados e personalização mais profunda
- Ao criar conta (como login na conta)
    - **O que faz:** Impede o rastreamento de usuários anônimos, proporcionando uma abordagem mais conservadora e voltada à privacidade, de forma que a atividade do usuário é rastreada *após* o login na conta

{% alert note %}
- Visitas ao site (sessões) contam para a sua cota de usuários ativos mensais (MAU).
- As versões do SDK or kit de desenvolvimento de software web da Braze e do SDK or kit de desenvolvimento de software JavaScript são automaticamente definidas como v6.8.0. Você pode atualizar a versão do SDK or kit de desenvolvimento de software a qualquer momento nas configurações da integração.
{% endalert %}

A Braze usa a integração com o Shopify para oferecer suporte a múltiplos identificadores que rastreiam seus usuários desde a experiência de compra como visitante até se tornarem usuários identificados:

| Identificador da Braze | Descrição |
| --- | --- |
| `device_id` da Braze | Um ID gerado aleatoriamente armazenado no navegador que rastreia a atividade de usuários anônimos por meio dos SDKs da Braze. |
| Alias de usuário do token do carrinho | Um alias que a Braze cria para rastrear eventos de atualização do carrinho. Esse token é criado usando o token do carrinho do Shopify. |
| Alias de usuário do token de checkout | Um alias que a Braze cria quando o usuário inicia o processo de checkout. Esse token é criado usando o token de checkout do Shopify.<br><br> Se um cliente usar o Shop Pay como opção de checkout acelerado, o Shopify pode ignorar certos eventos padrão de checkout e impedir que a Braze receba os dados necessários para adicionar o alias do token de checkout. |
| Alias do ID de cliente do Shopify | O ID de cliente do Shopify é atribuído como alias quando o ID externo é atribuído durante o login na conta ou quando um pedido é feito. |
| `external_id` da Braze | Um identificador exclusivo que ajuda a rastrear clientes entre dispositivos e plataformas. Isso mantém uma experiência de usuário consistente e melhora a análise de dados ao evitar múltiplos perfis quando os usuários trocam de dispositivo ou reinstalam o app.<br><br>A integração com o Shopify oferece suporte aos seguintes tipos de `external_id`: <br><br>{::nomarkdown}<ul><li>ID de cliente do Shopify (padrão)</li><li>ID externo personalizado</li><li>E-mail com hash (SHA-256)</li><li>E-mail com hash (SHA-1)</li><li>E-mail com hash (MD5)</li><li>E-mail</li></ul>{:/}A Braze atribui um `external_id` aos seus usuários chamando o método changeUser nos SDKs quando: <br><br>{::nomarkdown}<ul><li>Um usuário faz login ou cria uma conta</li><li>Um pedido é feito</li></ul>{:/}<br> Para saber mais sobre o que acontece quando você atribui um `external_id` a um perfil anônimo, consulte [Ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>A Braze também utilizará o `external_id` para atribuir dados comportamentais de eCommerce downstream provenientes dos webhooks do Shopify. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sincronização de usuários e dados" }

A integração requer que os SDKs da Braze e os serviços do Shopify trabalhem juntos para rastrear e atribuir adequadamente os dados do Shopify aos usuários corretos em tempo quase real. Para mais detalhes sobre os dados rastreados pela integração, consulte [Dados do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

{% alert note %}
- Se você estiver testando a integração, recomendamos usar o modo de navegação anônima ou limpar seus cookies para redefinir o `device_id` da Braze e simular o comportamento de um usuário anônimo.
- Embora um ID de cliente do Shopify seja gerado quando um e-mail é inserido no rodapé de newsletter do Shopify ou durante o processo de checkout antes de um pedido ser feito, esse ID de cliente não é acessível por meio dos Shopify Web Pixels. Por isso, a Braze não pode usar o método `changeUser` nessas duas situações.
{% endalert %}

### Sincronização de aceitações de marketing de e-mail e SMS do Shopify {#syncing-shopify-email-and-sms-marketing-opt-ins}

Se você ativar a coleta de inscritos nas suas configurações, precisará atribuir um grupo de inscrições para cada loja que você conectar à Braze. Isso significa que seus clientes serão categorizados como "subscribed" ou "unsubscribed" no grupo de inscrições da sua loja.

O status de aceitação de marketing do Shopify para e-mail e SMS pode ser atualizado das seguintes formas:
- **Atualização manual:** Você pode alterar manualmente o status de aceitação de marketing de e-mail ou SMS de um usuário no painel do Shopify.
- **Rodapé de newsletter do Shopify:** Se um usuário inserir seu e-mail no rodapé de newsletter padrão do Shopify, o status de aceitação será atualizado.
- **Checkout:** O consentimento do usuário é capturado no checkout quando os usuários marcam a caixa de seleção de marketing e prosseguem com o checkout selecionando **Pay now** no checkout de página única ou **Continue to shipping** no checkout de três páginas.

{% alert note %}
O status de aceitação de marketing de e-mail do Shopify não alterará o [estado de inscrição global de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions) de um usuário na Braze. O estado de inscrição padrão quando um perfil de usuário é criado é "subscribed". Lembre-se de usar o grupo de inscrições como parte dos critérios de entrada da sua Campaign ou Canvas.
{% endalert %}

Esta tabela mostra quais estados de aceitação de marketing do Shopify correspondem aos status dentro do seu grupo de inscrições na Braze.

| Estado de aceitação de marketing do Shopify | Estado do grupo de inscrições na Braze |
| --- | --- |
| E-mail inscrito | Subscribed |
| E-mail com inscrição cancelada | Unsubscribed |
| E-mail com confirmação pendente | Unsubscribed |
| E-mail inválido | Unsubscribed |
| SMS inscrito | Subscribed |
| SMS com inscrição cancelada | Unsubscribed |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sincronização de aceitações de marketing de e-mail e SMS do Shopify" }

### Formulários de inscrição {#sign-up-forms}

#### Rodapé de newsletter do Shopify {#shopify-newsletter-footer}

Usuários que inserirem seu endereço de e-mail no rodapé de newsletter do Shopify passarão por um destes fluxos:

##### Usuários que não fizeram login na conta {#users-who-havent-logged-into-their-account}

1. A Braze recebe um webhook de entrada do Shopify sempre que um cliente é criado ou atualizado.
2. A Braze cria um perfil de usuário contendo o endereço de e-mail e o alias do ID de cliente do Shopify associados a esse usuário.
3. O SDK or kit de desenvolvimento de software da Braze atualiza o perfil anônimo com o endereço de e-mail.

{% alert note %}
Isso pode resultar em um perfil duplicado até que o usuário se identifique criando sua conta, fazendo login na conta ou fazendo um pedido. A Braze oferece ferramentas de mesclagem em massa para ajudar você a automatizar a reconciliação de perfis duplicados. Consulte [Usuários duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users) para mais detalhes.
{% endalert %}

##### Usuários que já fizeram login na conta {#users-who-have-already-logged-into-their-account}

A Braze criará um perfil de usuário contendo o endereço de e-mail e o alias do ID de cliente do Shopify associados a esse usuário. A Braze não atualizará o endereço de e-mail do usuário logado, pois assumimos que o Shopify já forneceu essa informação.

#### Formulários de inscrição da Braze {#braze-sign-up-forms}

A Braze oferece dois tipos de modelos de formulários de inscrição:
- **[Formulários de inscrição de e-mail]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/email_capture):** Crie-os usando o editor de arrastar e soltar.
- **[Formulário de captura de e-mail do editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form):** Um formulário mais direto para capturar endereços de e-mail.

Quando você usa esses modelos de formulários de inscrição, a Braze atualiza automaticamente o status de inscrição global de e-mail no perfil de usuário. Para mais detalhes sobre como o estado de inscrição global de e-mail é tratado, incluindo informações sobre validação de e-mail, consulte a documentação de cada tipo de modelo de formulário.

{% alert note %}
- Certifique-se de incluir critérios de entrada na sua Campaign ou Canvas que incluam tanto o status de inscrição global de e-mail quanto o grupo de inscrições conectado à sua loja Shopify. Isso ajudará a garantir que você esteja direcionando o público certo.
- A Braze coleta informações de visitantes, como endereços de e-mail e números de telefone, por meio de mensagens no navegador. Essas informações são então enviadas para a API or interface de programação do aplicativo (API) de Visitantes do Shopify, mas não criam um perfil de cliente no Shopify. Para mais detalhes, consulte [Visitor API or interface de programação do aplicativo (API)](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Formulários de inscrição de terceiros {#third-party-sign-up-forms}

Se você estiver usando uma plataforma de terceiros ou um plugin do Shopify para seus formulários de inscrição, precisará trabalhar com seus desenvolvedores para integrar o código do SDK or kit de desenvolvimento de software da Braze para capturar o endereço de e-mail e o status de inscrição global de e-mail a partir dos envios de formulário. Para saber mais, consulte [Configuração de integração padrão do Shopify]({{site.baseurl}}/shopify_standard_integration) e [Configuração de integração personalizada do Shopify]({{site.baseurl}}/shopify_custom_integration).

### Sincronização de produtos {#product-syncing}

A Braze oferece suporte à sincronização dos produtos da sua loja Shopify em um catálogo da Braze. Para mais detalhes, consulte [Sincronização de produtos do Shopify]({{site.baseurl}}/shopify_catalogs).

## Solicitações de titulares de dados {#data-subject-requests}

Como parte da integração da Braze com o Shopify, a Braze recebe automaticamente os [webhooks de conformidade do Shopify](https://shopify.dev/docs/apps/build/privacy-law-compliance/). No entanto, como os clientes são os controladores dos dados de seus usuários finais, eles devem executar todas as ações necessárias para atender às solicitações de titulares de dados recebidas em relação aos dados de usuários finais na Braze (incluindo dados de usuários finais recebidos por meio da integração com o Shopify). Consulte nossa documentação de [Assistência Técnica para Proteção de Dados]({{site.baseurl}}/dp-technical-assistance) para mais detalhes.
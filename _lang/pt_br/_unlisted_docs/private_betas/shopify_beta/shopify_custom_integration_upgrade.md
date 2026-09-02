---
nav_title: Fazendo upgrade do Shopify (personalizado)
article_title: "Fazendo upgrade da sua integração personalizada com o Shopify"
description: "Saiba como fazer upgrade da sua integração personalizada com o Shopify para a Braze."
page_type: partner
search_tag: Partner
permalink: "/shopify_custom_upgrade/"
hidden: true
---

# Fazendo upgrade da sua integração com o Shopify (personalizado) {#upgrading-your-shopify-integration-custom}

> Saiba como fazer upgrade da sua integração com o Shopify usando a jornada personalizada para a Braze. Como parte do nosso compromisso em oferecer a melhor experiência possível, estamos exigindo que todas as integrações com o Shopify façam [upgrade]({{site.baseurl}}/shopify) para a versão mais recente até 28 de agosto de 2025. Esse upgrade é essencial porque mudanças significativas na tecnologia do Shopify vão impactar o funcionamento da nossa integração.

## Quem é elegível? {#whos-eligible}

Essa jornada de upgrade é destinada a marcas com uma loja Shopify headless ou Shopify Hydrogen.

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## Requisitos de upgrade {#upgrade-requirements}

Antes de começar, revise o seguinte:

| Requisito           | Descrição |
|-----------------------|-------------|
| **Mudanças críticas**  | Certifique-se de ter revisado todas as mudanças importantes do conector legado para o novo conector em [Visão geral do upgrade do Shopify]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection). |
| **Pré-requisitos de upgrade** | Certifique-se de ter concluído todos os [pré-requisitos de upgrade]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites) necessários com suas equipes de engenharia e marketing. Para fazer upgrade da sua loja headless do Shopify com a Braze, você precisa concluir duas etapas críticas:<br><br>- Inicializar e carregar o SDK para web da Braze para ativar o rastreamento no site<br>- Fazer upgrade da sua loja existente por meio da experiência de upgrade no produto |
| **Mudanças que causam interrupção**  | Revise e corrija todas as mudanças que causam interrupção sinalizadas na Braze. Para um passo a passo completo, continue em [Corrigindo mudanças que causam interrupção](#fixing-breaking-changes-fixing-breaking-changes). |
{: .reset-td-br-1 .reset-td-br-2  role="presentation"}

## Corrigindo mudanças que causam quebra {#fixing-breaking-changes}

Na Braze, acesse **Integrações de parceiros** > **Shopify** e selecione **Start upgrade**.

![Painel com a opção de iniciar o upgrade.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Todos os Canvas, Campaigns e Segments impactados que usam dados do Shopify serão sinalizados.

![Modal para revisar o que é impactado pelas mudanças que causam quebra.]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

Para a maioria dos eventos, recomendamos incluir os novos eventos e atributos obrigatórios do Shopify usando um operador "OR" para facilitar um upgrade tranquilo das mensagens ativas. Para casos mais específicos, consulte o seguinte:

{% tabs local %}
{% tab Carrinho abandonado %}
Para mensagens de carrinho abandonado, você precisará usar os novos modelos de Canvas de carrinho abandonado, que incluem:

{% multi_lang_include partners/shopify/abandoned_cart_template_features.md %}
{% endtab %}

{% tab Checkout abandonado %}
Para mensagens de checkout abandonado, você precisará usar o novo modelo de Canvas de checkout abandonado, que inclui:

{% multi_lang_include partners/shopify/abandoned_checkout_template_features.md %}

Para uma lista completa dos novos modelos de Canvas de eCommerce e blocos HTML pré-definidos para personalização de produtos disponíveis pela integração, consulte [Crie suas jornadas de usuário no Canvas]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys).

{% alert important %}
Se você não considerar as mensagens ativas que usam eventos descontinuados na integração com o Shopify, as mensagens impactadas não serão mais enviadas aos seus clientes.
{% endalert %}

Para saber mais, revise [Eventos do Shopify suportados]({{site.baseurl}}/shopify_upgrade_overview#supported-shopify-events).
{% endtab %}

{% tab Listas de inscritos %}
Se você está coletando inscritos de e-mail ou SMS do Shopify pela integração, confirme que suas mensagens ativas incluem as listas de inscritos correspondentes para sua loja Shopify.

Quando o upgrade for concluído, novos grupos de inscrições padrão serão criados para sua integração, e você precisará utilizá-los como parte do seu envio de mensagens ativo. Para saber mais sobre as mudanças, consulte [Coleta de inscritos]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection).
{% endtab %}
{% endtabs %}

## Fazendo upgrade do Shopify {#upgrading-shopify}

{% alert important %}
É essencial que você [corrija todas as alterações de quebra](#fixing-breaking-changes) antes de iniciar o upgrade.
{% endalert %}

### Etapa 1: Inicializar e carregar o Braze Web SDK para ativar o rastreamento no site {#step-1}

Se ainda não fez isso, inicialize e carregue o Braze Web SDK para ativar o rastreamento no site. Para um passo a passo completo, consulte [Configuração de integração personalizada do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration#step-1):
- Criar um app web na Braze
- Adicionar subdomínio e variáveis de ambiente
- Ativar o rastreamento no site
- Adicionar um evento de login de conta Shopify
- Adicionar rastreamento para eventos de Produto Visualizado e Atualização de Carrinho

### Etapa 2: Iniciar o upgrade {#step-2-start-the-upgrade}

Na Braze, acesse **Partner Integrations** > **Shopify** e selecione **Start upgrade**.

![Painel com a opção de iniciar o upgrade.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Concorde com as diretrizes de upgrade marcando a caixa e selecione **Start the upgrade**.

![Modal para confirmar que você entende que o upgrade pode causar alterações de quebra.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %}){: style="max-width:50%;"}

Verifique com seus desenvolvedores se você concluiu a Etapa 1 do upgrade do caminho personalizado marcando a caixa e selecione **Confirm**.

![Modal com uma caixa para verificar que você concluiu as etapas de 1 a 5.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_completed_steps.png %}){: style="max-width:50%;"}

{% alert important %}
Para que a integração funcione corretamente, certifique-se de concluir a [Etapa 1](#step-1) do upgrade personalizado. Se você pular esta etapa, a integração pode não funcionar adequadamente.
{% endalert %}

### Etapa 3: Reautorizar o app da Braze {#step-3-reauthorize-the-braze-app}

Para reautorizar o app da Braze, selecione **Go to Shopify**.

![Painel com a opção de acessar o Shopify.]({% image_buster /assets/unlisted_docs/img/shopify/custom_go_to_shopify.png %}){: style="max-width:35%"}

No site do Shopify, siga as instruções para reautorizar o app da Braze. Isso permite que a Braze acesse seus dados do Shopify.

{% alert important %}
O processo de reautorização pode levar alguns minutos, mas será atualizado automaticamente na sua página do Shopify quando for concluído.
{% endalert %}

![Painel de upgrade do Shopify com um ícone giratório ao lado de "Reauthorize the Braze app".]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_app_loading.png %}){: style="max-width:35%;"}

### Etapa 4: Escolher um tipo de ID externo {#step-4-choose-an-external-id-type}

O tipo de ID externo que você escolher será atribuído a novos perfis de clientes do Shopify quando uma conta Shopify for criada ou um pedido for realizado. Ele também será usado para atualizar perfis de usuários existentes se eles já tiverem um alias de ID de cliente Shopify, mas não possuírem um ID externo atribuído na Braze.

Para escolher o tipo de ID externo, volte para a Braze e selecione **Confirm external ID**.

![Painel de upgrade do Shopify com um botão para confirmar o ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/custom_confirm_external_id.png %}){: style="max-width:35%;"}

Escolha o ID externo que deseja usar para a integração do Shopify no seu espaço de trabalho. Quando terminar, selecione **Set external ID**.

![Modal com um menu suspenso para selecionar o ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_custom.png %}){: style="max-width:50%;"}

{% alert important %}
Por padrão, a Braze converte automaticamente os e-mails do Shopify para minúsculas antes de usá-los como ID externo. Se você estiver usando e-mail ou e-mail com hash como ID externo, confirme que seus endereços de e-mail também são convertidos para minúsculas antes de atribuí-los como ID externo ou antes de aplicar o hash a partir de outras fontes de dados. Isso ajuda a evitar discrepâncias nos IDs externos e a criação de perfis de usuários duplicados na Braze.
{% endalert %}

Se você selecionou um tipo de ID externo personalizado, prossiga para as etapas 4.1 a 4.3. Caso contrário, continue para a etapa 5.

#### Etapa 4.1: Criar o metafield `braze.external_id` {#step-41-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

Após a criação do metafield, preencha-o para seus clientes. Recomendamos as seguintes abordagens:

- **Escutar webhooks de criação de clientes:** Configure um webhook para escutar [eventos `customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Isso permite que você grave o metafield quando um novo cliente for criado.
- **Preencher retroativamente clientes existentes:** Use a [Admin API](https://shopify.dev/docs/api/admin-graphql) ou a [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para preencher retroativamente o metafield de clientes criados anteriormente.

#### Etapa 4.2: Criar um endpoint para recuperar o ID externo {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Você precisa criar um endpoint público que a Braze possa chamar para recuperar o ID externo. Isso é necessário para cenários em que o Shopify não pode fornecer o metafield `braze.external_id`.

##### Especificações do endpoint {#endpoint-specifications}

**Método:** `GET`

| Parâmetros | Descrição |
| --- | --- |
| `shopify_customer_id` | O ID do cliente Shopify. |
| `email_address` | O endereço de e-mail do usuário logado. |
| `shopify_storefront` | A storefront da requisição. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Exemplo de endpoint {#example-endpoint}

```
GET
https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```

##### Resposta esperada {#expected-response}

A Braze espera um código de status `200`. Qualquer outro código é considerado uma falha.

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

{% alert important %}
É importante validar que o `shopify_customer_id` e o `email_address` correspondem aos valores do cliente no Shopify. Você pode usar a [Admin API](https://shopify.dev/docs/api/admin-graphql) ou a [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para validar esses parâmetros e recuperar o metafield `braze.external_id`.
{% endalert %}

#### Etapa 4.3: Inserir o ID externo {#step-43-input-your-external-id}

Repita a [Etapa 4](#step-4-choose-an-external-id-type) e insira a URL do seu endpoint após selecionar ID externo personalizado como o tipo de ID externo da Braze.

##### Considerações {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

### Etapa 5: Ativar o app embed da Braze {#step-5-enable-the-braze-app-embed}

Para ativar o app embed da Braze dentro do tema da sua loja, volte para a Braze e selecione Go to Shopify.

![Painel de upgrade do Shopify com um botão para ativar o app embed da Braze.]({% image_buster /assets/unlisted_docs/img/shopify/custom_enable_app_embed.png %}){: style="max-width:35%;"}

No site do Shopify, ative o app embed da Braze e salve suas alterações.

![Um exemplo de app embed.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### Etapa 6: Verificar o upgrade {#step-6-verify-the-upgrade}

De volta à Braze, você será notificado quando a instalação da integração do Shopify for concluída.

![Página de integração do Shopify com um banner de sucesso.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

Para verificar se o novo conector do Shopify está ativo, teste o seguinte:

{% multi_lang_include partners/shopify/upgrade_validation_checklist.md %}

Se tiver alguma dúvida, [entre em contato com o Suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).
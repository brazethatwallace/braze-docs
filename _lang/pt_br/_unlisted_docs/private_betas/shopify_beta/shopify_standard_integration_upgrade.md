---
nav_title: Fazendo upgrade do Shopify
article_title: "Fazendo upgrade da sua integração com o Shopify"
description: "Saiba como fazer upgrade da sua integração com o Shopify para a Braze."
page_type: partner
search_tag: Partner
permalink: "/shopify_standard_upgrade/"
hidden: true
---

# Fazendo upgrade da sua integração com o Shopify (padrão) {#upgrading-your-shopify-integration-standard}

> Saiba como fazer upgrade da sua integração com o Shopify usando o caminho padrão para a Braze. Como parte do nosso compromisso em oferecer a melhor experiência possível, estamos exigindo que todas as integrações com o Shopify façam [upgrade]({{site.baseurl}}/shopify) para a versão mais recente até 28 de agosto de 2025. Esse upgrade é essencial porque mudanças significativas na tecnologia do Shopify impactarão o funcionamento da nossa integração.

## Quem é elegível? {#whos-eligible}

Esse caminho de upgrade é destinado a marcas com uma loja online no Shopify.

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## Requisitos para o upgrade {#upgrade-requirements}

Antes de começar, revise o seguinte:

- **Mudanças críticas:** certifique-se de que você revisou todas as mudanças importantes do conector legado para o novo conector em [Visão geral do upgrade do Shopify]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection).
- **Pré-requisitos do upgrade:** confirme que você concluiu todos os [pré-requisitos do upgrade]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites) necessários com suas equipes de engenharia e marketing.
- **Mudanças que causam quebra:** revise e corrija todas as mudanças que causam quebra sinalizadas na Braze. Para um passo a passo completo, continue em [Corrigindo mudanças que causam quebra](#fixing-breaking-changes-fixing-breaking-changes).

## Corrigindo mudanças que causam quebra {#fixing-breaking-changes}

Na Braze, acesse **Partner Integrations** > **Shopify** e selecione **Start upgrade**.

![Painel com a opção de iniciar o upgrade.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Todos os Canvas, Campaigns e Segments impactados que usam dados do Shopify serão sinalizados.

![Um modal para revisar o que é impactado pelas mudanças que causam quebra.]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

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
É essencial que você [corrija todas as mudanças que causam quebra](#fixing-breaking-changes) antes de iniciar o upgrade.
{% endalert %}

### Etapa 1: Iniciar o upgrade {#step-1-start-the-upgrade}

Na Braze, acesse **Partner Integrations** > **Shopify** e selecione **Start upgrade**.

![Painel com a opção de iniciar o upgrade.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Concorde com os termos e condições marcando a caixa e selecione **Start the upgrade**.

![Modal para confirmar que você entende que o upgrade pode causar mudanças que causam quebra.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %})

### Etapa 2: Configurar os SDKs da Braze {#step-2-set-up-the-braze-sdks}

A integração padrão adicionará automaticamente os SDKs da Braze ao seu site Shopify. Se você já integrou os SDKs da Braze diretamente ou usou uma ferramenta de terceiros para isso, coordene com seus desenvolvedores para remover a implementação anterior do SDK durante o upgrade.

![Modal confirmando que a nova integração implementará automaticamente o SDK da Braze e o JavaScript SDK na sua loja.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_integration.png %}){: style="max-width:70%;"}

### Etapa 3: Reautorizar o app da Braze {#step-3-reauthorize-the-braze-app}

Para reautorizar o app da Braze, selecione **Go to Shopify**.

![Painel de upgrade do Shopify com um botão para ir ao Shopify e reautorizar o app da Braze.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_braze_app.png %}){: style="max-width:35%;"}

No site do Shopify, siga as instruções para reautorizar seu app da Braze. Isso permite que a Braze acesse seus dados do Shopify.

{% alert note %}
O processo de reautorização pode levar alguns minutos, mas será atualizado automaticamente na sua página do Shopify quando for concluído.
{% endalert %}

![A página "Integration Settings" mostrando o status dos eventos do Shopify.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorization_status.png %})

### Etapa 4: Escolher um tipo de ID externo {#step-4-choose-an-external-id-type}

O tipo de ID externo que você escolher será atribuído a novos perfis de clientes do Shopify quando uma conta do Shopify for criada ou um pedido for feito. Ele também será usado para atualizar perfis de usuários existentes se eles já tiverem um alias de ID de cliente do Shopify, mas não tiverem um ID externo atribuído na Braze.

Para escolher seu tipo de ID externo, volte para a Braze e selecione **Confirm external ID**.

![Painel de upgrade do Shopify com um botão para confirmar o ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_external_id.png %}){: style="max-width:35%;"}

Escolha o ID externo que você gostaria de usar para a integração com o Shopify do seu espaço de trabalho. Quando terminar, selecione **Set external ID**.

![Modal com um dropdown para selecionar o ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_field.png %}){: style="max-width:70%;"}

{% alert important %}
Usar um endereço de e-mail ou um endereço de e-mail com hash como seu ID externo da Braze pode ajudar a simplificar o gerenciamento de identidade entre suas fontes de dados. No entanto, é importante considerar os riscos potenciais à privacidade do usuário e à segurança dos dados.<br><br>

- **Informação previsível:** endereços de e-mail são facilmente previsíveis, tornando-os vulneráveis a ataques.
- **Risco de exploração:** se um usuário mal-intencionado alterar seu navegador para enviar o endereço de e-mail de outra pessoa como seu ID externo, ele poderá acessar mensagens sensíveis ou informações da conta.
{% endalert %}

Por padrão, a Braze converte automaticamente os e-mails do Shopify para letras minúsculas antes de usá-los como ID externo. Se você está usando e-mail ou e-mail com hash como seu ID externo, confirme que seus endereços de e-mail também são convertidos para letras minúsculas antes de atribuí-los como seu ID externo ou antes de aplicar o hash a partir de outras fontes de dados. Isso ajuda a evitar discrepâncias nos IDs externos e a criação de perfis de usuário duplicados na Braze.

Se você selecionou um tipo de ID externo personalizado, prossiga para as etapas 4.1 a 4.3. Caso contrário, continue para a etapa 5.

#### Etapa 4.1: Criar o metafield `braze.external_id` {#step-41-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

Após a criação do metafield, preencha-o para seus clientes. Recomendamos as seguintes abordagens:

- **Escutar webhooks de criação de clientes:** configure um webhook para escutar [eventos `customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Isso permite que você preencha o metafield quando um novo cliente é criado.
- **Preencher retroativamente clientes existentes:** use a [Admin API](https://shopify.dev/docs/api/admin-graphql) ou a [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para preencher retroativamente o metafield para clientes criados anteriormente.

#### Etapa 4.2: Criar um endpoint para recuperar seu ID externo {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Você precisa criar um endpoint público que a Braze possa chamar para recuperar o ID externo. Isso é necessário para cenários em que o Shopify não pode fornecer o metafield `braze.external_id`.

##### Especificações do endpoint {#endpoint-specifications}

**Método:** `GET`

| Parâmetros | Descrição |
| --- | --- |
| `shopify_customer_id` | O ID de cliente do Shopify. |
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
{
    "external_id": "my_external_id"
}
```
{% endraw %}

{% alert important %}
É importante validar que o `shopify_customer_id` e o `email_address` correspondem aos valores do cliente no Shopify. Você pode usar a [Admin API](https://shopify.dev/docs/api/admin-graphql) ou a [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para validar esses parâmetros e recuperar o metafield `braze.external_id`.
{% endalert %}

#### Etapa 4.3: Inserir seu ID externo {#step-43-input-your-external-id}

Repita a [Etapa 4](#step-4-choose-an-external-id-type) e insira a URL do seu endpoint após selecionar ID externo personalizado como seu tipo de ID externo da Braze.

##### Considerações {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

### Etapa 5: Ativar o app embed da Braze {#step-5-enable-the-braze-app-embed}

Para ativar o app embed da Braze no tema da sua loja, volte para a Braze e selecione **Go to Shopify**.

![Painel de upgrade do Shopify com um botão para ativar o app embed da Braze.]({% image_buster /assets/unlisted_docs/img/shopify/enable_app_embed.png %}){: style="max-width:35%;"}

No site do Shopify, ative o app embed da Braze e salve suas alterações.

![Um exemplo de app embed.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### Etapa 6: Verificar o upgrade {#step-6-verify-the-upgrade}

De volta à Braze, você será notificado quando a instalação da sua integração com o Shopify for concluída.

![Página de integração com o Shopify com um banner de sucesso.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

Para verificar se o seu novo conector do Shopify está ativo, teste o seguinte:

{% multi_lang_include partners/shopify/upgrade_validation_checklist.md %}

Se você tiver alguma dúvida, [fale com o Suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support).
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

| Requisito | Descrição |
|-----------------------|-------------|
| **Mudanças críticas** | Certifique-se de que você revisou todas as mudanças importantes do conector legado para o novo conector em [Visão geral do upgrade do Shopify]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection). |
| **Pré-requisitos de upgrade** | Certifique-se de que você concluiu todos os [pré-requisitos de upgrade]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites) necessários com suas equipes de engenharia e marketing. Para fazer upgrade da sua loja Shopify headless com a Braze, você precisa concluir duas etapas críticas:<br><br>- Inicializar e carregar o Braze Web SDK para ativar o rastreamento no site<br>- Fazer upgrade da sua loja existente por meio da experiência de upgrade no produto |
| **Mudanças que causam quebra** | Revise e corrija todas as mudanças que causam quebra sinalizadas na Braze. Para um passo a passo completo, continue em [Corrigindo mudanças que causam quebra](#fixing-breaking-changes-fixing-breaking-changes). |
{: .reset-td-br-1 .reset-td-br-2  role="presentation"}

## Corrigindo mudanças que causam quebra {#fixing-breaking-changes}

Na Braze, acesse **Integrações de parceiros** > **Shopify** e selecione **Start upgrade**.

![Painel com a opção de iniciar o upgrade.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Todos os Canvas, Campaigns e Segments impactados que usam dados do Shopify serão sinalizados.

![Modal para revisar o que é impactado pelas mudanças que causam quebra.]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

Para a maioria dos eventos, recomendamos incluir os novos eventos e atributos obrigatórios do Shopify usando um operador "OR" para facilitar um upgrade tranquilo das mensagens ativas. Para casos mais específicos, consulte o seguinte:

{% tabs local %}
{% tab Carrinho abandonado %}
Para mensagens de carrinho abandonado, você precisará usar os novos Modelos de Canvas de carrinho abandonado, que incluem:

- Um novo gatilho baseado na ação "Performed cart updated"
- Critérios de saída pré-definidos para remover clientes que avançaram na jornada de compra
- Uma nova Liquid tag de carrinho de compras para suportar a personalização de produtos
{% endtab %}

{% tab Checkout abandonado %}
Para mensagens de checkout abandonado, você precisará usar o novo Modelo de Canvas de checkout abandonado, que inclui:

- O evento ecommerce.checkout_started pré-definido nos seus critérios de entrada
- Critérios de saída pré-definidos para remover clientes que avançaram na jornada de compra
- Uma nova Liquid tag de carrinho de compras para suportar a personalização de produtos

Para uma lista completa dos novos modelos de Canvas de eCommerce e blocos HTML pré-definidos para personalização de produtos disponíveis pela integração, consulte [Crie suas jornadas de usuário no Canvas]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys).

{% alert important %}
Se você não considerar as mensagens ativas que usam eventos descontinuados na integração com o Shopify, as mensagens impactadas não serão mais enviadas aos seus clientes.
{% endalert %}

Para saber mais, revise [Eventos do Shopify suportados]({{site.baseurl}}/shopify_upgrade_overview#supported-shopify-events).
{% endtab %}

{% tab Listas de inscritos %}
Se você está coletando inscritos de e-mail ou SMS do Shopify pela integração, confirme que suas mensagens ativas incluem as listas de inscritos correspondentes para sua loja Shopify.

Quando o upgrade for concluído, novos grupos de inscrições padrão serão criados para sua integração, e você precisará utilizá-los como parte do seu envio de mensagens ativo. Para mais informações sobre as mudanças, consulte [Coleta de inscritos]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection).
{% endtab %}
{% endtabs %}

## Fazendo upgrade do Shopify {#upgrading-shopify}

{% alert important %}
É essencial que você [corrija todas as mudanças que causam quebra](#fixing-breaking-changes) antes de iniciar o upgrade.
{% endalert %}

### Etapa 1: Inicializar e carregar o Braze Web SDK para ativar o rastreamento no site {#step-1}

Se você ainda não fez isso, inicialize e carregue o Braze Web SDK para ativar o rastreamento no site. Para um passo a passo completo, consulte [Configuração da integração personalizada com o Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration#step-1):
- Crie um app web da Braze
- Adicione subdomínio e variáveis de ambiente
- Ative o rastreamento no site
- Adicione um evento de login de conta Shopify
- Adicione rastreamento para eventos de Product Viewed e Cart Update

### Etapa 2: Iniciar o upgrade {#step-2-start-the-upgrade}

Na Braze, acesse **Integrações de parceiros** > **Shopify** e selecione **Start upgrade**.

![Painel com a opção de iniciar o upgrade.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Concorde com as diretrizes de upgrade marcando a caixa e selecione **Start the upgrade**.

![Modal para confirmar que você entende que o upgrade pode causar mudanças que causam quebra.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %}){: style="max-width:50%;"}

Verifique com seus desenvolvedores que você concluiu a Etapa 1 da jornada de upgrade personalizado marcando a caixa e selecione **Confirm**.

![Modal com uma caixa para verificar que você concluiu as etapas 1 a 5.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_completed_steps.png %}){: style="max-width:50%;"}

{% alert important %}
Para que a integração funcione corretamente, certifique-se de concluir a [Etapa 1](#step-1) do upgrade personalizado. Se você pular essa etapa, a integração pode não funcionar corretamente.
{% endalert %}

### Etapa 3: Reautorizar o app da Braze {#step-3-reauthorize-the-braze-app}

Para reautorizar o app da Braze, selecione **Go to Shopify**.

![Painel com a opção de ir para o Shopify.]({% image_buster /assets/unlisted_docs/img/shopify/custom_go_to_shopify.png %}){: style="max-width:35%"}

No site do Shopify, siga as instruções para reautorizar seu app da Braze. Isso permite que a Braze acesse seus dados do Shopify.

{% alert important %}
O processo de reautorização pode levar alguns minutos, mas será atualizado automaticamente na sua página do Shopify quando for concluído.
{% endalert %}

![Painel de upgrade do Shopify com um ícone de carregamento ao lado de "Reauthorize the Braze app".]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_app_loading.png %}){: style="max-width:35%;"}

### Etapa 4: Escolher um tipo de ID externo {#step-4-choose-an-external-id-type}

O tipo de ID externo que você escolher será atribuído a novos perfis de clientes do Shopify quando uma conta Shopify for criada ou um pedido for feito. Ele também será usado para atualizar perfis de usuários existentes se eles já tiverem um alias de ID de cliente do Shopify, mas não tiverem um ID externo atribuído na Braze.

Para escolher seu tipo de ID externo, volte para a Braze e selecione **Confirm external ID**.

![Painel de upgrade do Shopify com um botão para confirmar o ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/custom_confirm_external_id.png %}){: style="max-width:35%;"}

Escolha o ID externo que você gostaria de usar para a integração com o Shopify do seu espaço de trabalho. Quando terminar, selecione **Set external ID**.

![Modal com um menu suspenso para selecionar o ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_custom.png %}){: style="max-width:50%;"}

{% alert important %}
Por padrão, a Braze converte automaticamente os e-mails do Shopify para letras minúsculas antes de usá-los como ID externo. Se você está usando e-mail ou e-mail com hash como seu ID externo, confirme que seus endereços de e-mail também são convertidos para letras minúsculas antes de atribuí-los como seu ID externo ou antes de aplicar o hash a partir de outras fontes de dados. Isso ajuda a evitar discrepâncias nos IDs externos e a criação de perfis de usuário duplicados na Braze.
{% endalert %}

Se você selecionou um tipo de ID externo personalizado, prossiga para as etapas 4.1 a 4.3. Caso contrário, continue para a etapa 5.

#### Etapa 4.1: Criar o metafield `braze.external_id` {#step-41-create-the-brazeexternal_id-metafield}

1. No painel de administração do Shopify, acesse **Settings** > **Metafields**.
2. Selecione **Customers** > **Add definition**.
3. Em **Namespace and key**, insira `braze.external_id`.
4. Em **Type**, selecione **ID Type**.

Após a criação do metafield, preencha-o para seus clientes. Recomendamos as seguintes abordagens:

- **Escutar webhooks de criação de clientes:** Configure um webhook para escutar [eventos `customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Isso permite que você preencha o metafield quando um novo cliente é criado.
- **Preencher retroativamente clientes existentes:** Use a [Admin API](https://shopify.dev/docs/api/admin-graphql) ou a [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para preencher retroativamente o metafield para clientes criados anteriormente.

#### Etapa 4.2: Criar um endpoint para recuperar seu ID externo {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Você precisa criar um endpoint público que a Braze possa chamar para recuperar o ID externo. Isso é necessário para cenários em que o Shopify não pode fornecer o metafield `braze.external_id`.

##### Especificações do endpoint {#endpoint-specifications}

**Método:** `GET`

| Parâmetros | Descrição |
| --- | --- |
| `shopify_customer_id` | O ID do cliente no Shopify. |
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

#### Etapa 4.3: Inserir seu ID externo {#step-43-input-your-external-id}

Repita a [Etapa 4](#step-4-choose-an-external-id-type) e insira a URL do seu endpoint após selecionar ID externo personalizado como seu tipo de ID externo da Braze.

##### Considerações {#considerations}

- Se o seu ID externo não for gerado quando a Braze enviar uma requisição ao seu endpoint, a integração usará por padrão o ID de cliente do Shopify quando a função `changeUser` for chamada. Essa etapa é crucial para mesclar o perfil de usuário anônimo com o perfil de usuário identificado. Como resultado, pode haver um período temporário durante o qual diferentes tipos de IDs externos existam no seu espaço de trabalho.
- Quando o ID externo estiver disponível no metafield `braze.external_id`, a integração priorizará e atribuirá esse ID externo.
    - Se o ID de cliente do Shopify foi previamente definido como o ID externo da Braze, ele será substituído pelo valor do metafield `braze.external_id`.

### Etapa 5: Ativar o app embed da Braze {#step-5-enable-the-braze-app-embed}

Para ativar o app embed da Braze no tema da sua loja, volte para a Braze e selecione **Go to Shopify**.

![Painel de upgrade do Shopify com um botão para ativar o app embed da Braze.]({% image_buster /assets/unlisted_docs/img/shopify/custom_enable_app_embed.png %}){: style="max-width:35%;"}

No site do Shopify, ative o app embed da Braze e salve suas alterações.

![Exemplo de app embed.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### Etapa 6: Verificar o upgrade {#step-6-verify-the-upgrade}

De volta à Braze, você será notificado quando a instalação da sua integração com o Shopify for concluída.

![Página de integração com o Shopify com um banner de sucesso.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

Para verificar que seu novo conector do Shopify está ativo, teste o seguinte:

- **Canvas, Campaigns e Segments ativos:** Confirme que estão funcionando corretamente.
- **Processos de gerenciamento de identidade:** Confirme que esses processos estão funcionando conforme esperado.
- **Personalizações do SDK (opcional):** Se você fez personalizações na sua integração da Braze com o Shopify (como registrar eventos personalizados ou atributos), verifique se estão funcionando corretamente após o upgrade.
- **Coleta de inscritos de e-mail ou SMS (opcional):** Se você ativou anteriormente a coleta de inscritos de e-mail ou SMS, novos grupos de inscrições padrão serão criados para refletir o status mais recente dos seus inscritos durante o upgrade. Os grupos de inscrições padrão terão o nome da sua storefront do Shopify. Esses novos grupos de inscrições padrão estarão disponíveis aproximadamente 5 horas após o upgrade, e você precisará adicioná-los às suas mensagens ativas.

Se você tiver alguma dúvida, [fale com o Suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support).
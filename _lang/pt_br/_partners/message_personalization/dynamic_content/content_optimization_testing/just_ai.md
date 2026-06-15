---
nav_title: JustAI
article_title: JustAI
description: "Este artigo de referência descreve a parceria entre a Braze e a JustAI, uma plataforma SaaS de negócios baseada em IA que cria versões personalizadas de campanhas existentes e otimiza linhas de assunto, conteúdo criativo e layouts de e-mail HTML ao longo do tempo."
alias: ["/partners/just_ai/", "/partners/just_words/"]
page_type: partner
---

# Guia de integração da JustAI {#justai-integration-guide}

> A [JustAI](https://www.getjust.ai/) hiperpersonaliza mensagens em escala nos canais de marketing de ciclo de vida, permitindo que você teste dinamicamente centenas de variações e atualize automaticamente conteúdos com baixo desempenho.

Quando você usa a JustAI com o [Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) da Braze para personalizar suas Campaigns e Canvas existentes na Braze, a JustAI usa o Braze Currents para otimizar o conteúdo dinamicamente — para que você não precise fazer isso.

## Quais são os benefícios? {#what-are-the-benefits}

Após a conclusão da integração, você pode aproveitar a plataforma JustAI para:

- Ver resultados de experimentos em tempo real
- Editar textos dinamicamente
- Visualizar insights de desempenho

{% alert note %}
Dúvidas? Entre em contato com a JustAI pela [página de agendamento](https://www.getjust.ai/book-demo) ou pelo canal compartilhado no Slack.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta JustAI | Uma conta na [JustAI](https://www.getjust.ai/) é necessária para aproveitar essa parceria. Se você não tem uma conta JustAI, [agende uma chamada de integração de 30 minutos](https://www.getjust.ai/book-demo). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integrando a JustAI com a Braze {#integrating-justai-with-braze}

### Etapa 1: Criar um modelo JustAI {#step-1-create-a-justai-template}

1. Acesse o console da JustAI e [crie um novo modelo](https://console.getjust.ai/new).
2. Escolha um ID fácil de lembrar que use apenas letras, números e underscores.
3. Preencha os detalhes básicos da campanha.
4. Use a IA para gerar variações personalizadas.

![A plataforma de criação de modelos da JustAI.]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### Etapa 2: Criar uma chave de API da JustAI {#step-2-create-a-justai-api-key}

1. Acesse **Org Settings** > **API Keys** > **Generate API Key**.
2. Copie e salve a chave de API em um local seguro.

![O formulário de chave de API da JustAI.]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### Etapa 3: Usar a JustAI no seu conteúdo da Braze {#step-3-use-justai-in-your-braze-content}

A JustAI funciona com Canvas e Campaigns usando Conteúdo conectado. Se você estiver criando um Canvas, cada etapa de e-mail deve corresponder a um modelo JustAI exclusivo.

#### Etapa 3.1: Configurar seu teste A/B {#step-31-set-up-your-ab-test}

{% tabs %}
{% tab Canvas %}

1. Em um Canvas, selecione **Add Variant** > **Add Variant** até ter o número desejado de variantes e adicione etapas a cada variante (como uma etapa de mensagem de e-mail).
2. Divida o tráfego do público conforme desejado. Por exemplo, se você tiver duas variantes, pode dar 50% para cada uma. Ou pode ter duas variantes com 40% cada e um grupo de controle com 20%. Para saber mais sobre testes A/B para Canvas, consulte [Criando um Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
3. Nos criadores das etapas de mensagem que você deseja usar com Conteúdo conectado, cole o snippet de Conteúdo conectado do console da JustAI, como o snippet a seguir.

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Configuração de teste A/B em Canvas na Braze.]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Campaign %}

1. Na etapa **Compose Messages** da sua Campaign, crie duas variantes.
2. Na etapa **Target Audience**, acesse a seção **A/B Testing** e modifique as porcentagens de usuários que receberão cada uma das suas variantes (e seu grupo de controle opcional). Você pode personalizar ainda mais seu teste selecionando uma opção de otimização. Para saber mais sobre testes A/B para Campaigns, consulte [Criando testes multivariantes e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/).
3. No criador de mensagens, cole o snippet de Conteúdo conectado do console da JustAI. O snippet Liquid a seguir mostra um exemplo disso.

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Etapa 3.2: Adicionar personalização com atributos personalizados (opcional) {#step-32-add-personalization-with-custom-attributes-optional}

Para personalizar suas mensagens com atributos personalizados (como `industry`), use o seguinte formato Liquid:

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

Observe que o atributo personalizado `industry` é indicado por {% raw %}`&attrs.industry={{ custom_attribute.industry }}`{% endraw %}.

![Lógica Liquid da Braze em um criador de mensagens HTML.]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### Etapa 4: Pré-visualizar o e-mail {#step-4-preview-the-email}

Certifique-se de pré-visualizar o e-mail na Braze para confirmar que o conteúdo personalizado é renderizado corretamente.

![Pré-visualização de mensagem na Braze para um e-mail da JustAI.]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### Etapa 5: Configurar o Braze Currents {#step-5-set-up-braze-currents}

O Braze Currents permite o rastreamento de desempenho e a otimização ao longo do tempo.

1. Na Braze, acesse **Partner Integrations** > **Data Export**.
2. Selecione **Create New Test Current** e depois selecione **Test Amazon S3 Data Export**.

![Menu suspenso "Create New Test Current" com a opção "Test Amazon S3 Data Export".]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3. Insira o S3 Access ID, a AWS Secret Access Key, o nome do bucket e a pasta fornecidos pela JustAI durante a integração.

![Seção "Credentials" para a chave de acesso secreta da AWS.]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4. Selecione os eventos a serem rastreados, como envios, aberturas, cliques, cancelamentos de inscrição, conversões e outros.

![Seção "Message Engagement Events" com eventos para selecionar.]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5. Lance o Braze Current.

Tudo pronto! Agora você pode usar a JustAI com o Conteúdo conectado da Braze.
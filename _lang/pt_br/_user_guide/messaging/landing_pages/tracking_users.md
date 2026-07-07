---
nav_title: Rastrear usuários
article_title: Rastrear usuários por meio de um formulário
description: "Saiba como identificar usuários que enviam um formulário pela sua landing page adicionando uma Liquid tag às suas mensagens."
page_order: 2
---

# Rastrear usuários por meio de um formulário {#track-users-through-a-form}

> Saiba como rastrear usuários que enviam um formulário pela sua landing page adicionando uma Liquid tag de landing page às suas mensagens. Essa Liquid tag é compatível com todos os canais de envio de mensagens da Braze, incluindo e-mail, SMS, mensagens no app e muito mais. Para saber mais sobre rastreamento de dados, consulte [Sobre dados de rastreamento de landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/about_tracking_data).

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará criar uma [landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) e uma [campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign).

## Como funciona {#how-it-works}

Você pode adicionar uma Liquid tag {% raw %}`{% landing_page_url %}`{% endraw %} a qualquer uma das suas mensagens de canal único ou multicanal na Braze. Quando um usuário visitar essa landing page e enviar o formulário, a Braze vinculará automaticamente esses dados ao perfil existente dele, em vez de criar um novo perfil para esse usuário. No exemplo a seguir, a Liquid tag de landing page é usada para direcionar clientes a uma pesquisa:

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
Você também pode usar landing pages para geração de leads incorporando a URL da página nos seus canais externos. Depois de criar uma landing page, acesse **Landing Page Details** para obter a URL exclusiva da sua landing page.
{% endalert %}

## Usando Liquid tags de landing page {#using-landing-page-liquid-tags}

### Etapa 1: Verificar a URL da página {#page-url}

A Braze usará a URL da sua landing page para gerar a Liquid tag exclusiva. Se você quiser alterar a URL atual da página, acesse **Messaging** > **Landing Pages** e abra sua landing page. Em **page URL**, você pode inserir uma nova URL de página.

{% alert warning %}
Se você alterar a URL da página após enviar sua mensagem, qualquer usuário que tentar visitar sua landing page usando a URL antiga será direcionado para uma página `404`.
{% endalert %}

![Um exemplo de URL de página para uma landing page na Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### Etapa 2: Gerar a Liquid tag {#step-2-generate-the-liquid-tag}

Acesse **Messaging** > **Campaigns** e escolha uma campaign. No editor de mensagens, selecione **Personalization**.

![O botão "Add personalization" no editor de arrastar e soltar.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

A Braze gerará automaticamente uma Liquid tag usando a [URL da sua landing page](#page-url). Consulte a tabela a seguir para gerar sua tag:

| **Tipo de personalização** | Escolha **Landing Page**. |
| **Landing page** | Escolha a landing page [que você criou anteriormente](#prerequisites). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Gerar a Liquid tag" }

Para adicionar a Liquid tag à sua mensagem, você pode selecionar **Inserir** ou copiar o snippet para a área de transferência e adicioná-lo manualmente.

![Uma Liquid tag gerada automaticamente para a landing page selecionada.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

Seu snippet será semelhante ao seguinte:

{% raw %}
```ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### Etapa 3: Finalizar e enviar sua mensagem {#step-3-finalize-and-send-your-message}

Incorpore o snippet Liquid na sua mensagem e finalize o restante da mensagem. Por exemplo:

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

Quando estiver tudo pronto, você pode enviar a mensagem para começar a rastrear usuários pela sua landing page.
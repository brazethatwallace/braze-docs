---
nav_title: Redirecionar usuários
article_title: Redirecionar usuários
description: "Saiba como redirecionar usuários que enviaram um formulário por meio de uma landing page."
page_order: 3
---

# Redirecionar usuários por meio de uma landing page {#retarget-users-through-a-landing-page}

> Saiba como redirecionar usuários que enviaram um formulário por meio de uma landing page criando um segmento dedicado ou disparando uma mensagem quando o formulário é enviado.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará criar uma [landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

## Redirecionamento de usuários {#retargeting-users}

A Braze rastreia automaticamente quando um usuário envia um formulário de landing page. Você pode visualizar o número total de envios de um formulário em [análise de dados de landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#view-analytics). No entanto, para redirecionamento específico por usuário, você precisará redirecionar os usuários por meio do formulário da sua landing page usando um dos seguintes métodos:

- **Usando um Segment:** Você pode criar um novo Segment para identificar automaticamente os usuários que enviaram ou não um formulário de landing page.
- **Usando um disparador de mensagem:** Você pode configurar um disparador de mensagem para enviar mensagens automaticamente aos usuários ou inseri-los em um Canvas após o envio do formulário.

{% tabs local %}
{% tab Usando um Segment %}
Ao [criar um Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), no grupo "Redirecionamento", escolha **Submitted form on Landing Page**.

![Criação de Segment com o grupo de filtros selecionado como "Submitted Form on Landing Page".]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

A partir daqui, você pode segmentar os usuários com base em terem ou não enviado um formulário de landing page para a sua landing page.
{% endtab %}

{% tab Usando um disparador de mensagem %}
Ao escolher a opção de entrega para a sua [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou [Canvas]({{site.baseurl}}/user_guide/messaging/canvas), selecione **Action Based Delivery** e, em seguida, **Submitted Landing Page form**.

Todos os usuários que enviarem um formulário por meio dessa landing page receberão uma mensagem pelo canal de envio de mensagens escolhido ou serão inseridos no Canvas escolhido.

![Ação-gatilho de landing page no envio de mensagens.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
A opção de entrega baseada em ação para landing pages não está disponível para mensagens no app. Para direcionar usuários que enviaram um formulário em uma landing page com uma mensagem no app, selecione o filtro **Submitted Form on Landing Page** nas **Targeting Options** da sua Campaign.
{% endalert %}

{% endtab %}
{% endtabs %}
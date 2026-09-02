---
nav_title: Redirecionar usuários
article_title: Redirecionar usuários
description: "Saiba como redirecionar usuários que enviaram um formulário por meio de uma landing page."
page_order: 3
---

# Redirecionar usuários por meio de uma landing page {#retarget-users-through-a-landing-page}

> Saiba como redirecionar usuários que enviaram um formulário por meio de uma landing page criando um Segment or segmento or segmento dedicado ou disparando uma mensagem quando o formulário é enviado.

## Pré-requisitos {#prerequisites}

Antes de começar, crie uma [landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

## Redirecionamento de usuários {#retargeting-users}

A Braze rastreia automaticamente quando um usuário envia um formulário de landing page. Você pode visualizar o número total de envios de um formulário em [análise de dados de landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#view-analytics). Para redirecionamento específico de usuários, redirecione usuários por meio do formulário da sua landing page usando um dos seguintes métodos:

{% tabs local %}
{% tab Usando um Segment or segmento %}

Crie um novo Segment or segmento para identificar automaticamente os usuários que enviaram ou não um formulário de landing page. Ao [criar um Segment or segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), no grupo "Retargeting", escolha **Submitted Form on Landing Page**.

![Criação de Segment com o grupo de filtros selecionado como "Submitted Form on Landing Page".]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

A partir daqui, você pode segmentar usuários com base em terem ou não enviado um formulário de landing page para a sua landing page.
{% endtab %}

{% tab Usando um disparador de mensagem %}

Configure um disparador de mensagem para enviar mensagens automaticamente aos usuários ou inseri-los em um Canvas após o envio do formulário. Ao escolher a opção de entrega para sua [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou [Canvas]({{site.baseurl}}/user_guide/messaging/canvas), selecione **Action Based Delivery** e, em seguida, **Submitted a Landing Page form**.

Todos os usuários que enviarem um formulário por meio desse formulário de landing page receberão mensagens pelo canal de envio de mensagens escolhido ou serão inseridos no Canvas escolhido.

![Ação-gatilho de landing page no envio de mensagens.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
A opção de entrega baseada em ação para landing pages não está disponível para mensagens no app. Para direcionar usuários que enviaram um formulário em uma landing page com uma mensagem no app, selecione o filtro **Submitted Form on Landing Page** nas **Targeting Options** da sua Campaign.
{% endalert %}

{% endtab %}
{% endtabs %}

### Formulário de múltiplas etapas {#multi-step-form}

Para um [formulário de múltiplas etapas]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms), ambos os métodos de redirecionamento dependem do evento **Submitted a Landing Page form**, que só é registrado após o usuário concluir todas as etapas. Um usuário que envia algumas etapas, mas não todas, tem os dados salvos no perfil, mas não é incluído em nenhum dos métodos até concluir o formulário inteiro. Para saber mais, consulte [Rastrear dados de formulários parcialmente preenchidos]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms#track-data-from-partially-completed-forms).
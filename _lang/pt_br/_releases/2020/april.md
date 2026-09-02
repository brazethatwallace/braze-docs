---
nav_title: Abril
page_order: 9
noindex: true
page_type: update
description: "Este artigo contém notas de versão de abril de 2020."
---
# Abril de 2020 {#april-2020}

## Parceria com a Movable Ink {#movable-ink-partnership}

A Movable Ink oferece aos clientes da Braze a capacidade de usar recursos do Intelligent Creative, como cronômetros de contagem regressiva, enquetes e raspadinhas em suas campanhas de push, mensagens no app e cartões de conteúdo. A Movable Ink e a Braze oferecem uma abordagem mais completa para mensagens dinâmicas orientadas por dados, fornecendo aos usuários elementos em tempo real sobre as coisas que importam.

Comece a [integrar a Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/) em suas campanhas!

## Intelligent Timing

Ao programar uma campanha, você pode usar o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) (anteriormente chamado de Intelligent Delivery) para entregar sua mensagem a cada usuário no momento em que a Braze determina que um indivíduo tem maior probabilidade de engajamento.

As atualizações desse recurso incluem:
- **Esclarecimento sobre o horário de silêncio**: A funcionalidade do horário de silêncio permanece a mesma, mas a interface do usuário foi ajustada para maior clareza.
- **Adição do gráfico de prévia**: Agora é possível gerar um gráfico para ver quantos usuários receberão mensagens para cada hora do dia com o Intelligent Timing, bem como qual proporção de usuários tem dados suficientes para calcular um horário ideal.
- **Adição de fallback personalizado**: Agora é possível escolher o horário local no qual enviar uma mensagem aos usuários quando não houver dados de engajamento suficientes para calcular um horário ideal.

## Exportação do público do Facebook {#facebook-audience-export}

A Braze oferece a capacidade de exportar manualmente seus usuários da página Braze Segments para criar públicos personalizados do Facebook. Essa é uma exportação única e estática de público e só criará novos [públicos personalizados do Facebook]({{site.baseurl}}/partners/facebook/).

Disponível para todos os clusters, um novo processo de exportação de público do Facebook da Braze simplifica o fluxo de trabalho com etapas de integração claras. Você não precisa mais colocar os URIs de redirecionamento OAuth na lista de permissões para enviar públicos personalizados ou ajustar as configurações do app do Facebook para fazer a integração.

{% alert important %}
Observe que todos os clientes que atualmente usam o Facebook Custom Audiences devem reintegrar seus Segments da Braze com essas novas etapas.
{% endalert%}


## Atualizações da API or interface de programação do aplicativo (API) do bloco de conteúdo e do modelo de e-mail {#content-block-and-email-template-api-updates}

Os endpoints da API or interface de programação do aplicativo (API) [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) e [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) foram atualizados para incluir um novo campo `tags`. Esse campo listará, como uma matriz, todas as tags que se aplicam ao bloco ou modelo de e-mail atual.

## Endereço de remetente personalizado {#personalized-from-address}

Ao criar uma mensagem de e-mail na Braze, agora é possível personalizar o endereço do remetente da mensagem na seção **Informações de envio** da composição do e-mail. Você pode usar qualquer uma de nossas [tags de personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) compatíveis

![Endereço de remetente personalizado]({% image_buster /assets/img/personalized-from-name.png %}){: style="max-width:80%"}
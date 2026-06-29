---
nav_title: "Botões de ação por push"
article_title: "Botões de ação por push"
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o que são botões de ação por push e as diferenças entre as plataformas iOS e Android."
channel:
  - Push

---

# Botões de ação por push {#push-action-buttons}

> Os botões de ação por push permitem definir conteúdo e ações para botões ao usar notificações por push da Braze para iOS e Android. Com os botões de ação, seus usuários podem interagir diretamente com o app a partir de uma notificação, sem precisar abrir a experiência do app.

![Uma notificação por push do iOS com dois botões de ação por push: Accept e Decline.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

## Criando botões de ação {#creating-action-buttons}

Cada botão interativo pode direcionar para uma página da web, um deep link ou abrir o app.

- Para Campaigns de push padrão, você pode especificar seus botões de ação por push na seção **Comportamento ao clicar** do criador de mensagens push no dashboard.
- Para [Campaigns de push multiplataforma]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push/), os botões de ação podem ser configurados separadamente para cada plataforma na guia **Configurações**.

{% tabs %}
{% tab iOS %}
### iOS {#ios}

Para usar botões de ação nas suas mensagens push do iOS, faça o seguinte:

1. Ative os botões de ação na guia **Redigir**
2. Selecione sua **iOS Notification Category** entre as seguintes combinações de botões disponíveis:
 - Accept / Decline
 - Yes / No
 - Confirm / Cancel
 - More
 - Categoria personalizada do iOS pré-registrada

![Menu suspenso de categoria de notificação do iOS.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
Devido à forma como o iOS lida com botões, é necessário realizar etapas adicionais de integração ao configurar botões de ação por push, que estão descritas na nossa [documentação para desenvolvedores]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories). Em particular, você precisa configurar as categorias do iOS ou selecionar entre certas opções de botões padrão. Para integrações Android, esses botões funcionam automaticamente.
{% endalert %}

Pares predefinidos como **Yes** / **No** mapeiam o segundo botão para uma ação de descarte (**CLOSE**) por padrão, então ele não abre o app da mesma forma que o primeiro botão. **_Aberturas diretas_** não incluem esse tipo de toque, mas os dados de **Push Notification Open** no Currents ou Snowflake ainda podem registrá-lo com `button_action_type` e `button_string`. Para saber mais, consulte [Botões de ação por push e relatórios]({{site.baseurl}}/user_guide/channels/push/reporting/#push-action-buttons-and-reporting).
{% endtab %}
{% tab Android %}
### Android {#android}

Para usar botões de ação nas suas mensagens push do Android, faça o seguinte:

1. Ative os botões de ação na guia **Redigir**
2. Selecione <i class="fas fa-plus-circle"></i> **Add Button** e especifique o texto do botão e o **Comportamento ao clicar**. Você pode selecionar entre as seguintes ações disponíveis:
  - Open App
  - Redirect to Web URL
  - [Deep link]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/) Into Application

![Selecionando "Open App" como o comportamento ao clicar para um botão de notificação.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Você pode adicionar até três botões no seu push.

#### Limites de caracteres no Android {#android-character-limits}

Diferentemente dos botões do iOS, que são empilhados, os botões do Android são exibidos lado a lado em uma linha. Isso significa que quanto mais botões você adicionar (até três), menos espaço terá para o texto do botão.

![Botões de ação por push do Android com texto truncado.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

A tabela a seguir mostra quantos caracteres você pode adicionar antes que o texto do botão seja truncado, dependendo de quantos botões você tem:

| Número de botões | Máximo de caracteres por botão |
| --- | --- |
| 1 | 46 caracteres |
| 2 | 20 caracteres |
| 3 | 11 caracteres |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites de caracteres no Android" }
{% endtab %}
{% endtabs %}
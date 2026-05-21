---
nav_title: Push
article_title: Push
page_order: 7
page_type: landing
description: "Envie chamadas para ação urgentes por meio de notificações por push para dispositivos móveis e web para reengajar usuários e impulsionar ações."
channel:
  - Push
search_rank: 3
---

# Push {#push}

> As notificações por push são uma forma comprovada de enviar chamadas para ação urgentes por meio de dispositivos móveis ou web, além de reengajar usuários que não acessam o app há algum tempo. Elas direcionam o usuário diretamente ao conteúdo e demonstram o valor do seu aplicativo.

[![curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## Pré-requisitos {#prerequisites}

Antes de começar, certifique-se de ter o seguinte:

- **Push integrado ao seu app ou site.** Trabalhe com seus desenvolvedores para configurar isso. Para etapas detalhadas, consulte os guias de integração para [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android) e [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).
- **Uma estratégia de opt-in para push.** Os usuários devem conceder permissão de push em seus dispositivos. Considere usar [mensagens no app de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/) para explicar o valor antes de solicitar a permissão.

## Casos de uso {#use-cases}

| Caso de uso | Explicação |
| --- | --- |
| Integração inicial | Até que os usuários realizem as etapas iniciais para usar seu app (como registrar uma conta), o valor deles é bastante limitado. Use notificações por push para incentivar os usuários a concluir essas etapas para que possam começar a usar seu app por completo. |
| Primeiras compras | Depois que os usuários estiverem confortáveis usando seu app, você pode usar notificações por push para ajudar a convertê-los em compradores dentro do app. |
| Novos recursos | As notificações por push podem ser eficazes para informar usuários desengajados sobre novos recursos que podem atraí-los de volta ao seu app. |
| Ofertas por tempo limitado | Se você tem uma oferta com prazo, o push é uma ótima maneira de avisar seus usuários antes que ela expire. Essas mensagens geralmente carregam um alto senso de urgência e são ideais para lembrar usuários recentemente inativos sobre seu app. Por exemplo, se seu app é um jogo e você oferece um bônus de moeda no jogo por uma sequência diária de partidas, alertar um usuário de que sua sequência está em risco pode ser um push eficaz depois que ele atingir um certo número de dias. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

## Regulamentações de mensagens push {#push-message-regulations}

O push alcança o dispositivo do seu cliente diretamente, então as políticas de apps e lojas restringem como você pode usá-lo.

{% alert important %}
Suas mensagens push devem seguir as [Diretrizes de Revisão da Apple App Store](https://developer.apple.com/app-store/review/guidelines/) e as [políticas do Google Play](https://support.google.com/googleplay/android-developer/answer/9888379). Isso inclui regras sobre o uso de push para anúncios, spam, promoções e tópicos relacionados.
{% endalert %}

| Fonte da política | Resumo |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | Usos inaceitáveis incluem criar uma interface para exibir apps, extensões ou plug-ins de terceiros semelhante à App Store ou como uma coleção de interesse geral. |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | O push não deve ser necessário para o funcionamento do app e não deve conter informações pessoais sensíveis ou confidenciais. Não use push para promoções ou marketing direto, a menos que os clientes façam opt-in explicitamente por meio de linguagem de consentimento na interface do seu app e possam cancelar a inscrição dentro do app. |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | Você não pode monetizar recursos integrados como notificações por push, a câmera ou o giroscópio, nem serviços da Apple como Apple Music ou iCloud. |
| Google Play — [Uso não autorizado ou imitação de funcionalidade do sistema](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | Os apps não devem imitar ou interferir nas notificações do sistema. Notificações em nível de sistema são apenas para recursos essenciais do app (por exemplo, um app de companhia aérea notificando usuários sobre ofertas ou um jogo notificando usuários sobre promoções dentro do jogo). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Regulamentações de mensagens push" }

## Próximas etapas {#next-steps}

- [Configuração de push]({{site.baseurl}}/user_guide/channels/push/push_setup/)
- [Criar uma mensagem push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/)
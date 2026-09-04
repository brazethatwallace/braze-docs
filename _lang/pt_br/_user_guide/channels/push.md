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

> As notificações por push enviam chamadas para ação urgentes para dispositivos móveis e web, reengajando usuários que não acessaram o app recentemente. Elas direcionam o usuário diretamente ao conteúdo relevante e demonstram o valor contínuo do seu produto. Este hub aborda integração de push, estratégia de aceitação, tipos de mensagem, práticas recomendadas e configurações específicas de plataforma para iOS, Android e Web. Considere usar [mensagens no app de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) antes de solicitar a permissão do sistema. Consulte os guias de integração para [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android) e [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web) para começar.

[![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## Pré-requisitos {#prerequisites}

Antes de começar, verifique se você tem o seguinte:

- **Push integrado ao seu app ou website.** Trabalhe com seus desenvolvedores para configurar isso. Para etapas detalhadas, consulte os guias de integração para [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android) e [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web).
- **Uma estratégia de aceitação de push.** Os usuários precisam conceder permissão de push em seus dispositivos. Considere usar [mensagens no app de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) para explicar o valor antes de solicitar a permissão.

## Casos de uso {#use-cases}

| Caso de uso | Explicação |
| --- | --- |
| Integração inicial | Até que os usuários realizem as etapas iniciais para usar seu app (como registrar uma conta), o valor deles é bastante limitado. Use notificações por push para incentivar os usuários a concluir essas etapas, para que possam começar a usar seu app por completo. |
| Primeiras compras | Depois que os usuários estiverem confortáveis usando seu app, você pode usar notificações por push para ajudar a convertê-los em compradores dentro do app. |
| Novos recursos | Notificações por push podem ser eficazes para informar usuários desengajados sobre novos recursos que podem atraí-los de volta ao seu app. |
| Ofertas por tempo limitado | Se você tem uma oferta com prazo, o push é uma ótima maneira de avisar seus usuários antes que ela expire. Essas mensagens geralmente transmitem um alto senso de urgência e são ideais para lembrar usuários que pararam de usar o app recentemente. Por exemplo, se seu app é um jogo e você oferece um bônus de moeda do jogo por uma sequência diária de partidas, alertar um usuário de que sua sequência está em risco pode ser um push eficaz depois que ele atingir um determinado número de dias. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

## Regulamentações para mensagens push {#push-message-regulations}

O push chega diretamente ao dispositivo do seu cliente, por isso as políticas de apps e lojas regulam como você pode usá-lo.

{% alert important %}
Suas mensagens push devem seguir as [Diretrizes de Análise da Apple App Store](https://developer.apple.com/app-store/review/guidelines/) e as [políticas do Google Play](https://support.google.com/googleplay/android-developer/answer/9888379). Isso inclui regras sobre o uso de push para anúncios, spam, promoções e tópicos relacionados.
{% endalert %}

| Fonte da política | Resumo |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | Usos inaceitáveis incluem criar uma interface para exibir apps, extensões ou plug-ins de terceiros semelhante à App Store ou como uma coleção de interesse geral. |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | O push não deve ser obrigatório para o funcionamento do app e não deve conter informações pessoais sensíveis ou confidenciais. Não use push para promoções ou marketing direto, a menos que os clientes aceitem explicitamente por meio de uma linguagem de consentimento na interface do app e possam cancelar a aceitação no próprio app. |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | Você não pode monetizar recursos integrados, como notificações por push, câmera ou giroscópio, nem serviços da Apple, como Apple Music ou iCloud. |
| Google Play — [Uso não autorizado ou imitação de funcionalidades do sistema](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | Os apps não devem imitar ou interferir nas notificações do sistema. Notificações no nível do sistema são permitidas apenas para recursos essenciais do app (por exemplo, um app de companhia aérea notificando usuários sobre ofertas, ou um jogo notificando usuários sobre promoções dentro do jogo). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Regulamentações para mensagens push" }

## Perguntas frequentes {#frequently-asked-questions}

### Quando a Braze registra um envio bem-sucedido de push? {#when-does-braze-record-a-successful-send-for-push}

A Braze normalmente registra um **Envio** assim que a mensagem é despachada da Braze para a Apple, o Google ou seu serviço de web push. **Entregas**, aberturas, bounces e sinais de desinstalação são rastreados separadamente e podem chegar depois. Use as análises no nível da etapa e da Campaign junto com a [solução de problemas de push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) quando os **Envios** e as métricas subsequentes parecerem desalinhados.

## Próximos passos {#next-steps}

{% article_tiles %}
- name: Configuração de push
  link: /docs/user_guide/channels/push/push_setup
  description: Integre o push e defina as configurações de plataforma para iOS, Android e Web.
- name: Criar uma mensagem push
  link: /docs/user_guide/channels/push/create_a_push_message
  description: Crie e envie Campaigns e Canvas de push.
{% endarticle_tiles %}
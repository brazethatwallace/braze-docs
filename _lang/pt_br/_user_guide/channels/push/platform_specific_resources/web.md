---
nav_title: "Push para a web"
article_title: Notificações por push para a web
page_order: 8.5
page_type: reference
description: "Esta página de referência aborda brevemente as notificações por push para a web e fornece links para as etapas necessárias para criar uma."
platform: Web
channel:
  - Push
---

# Push para a web {#web-push}

> Saiba mais sobre notificações por push para a web na Braze e encontre recursos para criar as suas.

O push para a web é outra ótima maneira de engajar os usuários do seu aplicativo web. Os clientes que visitam seu site a partir de [navegadores compatíveis](#supported-browsers) podem aceitar receber push para a web do seu aplicativo, esteja a página carregada ou não.

## Pré-requisitos {#prerequisites}

Antes de criar e enviar qualquer mensagem push usando a Braze, você precisa trabalhar com seus desenvolvedores para integrar o push ao seu site. Para etapas detalhadas, consulte nosso [guia de integração de push para a web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web).

### Permissão de push {#push-permission}

Qualquer marca pode integrar e usar notificações por push para a web em seu site. As notificações podem alcançar visitantes atuais e anteriores, desde que tenham um navegador aberto, mas os visitantes devem [aceitar receber notificações]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#push-permission) — assim como no push tradicional de apps móveis.

{% alert tip %}
Considere usar uma mensagem no navegador para preparar os usuários a aceitar o push para a web, também conhecido como [push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).
{% endalert %}

## Visão geral {#overview}

As notificações por push para a web entregam atualizações urgentes e acionáveis que impulsionam conversões rápidas. Com o push para a web, você pode:

- Disparar mensagens assim que dados importantes mudam, como uma queda de preço
- Trazer as pessoas de volta ao seu site com botões de call-to-action claros
- Personalizar seu push com informações de produtos e clientes para tornar sua mensagem relevante

O push para a web funciona da mesma forma que as notificações por push de apps funcionam no seu celular. Para saber mais sobre como compor um push para a web, confira [Criar uma notificação por push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#creating-a-push-message).

![Exemplo de push para a web com a mesma mensagem push exibida em um laptop e um celular.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Possíveis casos de uso {#potential-use-cases}

Aqui estão alguns exemplos de casos de uso comuns de mensagens push para a web.

| Caso de uso | Descrição |
| --- | --- |
| Teste gratuito | Incentive novos visitantes do seu site a se inscreverem para testes gratuitos. Ao atrair os usuários com a chance de experimentar o que torna você especial, você aumenta a probabilidade de que se tornem clientes pagantes. |
| Download do app | Direcione os usuários da web para o seu app móvel para que obtenham ainda mais valor dos seus produtos. Considere usar personalização para destacar os benefícios do app com base nos padrões de engajamento atuais. |
| Descontos e promoções | Aumente a conscientização dos clientes sobre eventos e promoções com prazo limitado. Envie mensagens por múltiplos canais, incluindo push para a web, para aumentar a visibilidade das promoções da sua marca. |
| Abandono de carrinho | Envie lembretes automatizados para usuários que não concluíram suas transações, trazendo-os de volta ao fluxo de checkout. <br><br>Uma pesquisa realizada pela Braze descobriu que o push para a web é 53% mais eficaz que o e-mail e 23% mais impactante que o push móvel para fazer com que os destinatários voltem e concluam uma compra. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Possíveis casos de uso" }

## Navegadores compatíveis {#supported-browsers}

Os seguintes navegadores são compatíveis com notificações por push para a web.

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

- Chrome (e Chrome para Android)
- Safari (versão 16 ou mais recente)
- Firefox (e Firefox para Android)
- Opera
- Edge

Para saber mais sobre os padrões do protocolo de push e a compatibilidade de navegadores, você pode consultar recursos com base no seu navegador:

- [Safari (desktop)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (mobile)]({{site.baseurl}}/developer_guide/push_notifications?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)

## Endpoints de push para a web 410 (Gone) e inválidos {#410-gone-and-invalid-web-push-endpoints}

Navegadores e serviços de push podem retornar **410 Gone** (ou erros semelhantes de "endpoint inválido") quando uma inscrição de push para a web não é mais aceita. As causas comuns incluem:

- O usuário desativou as notificações do seu site nas configurações do navegador ou do sistema operacional.
- Um perfil de usuário diferente se inscreveu no mesmo perfil de navegador, então o endpoint foi rotacionado para o novo inscrito.
- A inscrição expirou após um longo período sem engajamento — depois que o usuário aceitar as notificações novamente, uma nova inscrição será criada na próxima sessão.

Depois que o usuário reativar as notificações, acione novamente o fluxo normal de registro de push para a web do seu site para que a Braze armazene o novo endpoint de inscrição.
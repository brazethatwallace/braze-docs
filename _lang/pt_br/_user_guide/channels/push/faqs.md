---
nav_title: FAQ
article_title: FAQ
page_order: 30
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem ao configurar campanhas de push."
page_type: FAQ
channel:
  - Push
---

# Perguntas frequentes {#frequently-asked-questions}

> Este artigo fornece respostas para algumas perguntas frequentes sobre o canal de push.

## Por que as notificações por push às vezes atrasam? {#why-are-push-notifications-sometimes-delayed}

A entrega geralmente segue três estágios: **processamento** pela Braze (segmentação, agendamento e envio ao provedor), transporte da Braze para o **APNs ou FCM** e entrega do provedor para o **dispositivo**. Atrasos podem ocorrer em qualquer estágio. A Braze não tem visibilidade sobre as filas do provedor ou do dispositivo; use o [registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs/) no cliente quando precisar identificar problemas de tempo no lado do dispositivo.

## O que acontece quando vários usuários fazem login em um único dispositivo? {#what-happens-when-multiple-users-log-into-a-single-device}

Quando um usuário faz logout de um dispositivo ou site, ele continua acessível por push até que outro usuário faça login. Nesse momento, o token por push é reatribuído ao novo usuário. Isso acontece porque cada dispositivo pode ter apenas uma inscrição de push ativa por app ou site.

Quando um token por push é reatribuído, a alteração é refletida no **Push Changelog** do perfil de usuário. No perfil de usuário, acesse a guia **Engagement**.

![O "Push Changelog" na seção "Contact Settings".]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

## Quando envio um push de teste, ele vai para todos os meus dispositivos? {#when-i-send-a-test-push-does-it-go-to-all-of-my-devices}

Sim. O push de teste é enviado para todos os dispositivos com push ativado associados ao perfil de usuário selecionado. Se você tiver vários celulares ou tablets conectados com o mesmo usuário, cada dispositivo com um token por push válido receberá a notificação.

Para enviar o push de teste para apenas um dispositivo, você pode remover os tokens por push dos outros dispositivos no perfil de usuário antes de testar. Alternativamente, se estiver enviando com o [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/), defina `send_to_most_recent_device_only` como `true` no objeto `apple_push` ou `android_push` para que apenas o dispositivo ativo mais recentemente receba o push.

## O que significa "Erro ao enviar push porque a carga útil era inválida"? {#what-does-error-sending-push-because-the-payload-was-invalid-mean}

Essa mensagem indica que o APNs rejeitou a solicitação de push devido a uma carga útil inválida (por exemplo, uma carga útil vazia ou grande demais).

Para mais informações e próximas etapas, consulte [Mensagens comuns de erro de push]({{site.baseurl}}/user_guide/channels/push/push_error_codes/).

## Por que um usuário com opt-in não tem um token por push? {#why-doesnt-an-opted-in-user-have-a-push-token}

Isso pode acontecer se o token por push do usuário foi reatribuído a outra pessoa que usou o mesmo dispositivo.

1. Acesse o **Push Changelog** na guia **Engagement** do perfil do usuário afetado.
2. Procure uma mensagem informando que o token por push foi movido para outro usuário.
3. Copie o token por push e cole na barra de pesquisa de usuários.
4. Se o token por push ainda existir, você será direcionado ao usuário que fez login mais recentemente no dispositivo.

Se você quiser que o token por push seja reatribuído ao usuário original:

1. Peça ao usuário original para fazer login no perfil com o token por push ausente.
2. Acione um novo envio de push. Isso moverá o token de volta para a conta, caso o push ainda esteja ativado no nível do dispositivo.

## Por que "Abrir URL da web dentro do app móvel" sempre abre o app quando estou testando uma campanha em rascunho? {#why-does-open-web-url-inside-mobile-app-always-open-the-app-when-im-testing-a-draft-campaign}

Quando uma campanha ainda está com status de **Rascunho** e você envia um push de teste, tocar na notificação sempre abre o app primeiro, independentemente de a opção **Abrir URL da web dentro do app móvel** estar selecionada ou desmarcada. Quando a campanha está **Ativa**, o comportamento ao clicar funciona conforme configurado.

Se você selecionou **Abrir URL da web** sem a opção **Dentro do app**, o link abre diretamente no navegador padrão do dispositivo. Se você selecionou **Abrir URL da web dentro do app móvel**, o link abre em uma visualização web dentro do app.

## Qual é a diferença entre "Enviar para Produção" e "Enviar para Desenvolvimento" nos certificados de push do iOS? {#what-is-the-difference-between-send-to-production-and-send-to-development-for-ios-push-certificates}

Ao adicionar um certificado de push da Apple na Braze, as opções **Enviar para Produção** e **Enviar para Desenvolvimento** determinam qual gateway do APNs (serviço de Notificações por Push da Apple) a Braze usa para entregar notificações por push:

- **Enviar para Desenvolvimento:** Selecione esta opção se o app foi compilado em modo de desenvolvimento no Xcode e assinado com um perfil de provisionamento de desenvolvimento. As notificações por push são roteadas pelo gateway de desenvolvimento (sandbox) da Apple.
- **Enviar para Produção:** Selecione esta opção se o app é distribuído via TestFlight da Apple, App Store ou distribuição empresarial. As notificações por push são roteadas pelo gateway de produção da Apple.

Se a opção errada for selecionada, as notificações por push falham silenciosamente porque o tipo de token por push não corresponde ao gateway. Normalmente, apps distribuídos pelo TestFlight ou pela App Store devem usar **Enviar para Produção**.

## Qual é a diferença entre os filtros "Push em Primeiro Plano Ativado" e "Push em Segundo Plano ou Primeiro Plano Ativado"? {#what-is-the-difference-between-the-foreground-push-enabled-and-background-or-foreground-push-enabled-filters}

Esses filtros de segmentação verificam condições diferentes:

| Filtro | O que verifica | Caso de uso |
|--------|---------------|----------|
| **Push em Primeiro Plano Ativado** | O usuário tem um token por push de primeiro plano válido **e** seu estado de inscrição de push é `Opted-In` ou `Subscribed`. | Direcionar usuários que podem receber notificações por push visíveis. |
| **Push em Segundo Plano ou Primeiro Plano Ativado** | O usuário tem qualquer token por push (primeiro plano ou segundo plano) **e** seu estado de inscrição de push é `Opted-In` ou `Subscribed`. Isso inclui usuários que desativaram notificações por push visíveis, mas ainda possuem um token por push de segundo plano. | Usado para [rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/), [notificações por push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/) e geofencing. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Qual é a diferença entre os filtros Push em Primeiro Plano Ativado e Push em Segundo Plano ou Primeiro Plano Ativado?" }

Um usuário pode ter `Push em Segundo Plano ou Primeiro Plano Ativado` sem ter `Push em Primeiro Plano Ativado`. Isso acontece quando o usuário desativou as notificações por push visíveis nas configurações do dispositivo, mas o app ainda mantém um token por push de segundo plano. Para mais informações, consulte [Usuários de push e inscrições]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#foreground-push-enabled).

## Como a Braze determina quando uma mensagem de push é enviada com sucesso? {#how-does-braze-determine-when-a-push-message-is-sent-successfully}

Uma mensagem é registrada como enviada assim que é recebida pelo provedor de notificação por push. Isso não significa necessariamente que o usuário recebeu ou visualizou a mensagem.

Para iOS, o provedor de notificação por push é o Apple Push Notification Service (APNs) e, para Android, normalmente é o Firebase Cloud Messaging (FCM). O provedor de notificação por push responde imediatamente com sucesso ou falha. Uma falha pode incluir um bounce ou uma nova tentativa por falha de rede.

Se uma mensagem de sucesso é retornada, o envio é registrado pela Braze e, em seguida, o serviço de push tenta entregar ao dispositivo. Se o dispositivo não puder ser alcançado imediatamente, o serviço faz novas tentativas até a opção de vencimento configurada na Braze (**TTL** para Android, **Expiry** para iOS). Se a mensagem expirar, o serviço de push descarta o push, mas isso não é considerado um bounce.

- Para Campaigns de push com entrega baseada em ação, o envio da mensagem é registrado assim que o usuário realiza a ação que aciona a Campaign.
- Para campanhas agendadas, o horário de envio é o momento em que a mensagem foi enfileirada e passada ao provedor de notificação por push.
- Para ambos os tipos de entrega, a mensagem é marcada como "enviada" na Braze e no perfil de usuário em **Campaigns Received**, mesmo que o usuário ainda não tenha visto ou recebido o push.

A métrica de "entregas" para push no dashboard é calculada no carregamento da página como o número de envios menos bounces.
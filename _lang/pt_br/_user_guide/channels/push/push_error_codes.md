---
nav_title: Mensagens de erro comuns de push
article_title: Mensagens de erro comuns de push
page_order: 22
page_type: reference
description: "Este artigo aborda mensagens de erro comuns relacionadas a push para iOS e Android, e apresenta possíveis soluções."
channel: push
platform:
- iOS
- Android
---

# Mensagens de erro comuns de push {#common-push-error-messages}

> Esta página aborda mensagens de erro comuns para envio de mensagens por push.

{% tabs %}
{% tab Android %}
## Push com bounce: MismatchSenderId {#push-bounced-mismatchsenderid}
`MismatchSenderId` indica uma falha de autenticação. O Firebase Cloud Messaging (FCM) autentica com alguns dados essenciais: senderID e chave de API or interface de programação do aplicativo (API) do FCM. Ambos devem ser validados quanto à precisão. Para saber mais, consulte a [documentação do Android](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) sobre esse problema.

Falhas comuns podem incluir:
- [senderID]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android) incorreto
- Registro múltiplo, caso o registro seja feito com outro serviço de push usando um senderID diferente

### Push com bounce: InvalidRegistration {#push-bounced-invalidregistration}
`InvalidRegistration` pode ocorrer quando um token por push está malformado. Falhas comuns podem incluir quando:
- As pessoas estão passando tokens de registro da Braze manualmente, mas não chamam `getToken()`. Por exemplo, podem estar passando o ID de instância inteiro. O token na mensagem de erro se parece com `&#124;ID&#124;1&#124;:[regular token]`.
- As pessoas estão se registrando em vários serviços. Atualmente, esperamos que os intents de registro de push cheguem no formato antigo. Portanto, se as pessoas estiverem se registrando em vários lugares e capturarmos intents de outros serviços, podemos obter tokens por push malformados.

### Push com bounce: NotRegistered {#notregistered}

`NotRegistered` geralmente significa que o app foi excluído do dispositivo (como nosso sinal de desinstalação). Isso também pode ocorrer se houver registro múltiplo e um segundo registro invalidar o token por push que a Braze recebe.

### DEVICE_UNREGISTERED {#device-unregistered}

Este erro aparece no Registro de atividades de envio de mensagem como: `Received 'Error: DEVICE_UNREGISTERED, ' sending to '[Token String]'`

Isso geralmente ocorre por um dos seguintes motivos:

- O usuário desinstalou o app. Essa é a causa mais comum. Quando o app é removido de um dispositivo, o token por push se torna inválido.
- As credenciais de push foram atualizadas no app. Se sua equipe alterou as credenciais ou certificados do FCM incluídos no app, os usuários que se registraram com as credenciais anteriores terão tokens inválidos até que o app os registre novamente.
- Uma lógica personalizada está cancelando o registro de usuários do push. Isso é raro, mas é tecnicamente possível cancelar programaticamente o registro de um dispositivo do push usando o [SDK or kit de desenvolvimento de software do Firebase/Android](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#deleteToken()).

{% alert note %}
Este erro não significa que o usuário está com push desativado — apenas que um token específico foi removido do perfil dele. Isso é comum para usuários que estão testando funcionalidades e instalando e desinstalando o app com frequência. Para verificar se o usuário ainda possui tokens válidos, acesse **Pesquisa de usuários** e revise a seção **Configurações de contato** na guia **Engajamento**.
{% endalert %}

### Entidade solicitada não encontrada {#requested-entity-was-not-found}

Este erro pode ocorrer pelos seguintes motivos:

- O usuário final desinstalou o app. Você pode verificar o perfil do usuário para confirmar se esse é o caso.
- Há um canal de notificação inválido. Dependendo da sua integração, os dispositivos podem ter tokens por push que são válidos apenas para determinados canais de notificação. Ao enviar para um canal inválido, a mensagem sofre bounce.
- O tamanho da carga útil é muito grande.

Para saber mais, consulte a [documentação do Google](https://firebase.google.com/docs/cloud-messaging/manage-tokens#stale-and-expired-tokens) sobre tokens de registro obsoletos e expirados.

{% endtab %}
{% tab iOS %}

### Erro ao enviar push porque a carga útil era inválida {#error-sending-push-because-the-payload-was-invalid}

Esta mensagem pode aparecer na guia **Engajamento** do perfil do usuário em **Configurações de contato** > **Changelog de push** quando o serviço de Notificações por Push da Apple (APNs) rejeita a solicitação de push por causa de uma carga útil inválida.

Na Braze, esta mensagem do dashboard pode corresponder a um dos seguintes motivos de erro do APNs:

- `PayloadEmpty`: a carga útil não continha o conteúdo obrigatório para o tipo de push enviado.
- `PayloadTooLarge`: a carga útil excedeu o tamanho máximo permitido pelo APNs.

Causas comuns incluem:

- Chaves personalizadas (e seus valores) tornando a carga útil muito grande (isso pode incluir valores renderizados por Liquid inesperadamente grandes).
- Um alerta ou corpo vazio ou ausente quando obrigatório (ou uma carga útil `aps` malformada de outra forma).

Próximas etapas:

- Reduza o tamanho da carga útil removendo chaves personalizadas e encurtando valores dinâmicos grandes.
- Se você envia pela API or interface de programação do aplicativo (API), valide a carga útil JSON final (incluindo o tamanho) antes de enviar.

### Push com bounce: BadToken {#push-bounced-badtoken}

O erro `BadToken` pode ocorrer por vários motivos:
- O token por push não está sendo enviado corretamente para a Braze (por exemplo, em `registerDeviceToken:` ou o equivalente da sua plataforma).
	- Verifique o token no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Ele geralmente deve se parecer com uma longa string de letras e números (como `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Se não for o caso, verifique o código envolvido no envio do token por push para a Braze.<br><br>
- Ambiente de provisionamento incompatível:
	- Se você se registrar com um certificado de desenvolvimento e tentar enviar com um de produção, poderá ver este erro.
	- A Braze só oferece suporte a certificados universais para ambientes de produção. Testar push em ambientes de desenvolvimento com um certificado universal não funcionará.
	- Este relatório envia bounces em produção, mas não em desenvolvimento.<br><br>
- Perfil de provisionamento incompatível:
	- Isso pode acontecer se o seu certificado não corresponder ao que foi usado para obter o token. Se houver essa suspeita, as próximas etapas incluem:
		- Garantir que o certificado de push usado para enviar push pelo dashboard da Braze e o perfil de provisionamento estejam configurados corretamente.
		- Recriar a certificação APNS e depois recriar o perfil de provisionamento após o certificado APNS ser configurado para o `app_id`. Isso às vezes pode resolver alguns problemas mais visíveis.

### Bundle ID não permitido {#bundle-id-not-allowed}

O erro `TopicDisallowed` significa que o APNs rejeitou o push porque o tópico (bundle ID) na solicitação não é permitido para as credenciais de autenticação sendo usadas. Para resolver isso:

1. **Verifique o bundle ID.** Confirme que o bundle ID configurado nas configurações do seu app na Braze corresponde exatamente ao bundle ID do seu app. Isso inclui quaisquer variações de sufixo (por exemplo, `.debug`, `.staging`).
2. **Verifique sua configuração de autenticação APNs.** Confirme que seu app está configurado com a chave `.p8` correta do APNs e que a chave está associada ao mesmo Apple Developer Team do app para o qual você está enviando.
3. **Confirme o ambiente do app.** Se você tem App IDs separados na Braze para builds de desenvolvimento e produção, verifique se cada um está configurado com as credenciais de push e o ambiente corretos.

### Unregistered {#ios-unregistered}

Este erro aparece no Registro de atividades de envio de mensagem como:

`Received 'Unregistered' sending to '[Token String]'`

Este é o equivalente iOS do erro [DEVICE_UNREGISTERED](#device-unregistered) do Android. Ele geralmente ocorre por um dos seguintes motivos:

- O usuário desinstalou o app. Essa é a causa mais comum.
- Os certificados de push foram atualizados. Se sua equipe alterou ou renovou os certificados APNs, os usuários que se registraram com os certificados anteriores podem ter tokens inválidos até que o app os registre novamente.
- Uma lógica personalizada está cancelando o registro de usuários do push. Isso é raro, mas é tecnicamente possível cancelar programaticamente o registro de notificações remotas usando o SDK or kit de desenvolvimento de software do iOS.

{% alert note %}
Este erro não significa que o usuário está com push desativado — apenas que um token específico foi removido do perfil dele. Para verificar se o usuário ainda possui tokens válidos, acesse **Pesquisa de usuários** e revise a seção **Configurações de contato** na guia **Engajamento**.
{% endalert %}

### InvalidProviderToken

O erro `InvalidProviderToken` significa que o APNs rejeitou a solicitação porque o token de autenticação (de uma chave `.p8`) ou o certificado de push (`.p12`) não corresponde ao bundle ID ou Team ID do app. Para resolver isso:

1. **Verifique seu Team ID e Key ID:** se você está usando uma chave de autenticação `.p8`, confirme que o **Team ID** e o **Key ID** configurados no dashboard da Braze (**Configurações** > **Configurações do app** > selecione seu app iOS) correspondem aos valores na sua conta Apple Developer.
2. **Verifique o bundle ID:** certifique-se de que o bundle ID registrado na Braze corresponde ao bundle ID do seu app. Uma incompatibilidade, como uma diferença de capitalização ou um sufixo `.debug`, causa este erro.
3. **Faça upload novamente da chave ou certificado:** se a chave `.p8` ou o certificado `.p12` foi regenerado ou revogado recentemente, faça upload da nova chave na Braze e remova a antiga.
4. **Confirme o ambiente APNs:** se você está usando um certificado `.p12`, verifique se selecionou o ambiente correto (desenvolvimento versus produção) ao fazer upload. Para chaves `.p8`, isso é tratado automaticamente.

### Push com bounce: serviço de feedback do APNS removido {#push-bounced-apns-feedback-service-removed}

Isso geralmente acontece quando alguém desinstala o app. A Braze consulta o serviço de feedback do APNS todas as noites para obter uma lista de tokens inválidos. Para saber mais, consulte a documentação da Apple sobre [Comunicação com APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}
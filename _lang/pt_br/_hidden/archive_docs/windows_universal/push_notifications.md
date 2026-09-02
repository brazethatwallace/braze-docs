---
nav_title: Notificações por push
article_title: Notificações por push para o Windows Universal
platform: Windows Universal
page_order: 1
description: "Este artigo aborda as instruções de integração de notificações por push para a plataforma Windows Universal."
channel: push
hidden: true
---

# Integração de notificações por push {#push-notification-integration}
{% multi_lang_include archive/windows_deprecation.md %}

![Um exemplo de push do Windows Universal.]({% image_buster /assets/img_archive/windows_uni_push_sample.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Uma notificação por push é um alerta fora do app que aparece na tela do usuário quando ocorre uma atualização importante. As notificações por push são uma forma valiosa de fornecer aos usuários conteúdo relevante e oportuno ou de reengajá-los com seu app.

Acesse nossa [documentação]({{site.baseurl}}/user_guide/channels/push/best_practices/) para obter práticas recomendadas adicionais.

## Etapa 1: Configure seu app para push {#step-1-configure-your-application-for-push}

Certifique-se de que, no arquivo `Package.appxmanifest`, as seguintes configurações estejam definidas:

Na guia **Application**, verifique se `Toast Capable` está definido como `YES`.

## Etapa 2: Configurar o dashboard da Braze {#step-2-configure-the-braze-dashboard}

1. [Encontre seu SID e Client Secret](http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx)
2. Na página **Settings** do dashboard da Braze, adicione o SID e o Client Secret nas suas configurações.<br>![]({% image_buster /assets/img_archive/windows_sid.png %} "Windows SID dashboard")

## Etapa 3: Atualização para registro de abertura em segundo plano {#step-3-update-for-background-open-logging}

No seu método `OnLaunched`, depois de chamar `OpenSession`, adicione o seguinte snippet de código.

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);
}
```

## Etapa 4: Criação de manipuladores de eventos {#step-4-creating-event-handlers}

Para ouvir os eventos que são disparados quando o push é recebido e ativado (clicado pelo usuário), crie manipuladores de eventos e adicione-os aos eventos do `PushManager`:

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

Seus manipuladores de eventos devem ter as seguintes assinaturas:

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## Etapa 5: Deep linking do push para seu app {#step-5-deep-linking-from-push-into-your-app}

### Parte 1: Criação de deep links para seu app {#part-1-creating-deep-links-for-your-app}

Os deep links são usados para levar os usuários de fora do app diretamente para uma determinada tela ou página do aplicativo. Normalmente, isso é feito registrando um esquema de URL (por exemplo, myapp://mypage) com um sistema operacional e registrando o seu aplicativo para lidar com esse esquema; quando o sistema operacional é solicitado a abrir uma URL desse formato, ele transfere o controle para o seu aplicativo.

O suporte a deep linking do WNS é diferente, pois inicia seu app com dados sobre para onde enviar o usuário. Quando o push do WNS é criado, ele pode incluir uma string de inicialização que é passada para o `OnLaunched` do seu app quando o push é clicado e o aplicativo é aberto. Já usamos essa string de inicialização para fazer o rastreamento de campanhas e oferecemos aos usuários a capacidade de anexar seus próprios dados, que podem ser analisados e usados para navegar o usuário quando o app é iniciado.

Se você especificar uma string de inicialização extra no dashboard ou na REST or transferir estado representacional API or interface de programação do aplicativo (API), ela será adicionada ao final da string de inicialização que criamos, após a chave "abextras=". Portanto, um exemplo de string de inicialização pode ser `ab_cn_id=_trackingid_abextras=page=settings`, no qual você especificou `page=settings` no parâmetro extra da string de inicialização para que possa analisá-la e levar o usuário à página de configurações.

### Parte 2: Deep links pelo dashboard {#part-2-deep-linking-through-the-dashboard}

Especifique a string a ser anexada à string de inicialização no campo "Additional Launch String Configuration" nas configurações de notificação por push.

![]({% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Deep Link Click Action")

### Parte 3: Deep links pela REST or transferir estado representacional API or interface de programação do aplicativo (API) {#part-3-deep-linking-through-the-rest-api}

A Braze também permite o envio de deep links por meio da REST or transferir estado representacional API or interface de programação do aplicativo (API). [Os objetos push do Windows Universal]({{site.baseurl}}/api/objects_filters/) aceitam um parâmetro opcional `extra_launch_string`.
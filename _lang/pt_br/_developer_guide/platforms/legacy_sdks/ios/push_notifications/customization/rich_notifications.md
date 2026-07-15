---
nav_title: Notificações Rich
article_title: Notificações por push avançadas para iOS
platform: iOS
page_order: 3
description: "Este artigo de referência aborda a implementação de notificações por push avançadas em seu aplicativo iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Notificações Rich do iOS 10 {#ios-10-rich-notifications}

O iOS 10 introduz a capacidade de enviar notificações por push com imagens, GIFs e vídeos. Para ativar essa funcionalidade, os clientes devem criar um `Service Extension`, um novo tipo de extensão que permite a modificação de uma carga útil push antes de ser exibida.

## Criação de uma extensão de serviço {#creating-a-service-extension}

Para criar uma [`Notification Service Extension`](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), acesse **File > New > Target** no Xcode e selecione **Notification Service Extension**.

![Seletor de target do Xcode criando uma Notification Service Extension para notificações Rich.]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Certifique-se de que **Embed In Application** esteja definido para incorporar a extensão em seu aplicativo.

## Configuração da extensão de serviço {#setting-up-the-service-extension}

Um `Notification Service Extension` é um binário próprio que acompanha seu app. Ele deve ser configurado no [Portal Apple Developer](https://developer.apple.com) com seu próprio ID de app e perfil de provisionamento.

O ID do pacote do `Notification Service Extension` deve ser diferente do ID do pacote do target principal do seu app. Por exemplo, se o ID do pacote do seu app for `com.company.appname`, você poderá usar `com.company.appname.AppNameServiceExtension` para a extensão de serviço.

### Configurar a extensão de serviço para funcionar com a Braze {#configuring-the-service-extension-to-work-with-braze}

A Braze envia uma carga útil de anexo no payload de APNs sob a chave `ab`, que usamos para configurar, baixar e exibir conteúdo avançado. Por exemplo:

```json
{
  "ab" :
    {
    ...

    "att" :
      {
       "url" : "http://mysite.com/myimage.jpg",
       "type" : "jpg"
       }
    },
  "aps" :
    {
    ...
    }
}
```

Os valores relevantes da carga útil são:

```objc
// The Braze dictionary key
static NSString *const AppboyAPNSDictionaryKey = @"ab";

// The attachment dictionary
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// The attachment URL
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// The type of the attachment - a suffix for the file you save
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

Para exibir manualmente a notificação por push com uma carga útil da Braze, baixe o conteúdo do valor em `AppboyAPNSDictionaryAttachmentURLKey`, salve-o como um arquivo com o tipo de arquivo armazenado na chave `AppboyAPNSDictionaryAttachmentTypeKey` e adicione-o aos anexos da notificação.

### Exemplo de código {#example-code}

Você pode escrever a extensão de serviço em Objective-C ou Swift.

Para usar nosso código de exemplo em Objective-C, substitua o conteúdo do target `Notification Service Extension` gerado automaticamente em `NotificationService.m` pelo conteúdo do Appboy [`NotificationService.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/StopwatchNotificationService/NotificationService.m).

Para usar nosso código de exemplo em Swift, substitua o conteúdo do target `Notification Service Extension` gerado automaticamente em `NotificationService.swift` pelo conteúdo do Appboy [`NotificationService.swift`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift).

## Criação de uma notificação Rich no seu dashboard {#creating-a-rich-notification-in-your-dashboard}

Para criar uma notificação Rich no seu dashboard da Braze, crie um push para iOS, anexe uma imagem ou GIF, ou forneça uma URL que hospede uma imagem, GIF ou vídeo. Os ativos são baixados no recebimento das notificações por push, portanto, planeje-se para grandes picos síncronos de solicitações se estiver hospedando seu conteúdo.

Consulte [`unnotificationattachment`](https://developer.apple.com/reference/usernotifications/unnotificationattachment) para obter uma lista dos tipos e tamanhos de arquivos compatíveis.
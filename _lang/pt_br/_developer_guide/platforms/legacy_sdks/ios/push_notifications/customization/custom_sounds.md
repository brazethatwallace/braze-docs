---
nav_title: Sons personalizados
article_title: Sons personalizados de notificações por push para iOS
platform: iOS
page_order: 3
description: "Este artigo de referência aborda a implementação de sons personalizados em suas notificações por push do iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Sons personalizados {#custom-sounds}

## Etapa 1: Hospedagem do som no app {#step-1-hosting-the-sound-in-the-app}

Os sons de notificação por push personalizados devem ser hospedados localmente no pacote principal do aplicativo cliente. São aceitos os seguintes formatos de dados de áudio:

- PCM linear
- MA4
- µLaw
- aLaw

É possível empacotar os dados de áudio em um arquivo AIFF, WAV ou CAF. No Xcode, adicione o arquivo de som ao seu projeto como um recurso não localizado do pacote de aplicativos.

Você pode usar a ferramenta afconvert para converter sons. Por exemplo, para converter o som do sistema PCM linear de 16 bits Submarine.aiff para áudio IMA4 em um arquivo CAF, use o seguinte comando no terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

Você pode inspecionar um som para determinar seu formato de dados abrindo-o no QuickTime Player e escolhendo **Show Movie Inspector** no menu **Movie**.

Os sons personalizados devem ter menos de 30 segundos quando reproduzidos. Se um som personalizado estiver acima desse limite, o som padrão do sistema será reproduzido.

## Etapa 2: Fornecimento ao dashboard de uma URL de protocolo para o som {#step-2-providing-the-dashboard-with-a-protocol-url-for-the-sound}

Seu som deve ser hospedado localmente no app. Você deve especificar uma URL de protocolo que direcione para o local do arquivo de som no app dentro do campo **Sound** no criador de push. Especificar "default" neste campo reproduzirá o som de notificação padrão no dispositivo. Isso pode ser especificado por meio da nossa [API or interface de programação do aplicativo (API) de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) ou do nosso dashboard em **Configurações** no criador de push, conforme ilustrado na captura de tela a seguir:

![Seu som deve ser hospedado localmente no app. Você deve especificar uma URL de protocolo que direcione para o local do arquivo de som no app dentro do campo Sound no criador de push. Especificar "default" neste campo reproduzirá o som de notificação padrão no dispositivo. Isso pode ser especificado por meio da API or interface de programação do aplicativo (API) de envio de mensagens ou do dashboard em Configurações no criador de push, conforme ilustrado na captura de tela a seguir.]({% image_buster /assets/img_archive/sound_push_ios.png %})

Se o arquivo de som especificado não existir ou se a palavra-chave "default" for inserida, a Braze usará o som de alerta padrão do dispositivo. Além do nosso dashboard, o som também pode ser configurado por meio da nossa [API or interface de programação do aplicativo (API) de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging). Consulte a documentação para desenvolvedores da Apple sobre a [preparação de sons de alerta personalizados](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) para obter informações adicionais.
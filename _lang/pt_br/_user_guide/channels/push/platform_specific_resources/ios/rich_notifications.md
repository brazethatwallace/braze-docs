---
nav_title: Criar notificações Rich
article_title: "Criando notificações por push avançadas para iOS"
page_order: 3
page_type: tutorial
description: "Este tutorial aborda os requisitos e as etapas para criar notificações Rich para iOS nas suas Campaigns da Braze."

platform: iOS
channel:
  - Push
tool:
  - Campaigns

---

# Criar notificações por push avançadas para iOS {#create-rich-push-notifications-for-ios}

> As notificações Rich permitem mais personalização nas suas notificações por push ao adicionar conteúdo além de texto. As notificações do Android já incluem imagens em notificações por push há algum tempo, exibidas como uma "Imagem de notificação expandida". A partir do iOS 10, seus clientes poderão receber notificações por push do iOS que incluem GIFs, imagens, vídeos ou áudio.

## Pré-requisitos {#prerequisites}

Antes de criar uma notificação Rich por push para iOS, observe os seguintes detalhes:

- Para garantir que seu app possa enviar notificações Rich, siga as instruções de [integração de push para iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications), pois seu desenvolvedor precisará adicionar uma extensão de serviço ao seu app.
- Os tipos de arquivo que atualmente suportamos para upload direto no nosso dashboard incluem JPEG, PNG ou GIF. Esses arquivos também podem ser inseridos no campo de URL com template, junto com estes tipos de arquivo adicionais: AIF, M4A, MP3, MP4 ou WAV.
- Consulte a [documentação da Apple](https://developer.apple.com/reference/usernotifications/unnotificationattachment) para limitações e especificações de mídia.
- As notificações Rich do iOS não estão disponíveis ao criar uma Campaign de push rápido.
- O iOS redimensiona as imagens para caber na tela e ajusta as imagens avançadas para a visualização ativa ou bloqueada.

{% alert note %}
Desde janeiro de 2020, as notificações Rich por push do iOS podem lidar com imagens de 1038x1038 com menos de 10&nbsp;MB, mas recomendamos usar o menor tamanho de arquivo possível. Na prática, enviar arquivos grandes pode causar estresse desnecessário na rede e tornar os tempos limite de download mais comuns.
{% endalert %}

{% alert important %}
As imagens de notificação por push podem não ser exibidas conforme esperado se o tamanho do arquivo da imagem for muito grande, a proporção estiver incorreta, o texto exceder o comprimento máximo da mensagem ou o texto do título exceder o comprimento máximo do título.
{% endalert %}

### Contagem de caracteres {#character-count}

Embora não possamos fornecer uma regra rígida para o número exato de caracteres a incluir em um push, [oferecemos algumas diretrizes]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/) a considerar ao projetar mensagens para iOS. Pode haver alguma variação dependendo da presença de uma imagem, do estado da notificação e da configuração de exibição do dispositivo do usuário, e do tamanho do dispositivo. Em caso de dúvida, seja breve e direto.

Como prática recomendada, a Braze sugere manter cada linha de texto, tanto para o título opcional quanto para o corpo da mensagem, em aproximadamente 30 a 40 caracteres em uma notificação por push para celular.

#### Estados da notificação {#notification-states}

Seus usuários podem visualizar notificações por push em diversas situações diferentes e podem ver diferentes comprimentos de texto, conforme a seguir.

<table aria-label="Estados da notificação">
  <caption>Estados da notificação</caption>
<thead>
  <tr>
    <th>Tela de bloqueio ou Central de notificações</th>
    <th>Expandida</th>
    <th>Dispositivo ativo</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">Este é o cenário mais comum.<br><br><b>Título:</b> 1 linha de texto<br><b>Corpo:</b> 4 linhas de texto<br><b>Imagem:</b> miniatura quadrada</td>
    <td width="33%">Quando um usuário pressiona e segura uma mensagem.<br><br><b>Título:</b> 1 linha de texto<br><b>Corpo:</b> 7 linhas de texto<br><b>Imagem:</b> proporção 2:1 (recomendada, veja a nota a seguir)</td>
    <td width="33%">Quando um usuário recebe um push enquanto o telefone está desbloqueado e ativo.<br><br><b>Título:</b> 1 linha de texto<br><b>Corpo:</b> 2 linhas de texto</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Estados da notificação" }

![Exemplos de notificações por push exibidas na tela de bloqueio, quando expandidas e quando o dispositivo está ativo.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Embora recomendemos uma proporção de 2:1 para notificações por push expandidas, praticamente qualquer proporção é suportada. As imagens sempre ocuparão toda a largura da notificação, e a altura será ajustada proporcionalmente.
{% endalert %}

#### Variáveis na truncagem de texto {#variables-in-text-truncation}

Ao criar conteúdo, considere os seguintes cenários que podem impactar a quantidade de texto exibido.

{% tabs %}
{% tab Horário %}

Dependendo de quando um usuário interage com uma notificação por push, o carimbo de data/hora pode encurtar o texto do título.

![Exemplo de notificação por push com carimbo de data/hora "agora" e contagem de caracteres do título de 35.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Contagem de caracteres do título: **35**

![Exemplo de notificação por push com carimbo de data/hora "3h atrás" e contagem de caracteres do título de 33.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Contagem de caracteres do título: **33**

![Exemplo de notificação por push com carimbo de data/hora "Ontem, 8:37" e contagem de caracteres do título de 22.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Contagem de caracteres do título: **22**

{% endtab %}
{% tab Imagens %}

O texto do corpo é encurtado em cerca de 10 caracteres por linha quando uma imagem está presente.

![Exemplo de notificação por push sem imagem e contagem de caracteres do corpo de 179.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Contagem de caracteres do corpo: **179**

![Exemplo de notificação por push com imagem e contagem de caracteres do corpo de 154.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Contagem de caracteres do corpo: **154**

{% endtab %}
{% tab Nível de interrupção %}

Para o iOS 15, as designações Urgente e Crítica empurram o título para uma nova linha sem o carimbo de data/hora, dando um pouco mais de espaço.

![Exemplo de notificação por push sem designação Urgente ou Crítica e contagem de caracteres do título de 35.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Contagem de caracteres do título: **35**

![Exemplo de notificação por push com designação Urgente e contagem de caracteres do título de 39.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Contagem de caracteres do título: **39**

{% endtab %}
{% tab Mais %}

Os seguintes detalhes também podem impactar a truncagem de texto:

- **Configurações de exibição do telefone:** um usuário pode aumentar ou diminuir o tamanho global da fonte da interface no telefone, geralmente por motivos de acessibilidade.
- **Largura do dispositivo:** a mensagem pode ser exibida em um telefone pequeno ou em um iPad largo.
- **Tipos de conteúdo:** emojis e caracteres largos como "m" e "w" ocupam mais espaço do que "i" ou "t", e palavras mais longas como "engajamento" podem quebrar de linha de forma mais abrupta do que palavras mais curtas.

{% endtab %}
{% endtabs %}

## Configurando sua notificação Rich para iOS {#setting-up-your-ios-rich-notification}

### Etapa 1: Crie uma Campaign de push {#step-1-create-a-push-campaign}

Siga as [etapas da Campaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/#creating-a-push-message) para redigir uma notificação por push para iOS. Você usará o mesmo criador que utiliza para configurar notificações por push que não contêm conteúdo avançado.

### Etapa 2: Adicione mídia {#step-2-add-media}

Adicione seu arquivo de imagem, GIF, áudio ou vídeo no campo **Rich Notification Media** no criador da mensagem. Consulte os [requisitos](#requirements) sobre como adicionar seus arquivos de conteúdo.

![Um exemplo de texto resumido para uma notificação por push.]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

Você também pode limitar esta mensagem para enviar apenas a usuários que possuem um dispositivo com iOS 10 ou superior. Para usuários que não atualizaram para o iOS 10, a notificação aparecerá apenas como texto, sem o conteúdo avançado, se você deixar a opção **Only send to devices with Rich Notification support** desmarcada.

![A seção de imagem de notificação expandida onde você pode adicionar uma imagem ou inserir uma URL de imagem.]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### Etapa 3: Continue criando sua Campaign {#step-3-continue-creating-your-campaign}

Depois que o conteúdo da sua notificação Rich for carregado no dashboard, você pode continuar [programando sua Campaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/#schedule-push-campaign).

Quando um usuário receber a notificação por push, ele pode pressionar com força a mensagem para expandir a imagem.

![Um usuário recebe uma notificação por push e pressiona com força a mensagem para mostrar uma imagem expandida que diz "Hello!".]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }
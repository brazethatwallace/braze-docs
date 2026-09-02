---
nav_title: Configurações avançadas
article_title: Configurações avançadas de push
platform: iOS
page_order: 5
description: "Este artigo de referência aborda as configurações avançadas de notificação por push do iOS, como opções de alerta, sons, vencimento e muito mais."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configurações avançadas {#advanced-settings}

Ao criar uma campanha de push, na etapa de composição, selecione **Configurações** para visualizar as configurações avançadas disponíveis.

![Configurações avançadas de campanha de push para iOS no dashboard da Braze.]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## Extração de dados de pares de valores-chave push {#extracting-data-from-push-key-value-pairs}

A Braze permite que você envie pares de valores de string personalizados, conhecidos como `extras`, juntamente com uma notificação por push para o seu aplicativo. Os extras podem ser definidos por meio do dashboard ou da API e estarão disponíveis como pares de valores-chave no dicionário `notification` passado para suas implementações de delegados push.

## Opções de alerta {#alert-options}

Marque a caixa de seleção **Alert Options** para ver um menu suspenso de valores-chave disponíveis para ajustar como a notificação aparece nos dispositivos.

## Adição do sinalizador content-available {#adding-content-available-flag}

Marque a caixa de seleção **Add Content-Available Flag** para instruir os dispositivos a baixar novos conteúdos em segundo plano. Geralmente, isso pode ser marcado se você estiver interessado em enviar [notificações silenciosas]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications).

## Adição do sinalizador de conteúdo mutável {#adding-mutable-content-flag}

Marque a caixa de seleção **Add Mutable-Content Flag** para ativar a personalização avançada do receptor em dispositivos iOS 10+. Esse sinalizador será enviado automaticamente ao criar uma [notificação Rich]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/rich_notifications), independentemente do valor dessa caixa de seleção.

## Atualizar o contador de badges do app {#update-app-badge-count}

Digite o número para o qual deseja atualizar a contagem de badges ou use a sintaxe Liquid para definir suas condições personalizadas. Você também pode atualizar a contagem de badges manualmente por meio da propriedade `applicationIconBadgeNumber` do seu aplicativo ou da carga útil da notificação por push. Para saber mais, consulte nosso artigo dedicado à [contagem de badges]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/badges).

## Sons {#sounds}

Aqui você pode inserir um caminho para um arquivo de som no pacote do seu app para especificar um som a ser reproduzido quando a mensagem push for recebida. Se o arquivo de som especificado não existir ou se a palavra-chave "default" for inserida, a Braze usará o som de alerta padrão do dispositivo. Para obter mais informações sobre personalização, consulte nosso artigo dedicado a [sons personalizados]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/custom_sounds).

## ID de recolhimento {#collapse-id}

Especifique um ID de recolhimento para agrupar notificações semelhantes. Se você enviar várias notificações com o mesmo ID de recolhimento, o dispositivo mostrará apenas a notificação recebida mais recentemente. Consulte a documentação da Apple sobre [notificações agrupadas](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

## Vencimento {#expiry}

Ao marcar a caixa de seleção **Expiry**, você poderá definir um tempo de vencimento para sua mensagem. Se o dispositivo de um usuário perder a conectividade, a Braze continuará tentando enviar a mensagem até o horário especificado. Se isso não for definido, a plataforma terá como padrão um vencimento de 30 dias. Observe que as notificações por push que expiram antes da entrega não são consideradas falhas e não serão registradas como bounce.
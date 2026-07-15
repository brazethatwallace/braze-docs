---
nav_title: Pares de chave-valor
article_title: Pares de chave-valor
page_order: 4
description: "Este artigo de referência aborda pares de chave-valor e como usá-los para enviar cargas úteis de dados extras para dispositivos de usuários."
channel:
  - push
  - in-app messages
  - content cards

---

# Pares de chave-valor {#key-value-pairs}

> Esta página aborda como usar pares de chave-valor para enviar cargas úteis de dados extras para dispositivos de usuários. Esse recurso está disponível nos canais de envio de mensagens push, no app, e-mail e Content Cards.

Use pares de chave-valor para adicionar metadados estruturados às mensagens. Essas cargas úteis de dados extras podem enriquecer as mensagens com informações contextuais adicionais que podem influenciar como uma mensagem é renderizada ou processada.

Como os pares de chave-valor são metadados, esses dados não são necessariamente visíveis para o destinatário, mas podem ser usados pelos seus sistemas ou processos conectados para personalizar o tratamento das mensagens.

Cada par consiste em:

- **Chave:** O identificador (Exemplo: `utm_source`)
- **Valor:** O dado associado (Exemplo: `newsletter`)

## Casos de uso {#use-cases}

Aqui estão alguns exemplos de casos de uso para adicionar metadados com pares de chave-valor:

1. **Parâmetros de rastreamento:** Anexar parâmetros UTM para fins de análise de dados
   - Chave: `utm_campaign`
   - Valor: `spring_sale`
2. **Tags personalizadas:** Adicionar tags para roteamento interno ou categorização
   - Chave: `priority`
   - Valor: `high`
3. **Gatilhos de comportamento:** Metadados usados para disparar ou personalizar comportamentos no app
   - Chave: `deep_link`
   - Valor: `app://promo-page`

## Notificações por push {#push-notifications}

Pares de chave-valor podem ser adicionados a notificações por push para Android, iOS e web. Você pode usar pares de chave-valor para atualizar métricas internas e conteúdo do app ou personalizar propriedades de notificações por push, como priorização de alertas, localização e sons.

No criador de mensagens, selecione a guia **Settings**, selecione **Add New Pair** e especifique seus pares de chave-valor.

Quando você adiciona pares de chave-valor no criador de mensagens, os valores são enviados como strings. Para push no iOS, as chaves reservadas de alerta do serviço de Notificações por Push da Apple (APNs) que você adiciona por meio de **Alert Options** (como `loc-args` para argumentos de localização) são formatadas com os tipos JSON corretos na carga útil. Para chaves personalizadas, seu app recebe valores de string, a menos que você os analise na sua integração.

### iOS

O serviço de Notificações por Push da Apple (APNs) suporta a definição de preferências de alerta e o envio de dados personalizados usando pares de chave-valor. O APNs utiliza a biblioteca reservada da Apple `aps`, que inclui chaves e valores predeterminados que governam as propriedades de alerta.

#### Biblioteca APS {#aps-library}

| Chave  | Tipo de valor  | Descrição do valor |
|-------------------|-----------------------------|----------------------------------|
| alert             | string ou objeto de dicionário | Para entradas de string, exibe um alerta com a string como mensagem com botões Fechar e Visualizar; para entradas que não são string, exibe um alerta ou banner dependendo das propriedades filhas da entrada |
| badge             | número                      | Governa o número exibido como badge no ícone do app                                                                                                                              |
| sound             | string                      | O nome do arquivo de som a ser reproduzido como alerta; deve estar no bundle do app ou na pasta ```Library/Sounds```                                                                                    |
| content-available | número                      | Valores de entrada 1 sinalizam ao app a disponibilidade de novas informações ao iniciar ou retomar a sessão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Biblioteca APS" }


##### Biblioteca de propriedades de alerta {#alert-properties-library}

| Chave            | Tipo de valor               | Descrição do valor                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | string                   | Uma string curta que o Apple Watch exibe brevemente como parte de uma notificação                                                                    |
| body         | string                   | O conteúdo da notificação por push                                                                                                                  |
| title-loc-key  | string ou null           | Uma chave que define a string de título para a localização atual a partir do arquivo ```Localizable.strings```                                          |
| title-loc-args | array de strings ou null | Valores de string que podem aparecer no lugar dos especificadores de formato de localização do título em title-loc-key                                           |
| action-loc-key | array de string ou null  | Se presente, a string especificada define a localização para os botões Fechar e Visualizar                                                         |
| loc-key        | string ou null           | Uma chave que define a mensagem de notificação para a localização atual a partir do arquivo ```Localizable.strings```                                  |
| loc-args       | array de strings         | Valores de string que podem aparecer no lugar dos especificadores de formato de localização em loc-key                                                       |
| launch-image   | strings                  | O nome de um arquivo de imagem no bundle do app que você deseja usar como imagem de lançamento quando os usuários tocam no botão de ação ou deslizam a ação |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Biblioteca de propriedades de alerta" }

O criador de mensagens da Braze lida automaticamente com a criação das seguintes chaves: **alert** e **suas propriedades**, **content-available**, **sound** e **category**.

Esses valores podem ser inseridos na guia **Settings** ao criar uma mensagem push. Selecione **Alert Options** e selecione uma chave de dicionário de alerta para que a chave seja automaticamente preenchida em uma nova entrada de chave-valor.

![Esses valores podem ser inseridos na guia Settings ao criar uma mensagem push. Selecione Alert Options e selecione uma chave de dicionário de alerta para que a chave seja automaticamente preenchida em uma nova entrada de chave-valor.]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Quando a Braze envia uma notificação por push para o APNs, a carga útil será formatada como JSON.

**Carga útil simples**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**Carga útil complexa**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### Pares de chave-valor personalizados {#custom-key-value-pairs}

Além dos valores de carga útil da biblioteca `aps`, você pode enviar pares de chave-valor personalizados para o dispositivo de um usuário. Os valores nesses pares são restritos a tipos primitivos: dicionário (objeto), array, string, número e booleano.

![Captura de tela relacionada a pares de chave-valor personalizados.]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Os casos de uso para pares de chave-valor personalizados incluem, entre outros, manutenção de métricas internas e definição do contexto para a interface do usuário. A Braze permite que você envie pares de chave-valor adicionais junto com uma notificação por push para serem usados pelo seu aplicativo por meio da [chave extras]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings#extracting-data-from-push-key-value-pairs). Se você preferir usar outra chave, confirme que seu app pode lidar com essa chave personalizada.

{% alert warning %}
Você deve evitar manipular uma chave ou dicionário de nível superior chamado ab no seu aplicativo.
{% endalert %}

A Apple aconselha os clientes a evitar incluir informações do cliente ou quaisquer dados sensíveis como dados de carga útil personalizada. Além disso, a Apple recomenda que qualquer ação associada a uma mensagem de alerta não exclua dados em um dispositivo.

{% alert warning %}
Se você estiver usando a API do provedor HTTP/2, qualquer carga útil individual que você enviar para o APNs não pode exceder um tamanho de 4096 bytes. A interface binária legada, que em breve será descontinuada, suporta apenas um tamanho de carga útil de 2048 bytes.
{% endalert %}

###### Campaigns disparadas por API {#api-triggered-campaigns}

A Braze permite que você envie pares de chave-valor de string definidos pelo usuário, conhecidos como `extras`. Para acessar seus extras em Campaigns disparadas por API e Campaigns agendadas disparadas por API, no dashboard defina uma chave como "example_key" e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em uma saída do console de desenvolvedor de `"extras": { "test": { "foo": 1, "bar": 1 }`.

### Android

A Braze permite que você envie cargas úteis de dados adicionais em notificações por push usando pares de chave-valor.

#### Carga útil de dados {#data-payload}

Semelhante ao push para iOS, você pode enviar pares de chave-valor personalizados para o dispositivo de um usuário.

Alguns casos de uso para pares de chave-valor personalizados incluem manutenção de métricas internas e definição do contexto para a interface do usuário, mas eles podem ser usados para qualquer finalidade que você escolher.

{% alert important %}
O backend do seu app deve ser capaz de processar pares de chave-valor personalizados para que a carga útil de dados funcione corretamente.
{% endalert %}

##### Campaigns disparadas por API

A Braze permite que você envie pares de chave-valor de string definidos pelo usuário, conhecidos como `extras`. Para acessar seus extras em Campaigns disparadas por API e Campaigns agendadas disparadas por API, no dashboard defina uma chave como "example_key" e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em uma saída do console de desenvolvedor de `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### Opções de mensagens FCM {#fcm-messaging-options}

As notificações por push para Android podem ser ainda mais personalizadas com opções de mensagens FCM. Essas incluem [prioridade de notificação]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings#notification-priority), [som]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings#sounds), postergação, tempo de vida e capacidade de agrupamento. Esses valores podem ser especificados na guia **Settings** ao criar uma mensagem push. Consulte [Configurações avançadas de notificações por push]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings) para mais instruções sobre como definir essas opções no criador de mensagens da Braze.

![Captura de tela relacionada às opções de mensagens FCM.]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Notificações por push silenciosas {#silent-push-notifications}

Uma notificação por push silenciosa é uma notificação por push que não contém mensagem de alerta ou som, usada para atualizar a interface ou o conteúdo do seu app em segundo plano. Essas notificações utilizam pares de chave-valor para disparar essas ações do app em segundo plano. As notificações por push silenciosas também alimentam nosso [rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

Os profissionais de marketing devem testar se as notificações por push silenciosas disparam o comportamento esperado antes de enviá-las aos usuários do app. Depois de redigir sua notificação por push silenciosa para [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift) ou [Android]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android), certifique-se de direcionar apenas um usuário teste filtrando por [ID de usuário externo]({{site.baseurl}}/developer_guide/rest_api/messaging#external-user-id) ou [endereço de e-mail]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

Ao lançar a Campaign, você deve verificar se não recebeu nenhuma notificação por push visível no seu dispositivo de teste.

{% alert note %}
O controle de notificações silenciosas do iOS pode causar os seguintes sintomas:

- Métricas de rastreamento de desinstalação menores do que o esperado para usuários iOS
- Entrega inconsistente ou atrasada de notificações por push silenciosas
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) que não são exibidas
- Push Stories que chegam sem as imagens, vídeos ou páginas esperados

Essa é uma limitação da plataforma Apple, não um problema da Braze. O iOS pode atrasar ou descartar notificações em segundo plano para alguns recursos da Braze, incluindo rastreamento de desinstalação e Push Stories. Para detalhes sobre o que o iOS limita e quando, consulte [Limitações do iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift#ios-limitations).
{% endalert %}

## Mensagens no app {#in-app-messages}

Você pode adicionar um par de chave-valor a uma mensagem no app no [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) selecionando a guia **Settings**, selecionando **Add New Pair** e especificando seus pares de chave-valor.

{% alert note %}
Pares de chave-valor não podem ser definidos por meio do editor de arrastar e soltar para mensagens no app.
{% endalert %}
![Captura de tela relacionada a mensagens no app.]({% image_buster /assets/img_archive/keyvalue_iam.png %})

### Campaigns disparadas por API

A Braze permite que você envie pares de chave-valor de string definidos pelo usuário, conhecidos como `extras`. Para acessar seus extras em Campaigns disparadas por API e Campaigns agendadas disparadas por API, no dashboard defina uma chave como "example_key" e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em uma saída do console de desenvolvedor de `"extras": { "test": { "foo": 1, "bar": 1 }`.

## E-mails {#emails}

Tanto o SparkPost quanto o SendGrid suportam pares de chave-valor em e-mails. Se você usa o SendGrid, os pares de chave-valor serão enviados como [argumentos únicos](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments). O SendGrid permite que você anexe um número ilimitado de pares de chave-valor com até 10.000 bytes de dados. Esses pares de chave-valor podem ser vistos em posts do [Event Webhook](https://sendgrid.com/docs/for-developers/tracking-events/event/) do SendGrid.

{% alert note %}
E-mails com bounce não entregarão pares de chave-valor ao SparkPost ou SendGrid.
{% endalert %}

![Guia de informações de envio do criador de mensagens de e-mail na Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Content Cards

Para adicionar um par de chave-valor a um Content Card, acesse a guia **Settings** no criador de mensagens da Braze e selecione **Add New Pair**.

![Adicionar par de chave-valor ao Content Card]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}
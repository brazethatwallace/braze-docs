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

Aqui estão alguns exemplos de casos de uso para adicionar metadados com pares de valores-chave:

1. **Parâmetros de rastreamento:** anexar parâmetros UTM para fins de análise de dados
   - Chave: `utm_campaign`
   - Valor: `spring_sale`
2. **Tags personalizadas:** adicionar tags para roteamento interno ou categorização
   - Chave: `priority`
   - Valor: `high`
3. **Disparadores de comportamento:** metadados usados para disparar ou personalizar comportamentos no app
   - Chave: `deep_link`
   - Valor: `app://promo-page`

## Notificações por push {#push-notifications}

Pares de valores-chave podem ser adicionados a notificações por push para Android, iOS e web. Você pode usar pares de valores-chave para atualizar métricas internas e conteúdo do app, ou personalizar propriedades de notificações por push, como priorização de alertas, localização e sons.

No criador de mensagem, selecione a guia **Settings**, selecione **Add New Pair** e especifique seus pares de valores-chave.

Quando você adiciona pares de valores-chave no criador de mensagem, os valores são enviados como strings. Para push iOS, as chaves de alerta reservadas do serviço de Notificações por Push da Apple (APN) que você adiciona por meio de **Alert Options** (como `loc-args` para argumentos de localização) são formatadas com os tipos JSON corretos na carga útil. Para chaves personalizadas, seu app recebe valores de string a menos que você os analise na sua integração.

### iOS

O serviço de Notificações por Push da Apple (APN) oferece suporte à definição de preferências de alerta e ao envio de dados personalizados usando pares de valores-chave. O APN utiliza a biblioteca `aps` reservada da Apple, que inclui chaves e valores predeterminados que controlam as propriedades de alerta.

#### Biblioteca APS {#aps-library}

| Chave  | Tipo de valor  | Descrição do valor |
|-------------------|-----------------------------|----------------------------------|
| alert             | string ou objeto de dicionário | Para entradas de string, exibe um alerta com a string como mensagem com botões Fechar e Visualizar; para entradas que não são strings, exibe um alerta ou banner dependendo das propriedades secundárias da entrada |
| badge             | número                      | Controla o número exibido como emblema no ícone do app                                                                                                                              |
| sound             | string                      | O nome do arquivo de som a ser reproduzido como alerta; deve estar no pacote do app ou na pasta ```Library/Sounds```                                                                                    |
| content-available | número                      | Valores de entrada 1 sinalizam ao app a disponibilidade de novas informações ao iniciar ou retomar a sessão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Biblioteca APS" }


##### Biblioteca de propriedades de alerta {#alert-properties-library}

| Chave            | Tipo de valor               | Descrição do valor                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | string                   | Uma string curta que o Apple Watch exibe brevemente como parte de uma notificação                                                                    |
| body         | string                   | O conteúdo da notificação por push                                                                                                                  |
| title-loc-key  | string ou null           | Uma chave que define a string de título para a localização atual a partir do arquivo ```Localizable.strings```                                          |
| title-loc-args | array de strings ou null | Valores de string que podem aparecer no lugar dos especificadores de formato de localização do título em title-loc-key                                           |
| action-loc-key | array de string ou null  | Se presente, a string especificada define a localização dos botões Fechar e Visualizar                                                         |
| loc-key        | string ou null           | Uma chave que define a mensagem de notificação para a localização atual a partir do arquivo ```Localizable.strings```                                  |
| loc-args       | array de strings         | Valores de string que podem aparecer no lugar dos especificadores de formato de localização em loc-key                                                       |
| launch-image   | strings                  | O nome de um arquivo de imagem no pacote do app que você deseja usar como imagem de inicialização quando os usuários tocam no botão de ação ou deslizam a ação |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Biblioteca de propriedades de alerta" }

O criador de mensagem da Braze lida automaticamente com a criação das seguintes chaves: **alert** e **suas propriedades**, **content-available**, **sound** e **category**.

Esses valores podem ser inseridos na guia **Settings** ao criar uma mensagem de push. Selecione **Alert Options** e selecione uma chave do dicionário de alerta para que a chave seja automaticamente preenchida em uma nova entrada de valor-chave.

![Esses valores podem ser inseridos na guia Settings ao criar uma mensagem de push. Selecione Alert Options e selecione uma chave do dicionário de alerta para que a chave seja automaticamente preenchida em uma nova entrada de valor-chave.]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Quando a Braze envia uma notificação por push para o APN, a carga útil será formatada como JSON.

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

##### Pares de valores-chave personalizados {#custom-key-value-pairs}

Além dos valores de carga útil da biblioteca `aps`, você pode enviar pares de valores-chave personalizados para o dispositivo do usuário. Os valores nesses pares são restritos a tipos primitivos: dicionário (objeto), array, string, número e booleano.

![Captura de tela relacionada a pares de valores-chave personalizados.]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Casos de uso para pares de valores-chave personalizados incluem, entre outros, manutenção de métricas internas e configuração de contexto para a interface do usuário. A Braze permite que você envie pares de valores-chave adicionais junto com uma notificação por push para serem usados pelo seu aplicativo dentro da [chave extras]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=swift#swift_settings). Se você preferir usar outra chave, confirme que seu app consegue lidar com essa chave personalizada.

{% alert warning %}
Você deve evitar manipular uma chave de nível superior ou um dicionário chamado ab no seu aplicativo.
{% endalert %}

A Apple aconselha os clientes a evitar incluir informações de clientes ou quaisquer dados sensíveis como dados de carga útil personalizada. Além disso, a Apple recomenda que nenhuma ação associada a uma mensagem de alerta exclua dados de um dispositivo.

{% alert warning %}
Se você estiver usando a API do provedor HTTP/2, qualquer carga útil individual que você enviar para o APN não pode exceder um tamanho de 4096 bytes. A interface binária legada, que será descontinuada em breve, suporta apenas um tamanho de carga útil de 2048 bytes.
{% endalert %}

###### Campaigns disparadas por API {#api-triggered-campaigns}

A Braze permite que você envie pares de valores-chave de string personalizados, conhecidos como `extras`. Para acessar seus extras em Campaigns disparadas por API e em Campaigns agendadas disparadas por API, no dashboard defina uma chave como "example_key" e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em uma saída do console de desenvolvedor de `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

A Braze permite que você envie cargas úteis de dados adicionais em notificações por push usando pares de valores-chave.

#### Carga útil de dados {#data-payload}

Semelhante ao push iOS, você pode enviar pares de valores-chave personalizados para o dispositivo do usuário.

Alguns casos de uso para pares de valores-chave personalizados incluem manutenção de métricas internas e configuração de contexto para a interface do usuário, mas podem ser usados para qualquer finalidade que você escolher.

{% alert important %}
O backend do seu app deve ser capaz de processar pares de valores-chave personalizados para que a carga útil de dados funcione corretamente.
{% endalert %}

##### Campaigns disparadas por API

A Braze permite que você envie pares de valores-chave de string personalizados, conhecidos como `extras`. Para acessar seus extras em Campaigns disparadas por API e em Campaigns agendadas disparadas por API, no dashboard defina uma chave como "example_key" e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em uma saída do console de desenvolvedor de `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### Opções de mensagens FCM {#fcm-messaging-options}

As notificações por push do Android podem ser personalizadas ainda mais com as opções de mensagem FCM. Essas incluem [prioridade de notificação]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), [som]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), postergação, tempo de vida e capacidade de colapso. Esses valores podem ser especificados na guia **Settings** ao criar uma mensagem de push. Consulte [Configurações avançadas de notificações por push]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings) para mais instruções sobre como definir essas opções no criador de mensagem da Braze.

![Captura de tela relacionada às opções de mensagens FCM.]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Notificações por push silenciosas {#silent-push-notifications}

Uma notificação por push silenciosa é uma notificação por push sem mensagem de alerta ou som, usada para atualizar a interface ou o conteúdo do seu app em segundo plano. Essas notificações utilizam pares de valores-chave para disparar essas ações em segundo plano no app. As notificações por push silenciosas também são a base do nosso [Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

Profissionais de marketing devem testar se as notificações por push silenciosas disparam o comportamento esperado antes de enviá-las para os usuários do app. Depois de compor sua notificação por push silenciosa para [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift) ou [Android]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android), certifique-se de direcionar apenas para um usuário teste, filtrando por [ID de usuário externo]({{site.baseurl}}/api/endpoints/messaging#external-user-id) ou [endereço de e-mail]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

Ao lançar a Campaign, você deve verificar se não recebeu nenhuma notificação por push visível no seu dispositivo de teste.

{% alert note %}
O controle de notificações silenciosas do iOS pode causar os seguintes sintomas:

- Métricas de Uninstall Tracking menores do que o esperado para usuários iOS
- Entrega inconsistente ou atrasada de notificações por push silenciosas
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) que não são exibidas
- Push Stories que chegam sem suas imagens, vídeos ou páginas esperados

Essa é uma limitação da plataforma Apple e não um problema da Braze. O iOS pode atrasar ou descartar notificações em segundo plano para alguns recursos da Braze, incluindo Uninstall Tracking e Push Stories. Para detalhes sobre o que o iOS controla e quando, consulte [Limitações do iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift#ios-limitations).
{% endalert %}

## Mensagens no app {#in-app-messages}

Adicione pares de valores-chave às mensagens no app que você criar com o [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

1. Na sua Campaign ou Canvas, crie ou edite uma mensagem no app e selecione o editor tradicional (não o de arrastar e soltar).
2. No criador de mensagem, selecione a guia **Configurações**.
3. Em **Pares de valores-chave**, selecione **Adicionar novo par**.
4. Insira uma chave e um valor para cada par. Para adicionar outro par, selecione **Adicionar novo par** novamente.

{% alert note %}
Os pares de valores-chave não estão disponíveis no editor de arrastar e soltar para mensagens no app. Use o editor tradicional para adicioná-los.
{% endalert %}

### Campaigns disparadas por API

A Braze permite que você envie pares de valores-chave de string personalizados, conhecidos como `extras`. Para acessar seus extras em Campaigns disparadas por API e em Campaigns agendadas disparadas por API, no dashboard defina uma chave como "example_key" e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em uma saída no console de desenvolvedor de `"extras": { "test": { "foo": 1, "bar": 1 }`.

## E-mails {#emails}

Tanto o SparkPost quanto o SendGrid suportam pares de valores-chave em e-mails. Se você usar o SendGrid, os pares de valores-chave serão enviados como [argumentos exclusivos](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments). O SendGrid permite anexar um número ilimitado de pares de valores-chave com até 10.000 bytes de dados. Esses pares de valores-chave podem ser vistos em posts do [Event Webhook](https://sendgrid.com/docs/for-developers/tracking-events/event/) do SendGrid.

{% alert note %}
E-mails com bounce não entregarão pares de valores-chave ao SparkPost ou SendGrid.
{% endalert %}

![Guia Informações de envio do criador de mensagem de e-mail na Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Content Cards

Para adicionar um par de chave-valor a um Content Card, acesse a guia **Settings** no criador de mensagens da Braze e selecione **Add New Pair**.

![Adicionar par de chave-valor ao Content Card]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}

{% alert note %}
As variantes de controle não suportam pares de chave-valor. Se você precisa capturar análise de dados para grupos de controle em testes A/B, crie uma variante de mensagem com um par de chave-valor como `control=true` e oculte-a no código do seu app enquanto registra impressões.
{% endalert %}
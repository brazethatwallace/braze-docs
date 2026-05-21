---
nav_title: "Configurações avançadas de push para Campaigns"
article_title: "Configurações avançadas de push para Campaigns"
page_order: 5
page_layout: reference
description: "Este artigo de referência aborda algumas configurações avançadas de push para Campaigns, como prioridade, URLs personalizadas, opções de entrega e mais."
platform: Android
channel:
  - Push
tool:
  - Campaigns

---

# Configurações avançadas de push para Campaigns {#advanced-push-campaign-settings}

> Existem muitas configurações avançadas disponíveis para notificações por push Android e Fire OS enviadas pelo dashboard da Braze. Este artigo descreve esses recursos e como usá-los com sucesso.

## ID de notificação {#notification-id}

Um ID de notificação é um identificador único para uma categoria de mensagem de sua escolha que informa ao serviço de envio de mensagens para considerar apenas a mensagem mais recente daquele ID. Definir um ID de notificação permite enviar apenas a mensagem mais recente e relevante, em vez de um acúmulo de mensagens desatualizadas e irrelevantes.

Para atribuir um ID de notificação, navegue até a página de composição do push ao qual deseja adicionar o ID e selecione a guia **Settings**. Insira um número inteiro na seção **Notification ID**. Para atualizar essa notificação após tê-la enviado, envie outra notificação com o mesmo ID que você usou anteriormente.

![Campo Notification ID.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## TTL (Time to Live) {#ttl}

O campo **Time to Live** permite definir um período personalizado para armazenar mensagens no serviço de envio de mensagens por push. Se o dispositivo permanecer offline além do TTL, a mensagem expirará e não será entregue.

Para editar o TTL do seu push Android, acesse o criador e selecione a guia **Settings**. Encontre o campo **Time to Live** e insira um valor em dias, horas ou segundos.

Os valores padrão de TTL são definidos pelo seu administrador na página [Configurações de push]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings/). Por padrão, a Braze define o TTL de push com o valor máximo para cada serviço de envio de mensagens por push. Embora as configurações padrão de TTL se apliquem globalmente, você pode substituí-las no nível da mensagem durante a criação da Campaign. Isso é útil quando diferentes Campaigns exigem diferentes níveis de urgência ou períodos de entrega.

Por exemplo, digamos que seu app hospeda um concurso semanal de trivia. Você envia uma notificação por push uma hora antes do início. Ao definir o TTL como 1 hora, você garante que os usuários que abrirem o app após o início do concurso não receberão uma notificação sobre um evento que já começou.

{% details Práticas recomendadas %}

#### Quando usar TTL mais curto {#when-to-use-shorter-ttl}

TTLs mais curtos garantem que os usuários recebam notificações oportunas para eventos ou promoções que perdem relevância rapidamente. Por exemplo:

- **Varejo:** Enviar um push para uma venda relâmpago que termina em 2 horas (TTL: 1-2 horas)
- **Delivery de comida:** Notificar os usuários quando o pedido está próximo (TTL: 10-15 minutos)
- **Apps de transporte:** Compartilhar atualizações de chegada de corrida (TTL: alguns minutos)
- **Lembretes de eventos:** Notificar os usuários quando um webinar está prestes a começar (TTL: menos de 1 hora)

#### Quando evitar TTL mais curto {#when-to-avoid-shorter-ttl}

- Se a mensagem da sua Campaign permanece relevante por vários dias ou semanas, como lembretes de renovação de assinatura ou promoções em andamento.
- Quando maximizar o alcance é mais importante do que a urgência, como em anúncios de atualização de app ou promoções de recursos.

{% enddetails %}

## Prioridade de entrega do Firebase Messaging {#fcm-priority}

O campo **Firebase Messaging Delivery Priority** permite controlar se um push é enviado com prioridade "normal" ou "alta" para o Firebase Cloud Messaging. Essa configuração determina a velocidade de entrega das mensagens e como elas afetam a vida útil da bateria do dispositivo.

| Prioridade | Descrição | Ideal para |
|---------|-------------|----------|
| Normal | Entrega otimizada para bateria que pode ser atrasada para economizar energia | Conteúdo não urgente, ofertas promocionais, atualizações de notícias |
| Alta | Entrega imediata com maior consumo de bateria | Notificações urgentes, alertas críticos, atualizações de eventos ao vivo, alertas de conta, notícias de última hora ou lembretes urgentes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Considerações {#considerations}

- **Configuração padrão**: Você pode definir uma prioridade FCM padrão para todas as Campaigns Android nas suas [Configurações de push]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings/). Essa configuração no nível da Campaign substituirá o padrão, se necessário.
- **Despriorização**: Se o FCM detectar que seu app envia frequentemente mensagens de alta prioridade que não resultam em notificações visíveis ao usuário ou engajamento, essas mensagens podem ser automaticamente despriorizadas para prioridade normal.
- **Impacto na bateria**: Mensagens de alta prioridade ativam dispositivos em modo de espera de forma mais agressiva e consomem mais bateria. Use essa prioridade com moderação.

Para informações mais detalhadas sobre tratamento de mensagens e despriorização, consulte a [documentação do FCM](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) e [Tratamento de mensagens e despriorização no Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize).

## Texto de resumo {#summary-text}

O texto de resumo permite definir texto adicional na visualização expandida da notificação. Ele também serve como legenda para notificações com imagens.

![Uma mensagem Android com o título "This is the title for the notification." e texto de resumo "This is the summary text for the notification."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

O texto de resumo será exibido abaixo do corpo da mensagem na visualização expandida.

![Uma mensagem Android com o título "This is the title for the notification." e texto de resumo "This is the summary text for the notification."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Para notificações por push que incluem imagens, o texto da mensagem será exibido na visualização recolhida, enquanto o texto de resumo será exibido como legenda da imagem quando a notificação for expandida.

## URIs personalizadas {#custom-uris}

O recurso **Custom URI** permite especificar uma URL da web ou um recurso Android para navegar quando a notificação é clicada. Se nenhuma URI personalizada for especificada, clicar na notificação levará os usuários ao seu app. Você pode usar a URI personalizada para criar deep links dentro do seu app, bem como direcionar os usuários para recursos que existem fora do seu app. Isso pode ser especificado pela nossa [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) ou na guia **Compose** do criador de push.

![Campo Custom URI.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## Prioridade de exibição da notificação {#notification-display-priority}

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

O nível de prioridade de uma notificação por push afeta como sua notificação é exibida na bandeja de notificações em relação a outras notificações. Também pode afetar a velocidade e a forma de entrega, já que mensagens de prioridade normal e inferior podem ser enviadas com latência ligeiramente maior ou agrupadas para preservar a vida útil da bateria, enquanto mensagens de alta prioridade são sempre enviadas imediatamente.

Esse recurso é útil para diferenciar suas mensagens com base em quão críticas ou urgentes elas são. Por exemplo, uma notificação sobre condições perigosas nas estradas seria uma boa candidata para receber alta prioridade, enquanto uma notificação sobre uma promoção em andamento deveria receber uma prioridade mais baixa. Você deve considerar se usar uma prioridade disruptiva é realmente necessário para a notificação que está enviando, pois ocupar constantemente o topo da caixa de entrada dos seus usuários ou interromper suas outras atividades pode ter um impacto negativo.

No Android O, a prioridade de notificação tornou-se uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir a prioridade de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar os sons de notificação. Para dispositivos com versões do Android anteriores ao O, é possível especificar um nível de prioridade para notificações Android e Fire OS pelo dashboard da Braze e pela API de envio de mensagens.

Para enviar mensagens a toda a sua base de usuários com uma prioridade específica, recomendamos que você especifique a prioridade indiretamente por meio da [configuração de canal de notificação](https://developer.android.com/training/notify-user/channels#importance) (para dispositivos O+) e envie a prioridade individual pelo dashboard (para dispositivos &#60;O).

Consulte a tabela a seguir para os níveis de prioridade que você pode definir em notificações por push Android ou Fire OS:

| Prioridade | Descrição | Valor de `priority` (para mensagens de API) |
|------|-----------|----------------------------|
| Máxima | Mensagens urgentes ou de tempo crítico. | `2` |
| Alta | Comunicação importante, como uma nova mensagem de um amigo. | `1` |
| Padrão | A maioria das notificações. Use se sua mensagem não se enquadra explicitamente em nenhum dos outros tipos de prioridade. | `0` |
| Baixa | Informações que você deseja que os usuários saibam, mas que não exigem ação imediata. | `-1`|
| Mínima | Informações contextuais ou de segundo plano. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para saber mais, consulte a documentação do Google sobre [notificações Android](http://developer.android.com/design/patterns/notifications.html).

## Categoria de push {#push-category}

As notificações por push Android oferecem a opção de especificar se sua notificação se enquadra em uma categoria predefinida. A interface do sistema Android pode usar essa categoria para tomar decisões de classificação ou filtragem sobre onde posicionar a notificação na bandeja de notificações do usuário.

![Guia Settings com a categoria definida como None, que é a configuração padrão.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| Categoria | Descrição |
|---|-------|
| None | Opção padrão. |
| Alarm | Alarme ou temporizador. |
| Call | Chamada recebida (voz ou vídeo) ou solicitação de comunicação síncrona similar. |
| Email | Mensagem assíncrona em massa (e-mail). |
| Error | Erro em operação em segundo plano ou status de autenticação. |
| Event | Evento de calendário. |
| Message | Mensagem direta recebida (SMS, mensagem instantânea, etc.). |
| Progress | Progresso de uma operação de longa duração em segundo plano. |
| Promotion | Promoção ou anúncio. |
| Recommendation | Uma recomendação específica e oportuna para um único item. |
| Reminder | Lembrete agendado pelo usuário. |
| Service | Indicação de serviço em execução em segundo plano. |
| Social | Atualização de rede social ou compartilhamento. |
| Status | Informação contínua sobre o dispositivo ou status contextual. |
| System | Atualização de status do sistema ou dispositivo. Reservado para uso do sistema. |
| Transport | Controle de transporte de mídia para reprodução. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Visibilidade do push {#push-visibility}

As notificações por push Android fornecem um campo opcional para determinar como uma notificação aparece na tela de bloqueio do usuário. Consulte a tabela a seguir para opções de visibilidade e descrições.

| Visibilidade | Descrição |
|---|-----|
| Pública | A notificação aparece na tela de bloqueio |
| Privada | A notificação é exibida com "Conteúdo oculto" como mensagem |
| Secreta | A notificação não é exibida na tela de bloqueio |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Além disso, os usuários Android podem substituir a forma como as notificações por push aparecem na tela de bloqueio alterando a configuração de privacidade de notificação em seu dispositivo. Essa configuração substituirá a visibilidade da notificação por push.

![Localização da prioridade de push no dashboard com Set Visibility ativado e definido como Private.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Independentemente da visibilidade, todas as notificações serão exibidas na tela de bloqueio do usuário se a configuração de privacidade de notificação no dispositivo for **Mostrar todo o conteúdo** (configuração padrão). Da mesma forma, as notificações não serão exibidas na tela de bloqueio se a privacidade de notificação estiver definida como **Não mostrar notificações**. A visibilidade só tem efeito se a privacidade de notificação estiver definida como **Ocultar conteúdo sensível**.

A visibilidade não tem efeito em dispositivos anteriores ao Android Lollipop 5.0.0, o que significa que todas as notificações serão exibidas nesses dispositivos.

Consulte nossa [documentação Android](https://developer.android.com/guide/topics/ui/notifiers/notifications) para saber mais.

## Sons de notificação {#notification-sounds}

No Android O, os sons de notificação tornaram-se uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir o som de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar suas notificações.

Para dispositivos com versões do Android anteriores ao Android O, a Braze permite definir o som de uma mensagem push individual pelo criador no dashboard. Você pode fazer isso especificando um recurso de som local no dispositivo (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`).

Selecionar **Default** neste campo reproduzirá o som de notificação padrão do dispositivo. Isso pode ser especificado pela nossa [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) ou em **Settings** no criador de push.

![O campo "Sound".]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Em seguida, insira a URI completa do recurso de som (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`) no campo do dashboard.

Para enviar mensagens a toda a sua base de usuários com um som específico, recomendamos que você especifique o som indiretamente por meio da [configuração de canal de notificação](https://developer.android.com/training/notify-user/channels) (para dispositivos O+) e envie o som individual pelo dashboard (para dispositivos &#60;O).
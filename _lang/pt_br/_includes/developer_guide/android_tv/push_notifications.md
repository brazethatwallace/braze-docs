## Sobre as notificações por push para a Android TV {#about-push-notifications-for-android-tv}

![Ilustração de um dispositivo Android TV usada no guia de notificações por push para Android TV.]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Embora não seja um recurso nativo, a integração de push da Android TV é possível com o uso do SDK or kit de desenvolvimento de software da Braze para Android e do Firebase Cloud Messaging para registrar um token por push para a Android TV. No entanto, é necessário criar uma interface do usuário para exibir a carga útil da notificação depois que ela for recebida.

## Pré-requisitos {#prerequisites}

Para usar esse recurso, você precisará concluir o seguinte:

- [Integrar o SDK or kit de desenvolvimento de software da Braze para Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Configurar notificações por push para o SDK or kit de desenvolvimento de software da Braze para Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)

## Configuração de notificações por push {#setting-up-push-notifications}

Para configurar notificações por push para a Android TV:

1. Crie uma exibição personalizada em seu app para exibir suas notificações.
2. Crie uma [fábrica de notificações personalizada]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_customization-display). Isso substituirá o comportamento padrão do SDK or kit de desenvolvimento de software e permitirá que você exiba manualmente as notificações. Ao retornar `null`, isso impedirá o processamento do SDK or kit de desenvolvimento de software e exigirá um código personalizado para exibir a notificação. Depois que essas etapas forem concluídas, você poderá começar a enviar push para a Android TV!<br><br>
3. (Opcional) Para rastrear a análise de dados de cliques de forma eficaz, configure o rastreamento de análise de cliques. Isso pode ser obtido com a criação de um [retorno de chamada de push]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_push-callback) para ouvir as intents de abertura e recebimento de push da Braze.

{% alert note %}
Essas notificações **não persistirão** e só ficarão visíveis para o usuário quando o dispositivo as exibir. Isso se deve ao fato de a central de notificações da Android TV não oferecer suporte a notificações históricas.
{% endalert %}

## Teste das notificações por push da Android TV {#testing-android-tv-push-notifications}

Para testar se a implementação do push foi bem-sucedida, envie uma notificação do dashboard da Braze como faria normalmente em um dispositivo Android.

- **Se o aplicativo estiver fechado:** a notificação por push exibirá uma notificação toast na tela.
- **Se o aplicativo estiver aberto:** você tem a oportunidade de exibir a mensagem em sua própria interface de usuário hospedada. Recomendamos seguir o estilo da interface do usuário das nossas mensagens no app do Android Mobile SDK or kit de desenvolvimento de software.

## Práticas recomendadas {#best-practices}

Para os profissionais de marketing que usam a Braze, o lançamento de uma campanha para a Android TV será idêntico ao lançamento de um push para os apps para mobile do Android. Para direcionar esses dispositivos exclusivamente, recomendamos selecionar o app Android TV na segmentação.

A resposta de entrega e clique retornada pelo FCM seguirá a mesma convenção de um dispositivo Android móvel; portanto, quaisquer erros serão visíveis no registro de atividades da mensagem.
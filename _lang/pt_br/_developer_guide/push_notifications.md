---
nav_title: Notificações por push
article_title: Notificações por push
page_order: 2.3
description: "Esta landing page reúne tudo sobre notificações por push."
---

# Notificações por push {#push-notifications}

> As [notificações por push]({{site.baseurl}}/user_guide/channels/push) permitem que você envie notificações do seu app quando eventos importantes ocorrerem. Você pode enviar uma notificação por push quando tiver novas mensagens instantâneas para entregar, alertas de notícias de última hora para enviar ou o episódio mais recente do programa de TV favorito do seu usuário pronto para ele baixar para visualização offline. Elas também são mais eficientes do que a busca em segundo plano, já que seu aplicativo só é iniciado quando necessário.

{% alert note %}
Se **Redirect to web URL** com **Open web URL inside app** não estiver selecionado, mas o link ainda abrir dentro do app, o app pode estar tratando a URL (por exemplo, com universal links no iOS ou App Links no Android). Para abrir o link no navegador, confirme que seu app delega a URL ao navegador do sistema quando o usuário toca na notificação, ou ajuste o tratamento de URLs do seu app para que a ação de clique corresponda à configuração do dashboard da Braze. Consulte a documentação de push da sua plataforma para saber como as ações de clique e o tratamento de URLs são configurados.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications.md %}
{% endsdktab %}

{% sdktab android tv %}
## Sobre notificações por push para Android TV {#about-push-notifications-for-android-tv}

![Ilustração de dispositivo Android TV usada no guia de notificações por push para Android TV.]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Embora não seja um recurso nativo, a integração de push para Android TV é possível utilizando o SDK Android da Braze e o Firebase Cloud Messaging para registrar um token por push para Android TV. No entanto, você deve criar uma interface para exibir a carga útil da notificação após ela ser recebida.

## Pré-requisitos {#prerequisites}

Para usar esse recurso, você deve concluir o seguinte:

- [Integrar o SDK Android da Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Configurar notificações por push para o SDK Android da Braze]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)

## Configurando notificações por push {#setting-up-push-notifications}

Para configurar notificações por push para Android TV:

1. Crie uma visualização personalizada no seu app para exibir suas notificações.
2. Crie uma [fábrica de notificações personalizada]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_customization-display). Isso substitui o comportamento padrão do SDK e permite que você exiba as notificações manualmente. Ao retornar `null`, isso impede que o SDK processe a notificação e requer código personalizado para exibi-la. Após concluir essas etapas, você pode começar a enviar push para Android TV.<br><br>
3. (Opcional) Para rastrear análises de cliques de forma eficaz, configure o rastreamento de análises de cliques. Isso pode ser feito criando um [retorno de chamada de push]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_push-callback) para escutar intents de push aberto e recebido da Braze.

{% alert note %}
Essas notificações não persistem e só ficam visíveis para o usuário quando o dispositivo as exibe. Isso ocorre porque a central de notificações do Android TV não suporta notificações históricas.
{% endalert %}

## Testando notificações por push para Android TV {#testing-android-tv-push-notifications}

Para testar se sua implementação de push foi bem-sucedida, envie uma notificação pelo dashboard da Braze como faria normalmente para um dispositivo Android.

- **Se o aplicativo estiver fechado**: A mensagem push exibe uma notificação toast na tela.
- **Se o aplicativo estiver aberto**: Você tem a oportunidade de exibir a mensagem na sua própria interface hospedada. Siga o estilo de interface das In-App Messages do SDK Android para dispositivos móveis.

## Práticas recomendadas {#best-practices}

Para profissionais de marketing que usam a Braze, lançar uma Campaign para Android TV é idêntico a lançar um push para apps Android para dispositivos móveis. Para segmentar esses dispositivos exclusivamente, selecione o app Android TV na segmentação.

A resposta de entrega e clique retornada pelo FCM segue a mesma convenção de um dispositivo Android móvel; portanto, quaisquer erros ficam visíveis no registro de atividade da mensagem.

{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/push_notifications.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications.md %}
{% endsdktab %}

{% sdktab huawei %}
{% multi_lang_include developer_guide/huawei/push_notifications.md %}
{% endsdktab %}

{% sdktab React Native %}
{% multi_lang_include developer_guide/react_native/push_notifications.md %}
{% endsdktab %}

{% sdktab safari %}
{% multi_lang_include developer_guide/safari/push_notifications.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/push_notifications.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin)%}
{% multi_lang_include developer_guide/xamarin/push_notifications.md %}
{% endsdktab %}
{% endsdktabs %}
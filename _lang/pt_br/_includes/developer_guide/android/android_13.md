# Atualizando para Android 13 {#upgrading-to-android-13}

> Este guia descreve as alterações relevantes introduzidas no Android 13 (2022) e as etapas de upgrade necessárias para a integração de seu SDK da Braze para Android.

Consulte a [documentação do desenvolvedor do Android 13](https://developer.android.com/about/versions/13) para obter um guia de migração completo.

## Android 13 Braze SDK

Para se preparar para o Android 13, faça o upgrade do SDK da Braze para a [versão mais recente (v21.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300). Ao fazer isso, você terá acesso ao nosso novo [recurso de push primer "sem código"]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Alterações no Android 13 {#changes-in-android-13}

### Permissão de push {#push-permission}

O Android 13 introduz uma [grande mudança](https://developer.android.com/about/versions/13/changes/notification-permission) na forma como os usuários gerenciam os apps que enviam notificações por push. No Android 13, os apps precisam obter permissão antes que as notificações por push possam ser exibidas.

![Uma mensagem push do Android perguntando "Permitir que Kitchenerie envie notificações para você?" com dois botões "Permitir" e "Não permitir" na parte inferior da mensagem.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

Essa nova permissão segue um padrão semelhante ao push para iOS e web, em que você tem apenas uma tentativa para obter a permissão. Se um usuário escolher `Don't Allow` ou dispensar o prompt, seu app não poderá solicitar permissão novamente.

Observe que os apps recebem uma [isenção](https://developer.android.com/about/versions/13/changes/notification-permission#eligibility) para usuários que já tinham as notificações por push ativadas antes de atualizar para o Android 13. Esses usuários [continuarão elegíveis](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps) para receber push quando atualizarem para o Android 13 sem precisar solicitar permissão.

#### Momento do prompt de permissão {#push-permission-timing}

**Direcionando para o Android 13**

Os apps direcionados ao Android 13 podem controlar quando solicitar permissão e exibir o prompt nativo de push.

Se o seu usuário fizer upgrade do Android 12 para o 13, seu app já estava instalado e você já estava enviando push, o sistema concede automaticamente a nova permissão de notificação a todos os apps elegíveis. Em outras palavras, esses apps podem continuar enviando notificações aos usuários, e os usuários não verão um prompt de permissão em tempo de execução.

Para mais detalhes, consulte a documentação do desenvolvedor do Android sobre os [efeitos em atualizações de apps existentes](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps).

**Direcionando para o Android 12 ou anterior**

Se o seu app ainda não é direcionado ao Android 13, quando um novo usuário no Android 13 instalar seu app, ele verá automaticamente um prompt de permissão de push quando o app criar seu primeiro canal de notificação (via `notificationManager.createNotificationChannel`). Usuários que já têm seu app instalado e então fazem upgrade para o Android 13 nunca verão um prompt e receberão automaticamente a permissão de push.

{% alert note %}
O SDK da Braze v23.0.0 cria automaticamente um canal de notificação padrão caso ainda não exista um quando uma notificação por push é recebida. Se você não direcionar para o Android 13, isso fará com que o prompt de permissão de push seja exibido, o que é necessário para mostrar a notificação.
{% endalert %}

## Preparação para o Android 13 {#next-steps}

É altamente recomendável que o seu app tenha como alvo o Android 13 para controlar quando a permissão push é solicitada aos usuários.

Isso permitirá que você otimize suas [taxas de aceitação push](https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps) solicitando aos usuários em momentos mais apropriados e proporcionará uma melhor experiência do usuário em como e quando seu app pede permissão push.

Para começar a usar nosso novo [recurso de push primer "sem código"]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), faça upgrade do SDK do Android para a [versão mais recente (v23.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300).
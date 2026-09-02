## Solução de problemas {#troubleshooting}

### Tocar na notificação por push não abre o app {#tapping-push-notification-doesnt-open-the-app}

No Android, se tocar em uma notificação por push traz automaticamente o app para o primeiro plano e abre o deep link é controlado pela flag nativa `com_braze_handle_push_deep_links_automatically`, que tem o valor padrão `false`.

Com o padrão `false`:

- O SDK or kit de desenvolvimento de software nativo ainda envia um broadcast `BRAZE_PUSH_CLICKED` e o listener `push_opened` do Dart ainda é acionado conforme esperado.
- O SDK or kit de desenvolvimento de software nativo não chama `startActivity()`, então o app não é trazido para o primeiro plano e o deep link não é seguido automaticamente.

Se esses dois comportamentos correspondem ao que você está observando, a configuração da flag provavelmente é a causa.
Para confirmar, verifique os logs do dispositivo em busca de uma entrada `BrazePushReceiver` tratando `com.braze.action.BRAZE_PUSH_CLICKED`, seguida de um evento `push_opened` nos logs do Flutter, sem uma abertura correspondente do app.

Para corrigir isso, defina `com_braze_handle_push_deep_links_automatically` como `true` no seu `braze.xml`:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Para saber mais, consulte [Adicionar deep links (Android)]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android) no guia de notificações por push do Flutter.

### Outros problemas de entrega e registro de push {#other-push-delivery-and-registration-issues}

Como o SDK or kit de desenvolvimento de software Flutter da Braze para Android é construído sobre o SDK or kit de desenvolvimento de software nativo Android da Braze, a maioria dos outros problemas de entrega, registro e logging de push (como incompatibilidade de sender ID, ausência do Google Play Services ou `BrazeFirebaseMessagingService` não registrado) também se aplica a apps Flutter. Para saber mais, consulte o [guia de solução de problemas nativo do Android]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android).
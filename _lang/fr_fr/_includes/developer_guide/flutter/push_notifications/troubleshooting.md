## Résolution des problèmes {#troubleshooting}

### Appuyer sur une notification push n'ouvre pas l'application {#tapping-push-notification-doesnt-open-the-app}

Sur Android, le fait qu'appuyer sur une notification push amène automatiquement votre application au premier plan et ouvre son deep link est contrôlé par le flag natif `com_braze_handle_push_deep_links_automatically`, dont la valeur par défaut est `false`.

Avec la valeur par défaut `false` :

- Le SDK natif envoie toujours un broadcast `BRAZE_PUSH_CLICKED` et votre listener Dart `push_opened` se déclenche comme prévu.
- Le SDK natif n'appelle pas `startActivity()`, donc votre application n'est pas amenée au premier plan et le deep link n'est pas suivi automatiquement.

Si ces deux comportements correspondent à ce que vous observez, le paramétrage du flag en est probablement la cause.
Pour confirmer, vérifiez les journaux de votre appareil pour une entrée `BrazePushReceiver` traitant `com.braze.action.BRAZE_PUSH_CLICKED`, suivie d'un événement `push_opened` dans vos journaux Flutter, sans lancement d'application correspondant.

Pour corriger cela, définissez `com_braze_handle_push_deep_links_automatically` sur `true` dans votre `braze.xml` :

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Pour en savoir plus, consultez [Ajouter des deep links (Android)]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android) dans le guide des notifications push Flutter.

### Autres problèmes de distribution et d'enregistrement des notifications push {#other-push-delivery-and-registration-issues}

Étant donné que le SDK Braze Flutter pour Android est construit sur le SDK natif Braze Android, la plupart des autres problèmes de distribution, d'enregistrement et de journalisation des notifications push (tels que les incohérences d'identifiant d'expéditeur, l'absence de Google Play Services ou le fait que `BrazeFirebaseMessagingService` ne soit pas enregistré) s'appliquent également aux applications Flutter. Pour en savoir plus, consultez le [guide de résolution des problèmes natif Android]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android).
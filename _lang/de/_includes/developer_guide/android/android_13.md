# Auf Android 13 upgraden {#upgrading-to-android-13}

> Dieser Leitfaden beschreibt die für Braze relevanten Änderungen in Android 13 (2022) sowie die erforderlichen Upgrade-Schritte für Ihre Braze-Android-SDK-Integration.

Eine vollständige Anleitung zur Migration finden Sie in der [Dokumentation für Android 13 Entwickler](https://developer.android.com/about/versions/13):in.

## Android 13 Braze SDK

Um sich auf Android 13 vorzubereiten, upgraden Sie bitte Ihr Braze SDK auf die [neueste Version (v21.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300). Damit erhalten Sie Zugang zu unserem neuen [„No-Code“-Push-Primer-Feature]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Änderungen in Android 13 {#changes-in-android-13}

### Push-Genehmigung {#push-permission}

Mit Android 13 [ändert sich](https://developer.android.com/about/versions/13/changes/notification-permission) die Art und Weise, wie Nutzer:innen Apps verwalten, die Push-Benachrichtigungen senden, erheblich. In Android 13 müssen Apps eine Genehmigung einholen, bevor Push-Benachrichtigungen angezeigt werden können.

![Eine Android-Push-Nachricht mit der Frage „Darf Kitchenerie Ihnen Benachrichtigungen senden?“ mit zwei Buttons „Zulassen“ und „Nicht zulassen“ am unteren Rand der Nachricht.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

Diese neue Genehmigung folgt einem ähnlichen Muster wie bei iOS und Web-Push, bei dem Sie nur einen Versuch haben, die Genehmigung einzuholen. Wenn eine Nutzer:in `Don't Allow` wählt oder die Aufforderung schließt, kann Ihre App nicht erneut um Genehmigung bitten.

Beachten Sie, dass Apps eine [Ausnahme](https://developer.android.com/about/versions/13/changes/notification-permission#eligibility) für Nutzer:innen erhalten, die zuvor Push-Benachrichtigungen aktiviert hatten, bevor sie auf Android 13 aktualisiert haben. Diese Nutzer:innen [bleiben berechtigt](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps), Push-Benachrichtigungen zu empfangen, wenn sie auf Android 13 aktualisieren, ohne eine Genehmigung anfordern zu müssen.

#### Zeitpunkt der Genehmigungsaufforderung {#push-permission-timing}

**Targeting auf Android 13**

Apps, die auf Android 13 abzielen, können steuern, wann sie die Genehmigung anfordern und die native Push-Aufforderung anzeigen.

Wenn Ihre Nutzer:in von Android 12 auf 13 aktualisiert, Ihre App zuvor installiert war und Sie bereits Push-Benachrichtigungen gesendet haben, gewährt das System die neue Benachrichtigungsgenehmigung automatisch vorab an alle berechtigten Apps. Mit anderen Worten: Diese Apps können weiterhin Benachrichtigungen an Nutzer:innen senden, und die Nutzer:innen sehen keine Laufzeit-Genehmigungsaufforderung.

Weitere Details finden Sie in der Android-Entwicklerdokumentation zu den [Auswirkungen auf Updates bestehender Apps](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps).

**Targeting auf Android 12 oder früher**

Wenn Ihre App noch nicht auf Android 13 abzielt und eine neue Nutzer:in auf Android 13 Ihre App installiert, wird automatisch eine Push-Genehmigungsaufforderung angezeigt, sobald Ihre App ihren ersten Benachrichtigungskanal erstellt (über `notificationManager.createNotificationChannel`). Nutzer:innen, die Ihre App bereits installiert haben und dann auf Android 13 aktualisieren, sehen keine Aufforderung und erhalten automatisch die Push-Genehmigung.

{% alert note %}
Braze SDK v23.0.0 erstellt automatisch einen Standard-Benachrichtigungskanal, wenn beim Empfang einer Push-Benachrichtigung noch keiner vorhanden ist. Wenn Sie nicht auf Android 13 abzielen, wird dadurch die Push-Genehmigungsaufforderung angezeigt, die zum Anzeigen der Benachrichtigung erforderlich ist.
{% endalert %}

## Vorbereitungen für Android 13 {#next-steps}

Es wird dringend empfohlen, dass Ihre App auf Android 13 abzielt, um zu kontrollieren, wann Nutzer:innen zur Push-Genehmigung aufgefordert werden.

Auf diese Weise können Sie Ihre [Push-Opt-in-Raten](https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps) optimieren, indem Sie die Nutzer:innen zu geeigneteren Zeitpunkten auffordern. Dies führt zu einem besseren Nutzer:innen-Erlebnis in Bezug darauf, wie und wann Ihre App um die Push-Genehmigung bittet.

Um unser neues [„No-Code“-Push-Primer-Feature]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) zu nutzen, upgraden Sie Ihr Android SDK auf die [neueste Version (v23.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300).
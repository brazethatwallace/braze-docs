---
nav_title: Rich-Benachrichtigungen erstellen
article_title: "Rich-Push-Benachrichtigungen für iOS erstellen"
page_order: 3
page_type: tutorial
description: "Dieses Tutorial behandelt die Voraussetzungen und Schritte zum Erstellen von iOS-Rich-Benachrichtigungen für Ihre Braze Campaigns."

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Rich-Push-Benachrichtigungen für iOS erstellen {#create-rich-push-notifications-for-ios}

> Rich-Benachrichtigungen ermöglichen eine stärkere Anpassung Ihrer Push-Benachrichtigungen, indem zusätzliche Inhalte über reinen Text hinaus hinzugefügt werden. Android-Benachrichtigungen enthalten bereits seit einiger Zeit Bilder in Push-Benachrichtigungen, die als „erweitertes Benachrichtigungsbild“ bezeichnet werden. Ab iOS 10 können Ihre Kund:innen iOS-Push-Benachrichtigungen empfangen, die GIFs, Bilder, Videos oder Audio enthalten.

## Voraussetzungen {#prerequisites}

Bevor Sie eine Rich-Push-Benachrichtigung für iOS erstellen, beachten Sie die folgenden Details:

- Um sicherzustellen, dass Ihre App Rich-Benachrichtigungen senden kann, folgen Sie den Anweisungen zur [iOS-Push-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#ios-10-rich-notifications), da Ihre Entwickler:innen eine Serviceerweiterung zu Ihrer App hinzufügen müssen.
- Dateitypen, die wir derzeit für den direkten Upload in unserem Dashboard unterstützen, sind JPEG, PNG oder GIF. Diese Dateien können auch in das vorlagenbasierte URL-Feld eingegeben werden, zusammen mit diesen zusätzlichen Dateitypen: AIF, M4A, MP3, MP4 oder WAV.
- Weitere Informationen zu Medienbeschränkungen und -spezifikationen finden Sie in der [Apple-Dokumentation](https://developer.apple.com/reference/usernotifications/unnotificationattachment).
- iOS skaliert Bilder, um sie an den Bildschirm anzupassen, und skaliert Rich-Bilder für die aktive oder gesperrte Ansicht.

{% alert note %}
Seit Januar 2020 können iOS-Rich-Push-Benachrichtigungen Bilder mit 1038x1038 Pixeln verarbeiten, die unter 10&nbsp;MB groß sind. Wir empfehlen jedoch, eine möglichst kleine Dateigröße zu verwenden. In der Praxis kann das Senden großer Dateien sowohl unnötige Netzwerkbelastung verursachen als auch Download-Timeouts häufiger auftreten lassen.
{% endalert %}

{% alert important %}
Push-Benachrichtigungsbilder werden möglicherweise nicht wie erwartet angezeigt, wenn die Dateigröße des Bildes zu groß ist, das Seitenverhältnis nicht stimmt, der Text die maximale Nachrichtenlänge überschreitet oder der Titeltext die maximale Titellänge überschreitet.
{% endalert %}

### Zeichenanzahl {#character-count}

Obwohl wir keine feste Regel für die genaue Anzahl der Zeichen in einer Push-Benachrichtigung angeben können, [bieten wir einige Richtlinien]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats) an, die Sie beim Entwerfen von iOS-Nachrichten berücksichtigen sollten. Es kann Abweichungen geben, abhängig vom Vorhandensein eines Bildes, dem Benachrichtigungsstatus und den Anzeigeeinstellungen des Geräts der Nutzer:innen sowie der Gerätegröße. Im Zweifelsfall halten Sie es kurz und prägnant.

Als Best Practice empfiehlt Braze, jede Textzeile sowohl für den optionalen Titel als auch für den Nachrichtentext in einer mobilen Push-Benachrichtigung auf etwa 30–40 Zeichen zu beschränken.

#### Benachrichtigungszustände {#notification-states}

Ihre Nutzer:innen können Push-Benachrichtigungen in verschiedenen Situationen sehen und dabei unterschiedliche Textlängen angezeigt bekommen.

<table aria-label="Benachrichtigungszustände">
  <caption>Benachrichtigungszustände</caption>
<thead>
  <tr>
    <th>Sperrbildschirm oder Mitteilungszentrale</th>
    <th>Erweitert</th>
    <th>Gerät aktiv</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">Dies ist das häufigste Szenario.<br><br><b>Titel:</b> 1 Textzeile<br><b>Text:</b> 4 Textzeilen<br><b>Bild:</b> quadratisches Vorschaubild</td>
    <td width="33%">Wenn Nutzer:innen eine Nachricht lange gedrückt halten.<br><br><b>Titel:</b> 1 Textzeile<br><b>Text:</b> 7 Textzeilen<br><b>Bild:</b> Seitenverhältnis 2:1 (empfohlen, siehe folgenden Hinweis)</td>
    <td width="33%">Wenn Nutzer:innen eine Push-Benachrichtigung erhalten, während ihr Telefon entsperrt und aktiv ist.<br><br><b>Titel:</b> 1 Textzeile<br><b>Text:</b> 2 Textzeilen</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Benachrichtigungszustände" }

![Beispiel-Push-Benachrichtigungen für die Anzeige auf dem Sperrbildschirm, im erweiterten Zustand und bei aktivem Gerät.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Obwohl wir ein Seitenverhältnis von 2:1 für erweiterte Push-Benachrichtigungen empfehlen, wird nahezu jedes Seitenverhältnis unterstützt. Bilder erstrecken sich immer über die gesamte Breite der Benachrichtigung, und die Höhe wird entsprechend angepasst.
{% endalert %}

#### Variablen bei der Textkürzung {#variables-in-text-truncation}

Berücksichtigen Sie beim Erstellen von Inhalten die folgenden Szenarien, die beeinflussen können, wie viel Text angezeigt wird.

{% tabs %}
{% tab Zeitstempel %}

Je nachdem, wann Nutzer:innen mit einer Push-Benachrichtigung interagieren, kann der Zeitstempel den Titeltext verkürzen.

![Beispiel-Push-Benachrichtigung mit dem Zeitstempel „jetzt“ und einer Titelzeichenanzahl von 35.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Titelzeichenanzahl: **35**

![Beispiel-Push-Benachrichtigung mit dem Zeitstempel „vor 3 Std.“ und einer Titelzeichenanzahl von 33.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Titelzeichenanzahl: **33**

![Beispiel-Push-Benachrichtigung mit dem Zeitstempel „Gestern, 8:37“ und einer Titelzeichenanzahl von 22.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Titelzeichenanzahl: **22**

{% endtab %}
{% tab Bilder %}

Der Nachrichtentext wird um etwa 10 Zeichen pro Zeile verkürzt, wenn ein Bild vorhanden ist.

![Beispiel-Push-Benachrichtigung ohne Bild und einer Textzeichenanzahl von 179.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Textzeichenanzahl: **179**

![Beispiel-Push-Benachrichtigung mit Bild und einer Textzeichenanzahl von 154.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Textzeichenanzahl: **154**

{% endtab %}
{% tab Unterbrechungsstufe %}

Für iOS 15 verschieben die Kennzeichnungen „Zeitkritisch“ und „Kritisch“ den Titel in eine neue Zeile ohne Zeitstempel, was etwas mehr Platz bietet.

![Beispiel-Push-Benachrichtigung ohne Kennzeichnung „Zeitkritisch“ oder „Kritisch“ und einer Titelzeichenanzahl von 35.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Titelzeichenanzahl: **35**

![Beispiel-Push-Benachrichtigung mit der Kennzeichnung „Zeitkritisch“ und einer Titelzeichenanzahl von 39.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Titelzeichenanzahl: **39**

{% endtab %}
{% tab Weitere %}

Die folgenden Details können ebenfalls die Textkürzung beeinflussen:

- **Anzeigeeinstellungen des Telefons:** Nutzer:innen können die globale UI-Schriftgröße auf ihrem Telefon vergrößern oder verkleinern, in der Regel aus Gründen der Barrierefreiheit.
- **Gerätebreite:** Die Nachricht könnte auf einem kleinen Telefon oder einem breiten iPad angezeigt werden.
- **Inhaltstypen:** Emojis und breite Zeichen wie „m“ und „w“ nehmen mehr Platz ein als „i“ oder „t“, und längere Wörter wie „Engagement“ können abrupter umgebrochen werden als kürzere Wörter.

{% endtab %}
{% endtabs %}

## Einrichten Ihrer iOS-Rich-Benachrichtigung {#setting-up-your-ios-rich-notification}

### 1. Schritt: Push-Campaign erstellen {#step-1-create-a-push-campaign}

Folgen Sie den [Campaign-Schritten]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#creating-a-push-message), um eine Push-Benachrichtigung für iOS zu verfassen. Sie verwenden denselben Composer, den Sie auch zum Einrichten von Push-Benachrichtigungen ohne Rich-Inhalte nutzen.

### 2. Schritt: Medien hinzufügen {#step-2-add-media}

Fügen Sie Ihre Bild-, GIF-, Audio- oder Videodatei im Feld **iOS Notification Image** im Composer der Nachricht hinzu. Informationen zum Hinzufügen Ihrer Inhaltsdateien finden Sie in den [Voraussetzungen](#requirements).

![Ein Beispiel für einen Zusammenfassungstext einer Push-Benachrichtigung.]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

Sie können diese Nachricht auch so einschränken, dass sie nur an Nutzer:innen gesendet wird, deren Gerät iOS 10 oder höher ausführt. Für Nutzer:innen, die nicht auf iOS 10 aktualisiert haben, wird sie als reine Textbenachrichtigung ohne Rich-Inhalte angezeigt, wenn Sie die Option **Only send to devices with Rich Notification support** nicht aktivieren.

![Der Abschnitt „Erweitertes Benachrichtigungsbild“, in dem Sie ein Bild hinzufügen oder eine Bild-URL eingeben können.]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### 3. Schritt: Campaign-Erstellung fortsetzen {#step-3-continue-creating-your-campaign}

Sobald Ihre Rich-Benachrichtigungsinhalte in das Dashboard hochgeladen wurden, können Sie mit der [Planung Ihrer Campaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#schedule-push-campaign) fortfahren.

Wenn Nutzer:innen die Push-Benachrichtigung erhalten, können sie fest auf die Push-Nachricht drücken, um das Bild zu vergrößern.

![Nutzer:innen erhalten eine Push-Benachrichtigung und drücken fest auf die Nachricht, um ein erweitertes Bild mit dem Text „Hello!“ anzuzeigen.]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }
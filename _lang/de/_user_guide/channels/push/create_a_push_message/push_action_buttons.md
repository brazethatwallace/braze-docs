---
nav_title: "Push-Action-Buttons"
article_title: "Push-Action-Buttons"
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt Push-Action-Buttons und die Unterschiede zwischen iOS- und Android-Plattformen."
channel:
  - Push

---

# Push-Action-Buttons {#push-action-buttons}

> Mit Push-Action-Buttons können Sie Inhalte und Aktionen für Buttons festlegen, wenn Sie Push-Benachrichtigungen von Braze für iOS und Android verwenden. Mit Aktions-Buttons können Ihre Nutzer:innen direkt über eine Benachrichtigung mit Ihrer App interagieren, ohne in ein App-Erlebnis klicken zu müssen.

![Eine iOS-Push-Benachrichtigung mit zwei Push-Action-Buttons: „Akzeptieren“ und „Ablehnen“.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

## Aktions-Buttons erstellen {#creating-action-buttons}

Jeder interaktive Button kann auf eine Webseite oder einen Deeplink verweisen oder die App öffnen.

- Bei Standard-Push-Campaigns können Sie Ihre Push-Action-Buttons im Abschnitt **On-Klick, der Behavior** des Push-Nachrichten-Editors im Dashboard festlegen.
- Bei [plattformübergreifenden Push-Campaigns]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push) können Aktions-Buttons unter dem Tab **Einstellungen** für jede Plattform separat konfiguriert werden.

{% tabs %}
{% tab iOS %}
### iOS {#ios}

Um Aktions-Buttons in Ihren iOS-Push-Nachrichten zu verwenden, gehen Sie wie folgt vor:

1. Aktivieren Sie Aktions-Buttons im Tab **Verfassen**.
2. Wählen Sie Ihre **iOS Notification Category** aus den folgenden verfügbaren Button-Kombinationen:
 - Akzeptieren / Ablehnen
 - Ja / Nein
 - Bestätigen / Abbrechen
 - Mehr
 - Vorregistrierte benutzerdefinierte iOS-Kategorie

![Dropdown-Menü für iOS Notification Category.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
Aufgrund der Art und Weise, wie iOS Buttons handhabt, müssen Sie beim Einrichten von Push-Action-Buttons zusätzliche Integrationsschritte durchführen, die in unserer [Entwickler:innen-Dokumentation]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=swift#swift_customizing-push-categories) beschrieben sind. Insbesondere müssen Sie entweder iOS-Kategorien konfigurieren oder aus bestimmten Standard-Button-Optionen auswählen. Bei Android-Integrationen funktionieren diese Buttons automatisch.
{% endalert %}

Voreingestellte Paare wie **Yes** / **No** ordnen dem zweiten Button standardmäßig eine abweisende (**CLOSE**) Aktion zu, sodass er die App nicht auf die gleiche Weise öffnet wie der erste Button. **_Direkte Öffnungen_** umfassen diese Art von Tippen nicht, aber **Push Notification Open**-Daten in Currents oder Snowflake können es dennoch mit `button_action_type` und `button_string` protokollieren. Weitere Informationen finden Sie unter [Push-Action-Buttons und Berichterstattung]({{site.baseurl}}/user_guide/channels/push/reporting#push-action-buttons-and-reporting).
{% endtab %}
{% tab Android %}
### Android {#android}

Um Aktions-Buttons in Ihren Android-Push-Nachrichten zu verwenden, gehen Sie wie folgt vor:

1. Aktivieren Sie Aktions-Buttons im Tab **Verfassen**.
2. Wählen Sie <i class="fas fa-plus-circle"></i> **Add Button** und geben Sie Ihren Button-Text sowie das **On-Klick, der Behavior** an. Sie können aus den folgenden verfügbaren Aktionen auswählen:
  - App öffnen
  - Zu Web-URL weiterleiten
  - [Deeplink]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls) in die Anwendung

![Auswahl von „App öffnen“ als On-Klick, der-Verhalten für einen Benachrichtigungs-Button.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Sie können bis zu drei Buttons in Ihrer Push-Benachrichtigung hinzufügen.

#### Zeichenbegrenzungen bei Android {#android-character-limits}

Im Gegensatz zu iOS-Buttons, die gestapelt werden, werden Android-Buttons nebeneinander in einer Reihe angezeigt. Das bedeutet, je mehr Buttons Sie hinzufügen (bis zu drei), desto weniger Platz steht für den Button-Text zur Verfügung.

![Android-Push-Action-Buttons mit abgeschnittenem Text.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

Die folgende Tabelle zeigt, wie viele Zeichen Sie hinzufügen können, bevor Ihr Button-Text abgeschnitten wird, abhängig von der Anzahl der Buttons:

| Anzahl der Buttons | Maximale Zeichen pro Button |
| --- | --- |
| 1 | 46 Zeichen |
| 2 | 20 Zeichen |
| 3 | 11 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zeichenbegrenzungen bei Android" }
{% endtab %}
{% endtabs %}
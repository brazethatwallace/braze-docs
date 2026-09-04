---
nav_title: Nutzer:innenverwaltung
article_title: LINE-Nutzer:innenverwaltung
page_order: 0
description: "Dieser Artikel behandelt die LINE-Nutzer-ID und wie Sie diese festlegen."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# LINE-Nutzer:innenverwaltung {#line-user-management}

> Die LINE-Nutzer-ID wird im Kundenprofil-Attribut `native_line_id` gespeichert, das zum Senden von Nachrichten an Nutzer:innen über den LINE-Kanal verwendet wird. Dieser Artikel beschreibt, wie Sie das Attribut `native_line_id` festlegen und finden.

Nutzerdaten werden in einem [Braze-Kundenprofil]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) dargestellt. Ein Kundenprofil speichert Informationen und Attribute über die Nutzer:innen eines Unternehmens, wie z. B. Vornamen und E-Mail-Adressen.

Wenn Sie LINE-Nachrichten über Braze senden, verwendet Braze das Attribut `native_line_id`, um zu identifizieren, an welche Nutzer:innen die Nachricht gesendet werden soll. Wenn LINE Braze Webhook-Ereignisse sendet, z. B. wenn Nutzer:innen einem Kanal folgen oder auf eine Nachricht antworten, wird die `native_line_id` verwendet, um das entsprechende Kundenprofil zu finden.

{% alert note %}
LINE-Nutzer-IDs sind je LINE-Anbieter unterschiedlich. Bestimmte Nutzer:innen haben für jeden Anbieter, dem sie folgen, unterschiedliche LINE-Nutzer-IDs. Nutzer:innen kennen ihre LINE-ID wahrscheinlich nicht (im Gegensatz zu ihrer E-Mail-Adresse oder Telefonnummer), da sie sich für jede Marke, der sie folgen, ändert.
{% endalert %}

## Festlegen des Attributs `native_line_id` {#setting-the-native_line_id-attribute}

Es gibt verschiedene Szenarien, in denen `native_line_id` im Kundenprofil festgelegt wird. Diese sind im Folgenden beschrieben.

| Szenario | Ob ein Kundenprofil mit `native_line_id` existiert | Ergebnis |
| --- | --- | --- |
| Nutzer:in folgt einem LINE-Kanal | Nein | Ein anonymes Kundenprofil wird erstellt (Zusammenführung erforderlich):<br> - `native_line_id` wird auf die LINE-ID der Nutzerin oder des Nutzers gesetzt <br>- `line_id`-Nutzer-Alias wird auf die LINE-ID der Nutzerin oder des Nutzers gesetzt<br>- Die Nutzerin oder der Nutzer wird in die Braze-Abo-Gruppe des Kanals aufgenommen |
| Nutzer:in folgt einem LINE-Kanal | Ja | Alle Nutzerprofile mit der `native_line_id`:<br>- Werden in die Braze-Abo-Gruppe des Kanals aufgenommen |
| Unternehmen verwendet CSV-Upload mit einer `native_line_id`-Spalte | Nein | Wenn kein Kundenprofil für die angegebene `external_id` oder den Nutzer-Alias existiert:<br>- `native_line_id` wird auf den angegebenen Wert gesetzt<br> - Alle anderen im CSV angegebenen Attribute werden im Kundenprofil gesetzt |
| Unternehmen verwendet CSV-Upload mit einer `native_line_id`-Spalte | Ja | Wenn ein Kundenprofil für die angegebene `external_id` oder den Nutzer-Alias existiert:<br>- `native_line_id` wird auf den angegebenen Wert gesetzt<br>- Alle anderen im CSV angegebenen Attribute werden im Kundenprofil gesetzt<br>- Mehrere Profile haben dieselbe `native_line_id` |
| Unternehmen verwendet den Endpunkt `/users/track` und gibt das Attribut `native_line_id` an | Nein | Wenn kein Kundenprofil für die angegebene Nutzerin oder den angegebenen Nutzer existiert ([angegeben durch `external_id`, `user_alias`, `braze_id` oder `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution)):<br>- `native_line_id` wird auf den angegebenen Wert gesetzt<br>- Alle anderen in der Anfrage angegebenen Attribute werden im Kundenprofil gesetzt |
| Unternehmen verwendet den Endpunkt `/users/track` und gibt das Attribut `native_line_id` an | Ja | Wenn ein Kundenprofil für die angegebene Nutzerin oder den angegebenen Nutzer existiert ([angegeben durch `external_id`, `user_alias`, `braze_id` oder `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution)):<br>- `native_line_id` wird auf den angegebenen Wert gesetzt<br>- Alle anderen in der Anfrage angegebenen Attribute werden im Kundenprofil gesetzt<br>- Mehrere Profile haben dieselbe `native_line_id` |
| Unternehmen fordert Braze auf, den Abo-Status-Synchronisierer auszuführen | Nein | Wenn eine LINE-Nutzer-ID von LINE zurückgegeben wird, für die kein entsprechendes Kundenprofil in Braze existiert, wird ein anonymes Kundenprofil erstellt:<br>- `native_line_id` wird auf die LINE-ID der Nutzerin oder des Nutzers gesetzt<br>- `line_id`-Nutzer-Alias wird auf die LINE-ID der Nutzerin oder des Nutzers gesetzt<br>- Die Nutzerin oder der Nutzer wird in die Braze-Abo-Gruppe des Kanals aufgenommen<br><br>Beachten Sie: Wenn später Nutzer:innen mit derselben LINE-ID erstellt werden, gibt es doppelte Nutzer:innen, aber beide haben den korrekten LINE-Abo-Status. Die Zusammenführung von Nutzer:innen kann Ihre Nutzerbasis in diesen Fällen bereinigen. |
| Unternehmen fordert Braze auf, den Abo-Status-Synchronisierer auszuführen | Ja | Wenn eine LINE-Nutzer-ID von LINE zurückgegeben wird, für die ein entsprechendes Kundenprofil in Braze existiert:<br>- Die Nutzerin oder der Nutzer wird in die Braze-Abo-Gruppe des Kanals aufgenommen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Festlegen des Attributs native_line_id" }

## Finden der `native_line_id` {#finding-the-native_line_id}

Wenn Sie ein Kundenprofil im Braze-Dashboard anzeigen, können Sie überprüfen, ob das Attribut `native_line_id` gesetzt ist, indem Sie zum Tab **Engagement** > Abschnitt **Contact Settings** > Abschnitt **LINE** navigieren.

Wenn die `native_line_id` gesetzt wurde, wird sie unter **LINE User ID** angezeigt. Andernfalls wird sie nicht angezeigt.

![LINE-Kontakteinstellungen im Tab „Engagement“.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}
---
nav_title: Nutzerprofil-Lebenszyklus
article_title: Nutzerprofil-Lebenszyklus
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt den Nutzerprofil-Lebenszyklus von Braze und die verschiedenen Möglichkeiten, wie ein Nutzerprofil identifiziert und referenziert werden kann."

---

# Nutzerprofil-Lebenszyklus {#user-profile-lifecycle}

> Dieser Artikel beschreibt den Nutzerprofil-Lebenszyklus von Braze und die verschiedenen Möglichkeiten, ein Nutzerprofil zu identifizieren und zu referenzieren. Wenn Sie Ihren Kundenlebenszyklus besser verstehen möchten, sehen Sie sich stattdessen unseren Braze-Lernkurs zur [Abbildung von Nutzer:innen-Lebenszyklen](https://learning.braze.com/mapping-customer-lifecycles) an.

Alle persistenten Daten, die mit einer Nutzer:in verbunden sind, werden in deren Nutzerprofil gespeichert. Nachdem ein Nutzerprofil erstellt wurde – entweder über die API oder nachdem eine Nutzer:in vom SDK erkannt wurde – können Sie diesem Profil eine Reihe von Parametern zuweisen, um die Nutzer:in zu identifizieren und zu referenzieren.

Diese Parameter umfassen:

* `braze_id` (zugewiesen von Braze)
* `external_id`
* `email`
* `phone`
* Beliebig viele angepasste Nutzer-Aliasse, die Sie festlegen

## Anonyme Nutzerprofile {#anonymous-user-profiles}

Alle Nutzer:innen ohne eine zugewiesene `external_id` werden als [anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) bezeichnet. Dabei kann es sich beispielsweise um Nutzer:innen handeln, die Ihre Website besucht, sich aber nicht registriert haben, oder um Nutzer:innen, die Ihre mobile App heruntergeladen, aber kein Profil erstellt haben.

Wenn Nutzer:innen erstmals vom SDK erkannt werden, wird ein anonymes Nutzerprofil mit einer zugehörigen `braze_id` erstellt: ein eindeutiger Bezeichner, der automatisch von Braze zugewiesen wird, nicht bearbeitet werden kann und gerätespezifisch ist. Dieser Bezeichner kann verwendet werden, um das Nutzerprofil über die [API]({{site.baseurl}}/api/endpoints/user_data) zu aktualisieren.

## Identifizierte Nutzerprofile {#identified-user-profiles}

Nachdem eine Nutzer:in in Ihrer App erkennbar ist (durch Angabe einer Nutzer-ID oder E-Mail-Adresse), empfehlen wir, dem Nutzerprofil eine `external_id` über die Methode `changeUser` zuzuweisen ([web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)). Eine `external_id` ermöglicht es Ihnen, dasselbe Nutzerprofil über mehrere Geräte hinweg zu identifizieren.

Weitere Vorteile der Verwendung einer `external_id` sind unter anderem:

- Ein konsistentes Nutzererlebnis über mehrere Geräte und Plattformen hinweg bieten (z. B. keine Benachrichtigungen für inaktive Nutzer:innen an das Android-Tablet senden, wenn sie treue Nutzer:innen der iPhone-App sind).
- Die Genauigkeit Ihrer Analytics verbessern, indem Sie sicherstellen, dass Nutzer:innen nicht jedes Mal ein neues Nutzerprofil erstellen, wenn sie die App deinstallieren und neu installieren oder auf einem anderen Gerät installieren.
- Den Import von Nutzerdaten aus Quellen außerhalb der App über die [Nutzerdaten-Endpunkte]({{site.baseurl}}/api/endpoints/user_data) ermöglichen und Nutzer:innen mit transaktionalen Nachrichten über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) ansprechen.
- Einzelne Nutzer:innen über unsere „Testing“-[Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) im Segmenter und auf der Seite [**Nutzer:innen suchen**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) suchen.

### Überlegungen zu externen IDs {#considerations-for-external-ids}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

#### Risiko der Verwendung einer E-Mail oder gehashten E-Mail als externe ID {#risk-of-using-an-email-or-hashed-email-as-an-external-id}

Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als Braze externe ID kann die Identitätsverwaltung über Ihre Datenquellen hinweg vereinfachen; es ist jedoch wichtig, die potenziellen Risiken für den Datenschutz und die Datensicherheit zu berücksichtigen.

- **Erratbare Informationen:** E-Mail-Adressen sind leicht zu erraten, was sie anfällig für Angriffe macht.
- **Risiko des Missbrauchs:** Wenn böswillige Nutzer:innen ihren Webbrowser so manipulieren, dass die E-Mail-Adresse einer anderen Person als ihre externe ID gesendet wird, könnten sie potenziell auf vertrauliche Nachrichten oder Kontoinformationen zugreifen.

### Was passiert, wenn Sie anonyme Nutzer:innen identifizieren {#what-happens-when-you-identify-anonymous-users}

Beim Identifizieren anonymer Nutzer:innen können zwei Szenarien eintreten:

1) **Eine anonyme Nutzer:in wird zu einer neuen identifizierten Nutzer:in:** <br>Wenn die `external_id` in Braze noch nicht existiert, wird die anonyme Nutzer:in zu einer neuen identifizierten Nutzer:in und behält alle Attribute und den Verlauf des anonymen Nutzerprofils bei.

2) **Eine anonyme Nutzer:in wird als bereits existierende Nutzer:in identifiziert:** <br>Wenn die `external_id` bereits in Braze existiert, wurde diese Nutzer:in zuvor auf andere Weise im System identifiziert, z. B. über ein anderes Gerät (wie ein Tablet) oder importierte Nutzerdaten.

Mit anderen Worten: Sie haben bereits ein Nutzerprofil für diese Nutzer:in. In diesem Fall wird Braze Folgendes tun:
1. Das anonyme Nutzerprofil verwaisen lassen
2. [Bestimmte Nutzerprofilfelder]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior), die im identifizierten Nutzerprofil noch nicht vorhanden sind, aus dem anonymen Profil zusammenführen
3. Das anonyme Profil aus Ihrer Nutzerbasis entfernen, damit die Nutzeranzahl nicht aufgebläht wird

Wenn sowohl die anonyme Nutzer:in als auch die bekannte Nutzer:in einen Vornamen haben, wird der Vorname der bekannten Nutzer:in beibehalten. Wenn die bekannte Nutzer:in einen Nullwert hat und die anonyme Nutzer:in einen Wert besitzt, wird der Wert der anonymen Nutzer:in in das Profil der bekannten Nutzer:in übernommen, sofern der Wert unter diese [bestimmten Nutzerprofilfelder]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) fällt.

{% alert important %}
Nicht alle Daten werden aus dem anonymen Profil zusammengeführt. Push-Token und der Nachrichtenverlauf werden übertragen, und angepasste Attribute, angepasste Events sowie die Kaufhistorie aus dem anonymen Profil werden nur dann in die identifizierte Nutzer:in übernommen, wenn diese Felder im identifizierten Nutzerprofil noch nicht vorhanden sind. Bei widersprüchlichen Daten werden die Werte der identifizierten Nutzer:in beibehalten. Siehe [Zusammenführungsverhalten]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) für die vollständige Liste der Felder, die übertragen bzw. nicht übertragen werden.
{% endalert %}

Informationen zum Festlegen einer `external_id` für ein Nutzerprofil finden Sie in unserer Dokumentation ([iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)).

{% alert note %}
Verwaiste Nutzer:innen sind nicht berechtigt, Nachrichten zu empfangen.
{% endalert %}

### Doppelte Nutzer:innen zusammenführen {#merging-duplicate-users}

Wenn Sie doppelte Nutzerprofile in Ihrem Workspace identifizieren, können Sie diese über die REST API zusammenführen. Weitere Informationen zum Zusammenführen von Nutzer:innen und den verfügbaren Methoden finden Sie unter [Doppelte Nutzer:innen zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

## Nutzer-Aliase {#user-aliases}

Um Nutzer:innen über andere Bezeichner als die Braze `external_id` anzusprechen, können Sie Nutzer-Aliase für ein Nutzerprofil festlegen. Jeder Alias, der für ein Nutzerprofil festgelegt wird, wirkt zusätzlich zur `braze_id` oder `external_id` der Nutzer:innen und ersetzt diese nicht. Es gibt keine Begrenzung für die Anzahl der Aliase, die Sie für ein Nutzerprofil festlegen können.

Jeder Alias funktioniert als Schlüssel-Wert-Paar, das aus zwei Teilen besteht: einem `alias_label`, das den Schlüssel des Alias definiert, und einem `alias_name`, das den Wert definiert. Ein `alias_name` für ein einzelnes Label muss innerhalb Ihrer Nutzerbasis eindeutig sein (genau wie bei `external_id`). Wenn Sie versuchen, ein zweites Nutzerprofil mit einer bereits vorhandenen Label-und-Name-Kombination zu aktualisieren, wird das Nutzerprofil nicht aktualisiert.

### Nutzer-Aliase aktualisieren {#updating-user-aliases}

Ein Alias kann nach dem Festlegen mit einem neuen Namen für ein bestimmtes Label aktualisiert werden, entweder über unsere [Nutzerdaten-Endpunkte]({{site.baseurl}}/developer_guide/rest_api/user_data#new-user-alias-endpoint) oder durch Übergabe eines neuen Namens über das SDK. Der Nutzer-Alias ist dann beim Exportieren der Daten dieser Nutzer:innen sichtbar.

![Zwei verschiedene Nutzerprofile für separate Nutzer:innen mit demselben Nutzer-Alias-Label, aber unterschiedlichen Alias-Namen]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### Anonyme Nutzer:innen taggen {#tagging-anonymous-users}

Nutzer-Aliase ermöglichen es Ihnen auch, anonyme Nutzer:innen mit einem Bezeichner zu taggen. Wenn beispielsweise Nutzer:innen Ihrer E-Commerce-Website ihre E-Mail-Adresse angeben, sich aber noch nicht registriert haben, kann die E-Mail-Adresse als Alias für diese anonymen Nutzer:innen verwendet werden. Diese Nutzer:innen können dann über ihre Aliase exportiert oder über die API referenziert werden.

### Verhalten von Aliasen bei anonymen Nutzerprofilen {#behavior-of-aliases-on-anonymous-user-profiles}

Wenn ein anonymes Nutzerprofil mit einem Alias später mit einer `external_id` erkannt wird, wird es als normales identifiziertes Nutzerprofil behandelt, behält aber seinen bestehenden Alias bei und kann weiterhin über diesen Alias referenziert werden.

### Nach einem Nutzer-Alias suchen {#searching-for-a-user-alias}

Wenn Sie den Alias-Namen und das Label von Nutzer:innen kennen, können Sie die Nutzer:innen unter **Nutzer:innen suchen** im Format `alias_label:alias_name` finden. Wenn Sie beispielsweise ein Alias-only-Profil mit dem Namen `alias_name: bobby_alias` und dem Label `alias_label: m4pzOndtA-CnO0u` haben, können Sie diese Nutzer:innen finden, indem Sie `m4pzOndtA-CnO0u:bobby_alias` eingeben.

Wenn Sie diese Informationen nicht kennen, können Sie den [`Export user profile by identifier`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) aufrufen und den Nutzer-Alias in der API-Antwort finden.

### Aliase für bekannte Nutzerprofile festlegen {#setting-aliases-on-known-user-profiles}

Ein Nutzer-Alias kann auch für ein bekanntes Nutzerprofil festgelegt werden, um bekannte Nutzer:innen über eine andere extern bekannte ID zu referenzieren. Beispielsweise können Nutzer:innen eine Business-Intelligence-Tool-ID (wie eine Amplitude-ID) haben, die Sie innerhalb von Braze referenzieren möchten.

Informationen zum Festlegen eines Nutzer-Alias finden Sie in unserer Dokumentation für jede Plattform ([iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids#aliasing-users), [Internet]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#aliasing-users)).

![Ein Flussdiagramm des Nutzerprofil-Lebenszyklus in Braze. Wenn changeUser() für anonyme Nutzer:innen aufgerufen wird, werden diese zu identifizierten Nutzer:innen und die Daten werden in ihr identifiziertes Nutzerprofil migriert. Identifizierte Nutzer:innen haben eine Braze-ID und eine externe ID. Wenn zu diesem Zeitpunkt für zweite anonyme Nutzer:innen changeUser() aufgerufen wird, werden Nutzerdatenfelder, die noch nicht bei den identifizierten Nutzer:innen vorhanden sind, zusammengeführt. Wenn den identifizierten Nutzer:innen ein Alias zu ihrem bestehenden Nutzerprofil hinzugefügt wird, werden keine Daten beeinflusst, aber sie werden zu identifizierten Nutzer:innen mit Alias. Wenn dann für dritte anonyme Nutzer:innen mit demselben Alias-Label wie die identifizierten Nutzer:innen, aber einem anderen Alias-Namen, changeUser() aufgerufen wird, werden alle Felder, die bei den identifizierten Nutzer:innen nicht vorhanden sind, zusammengeführt und das Alias-Label im identifizierten Nutzerprofil wird beibehalten.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
Fällt es Ihnen schwer, sich vorzustellen, wie dies für den Nutzerprofil-Lebenszyklus Ihrer Kund:innen aussehen könnte? Besuchen Sie [Best Practices]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices), um Best Practices zur Nutzerdatenerfassung einzusehen.
{% endalert %}

## Erweiterter Anwendungsfall {#advanced-use-case}

Sie können einen neuen Nutzer-Alias für bestehende identifizierte Nutzerprofile über unser SDK und unsere API mithilfe der [Nutzerdaten-Endpunkte]({{site.baseurl}}/developer_guide/rest_api/user_data#new-user-alias-endpoint) festlegen. Nutzer-Aliase können jedoch nicht über die API für ein bestehendes unbekanntes Nutzerprofil festgelegt werden.

Die Nutzer-Aliase werden im Prozess ebenfalls zusammengeführt. Wenn jedoch sowohl das zu verwaisende als auch das Ziel-Nutzerprofil einen Alias mit demselben Label haben, wird nur der Alias des Ziel-Nutzerprofils beibehalten.

Durch das Deinstallieren und Neuinstallieren einer App wird eine neue anonyme `braze_id` für diese:n Nutzer:in generiert.

### Fehlerbehebung mit Nutzer-IDs {#troubleshooting-with-user-ids}

Alle Nutzer-IDs können verwendet werden, um Nutzer:innen in Ihrem Dashboard zu finden und für Tests zu identifizieren. Um Ihre:n Nutzer:in im Braze-Dashboard zu finden, lesen Sie [Testnutzer:innen hinzufügen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users).

{% alert important %}
Braze blockiert Nutzerprofile, die ungewöhnlich groß werden („Dummy-Nutzer:innen“), da diese Profile in der Regel das Ergebnis einer fehlerhaften Integration sind. Ein Profil wird blockiert, wenn es einen der folgenden Schwellenwerte überschreitet:

- Mehr als 5.000.000 Sitzungen
- Mehr als 20.000 verschiedene Namen für angepasste Events
- Mehr als 20.000 verschiedene Produktnamen bei Käufen

Nachdem ein Profil blockiert wurde, nimmt Braze keine eingehenden Daten mehr für dieses Profil auf – weder von den SDKs noch von der REST API. Wenn Sie feststellen, dass dies bei einem/einer legitimen Nutzer:in passiert ist, wenden Sie sich an Ihre:n Braze Account Manager. Weitere Informationen finden Sie unter [Spam-Blockierung]({{site.baseurl}}/user_archival).
{% endalert %}
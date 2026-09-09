---
nav_title: Kundenprofil-Lebenszyklus
article_title: Kundenprofil-Lebenszyklus
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt den Kundenprofil-Lebenszyklus von Braze und die verschiedenen Möglichkeiten, wie ein Kundenprofil identifiziert und referenziert werden kann."

---

# Kundenprofil-Lebenszyklus {#user-profile-lifecycle}

> Dieser Artikel beschreibt den Kundenprofil-Lebenszyklus von Braze und die verschiedenen Möglichkeiten, ein Kundenprofil zu identifizieren und zu referenzieren. Wenn Sie Ihren Kundenlebenszyklus besser verstehen möchten, sehen Sie sich stattdessen unseren Braze-Lernkurs zur [Abbildung von Nutzer:innen-Lebenszyklen](https://learning.braze.com/mapping-customer-lifecycles) an.

Alle persistenten Daten, die mit einer Nutzer:in verbunden sind, werden in deren Kundenprofil gespeichert. Nachdem ein Kundenprofil erstellt wurde – entweder über die API oder nachdem eine Nutzer:in vom SDK erkannt wurde – können Sie diesem Profil eine Reihe von Parametern zuweisen, um die Nutzer:in zu identifizieren und zu referenzieren.

Diese Parameter umfassen:

* `braze_id` (zugewiesen von Braze)
* `external_id`
* `email`
* `phone`
* Beliebig viele angepasste Nutzer-Aliasse, die Sie festlegen

## Anonyme Nutzerprofile {#anonymous-user-profiles}

Alle Nutzer:innen ohne zugewiesene `external_id` werden als [anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) bezeichnet. Dabei kann es sich beispielsweise um Nutzer:innen handeln, die Ihre Website besucht, sich aber nicht registriert haben, oder um Nutzer:innen, die Ihre mobile App heruntergeladen, aber kein Profil erstellt haben.

Wenn Nutzer:innen erstmals vom SDK erkannt werden, wird ein anonymes Kundenprofil mit einer zugehörigen `braze_id` erstellt: ein eindeutiger Bezeichner, der automatisch von Braze zugewiesen wird, nicht bearbeitet werden kann und gerätespezifisch ist. Dieser Bezeichner kann verwendet werden, um das Kundenprofil über die [API]({{site.baseurl}}/api/endpoints/user_data) zu aktualisieren.

## Identifizierte Nutzerprofile {#identified-user-profiles}

Nachdem eine:r Nutzer:in in Ihrer App erkennbar ist (z. B. durch Angabe einer Nutzer-ID oder E-Mail-Adresse), empfehlen wir, dem Kundenprofil über die Methode `changeUser` ([Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)) eine `external_id` zuzuweisen. Eine `external_id` ermöglicht es Ihnen, dasselbe Kundenprofil über mehrere Geräte hinweg zu identifizieren.

Zu den weiteren Vorteilen der Verwendung einer `external_id` gehören:

- Ein konsistentes Nutzererlebnis über mehrere Geräte und Plattformen hinweg bereitstellen (z. B. keine Benachrichtigungen für inaktive Nutzer:innen an das Android-Tablet senden, wenn diese treue Nutzer:innen der iPhone-App sind).
- Die Genauigkeit Ihrer Analytics verbessern, indem bestätigt wird, dass Nutzer:innen nicht jedes Mal ein neues Kundenprofil erstellen, wenn sie die App deinstallieren und neu installieren oder auf einem anderen Gerät installieren.
- Den Import von Nutzerdaten aus Quellen außerhalb der App über die [Nutzerdaten-Endpunkte]({{site.baseurl}}/api/endpoints/user_data) ermöglichen und Nutzer:innen mit transaktionalen Nachrichten über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) ansprechen.
- Einzelne Nutzer:innen mithilfe unserer „Testing“-[Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) im Segmentierer und auf der Seite [**Nutzer:innen suchen**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) suchen.

### Hinweise zu externen IDs {#considerations-for-external-ids}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

#### Risiko bei der Verwendung einer E-Mail oder gehashten E-Mail als externe ID {#risk-of-using-an-email-or-hashed-email-as-an-external-id}

Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als externe ID in Braze kann die Identitätsverwaltung über Ihre Datenquellen hinweg vereinfachen. Es ist jedoch wichtig, die potenziellen Risiken für die Privatsphäre und die Datensicherheit der Nutzer:innen zu berücksichtigen.

- **Erratbare Informationen:** E-Mail-Adressen sind leicht zu erraten, was sie anfällig für Angriffe macht.
- **Risiko des Missbrauchs:** Wenn böswillige Nutzer:innen ihren Webbrowser so manipulieren, dass die E-Mail-Adresse einer anderen Person als externe ID gesendet wird, könnten sie möglicherweise auf vertrauliche Nachrichten oder Kontoinformationen zugreifen.

### Was passiert, wenn Sie anonyme Nutzer:innen identifizieren {#what-happens-when-you-identify-anonymous-users}

Bei der Identifizierung anonymer Nutzer:innen können zwei Szenarien eintreten:

1) **Anonyme:r Nutzer:in wird zu identifizierten Nutzer:in:** <br>Wenn die `external_id` in Braze noch nicht existiert, wird die/der anonyme Nutzer:in zu einer/einem neuen identifizierten Nutzer:in und behält alle Attribute und den gesamten Verlauf des anonymen Profils bei.

2) **Anonyme:r Nutzer:in wird als bereits existierende:r Nutzer:in identifiziert:** <br>Wenn die `external_id` bereits in Braze existiert, wurde diese:r Nutzer:in zuvor auf andere Weise im System identifiziert, z. B. über ein anderes Gerät (wie ein Tablet) oder importierte Nutzerdaten.

Mit anderen Worten: Sie haben bereits ein Kundenprofil für diese:n Nutzer:in. In diesem Fall führt Braze Folgendes aus:
1. Das anonyme Kundenprofil verwaisen lassen
2. [Bestimmte Nutzerprofilfelder]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior), die noch nicht im identifizierten Kundenprofil vorhanden sind, aus dem anonymen Profil zusammenführen
3. Das anonyme Profil aus Ihrer Nutzerbasis entfernen, damit die Nutzeranzahl nicht aufgebläht wird

Wenn sowohl die/der anonyme als auch die/der bekannte Nutzer:in einen Vornamen haben, wird der Vorname der/des bekannten Nutzer:in beibehalten. Wenn die/der bekannte Nutzer:in einen Nullwert hat und die/der anonyme Nutzer:in einen Wert besitzt, wird der Wert der/des anonymen Nutzer:in in das Profil der/des bekannten Nutzer:in übernommen, sofern der Wert unter diese [bestimmten Nutzerprofilfelder]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) fällt.

{% alert important %}
Nicht alle Daten werden aus dem anonymen Profil zusammengeführt. Push-Token und der Nachrichtenverlauf werden übertragen, und angepasste Attribute, angepasste Events sowie die Kaufhistorie aus dem anonymen Profil werden nur dann in das identifizierte Kundenprofil übernommen, wenn diese Felder im identifizierten Kundenprofil noch nicht vorhanden sind. Bei widersprüchlichen Daten werden die Werte der/des identifizierten Nutzer:in beibehalten. Die vollständige Liste der Felder, die übertragen bzw. nicht übertragen werden, finden Sie unter [Zusammenführungsverhalten]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).
{% endalert %}

Informationen zum Festlegen einer `external_id` für ein Kundenprofil finden Sie in unserer Dokumentation ([iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)).

### Reporting und zusammengeführte Profile {#reporting-and-merged-profiles}

Wenn anonyme und identifizierte Profile nach einem Versand zusammengeführt werden, ordnen die Campaign-Zusammenfassungen im Dashboard diesen Versand dem überlebenden (identifizierten) Profil zu. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), der [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) und der Tab [Nachrichtenverlauf]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab) ordnen den Versand weiterhin der Nutzer-ID des verwaisten Profils zu – also der ID zum Zeitpunkt des Versands. Dies ist das erwartete Verhalten. Die vollständige Liste der übertragenen Felder finden Sie unter [Zusammenführungsverhalten]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

Um diesen Versand in Currents, im Query Builder oder im Nachrichtenverlauf zu finden, suchen Sie nach der `braze_id` des verwaisten Profils. Eine Abfrage, die nur die `braze_id` der/des identifizierten Nutzer:in verwendet, gibt den Versand vor der Zusammenführung nicht zurück.

{% alert note %}
Verwaiste Nutzer:innen sind nicht berechtigt, Nachrichten zu empfangen.
{% endalert %}

### Zusammenführen doppelter Nutzer:innen {#merging-duplicate-users}

Wenn Sie doppelte Nutzerprofile in Ihrem Workspace identifizieren, können Sie diese über die REST API zusammenführen. Weitere Informationen zum Zusammenführen von Nutzer:innen und den verfügbaren Methoden finden Sie unter [Doppelte Nutzer:innen zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

## Nutzer-Aliase {#user-aliases}

Um Nutzer:innen durch andere Bezeichner als die Braze `external_id` zu referenzieren, können Sie Nutzer-Aliase für ein Kundenprofil festlegen. Jeder Alias, der für ein Kundenprofil festgelegt wird, funktioniert zusätzlich zur `braze_id` oder `external_id` der Nutzer:innen – und nicht als Ersatz dafür. Es gibt keine Begrenzung für die Anzahl der Aliase, die Sie für ein Kundenprofil festlegen können.

Jeder Alias funktioniert als Schlüssel-Wert-Paar, das aus zwei Teilen besteht: einem `alias_label`, das den Schlüssel des Alias definiert, und einem `alias_name`, das den Wert definiert. Ein `alias_name` für ein einzelnes Label muss über Ihre gesamte Nutzerbasis hinweg eindeutig sein (genau wie bei `external_id`). Wenn Sie versuchen, ein zweites Kundenprofil mit einer bereits vorhandenen Label-Name-Kombination zu aktualisieren, wird das Kundenprofil nicht aktualisiert.

### Nutzer-Aliase aktualisieren {#updating-user-aliases}

Ein Alias kann nach der Festlegung mit einem neuen Namen für ein bestimmtes Label aktualisiert werden – entweder über unsere [Nutzerdaten-Endpunkte]({{site.baseurl}}/api/endpoints/user_data) oder durch die Übergabe eines neuen Namens über das SDK. Der Nutzer-Alias ist dann beim Exportieren der Daten dieser Nutzer:innen sichtbar.

![Zwei verschiedene Nutzerprofile für unterschiedliche Nutzer:innen mit demselben Nutzer-Alias-Label, aber unterschiedlichen Alias-Namen]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### Anonyme Nutzer:innen taggen {#tagging-anonymous-users}

Nutzer-Aliase ermöglichen es Ihnen auch, anonyme Nutzer:innen mit einem Bezeichner zu versehen. Wenn beispielsweise eine Nutzer:in Ihre E-Commerce-Website ihre E-Mail-Adresse angibt, sich aber noch nicht registriert hat, kann die E-Mail-Adresse als Alias für diese anonyme Nutzer:in verwendet werden. Diese Nutzer:innen können dann über ihre Aliase exportiert oder über die API referenziert werden.

### Verhalten von Aliasen bei anonymen Nutzerprofilen {#behavior-of-aliases-on-anonymous-user-profiles}

Wenn ein anonymes Kundenprofil mit einem Alias später mit einer `external_id` erkannt wird, wird es als normales identifiziertes Kundenprofil behandelt, behält aber seinen bestehenden Alias und kann weiterhin über diesen Alias referenziert werden.

### Nach einem Nutzer-Alias suchen {#searching-for-a-user-alias}

Wenn Sie den Alias-Namen und das Label einer Nutzer:in kennen, können Sie die Nutzer:in unter **Nutzer:innen suchen** im Format `alias_label:alias_name` finden. Wenn Sie beispielsweise ein Alias-only-Profil mit dem Namen `alias_name: bobby_alias` und dem Label `alias_label: m4pzOndtA-CnO0u` haben, können Sie diese Nutzer:in finden, indem Sie `m4pzOndtA-CnO0u:bobby_alias` eingeben.

Wenn Sie diese Informationen nicht kennen, können Sie den [`Export user profile by identifier`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) aufrufen und den Nutzer-Alias in der API-Antwort finden.

### Aliase für bekannte Nutzerprofile festlegen {#setting-aliases-on-known-user-profiles}

Ein Nutzer-Alias kann auch für ein bekanntes Kundenprofil festgelegt werden, um eine bekannte Nutzer:in über eine andere extern bekannte ID zu referenzieren. Beispielsweise kann eine Nutzer:in eine Business-Intelligence-Tool-ID (wie eine Amplitude-ID) haben, die Sie innerhalb von Braze referenzieren möchten.

Informationen zum Festlegen eines Nutzer-Alias finden Sie in unserer Dokumentation für jede Plattform ([iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)).

![Ein Flussdiagramm des Kundenprofil-Lebenszyklus in Braze. Wenn changeUser() für eine anonyme Nutzer:in aufgerufen wird, wird diese zu einer identifizierten Nutzer:in und die Daten werden in ihr identifiziertes Kundenprofil migriert. Die identifizierte Nutzer:in hat eine Braze-ID und eine externe ID. Wenn zu diesem Zeitpunkt für eine zweite anonyme Nutzer:in changeUser() aufgerufen wird, werden Nutzerdatenfelder, die noch nicht in der identifizierten Nutzer:in vorhanden sind, zusammengeführt. Wenn der identifizierten Nutzer:in ein Alias zu ihrem bestehenden Kundenprofil hinzugefügt wird, sind keine Daten betroffen, aber sie wird zu einer identifizierten Nutzer:in mit Alias. Wenn dann für eine dritte anonyme Nutzer:in mit demselben Alias-Label wie die identifizierte Nutzer:in, aber einem anderen Alias-Namen changeUser() aufgerufen wird, werden alle Felder, die in der identifizierten Nutzer:in nicht vorhanden sind, zusammengeführt und das Alias-Label im identifizierten Kundenprofil bleibt erhalten.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
Fällt es Ihnen schwer, sich vorzustellen, wie dies für den Kundenprofil-Lebenszyklus Ihrer Kund:innen aussehen könnte? Besuchen Sie [Best Practices]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices), um Best Practices für die Nutzerdatenerfassung einzusehen.
{% endalert %}

## Erweiterter Anwendungsfall {#advanced-use-case}

Sie können einen neuen Nutzer-Alias für bestehende identifizierte Nutzerprofile über unser SDK und unsere API mithilfe der [Nutzerdaten-Endpunkte]({{site.baseurl}}/api/endpoints/user_data) festlegen. Nutzer-Aliase können jedoch nicht über die API für ein bestehendes unbekanntes Kundenprofil festgelegt werden.

Die Nutzer-Aliase werden dabei ebenfalls zusammengeführt. Wenn jedoch sowohl das zu verwaisende als auch das Ziel-Kundenprofil einen Alias mit demselben Label haben, wird nur der Alias des Ziel-Nutzerprofils beibehalten.

Durch Deinstallieren und erneutes Installieren einer App wird eine neue anonyme `braze_id` für diese:n Nutzer:in erzeugt.

### Fehlerbehebung mit Nutzer-IDs {#troubleshooting-with-user-ids}

Alle Nutzer-IDs können verwendet werden, um Nutzer:innen in Ihrem Dashboard zu finden und zu identifizieren, z. B. zu Testzwecken. Um Ihre:n Nutzer:in im Braze-Dashboard zu finden, lesen Sie den Abschnitt [Testnutzer:innen hinzufügen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users).

{% alert important %}
Braze blockiert Nutzerprofile, die ungewöhnlich groß werden (sogenannte „Dummy-Nutzer:innen“), da diese Profile in der Regel das Ergebnis einer fehlerhaften Integration sind. Ein Profil wird blockiert, wenn es einen der folgenden Schwellenwerte überschreitet:

- Mehr als 5.000.000 Sitzungen
- Mehr als 20.000 verschiedene angepasste Event-Namen
- Mehr als 20.000 verschiedene Produktnamen in Käufen

Nachdem ein Profil blockiert wurde, nimmt Braze keine eingehenden Daten mehr für dieses Profil auf – weder von den SDKs noch von der REST API. Wenn Sie feststellen, dass dies bei einem/einer legitimen Nutzer:in passiert ist, wenden Sie sich an Ihren Braze Account Manager:in. Weitere Informationen finden Sie unter [Spam-Blockierung]({{site.baseurl}}/user_archival).
{% endalert %}
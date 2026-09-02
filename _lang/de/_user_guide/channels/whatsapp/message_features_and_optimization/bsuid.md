---
nav_title: Nutzernamen und BSUID
article_title: WhatsApp-Nutzernamen und geschäftsbezogene Nutzer-IDs
page_order: 7
description: "Erfahren Sie, wie WhatsApp-Nutzernamen und geschäftsbezogene Nutzer-IDs (BSUIDs) die Nutzeridentifikation, das Messaging und die Datenverarbeitung in Braze beeinflussen."
page_type: reference
alias: "/whatsapp_usernames/"
channel:
  - WhatsApp
hidden: true
noindex: true
---

# WhatsApp-Nutzernamen und geschäftsbezogene Nutzer-IDs {#whatsapp-usernames-and-business-scoped-user-ids}

> Im Juni 2026 plant WhatsApp die Einführung von Nutzernamen: ein optionales Datenschutz-Feature, das die Telefonnummern von Nutzer:innen verbirgt, wenn sie mit Unternehmen kommunizieren. Braze ist vollständig auf diese Änderung vorbereitet; für die meisten Kund:innen müssen weder Campaigns noch Canvases angepasst werden.

{% alert important %}
WhatsApp-Nutzernamen und geschäftsbezogene Nutzer-IDs (BSUIDs) sollen voraussichtlich im Juni 2026 eingeführt werden, wobei die Braze-Updates zeitlich auf dieses Release abgestimmt sind. Die in diesem Artikel beschriebenen Braze-Updates sind **noch nicht** verfügbar.
{% endalert %}

Wenn WhatsApp-Nutzer:innen einen Nutzernamen einrichten, wird ihre Telefonnummer nicht mehr automatisch mit den Unternehmen geteilt, denen sie Nachrichten senden. Stattdessen stellt WhatsApp den Unternehmen eine geschäftsbezogene Nutzer-ID (BSUID) bereit – einen eindeutigen Bezeichner, der spezifisch für jedes Unternehmensportfolio und jede:n Nutzer:in ist.

Braze verarbeitet BSUIDs automatisch. Nutzer:innen, die einen Nutzernamen einrichten, erscheinen weiterhin in Ihrem Braze-Workspace, empfangen Nachrichten, triggern Canvases und erzeugen Events. Einige Kund:innen müssen sich möglicherweise [auf die Änderung vorbereiten](#how-to-prepare-for-the-change).

## Geschäftsbezogene Nutzer-ID (BSUID) {#business-scoped-user-id-bsuid}

Eine BSUID ist ein eindeutiger, persistenter Bezeichner, den WhatsApp einem/einer Nutzer:in innerhalb Ihres spezifischen Geschäftsportfolios zuweist. Betrachten Sie sie als eine alternative Telefonnummer für Nutzer:innen, die ihre Telefonnummer privat halten möchten.

BSUIDs haben drei wesentliche Merkmale:

| Merkmal | Beschreibung |
| ----- | ----- |
| Eindeutig | Keine zwei Nutzer:innen teilen sich innerhalb Ihres Geschäftsportfolios dieselbe BSUID. |
| Geschäftsbezogen | Dieselbe Person hat bei jedem Unternehmen, dem sie eine Nachricht sendet, eine andere BSUID. BSUIDs können nicht über verschiedene Geschäftsportfolios hinweg geteilt oder verglichen werden. |
| In Webhooks verfügbar | BSUIDs sind in allen Webhook-Payloads enthalten, die aktuell die Telefonnummer der/des Nutzer:in übermitteln. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Geschäftsbezogene Nutzer-ID (BSUID)" }

## Änderungen bei den WhatsApp-Nutzertypen {#changes-to-whatsapp-user-types}

Nach der Einführung von WhatsApp-Nutzernamen wird es zwei Typen von WhatsApp-Nutzer:innen geben:

| Nutzertyp | WhatsApp-Identifikation | Was Braze erhält |
| ----- | ----- | ----- |
| Nutzer:innen ohne Nutzernamen | Telefonnummer (keine Änderung) | Telefonnummer (keine Änderung) |
| Nutzer:innen mit Nutzernamen | Nutzername (angezeigt), BSUID (Backend) | BSUID, Telefonnummer für Nutzer:innen, die bereits eine Konversation mit Ihrem Unternehmen haben |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Änderungen bei den WhatsApp-Nutzertypen" }

Der wesentliche Unterschied besteht darin, dass Nutzer:innen, die einen Nutzernamen verwenden, ihre Telefonnummer nur dann mit Ihrem Unternehmen teilen, wenn Sie zuvor eine Konversation mit ihnen geführt haben oder wenn sie in Ihrem WhatsApp-Kontaktbuch erscheinen.

## So verarbeitet Braze BSUIDs {#how-braze-will-handle-bsuids}

Braze speichert BSUIDs als [Nutzer-Alias]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases) mit dem Label `whats_app_bsuid` im Nutzerprofil. Das bedeutet, dass Nutzer:innen, die nur eine BSUID haben, vollständige Braze-Nutzerprofile besitzen und Canvases betreten, Nachrichten empfangen, Ereignisse generieren und über die API aktualisiert werden können.

### Nachrichten senden {#send-messages}

Wenn Braze eine WhatsApp-Nachricht sendet, wird die Telefonnummer verwendet, sofern eine verfügbar ist. Wenn Nutzer:innen nur eine BSUID haben (z. B. Nutzer:innen, die Ihnen zum ersten Mal nach der Einführung eines Nutzernamens schreiben), sendet Braze stattdessen über die BSUID. Änderungen an Ihren Nachrichtenvorlagen, Campaigns oder Canvas-Schritten sind nicht erforderlich.

### Eingehende Nachrichten und Canvas-Trigger {#inbound-messages-and-canvas-triggers}

Wenn Nutzer:innen mit einem Nutzernamen Ihnen eine eingehende WhatsApp-Nachricht senden, wird Braze:

1. Die Nutzer:innen anhand der BSUID oder Telefonnummer nachschlagen (je nachdem, was im Webhook verfügbar ist).
2. Wenn keine übereinstimmenden Nutzer:innen gefunden werden, ein neues anonymes Nutzerprofil erstellen, in dem die BSUID als Nutzer-Alias gespeichert ist.
3. Alle Canvases oder Campaigns triggern, die so konfiguriert sind, dass sie bei einer eingehenden WhatsApp-Nachricht starten.

### Nutzerprofil {#user-profile}

Sie können die BSUID von Nutzer:innen in deren Braze-Nutzerprofil im WhatsApp-Bereich einsehen.

![Nutzerprofil mit einem WhatsApp-Bereich, der die geschäftsbezogene Nutzer-ID enthält.]({% image_buster /assets/img/whatsapp/bsuid_profile.png %}){: style="max-width:60%;"}

### Abo-Gruppen {#subscription-groups}

Die Verwaltung von Abo-Gruppen funktioniert für BSUID-Nutzer:innen genauso wie für alle Nutzer:innen, die über einen Nutzer-Alias identifiziert werden. Sie können den Abo-Status für BSUID-Nutzer:innen auf folgende Weise aktualisieren:

- Über den [users/track-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) mit `user_alias`
- Über den [User Update]({{site.baseurl}}/user_update)-Canvas-Schritt (funktioniert automatisch)
- Per CSV-Upload

{% alert note %}
Der [subscription/status/set-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) unterstützt [`user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object) nicht. Verwenden Sie den [users/track-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track), um den Abo-Status für Nutzer:innen zu aktualisieren, die nur eine BSUID haben.
{% endalert %}

### Currents und Ereignisdaten {#currents-and-event-data}

Alle WhatsApp-Currents-Ereignisse (Senden, Zustellung, Gelesen, Fehler, Eingang empfangen, Abbruch, Wiederholung) enthalten ein BSUID-Feld. Bei Nutzer:innen, die sowohl eine Telefonnummer als auch eine BSUID haben, werden beide Felder einbezogen. Bei Nutzer:innen, die nur eine BSUID haben, wird nur das BSUID-Feld einbezogen (das Telefonnummernfeld ist leer).

## So bereiten Sie sich auf die Änderung vor {#how-to-prepare-for-the-change}

Für die meisten Kund:innen ist keine Aktion erforderlich. Braze übernimmt automatisch das BSUID-Routing, die Nutzererstellung und das Event-Tracking. Wir empfehlen jedoch, das [WhatsApp-Kontaktbuch zu aktivieren](#enable-whatsapp-contact-book) und [Business-Portfolios zu verknüpfen](#link-business-portfolios-if-you-use-multiple-wabas), wenn Sie mehrere WhatsApp Business Accounts (WABAs) verwenden.

### WhatsApp-Kontaktbuch aktivieren {#enable-whatsapp-contact-book}

Das Kontaktbuch ist ein Meta-Feature, das Telefonnummern von Nutzer:innen erfasst, mit denen Sie bereits kommuniziert haben. Wenn Nutzer:innen einen Nutzernamen einrichten, bleibt ihre Telefonnummer für Ihr Unternehmen sichtbar, sofern sie in Ihrem Kontaktbuch erscheinen. Das bedeutet, dass Braze Nutzer:innen weiterhin anhand der Telefonnummer identifizieren kann, auch nachdem sie einen Nutzernamen aktiviert haben.

So aktivieren Sie das Kontaktbuch:

1. Navigieren Sie zu **Meta Business Suite** > **Business settings** > **Business info**.
2. Bestätigen Sie, dass das Kontaktbuch-Feature aktiviert ist.

{% alert tip %}
Das Kontaktbuch-Feature ist standardmäßig aktiviert. Wir empfehlen jedoch, dies in Ihren Meta-Business-Einstellungen zu überprüfen. Wenn das Kontaktbuch deaktiviert ist, erscheinen Nutzer:innen, die einen Nutzernamen einrichten, als neue reine BSUID-Nutzer:innen – selbst wenn Sie ihnen zuvor bereits Nachrichten gesendet haben.
{% endalert %}

### Business-Portfolios verknüpfen, wenn Sie mehrere WABAs verwenden {#link-business-portfolios-if-you-use-multiple-wabas}

BSUIDs sind auf ein einzelnes Business-Portfolio beschränkt. Wenn Ihre Organisation WABAs aus mehreren Business-Portfolios innerhalb desselben Braze-Workspace verwaltet, hat dieselbe Person für jedes Portfolio eine andere BSUID. Dies kann zu doppelten Braze-Nutzerprofilen führen.

Um dies zu verhindern, wenden Sie sich an Ihren Meta-Ansprechpartner, um zu prüfen, ob Ihr Unternehmen berechtigt ist, Portfolios zu verknüpfen. Weitere Informationen finden Sie unter [Business-Portfolios und übergeordnete BSUIDs verknüpfen](#link-business-portfolios-and-parent-bsuids).

Wenn sich alle Ihre WABAs innerhalb desselben Business-Portfolios befinden, ist keine Aktion erforderlich.

## Geschäftsportfolios und übergeordnete BSUIDs verknüpfen {#link-business-portfolios-and-parent-bsuids}

Wenn Ihre Organisation mehrere WhatsApp Business Accounts (WABAs) über verschiedene Geschäftsportfolios hinweg betreibt, können Sie Ihren Meta-Ansprechpartner bitten zu prüfen, ob Ihr Unternehmen berechtigt ist, diese Portfolios miteinander zu verknüpfen. Die Berechtigung wird von Meta festgelegt und steht verwalteten Unternehmen zur Verfügung.

### Verhalten bei verknüpften Portfolios {#linked-portfolio-behavior}

Wenn Ihre Geschäftsportfolios verknüpft sind, fügt WhatsApp in allen Nachrichten-Webhooks neben der regulären BSUID eine übergeordnete BSUID (Parent BSUID) hinzu. Die übergeordnete BSUID wird einer neuen `parent_user_id`-Eigenschaft im Webhook-Payload zugewiesen.

Übergeordnete BSUIDs haben dieselben Eigenschaften wie reguläre BSUIDs, werden jedoch über alle geschäftlichen Telefonnummern innerhalb Ihrer verknüpften Portfolios hinweg geteilt. Das bedeutet, dass dieselbe Nutzerin oder derselbe Nutzer unabhängig davon, welcher WABA sie oder er eine Nachricht sendet, einen einzigen konsistenten Bezeichner hat – so wird das Risiko doppelter Nutzerprofile vermieden.

Eine übergeordnete BSUID enthält `ENT` zwischen dem Ländercode und dem alphanumerischen Bezeichner. Zum Beispiel:

```
US.ENT.11815799212886844830
```

Eine reguläre BSUID enthält kein `ENT`.

### Wie Braze übergeordnete BSUIDs verwendet {#how-braze-uses-parent-bsuids}

Wenn ein Webhook sowohl eine reguläre BSUID als auch eine übergeordnete BSUID enthält, verwendet Braze die übergeordnete BSUID als primären Bezeichner. Dadurch kann eine Nutzerin oder ein Nutzer, die bzw. der über mehrere WABAs in Ihren verknüpften Portfolios Nachrichten sendet, konsistent demselben Braze-Nutzerprofil zugeordnet werden.

Wenn keine übergeordnete BSUID vorhanden ist (z. B. weil Ihre Portfolios nicht verknüpft sind oder die Nutzerin bzw. der Nutzer einer nicht verknüpften WABA schreibt), verwendet Braze die reguläre BSUID. Reguläre BSUIDs funktionieren in allen Fällen weiterhin normal.

{% alert note %}
Meta verwaltet den Prozess der Verknüpfung von Geschäftsportfolios. Wenden Sie sich an Ihren Meta-Ansprechpartner, um loszulegen. Sie können Nutzer:innen weiterhin über ihre reguläre BSUID kontaktieren, auch wenn Ihre Portfolios verknüpft sind; übergeordnete BSUIDs sind ergänzend und kein Ersatz.
{% endalert %}

| Szenario | Von Braze verwendeter Bezeichner |
| ----- | ----- |
| Einzelnes Geschäftsportfolio | Reguläre BSUID |
| Mehrere verknüpfte Portfolios | Übergeordnete BSUID (bevorzugt). Falls keine übergeordnete BSUID vorhanden ist, wird die reguläre BSUID verwendet |
| Mehrere nicht verknüpfte Portfolios | Reguläre BSUID (kann zu doppelten Nutzerprofilen pro Portfolio führen) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wie Braze übergeordnete BSUIDs verwendet" }

## Häufig gestellte Fragen {#frequently-asked-questions}

### Werden meine bestehenden Campaigns und Canvases nicht mehr funktionieren, wenn WhatsApp-Nutzernamen eingeführt werden? {#will-my-existing-campaigns-and-canvases-break-when-whatsapp-usernames-launch}

Nein. Bestehende Campaigns und Canvases funktionieren weiterhin. Nutzer:innen, die keinen Nutzernamen einrichten, sind in keiner Weise betroffen. Für Nutzer:innen, die einen Nutzernamen einrichten und bereits einen Gesprächsverlauf mit Ihrem Unternehmen haben, verwendet Braze weiterhin deren Telefonnummer als primären Bezeichner.

### Was passiert mit Nutzer:innen, die einen Nutzernamen einrichten, aber bereits mit meinem Unternehmen kommuniziert haben? {#what-happens-to-a-user-who-adopts-a-username-but-has-already-messaged-my-business}

Wenn Ihr WhatsApp-Kontaktbuch aktiviert ist und Sie innerhalb der letzten 30 Tage eine vorherige Konversation mit den Nutzer:innen hatten (oder ihnen eine Nachricht gesendet haben), erscheint deren Telefonnummer weiterhin in den Webhook-Payloads neben der BSUID. Braze ordnet sie ihrem bestehenden Nutzerprofil zu. Es wird kein doppeltes Profil erstellt.

### Was passiert, wenn Nutzer:innen einen Nutzernamen einrichten und keine vorherige Konversation mit meinem Unternehmen hatten? {#what-if-a-user-adopts-a-username-and-has-no-prior-conversation-with-my-business}

Braze empfängt die BSUID der Nutzer:innen im eingehenden Webhook und ordnet sie entweder einem bestehenden Nutzerprofil zu (wenn Sie deren BSUID zuvor gespeichert haben) oder erstellt ein neues anonymes Nutzerprofil, in dem die BSUID als Nutzer-Alias gespeichert wird. Diese Nutzer:innen können dann in Canvases eintreten, ausgehende Nachrichten erhalten und mithilfe der Standard-Identitätsauflösungs-Tools von Braze identifiziert oder mit anderen Profilen zusammengeführt werden.

### Kann ich BSUID-Nutzer:innen in Segmenten ansprechen? {#can-i-target-bsuid-users-in-segments}

BSUID-Nutzer:innen sind vollwertige Braze-Nutzerprofile, sodass Sie sie über Standard-Zielgruppenfilter ansprechen können (z. B. „hat eine WhatsApp-Nachricht erhalten“ oder Abo-Gruppen-Zugehörigkeit). Das gezielte Segmentieren nach BSUID-Werten (z. B. „BSUID existiert“ oder „BSUID gleich X“) wird jedoch nicht unterstützt.

### Wie funktioniert die WhatsApp-Preisgestaltung für BSUID-Nutzer:innen? {#how-does-whatsapp-pricing-work-for-bsuid-users}

Die Preisgestaltung für WhatsApp-Konversationen richtet sich nach dem Land der Nutzer:innen. Bei Nutzer:innen, die über eine Telefonnummer identifiziert werden, leitet Meta das Land aus der Landesvorwahl der Telefonnummer ab. Bei BSUID-identifizierten Nutzer:innen ist das Land direkt in der BSUID selbst kodiert – beispielsweise repräsentiert eine BSUID, die mit `US` beginnt, eine:n Nutzer:in in den Vereinigten Staaten.

Das bedeutet, dass das Preisverhalten konsistent ist, unabhängig davon, ob Nutzer:innen über eine Telefonnummer oder eine BSUID identifiziert werden. Das zur Berechnung der Konversationstarife verwendete Land wird durch den von Meta bereitgestellten Bezeichner bestimmt, und Braze leitet diesen ohne Änderung weiter. Sie müssen nichts anders machen, sollten sich aber bewusst sein, dass bei der Kommunikation mit BSUID-only-Nutzer:innen die länderbasierte Preisgestaltung von Meta auf dem in der BSUID der Nutzer:innen kodierten Land basiert und nicht auf einer Telefonnummer.

### Wie referenziere ich BSUID-Nutzer:innen in API-Aufrufen? {#how-do-i-reference-a-bsuid-user-in-api-calls}

Verwenden Sie den Parameter `user_alias` mit `alias_label: "whats_app_bsuid"` und `alias_name` auf den BSUID-Wert der Nutzer:innen gesetzt. Zum Beispiel:

```json
{
  "user_alias": {
    "alias_label": "whats_app_bsuid",
    "alias_name": "DDC91135R"
  }
}
```

Dies funktioniert mit `users/track`, `users/identify`, CSV-Upload und dem Canvas-Schritt „User Update“.

### Werden meine Currents-Datenpipelines nicht mehr funktionieren? {#will-my-currents-data-pipelines-break}

Currents-Events für WhatsApp enthalten ein `bsuid`-Feld neben dem bestehenden Telefonnummernfeld. Bei Nutzer:innen, die nur eine BSUID haben, ist das Telefonnummernfeld leer. Wenn Ihre nachgelagerten Pipelines strenge Anforderungen an das Telefonnummernfeld haben, stellen Sie sicher, dass sie einen Null- oder Leerwert verarbeiten können.

### Ich habe mehrere WABAs über verschiedene Business-Portfolios hinweg. Werden dieselben Nutzer:innen als zwei verschiedene Profile in Braze erscheinen? {#i-have-multiple-wabas-across-different-business-portfolios-will-the-same-user-appear-as-two-different-profiles-in-braze}

Ohne verknüpfte Portfolios: ja. Dieselben WhatsApp-Nutzer:innen haben pro Business-Portfolio eine unterschiedliche BSUID, und Braze erstellt für jede ein separates Profil.

Um dies zu beheben, wenden Sie sich an Ihren Meta-Ansprechpartner, um die Berechtigung für die Portfolio-Verknüpfung zu prüfen. Bei einer Verknüpfung stellt Meta eine übergeordnete BSUID bereit, die über alle Portfolios hinweg geteilt wird, und Braze verwendet diese, um die Nutzer:innen konsistent über Ihre WABAs hinweg zu identifizieren. Weitere Details finden Sie unter [Business-Portfolios und übergeordnete BSUIDs verknüpfen](#link-business-portfolios-and-parent-bsuids).

### Kann ich das Kontaktbuch deaktivieren? {#can-i-disable-the-contact-book}

Wir empfehlen dringend, das Kontaktbuch aktiviert zu lassen. Wenn das Kontaktbuch deaktiviert wird, gehen alle historischen Telefonnummern-Datensätze Ihrer Nutzer:innen verloren. Nutzer:innen, die Nutzernamen eingerichtet haben, würden dann als neue BSUID-only-Nutzer:innen erscheinen, selbst wenn Sie ihnen zuvor Nachrichten gesendet haben.

## Zusätzliche Ressourcen {#additional-resources}

* [WhatsApp-Einrichtung]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)
* [Nutzer-Aliase]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)
* [WhatsApp-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
* [WhatsApp-Currents-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#whatsapp-abort-events)
* [Meta: Business-scoped user IDs](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids)
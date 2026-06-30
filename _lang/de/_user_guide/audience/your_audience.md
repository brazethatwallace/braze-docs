---
nav_title: Ihre Zielgruppe
article_title: Ihre Braze-Zielgruppe
page_order: 0
page_type: reference
description: "Erfahren Sie, wie Braze Ihre Nutzer:innen definiert und verwaltet, Nutzer:innen identifiziert und Nutzerdaten für Segmentierung, Personalisierung und kanalübergreifendes Messaging nutzt."

---

# Ihre Braze-Zielgruppe {#your-braze-audience}

> Erfahren Sie, wie Braze Ihre Nutzer:innen definiert und verwaltet, Nutzer:innen identifiziert und Nutzerdaten für Segmentierung, Personalisierung und kanalübergreifendes Messaging nutzt.

In Braze repräsentiert ein:e Nutzer:in (und das zugehörige Nutzerprofil) eine einzelne Person, der Sie Nachrichten senden und die Sie analysieren können.

## Nutzerprofile {#user-profiles}

Ein [Nutzerprofil]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) dient als zentrale Informationsquelle für alles, was Braze über diese Person weiß, einschließlich:

- Bezeichner (wie Nutzer-IDs oder externe IDs)
- Geräte und Messaging-Kanäle
- Verhaltensdaten und Events
- Attribute und Präferenzen
- Verlauf des Nachrichten-Engagements

Ein einzelnes Nutzerprofil kann mit mehreren Geräten und Kanälen verknüpft sein, sodass Sie eine Person plattformübergreifend verstehen und ansprechen können.

## Anonyme Nutzer:innen und identifizierte Nutzer:innen {#anonymous-users-and-identified-users}

Nutzer:innen in Braze befinden sich in der Regel in einem von zwei Zuständen.

### Anonyme Nutzer:innen {#anonymous-users}

Ein:e [anonyme:r Nutzer:in]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) ist jemand, der mit Ihrer App oder Website interagiert hat, dem aber noch kein Bezeichner aus Ihrem System zugewiesen wurde (z. B. eine `external_id`).

- Anonyme Nutzer:innen werden automatisch erstellt, wenn das Braze SDK initialisiert wird
- Sie können weiterhin Events, Attribute und Nachrichten-Engagement tracken
- Diese Nutzer:innen können je nach Kanal und Opt-in-Status Nachrichten erhalten

### Identifizierte Nutzer:innen {#identified-users}

Ein:e [identifizierte:r Nutzer:in]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#identified-user-profiles) ist jemand, der mit einer von Ihnen bereitgestellten `external_id` verknüpft wurde (z. B. eine Kunden-ID oder Konto-ID).

Die Identifizierung von Nutzer:innen ermöglicht Ihnen:

- Aktivitäten über Geräte und Sitzungen hinweg zusammenzuführen
- Nachrichten konsistent über alle Kanäle zu senden
- Mithilfe langfristiger Nutzerdaten zu segmentieren und zu personalisieren
- Profile über APIs und Integrationen zu verwalten

Wenn ein:e anonyme:r Nutzer:in später identifiziert wird, führt Braze berechtigte Daten gemäß [diesem Zusammenführungsverhalten]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) in das identifizierte Profil zusammen. Beispielsweise werden Push-Token und der Nachrichtenverlauf übernommen, und viele Felder aus dem anonymen Profil werden nur dann zusammengeführt, wenn sie im identifizierten Profil noch nicht gesetzt sind. Bei Konflikten wird das identifizierte Profil beibehalten.

## Nutzer:innen über Kanäle erreichen {#message-users-through-channels}

Ein [Kanal]({{site.baseurl}}/user_guide/channels) ist eine bestimmte Art, wie Braze eine Nachricht an Nutzer:innen zustellen kann. Gängige Kanäle sind:

- [Push (Internet oder Mobilgerät)]({{site.baseurl}}/user_guide/channels/push)
- [E-Mail]({{site.baseurl}}/user_guide/channels/email)
- [SMS, MMS und RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
- [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp)
- [In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
- [Banner]({{site.baseurl}}/user_guide/channels/banners)
- [LINE]({{site.baseurl}}/user_guide/channels/line)
- [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks)

Ein einzelnes Nutzerprofil kann mehrere Kanäle umfassen, z. B. sowohl eine E-Mail-Adresse als auch ein Mobilgerät. Braze nutzt dieses Modell, um Messaging kanalübergreifend zu koordinieren und gleichzeitig eine einheitliche Sicht auf die Nutzer:innen beizubehalten.

Jeder Kanal hat eigene Zustellungsregeln, Opt-in-Anforderungen und Metadaten, ist aber immer mit demselben Nutzerprofil verknüpft.

## Wie Nutzer:innen in Braze angelegt werden {#ways-users-enter-braze}

Nutzer:innen werden in Braze angelegt, sobald jemand über eine unterstützte Integration oder einen Kanal mit Ihrer Marke interagiert. Wie sie hinzugefügt werden, hängt von Ihrer Braze-Implementierung ab.

{% tabs %}
{% tab Mobile Apps %}
- Wenn Nutzer:innen Ihre App zum ersten Mal öffnen, erstellt das Braze SDK ein Nutzerprofil.
- Geräte und Push-Token werden automatisch registriert.
- Events und Attribute können sofort protokolliert werden.
{% endtab %}

{% tab Internet %}
- Nutzer:innen werden erstellt, wenn das Web SDK initialisiert wird.
- Web-Push-Abos registrieren einen Browser als Messaging-Kanal.
{% endtab %}

{% tab E-Mail und SMS %}
- Nutzer:innen können erstellt werden, wenn Sie Daten hochladen, APIs aufrufen oder Opt-ins erfassen.
- E-Mail-Adressen und Telefonnummern werden als Kanalbezeichner gespeichert.
- Der Opt-in-Status wird pro Kanal und pro Region erfasst.
{% endtab %}

{% tab APIs und Integrationen %}
- Sie können Nutzer:innen direkt über [REST APIs]({{site.baseurl}}/api/endpoints/user_data) oder durch [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) erstellen oder aktualisieren.
- Externe Tools (wie CDPs, CRMs oder Data Warehouses) können Nutzer:innen automatisch mit Braze synchronisieren.
{% endtab %}
{% endtabs %}

## Datenquellen für Zielgruppen {#audience-data-sources}

Nutzerdaten in Braze stammen in der Regel aus einer Kombination verschiedener Quellen.

{% tabs %}
{% tab Automatische Erfassung %}
Braze SDKs erfassen automatisch kontextbezogene Daten wie:

- Gerätetyp und Betriebssystem
- Sprache und Zeitzone
- App-Version und Sitzungsaktivität
{% endtab %}

{% tab Nutzerverhalten %}
Wenn Nutzer:innen mit Ihrer App oder Ihren Nachrichten interagieren, erfasst Braze:

- [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) (z. B. Käufe oder Feature-Nutzung)
- Nachrichtenöffnungen, Klicks und Conversions
- Sitzungsaktivität und Engagement-Trends
{% endtab %}

{% tab Ihre Systeme %}
Sie können Daten aus Ihren eigenen Tools an Braze senden über:

- [REST APIs]({{site.baseurl}}/api/endpoints/user_data)
- [CSV-Uploads]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)
- Geplante Datensynchronisierungen

Dies umfasst häufig Bezeichner, Kontodaten oder historischen Kontext.
{% endtab %}
{% endtabs %}

### Von Nutzer:innen bereitgestellte Eingaben {#user-provided-input}

Nutzer:innen können Daten direkt bereitstellen über:

- [Präferenzzentren]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)
- Formulare oder Umfragen (SDKs oder Integrationen)
- In-App-Erlebnisse

### Integrationen {#integrations}

Braze lässt sich über Integrationen mit Plattformen wie [Segment]({{site.baseurl}}/partners/segment), Data Warehouses und Analytics-Technologiepartnern verbinden, sodass Nutzerdaten automatisch in Nutzerprofile einfließen.

## Nutzerdaten verwalten {#manage-user-data}

Sie können Nutzerdaten auf verschiedene Arten hinzufügen, aktualisieren oder entfernen:

- **Dashboard-Tools** für manuelle Bearbeitungen oder CSV-Uploads
- **APIs** für Realtime- oder programmatische Updates
- **SDKs** zur direkten Erfassung von Verhalten in Ihrer App oder auf Ihrer Website
- **Integrationen** für laufende Synchronisierung

Daten können entfernt werden durch:

- Löschen von Attributwerten
- Entfernen von Tags
- Aktualisieren von Abo-Status
- Zurücksetzen von Nutzer:innen beim Logout (für anonyme Anwendungsfälle)

## Features für Zielgruppendaten {#audience-data-features}

Sobald Nutzerdaten in Braze vorhanden sind, unterstützen sie nahezu jede Engagement-Funktion. Je vollständiger und genauer Ihre Nutzerdaten sind, desto effektiver können Sie die folgenden Features nutzen.

| Feature | Beschreibung |
| ---- | ---- |
| [Segmentierung]({{site.baseurl}}/user_guide/audience/segments) | Erstellen Sie Zielgruppen basierend auf: {::nomarkdown}<ul><li>Attributen und angepassten Feldern</li> <li>Events und Verhaltensweisen</li> <li>Nachrichten-Engagement</li> <li>Geräte- und Kanaleigenschaften</li></ul>{:/} <br>Segmente können über Campaigns und Canvases hinweg wiederverwendet werden. |
| [Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) | Nutzen Sie Nutzerdaten, um Inhalte anzupassen, z. B.: {::nomarkdown}<ul><li>Namen und Präferenzen im Nachrichtentext</li> <li>Dynamische Empfehlungen</li> <li>Standort- oder sprachspezifische Inhalte</li></ul>{:/} |
| Automatisierung und Orchestrierung | Triggern Sie Nachrichten und Journeys basierend auf: {::nomarkdown}<ul><li>Nutzeraktionen</li> <li>Attributänderungen</li> <li>Zeitbasierten Bedingungen</li></ul>{:/} |
| Kanalübergreifende Koordination | Erreichen Sie Nutzer:innen auf dem am besten geeigneten Kanal unter Berücksichtigung von: {::nomarkdown}<ul><li>Opt-in-Status</li> <li>Häufigkeitsbegrenzungen</li> <li>Kanalpräferenzen</li></ul>{:/} |
| [Analytics und Insights]({{site.baseurl}}/user_guide/analytics) | Verstehen Sie das Verhalten verschiedener Zielgruppen durch Analyse von: {::nomarkdown}<ul><li>Engagement-Raten</li> <li>Conversion-Pfaden</li> <li>Segment-Performance im Zeitverlauf</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Features für Zielgruppendaten" }
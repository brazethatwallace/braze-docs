---
nav_title: Ihre Zielgruppe
article_title: Ihre Braze-Zielgruppe
page_order: 0
page_type: reference
description: "Erfahren Sie, wie Braze Ihre Nutzer:innen definiert und verwaltet, Nutzer:innen identifiziert und Nutzerdaten für Segmentierung, Personalisierung und kanalübergreifendes Messaging nutzt."

---

# Ihre Braze-Zielgruppe {#your-braze-audience}

> Erfahren Sie, wie Braze Ihre Nutzer:innen definiert und verwaltet, Nutzer:innen identifiziert und Nutzerdaten für Segmentierung, Personalisierung und kanalübergreifendes Messaging nutzt.

In Braze repräsentiert ein:e Nutzer:in (und das zugehörige Kundenprofil) eine einzelne Person, der Sie Nachrichten senden und die Sie analysieren können.

## Nutzerprofile {#user-profiles}

Ein [Nutzerprofil]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) dient als zentrale Informationsquelle für alles, was Braze über eine Person weiß, darunter:

- Bezeichner (wie Nutzer-IDs oder externe IDs)
- Geräte und Messaging-Kanäle
- Verhaltensdaten und Events
- Attribute und Präferenzen
- Verlauf des Nachrichten-Engagements

Ein einzelnes Nutzerprofil kann mit mehreren Geräten und Kanälen verknüpft werden, sodass Sie eine Person plattformübergreifend ganzheitlich verstehen und ansprechen können.

## Anonyme und identifizierte Nutzer:innen {#anonymous-users-and-identified-users}

Nutzer:innen in Braze fallen in der Regel in einen von zwei Zuständen.

### Anonyme Nutzer:innen {#anonymous-users}

Eine [anonyme Nutzerin oder ein anonymer Nutzer]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) ist jemand, der mit Ihrer App oder Website interagiert hat, aber noch keinen Bezeichner aus Ihrem System erhalten hat (z. B. eine `external_id`).

- Anonyme Nutzer:innen werden automatisch erstellt, wenn das Braze SDK initialisiert wird
- Sie können weiterhin Events, Attribute und Nachrichten-Engagement tracken
- Diese Nutzer:innen können je nach Kanal und Opt-in-Status Nachrichten erhalten

#### Anonyme Nutzer:innen und Einwilligung {#anonymous-users-and-consent}

Wenn Sie das Braze SDK in einen Einwilligungs-Wrapper einbetten müssen, um Ihre Einwilligungsrichtlinien einzuhalten, können Sie anonyme Daten erfassen, bevor Nutzer:innen ihre Einwilligung erteilen. Wenn das SDK initialisiert wird, wird ein anonymes Nutzerprofil erstellt, sodass Sie Verhalten tracken und gleichzeitig die Einwilligungsanforderungen einhalten können.

**Nachrichten an anonyme Nutzer:innen senden:**
Anonyme Nutzer:innen können Nachrichten auslösen und empfangen, solange das Braze SDK initialisiert bleibt. Dazu gehören:

- [In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [Push-Benachrichtigungen]({{site.baseurl}}/user_guide/channels/push) (wenn Push-Token registriert sind)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)

Wenn Sie die SDK-Initialisierung jedoch deaktivieren oder verhindern, wenn eine Nutzerin oder ein Nutzer keine Einwilligung erteilt oder die Einwilligung widerruft, funktionieren SDK-gesteuerte Kanäle für diese Person nicht.

**Nutzer:innen basierend auf dem Einwilligungsstatus ansprechen:**
Um Nutzer:innen basierend auf ihrem Einwilligungsstatus anzusprechen, legen Sie ein angepasstes Nutzerattribut (z. B. `has_marketing_consent`) in ihrem Profil fest. Sie können dann Segments basierend auf diesem Attribut erstellen und diesen Wert synchron halten, wenn Nutzer:innen ihre Einwilligungseinstellungen außerhalb von Braze ändern. Weitere Informationen zum Targeting anonymer Nutzer:innen finden Sie unter [Anwendungsfälle]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#use-cases).

### Identifizierte Nutzer:innen {#identified-users}

Eine [identifizierte Nutzerin oder ein identifizierter Nutzer]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#identified-user-profiles) ist eine Person, die mit einer von Ihnen bereitgestellten `external_id` verknüpft wurde (z. B. einer Kunden-ID oder Konto-ID).

Das Identifizieren einer Nutzerin oder eines Nutzers ermöglicht es Ihnen:

- Aktivitäten über Geräte und Sitzungen hinweg zusammenzuführen
- Nachrichten konsistent über alle Kanäle hinweg zu senden
- Mithilfe langfristiger Nutzerdaten zu segmentieren und zu personalisieren
- Profile über APIs und Integrationen zu verwalten

Wenn anonyme Nutzer:innen später identifiziert werden, führt Braze berechtigte Daten gemäß [diesem Zusammenführungsverhalten]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) in das identifizierte Profil zusammen. Beispielsweise werden Push-Token und der Nachrichtenverlauf übernommen, und viele Felder des anonymen Profils werden nur dann zusammengeführt, wenn sie im identifizierten Profil noch nicht gesetzt sind. Bei widersprüchlichen Werten wird das identifizierte Profil beibehalten.

## Nutzer:innen über Kanäle ansprechen {#message-users-through-channels}

Ein [Kanal]({{site.baseurl}}/user_guide/channels) ist eine bestimmte Art und Weise, wie Braze eine Nachricht an eine:n Nutzer:in zustellen kann. Gängige Kanäle sind:

- [Push (Internet oder Mobilgerät)]({{site.baseurl}}/user_guide/channels/push)
- [E-Mail]({{site.baseurl}}/user_guide/channels/email)
- [SMS, MMS und RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
- [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp)
- [In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
- [Banner]({{site.baseurl}}/user_guide/channels/banners)
- [LINE]({{site.baseurl}}/user_guide/channels/line)
- [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks)

Ein einzelnes Nutzerprofil kann über mehrere Kanäle verfügen, beispielsweise sowohl eine E-Mail-Adresse als auch ein Mobilgerät. Braze nutzt dieses Modell, um Messaging kanalübergreifend zu koordinieren und gleichzeitig eine einheitliche Sicht auf die:den Nutzer:in beizubehalten.

Jeder Kanal hat eigene Zustellregeln, Opt-in-Anforderungen und Metadaten, ist aber stets mit demselben Nutzerprofil verknüpft.

## Wege, wie Nutzer:innen in Braze angelegt werden {#ways-users-enter-braze}

Nutzer:innen werden in Braze angelegt, sobald jemand über eine unterstützte Integration oder einen unterstützten Kanal mit Ihrer Marke interagiert. Wie sie hinzugefügt werden, hängt davon ab, wie Sie Braze implementiert haben.

{% tabs %}
{% tab Mobile Apps %}
- Wenn ein:e Nutzer:in Ihre App zum ersten Mal öffnet, erstellt das Braze SDK ein Nutzerprofil.
- Geräte und Push-Token werden automatisch registriert.
- Events und Attribute können sofort protokolliert werden.
{% endtab %}

{% tab Web %}
- Nutzer:innen werden angelegt, wenn das Web-SDK initialisiert wird.
- Web-Push-Abonnements registrieren einen Browser als Messaging-Kanal.
{% endtab %}

{% tab E-Mail und SMS %}
- Nutzer:innen können angelegt werden, wenn Sie Daten hochladen, APIs aufrufen oder Opt-ins erfassen.
- E-Mail-Adressen und Telefonnummern werden als Kanal-Bezeichner gespeichert.
- Der Opt-in-Status wird pro Kanal und pro Region nachverfolgt.
{% endtab %}

{% tab APIs und Integrationen %}
- Sie können Nutzer:innen direkt über [REST APIs]({{site.baseurl}}/api/endpoints/user_data) oder durch [Importieren einer CSV-Datei]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) erstellen oder aktualisieren.
- Externe Tools (wie Customer Data Platforms (CDPs), CRM-Systeme oder Data Warehouses) können Nutzer:innen automatisch mit Braze synchronisieren.
{% endtab %}
{% endtabs %}

## Zielgruppen-Datenquellen {#audience-data-sources}

Nutzerdaten in Braze stammen in der Regel aus einer Kombination verschiedener Quellen.

{% tabs %}
{% tab Automatische Erfassung %}
Braze SDKs erfassen automatisch kontextbezogene Daten wie:

- Gerätetyp und Betriebssystem
- Sprache und Zeitzone
- App-Version und Sitzungsaktivität
{% endtab %}

{% tab Nutzerverhalten %}
Wenn Nutzer:innen mit Ihrer App oder Ihren Nachrichten interagieren, zeichnet Braze Folgendes auf:

- [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) (zum Beispiel Käufe oder Feature-Nutzung)
- Nachrichtenöffnungen, Klicks und Konversionen
- Sitzungsaktivität und Engagement-Trends
{% endtab %}

{% tab Ihre Systeme %}
Sie können Daten aus Ihren eigenen Tools mithilfe der folgenden Optionen an Braze senden:

- [REST APIs]({{site.baseurl}}/api/endpoints/user_data)
- [CSV-Uploads]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)
- Geplante Datensynchronisierungen

Dies umfasst häufig Bezeichner, Kontodaten oder historischen Kontext.
{% endtab %}
{% endtabs %}

### Von Nutzer:innen bereitgestellte Eingaben {#user-provided-input}

Nutzer:innen können Daten direkt bereitstellen über:

- [Präferenzcenter]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)
- Formulare oder Umfragen (SDKs oder Integrationen)
- In-App-Erlebnisse

### Integrationen {#integrations}

Braze lässt sich über Integrationen mit Plattformen wie [Segment]({{site.baseurl}}/partners/segment), Data Warehouses und Analytics-Technologiepartnern verbinden, sodass Nutzerdaten automatisch in Nutzerprofile einfließen.

## Nutzerdaten verwalten {#manage-user-data}

Sie können Nutzerdaten auf verschiedene Arten hinzufügen, aktualisieren oder entfernen:

- **Dashboard-Tools** für manuelle Bearbeitungen oder CSV-Uploads
- **APIs** für Realtime- oder programmatische Updates
- **SDKs** zum Erfassen von Verhalten direkt in Ihrer App oder auf Ihrer Website
- **Integrationen** für die fortlaufende Synchronisierung

Daten können auf folgende Weise entfernt werden:

- Attributwerte löschen
- Tags entfernen
- Abo-Status aktualisieren
- Nutzer:innen beim Abmelden zurücksetzen (für Anwendungsfälle mit anonymen Nutzer:innen)

## Zielgruppendaten-Features {#audience-data-features}

Sobald Nutzerdaten in Braze vorhanden sind, unterstützen sie nahezu jede Engagement-Funktion. Je vollständiger und genauer Ihre Nutzerdaten sind, desto effektiver können Sie die folgenden Features nutzen.

| Feature | Beschreibung |
| ---- | ---- |
| [Segmentierung]({{site.baseurl}}/user_guide/audience/segments) | Erstellen Sie Zielgruppen basierend auf: {::nomarkdown}<ul><li>Attributen und angepassten Feldern</li> <li>Events und Verhaltensweisen</li> <li>Nachrichten-Engagement</li> <li>Geräte- und Kanaleigenschaften</li></ul>{:/} <br>Segments können in Campaigns und Canvases wiederverwendet werden. |
| [Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) | Nutzen Sie Nutzerdaten, um Inhalte anzupassen, z. B.: {::nomarkdown}<ul><li>Namen und Präferenzen im Nachrichtentext</li> <li>Dynamische Empfehlungen</li> <li>Standort- oder sprachspezifische Inhalte</li></ul>{:/} |
| Automatisierung und Orchestrierung | Lösen Sie Nachrichten und Journeys aus basierend auf: {::nomarkdown}<ul><li>Nutzeraktionen</li> <li>Attributänderungen</li> <li>Zeitbasierten Bedingungen</li></ul>{:/} |
| Kanalübergreifende Koordination | Erreichen Sie Nutzer:innen auf dem am besten geeigneten Kanal unter Berücksichtigung von: {::nomarkdown}<ul><li>Opt-in-Status</li> <li>Frequency Caps</li> <li>Kanalpräferenzen</li></ul>{:/} |
| [Analytics und Insights]({{site.baseurl}}/user_guide/analytics) | Verstehen Sie, wie sich verschiedene Zielgruppen verhalten, indem Sie Folgendes analysieren: {::nomarkdown}<ul><li>Engagement-Raten</li> <li>Konversionspfade</li> <li>Segment-Performance im Zeitverlauf</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zielgruppendaten-Features" }
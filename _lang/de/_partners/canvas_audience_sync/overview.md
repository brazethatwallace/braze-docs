---
nav_title: Über Audience Sync
article_title: Über Audience Sync
alias: /partners/about_audience_sync/
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync für Facebook verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
page_order: 0
tool:
  - Canvas
---

# Über Audience Sync {#about-audience-sync}

> Mit dem Braze Audience Sync Feature können Sie die Reichweite Ihrer Campaigns auf viele der wichtigsten sozialen und Werbetechnologien ausweiten. Mit [Braze-Canvas]({{site.baseurl}}/user_guide/messaging/canvas) können Marken dynamisch und sicher First-Party-Nutzerdaten mit dem Werbe-Ökosystem synchronisieren, um Marketing und Betrieb effizienter zu gestalten.

## Verfügbarkeit der Funktion {#feature-availability}

Alle Braze-Kund:innen haben sofort Zugang zu Audience Sync mit Google und Facebook. Kund:innen mit Action Credits können jedoch auf alle Audience-Sync-Partner zugreifen. Um zusätzliche Audience-Sync-Ziele für Kund:innen ohne Action Credits freizuschalten, erwerben Sie Audience Sync Pro. Wenden Sie sich an Ihren Braze Account Manager, um weitere Informationen zu erhalten.

## Anwendungsfälle {#use-cases}

- Targeting von hochwertigen Nutzer:innen über eigene und bezahlte Kanäle, um zusätzliche Käufe oder Engagement zu fördern.
- Erstellen von Lookalike Audiences Ihrer hochwertigen Nutzer:innen, um die Akquisitionskosten und Conversions bei der Neukundengewinnung zu optimieren.
- Retargeting von Nutzer:innen mit Anzeigen, die auf andere Marketingkanäle weniger ansprechen.
- Erstellen von Suppression Audiences, um zu verhindern, dass Nutzer:innen Werbung erhalten, wenn sie bereits treue Verbraucher:innen Ihrer Marke sind.

## Übersicht {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| Ziel | Zeit bis zur Zuordnung der Zielgruppenmitglieder | Rate-Limit | Lookalike oder Actalike | Tipps |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync) | Bis zu 24 Stunden | 250.000 Anfragen pro Minute. Alle 5 Sekunden gebündelt mit automatischem Retry. | Ja | {::nomarkdown}<ul><li>Criteo unterstützt bis zu 1.000 Werbezielgruppen.</li><li>Die minimale Zielgruppengröße beträgt 500, empfohlen werden über 20.000.</li></ul>{:/} |
| [Facebook oder Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) | Bis zu 24 Stunden | 190.000 Werbekonten pro Stunde | Ja | {::nomarkdown}<ul><li>Facebook unterstützt bis zu 500 Werbezielgruppen.</li><li>Facebook erfordert Zielgruppen von mindestens 1.000 Nutzer:innen.</li></ul>{:/} |
| [Google Ads oder YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) | Zwischen 6 und 12 Stunden | Alle 5 Sekunden gebündelt mit automatischem Retry basierend auf dem Feedback von Google | Nein | {::nomarkdown}<ul><li><b>Customer Match:</b> Verwenden Sie entweder die mobile Werbe-ID oder E-Mail-Adresse bzw. Telefonnummer.</li><li>Google Audiences erfordern mindestens 5.000 Nutzer:innen, bevor Anzeigen ausgeliefert werden.</li><li>Die Zielgruppengröße wird als null angezeigt, bis mindestens 1.000 Nutzer:innen vorhanden sind.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync) | Bis zu 48 Stunden | Braze bündelt bis zu 2.000 Nutzer:innen pro Anfrage mit automatischem Retry von bis zu ca. 13 Stunden. | KI-gestützte prädiktive Zielgruppen | {::nomarkdown}<ul><li>Die minimale Zielgruppengröße beträgt 300 Mitglieder unter Berücksichtigung des Standort-Targetings.</li><li>LinkedIn zeigt die Übereinstimmungsrate im Braze-Dashboard an.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync) | Zwischen 24 und 48 Stunden | Pinterest verarbeitet 7 Abfragen pro Sekunde und 1.900 Nutzer:innen pro Anfrage. Braze bündelt Nutzer:innen alle 5 Sekunden. | Ja | Pinterest-Zielgruppen erfordern mindestens 100 Nutzer:innen. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync) | Nicht zutreffend | Snapchat verarbeitet 10 Abfragen pro Sekunde und 100.000 Nutzer:innen pro Anfrage. Braze bündelt Nutzer:innen alle 5 Sekunden. | Ja | Snapchat unterstützt bis zu 1.000 Werbezielgruppen. |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync) | Bis zu 24 Stunden | Nicht zutreffend | Ja | {::nomarkdown}<ul><li>Es gibt keine Mindestzielgruppengröße für CRM-Zielgruppen in The Trade Desk.</li><li>Es gibt kein Limit für die Anzahl der unterstützten Zielgruppen in The Trade Desk.</li><li>Wenn Sie mit einer Zielgruppe synchronisieren, deren Region auf EU gesetzt ist, wird die Telefonnummer nicht unterstützt.</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync) | Zwischen 24 und 48 Stunden | TikTok verarbeitet 50 Abfragen pro Sekunde und 10.000 Nutzer:innen pro Anfrage. Braze bündelt Nutzer:innen alle 5 Sekunden. | Ja | {::nomarkdown}<ul><li>TikTok unterstützt bis zu 400 Werbezielgruppen.</li><li>TikTok-Zielgruppen erfordern mindestens 1.000 Nutzer:innen, bevor Anzeigen ausgeliefert werden.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Übersicht" }
<sup>Wenn das Rate-Limit erreicht wird, wiederholt Braze die Synchronisierung über einen Zeitraum von 13 Stunden.</sup>

## So funktioniert es {#how-it-works}

Um Audience Sync mit Google oder Facebook zu verwenden, verbinden Sie Ihr Werbekonto, indem Sie auf der Seite **Technologie-Partner** nach dem Partner suchen.

![Facebook-Technologie-Partner.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Google Ads-Technologie-Partner.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

Nachdem Sie Ihr Werbekonto verbunden haben, können Sie einen Canvas mit einem Audience-Sync-Schritt erstellen.

![Canvas-Komponentenmenü zum Hinzufügen des Audience-Sync-Schritts zur User Journey.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

Wählen Sie als Nächstes den Partner aus, mit dem Sie Zielgruppen synchronisieren möchten.

![Option zur Auswahl Ihres Audience-Sync-Partners im Audience-Sync-Schritt.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

Für jeden Partner müssen Sie im Rahmen Ihres Audience-Sync-Schritts Folgendes konfigurieren:

- Werbekonto
- Zielgruppe
- Aktion zum Hinzufügen oder Entfernen von Nutzer:innen
- Abzugleichende Felder

Beachten Sie, dass Braze Nutzer:innen synchronisiert, sobald sie den Audience-Sync-Schritt in Ihrem Canvas erreichen.

Für jedes Audience-Sync-Ziel kann der Partner unterschiedliche Anforderungen an die Felder stellen, die Braze senden kann. Weitere Einzelheiten finden Sie in der jeweiligen Partnerdokumentation.

### Audience Sync Pro

Um einen Audience Sync Pro-Partner wie Criteo, LinkedIn, Pinterest, Snapchat oder TikTok zu verwenden, können Sie Ihre Partner basierend auf Ihren Audience Sync Pro-Kaufkontingenten im Abschnitt **Audience Sync Pro** auf der Seite **Technologie-Partner** auswählen.

![Audience Sync Pro ohne bisher ausgewählte Partner.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

Wählen Sie zunächst die Partner aus, die Sie verwenden möchten. Jeder Kauf von Audience Sync Pro stellt Ihnen 3 zugewiesene Audience Sync Pro-Ziele zur Verfügung, die in jedem Ihrer Workspaces innerhalb Ihres Dashboards verfügbar sind.

![Option zur Auswahl von bis zu drei Partnern für die Verbindung mit Braze.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Nachdem Sie Ihre Audience Sync Pro-Ziele ausgewählt haben, verbinden Sie das Werbekonto des ausgewählten Partners, indem Sie auf die Partner-Kachel klicken.

![Ein Beispiel mit Snapchat und TikTok als ausgewählte Partner für Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Snapchat Audience Sync-Einstellungen mit der Meldung „Sie haben erfolgreich 1 Snapchat-Konto verbunden“.]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Erstellen Sie abschließend Ihren Audience-Sync-Schritt in Canvas mit diesem Audience Sync Pro-Ziel.

### Batching und Latenz {#batching-and-latency}

Wenn Nutzer:innen einen Audience-Sync-Schritt in Canvas erreichen, reiht Braze sie in ein Batching-System ein, das Nutzer:innen-Updates aggregiert, bevor sie an die Partner-API gesendet werden. Ein Batch wird gesendet, wenn eine der folgenden Bedingungen eintritt:

- **Der Batch erreicht sein Größenlimit.** Dieses variiert je nach Partner:
  - Standardmäßig werden bis zu 2.000 Nutzer:innen unterstützt
  - Google Ads unterstützt bis zu 10.000 Nutzer:innen
  - Facebook und TikTok unterstützen bis zu 2.000 Nutzer:innen
- **Der Batch-Latenz-Timer läuft ab.** Der Standardwert beträgt eine Stunde, ist aber pro Partner konfigurierbar. Beispielsweise verwendet The Trade Desk 10 Minuten.

Canvases mit hohem Volumen können früher dispatchen, da Batches schneller gefüllt werden. Canvases mit niedrigem Volumen warten, bis der Latenz-Timer abläuft. Braze garantiert keine feste Dispatch-Zeit; das Timing hängt von der Batch-Größe und dem konfigurierten Latenzfenster ab.

Braze zeichnet die Dispatch-Aktivität in internen Protokollen zur Überwachung und Fehlerbehebung auf, aber diese Zeitstempel werden nicht als abfragbare Felder bereitgestellt. Nachdem Braze einen Batch an die Partner-API gesendet hat, verarbeitet der Partner das Zielgruppen-Update gemäß seinen eigenen Service-Level-Agreements – in der Regel 6–48 Stunden.

Braze erhält keine Bestätigung von Partnern, dass einzelne Nutzer:innen abgeglichen oder synchronisiert wurden. Partnerantworten sind HTTP-Empfangsbestätigungen, keine Match-Bestätigungen. Um zu überprüfen, ob eine Zielgruppe befüllt wurde, prüfen Sie die Werbeplattform des Partners (z. B. Google Ads Audience Manager oder Meta Business Manager).

### Audience Sync-Fehler-E-Mails {#audience-sync-error-emails}

Wenn der Fehler mit der gesamten Partnerintegration zusammenhängt (z. B. ein Autorisierungsproblem), wird eine E-Mail an die Person gesendet, die die Integration verbunden hat. Wenn diese Person nicht mehr existiert, erhalten die Administrator:innen die E-Mails.

Wenn der Fehler mit Problemen der Audience-Sync-Komponente zusammenhängt (z. B. „Zielgruppe existiert nicht“) in Canvas, wird eine E-Mail an die Person gesendet, die den Canvas eingerichtet hat. Wenn diese Person nicht mehr existiert, wird auf den Unternehmensadministrator zurückgefallen.

Um zu konfigurieren, wer diese E-Mails erhält, wenden Sie sich an Ihren Customer-Success-Manager, damit Empfänger:innen unter **Benachrichtigungseinstellungen** hinzugefügt werden. Diese Einstellung deckt sowohl Integrationsfehler als auch Fehler der Audience-Sync-Komponente ab. Empfänger:innen, die Sie hinzufügen, erhalten diese E-Mails zusätzlich zu der Person, die mit dem Fehler verknüpft ist.

## Überlegungen zum Datenschutz {#data-privacy-considerations}

{% alert important %}
Diese Dokumentation ist nicht dazu bestimmt und darf nicht als Rechtsberatung herangezogen werden. Die Nutzung von Audience Sync unterliegt bestimmten gesetzlichen Anforderungen. Um sicherzustellen, dass Sie die Funktion in Übereinstimmung mit allen geltenden Gesetzen verwenden, sollten Sie den Rat Ihrer Rechtsabteilung einholen.
{% endalert %}

Beim Aufbau von Zielgruppen für Ad-Tracking möchten Sie möglicherweise bestimmte Nutzer:innen basierend auf deren Präferenzen ein- oder ausschließen und Datenschutzgesetze einhalten, wie z.&nbsp;B. das Recht auf „Do Not Sell or Share“ gemäß dem [CCPA](https://oag.ca.gov/privacy/ccpa). Marketer sollten die entsprechenden Filter für die Berechtigung der Nutzer:innen in ihren Canvas-Eintrittskriterien implementieren. Die folgenden Optionen können dabei helfen.

Wenn Sie die [iOS IDFA über das Braze SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations) erfasst haben, können Sie den Filter „Ads Tracking Enabled“ verwenden. Wählen Sie den Wert `true`, um Nutzer:innen nur dann an Audience-Sync-Ziele zu senden, wenn sie ihr Opt-in gegeben haben.

![Ein Canvas mit einer Eintrittszielgruppe „Ad Tracking Enabled ist true“.]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

Wenn Sie `opt-ins`, `opt-outs`, `Do Not Sell Or Share` oder andere relevante angepasste Attribute erfassen, sollten Sie diese als Filter in Ihre Canvas-Eintrittskriterien aufnehmen:

![Ein Canvas mit einer Eintrittszielgruppe „opted_in_marketing ist gleich true“.]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Weitere Informationen zur Einhaltung dieser Datenschutzgesetze innerhalb der Braze-Plattform finden Sie unter [Technische Unterstützung zum Datenschutz]({{site.baseurl}}/dp-technical-assistance).

## Verwaltung der Einwilligung für Werbe-Targeting {#managing-consent-for-ad-targeting}

Als Werbetreibende:r sind Sie dafür verantwortlich, die Einwilligung für Ad-Tracking oder das Targeting Ihrer Nutzer:innen zu verwalten.

Um Werbung an Ihre Nutzer:innen zu senden, müssen Sie alle geltenden Gesetze und Vorschriften sowie die Richtlinien und Anforderungen der jeweiligen Werbeplattform einhalten. Verwenden Sie Braze nur, um Nutzer:innen zu targetieren und zu synchronisieren, deren Einwilligung Sie eingeholt haben.

Um Ihre Zielgruppenlisten auf diesen Werbeplattformen aktuell zu halten und Nutzer:innen zu entfernen, die ihre Einwilligung widerrufen haben, richten Sie ein Canvas ein, um Nutzer:innen mithilfe eines Audience-Sync-Schritts aus bestehenden Zielgruppenlisten zu entfernen.
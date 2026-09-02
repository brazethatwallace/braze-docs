---
nav_title: Über Audience Sync
article_title: Über Audience Sync
alias: /partners/about_audience_sync/
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync für Facebook verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Trigger or triggern or triggern, Segmentierung und mehr zuzustellen."
page_order: 0
tool:
  - Canvas
---

# Über Audience Sync {#about-audience-sync}

> Mit dem Braze Audience Sync Feature können Sie die Reichweite Ihrer Campaigns auf viele der wichtigsten sozialen und Werbetechnologien ausweiten. Mit [Braze-Canvas]({{site.baseurl}}/user_guide/messaging/canvas) können Marken dynamisch und sicher First-Party-Nutzerdaten mit dem Werbe-Ökosystem synchronisieren, um Marketing und Betrieb effizienter zu gestalten.

## Feature-Verfügbarkeit {#feature-availability}

Alle Braze-Kund:innen haben sofort Zugang zu Audience Sync für Google und Facebook, aber Kund:innen mit Action Credits können auf alle Audience Sync-Partner zugreifen. Um zusätzliche Audience Sync-Ziele für Kund:innen ohne Action Credits freizuschalten, erwerben Sie Audience Sync Pro. Wenden Sie sich an Ihren Braze Account Manager:in für weitere Details.

## Anwendungsfälle {#use-cases}

- Targeting von High-Value-Nutzer:innen über eigene und bezahlte Kanäle, um zusätzliche Käufe oder Engagement zu fördern.
- Erstellung von Lookalike-Zielgruppen Ihrer High-Value-Nutzer:innen, um die Akquisitionskosten und Konversionen bei der Neukundengewinnung zu optimieren.
- Retargeting von Nutzer:innen mit Anzeigen, die auf andere Marketingkanäle weniger ansprechen.
- Erstellung von Suppressions-Zielgruppen, um zu verhindern, dass Nutzer:innen Werbung erhalten, wenn sie bereits treue Verbraucher:innen Ihrer Marke sind.

## Übersicht {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| Ziel | Zeit, bis das Ziel Zielgruppenmitglieder abgleicht | Rate-Limit | Lookalike oder Actalike | Tipps |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync) | Bis zu 24 Stunden | 250.000 Anfragen pro Minute. Alle 5 Sekunden gebündelt mit automatischem Retry. | Ja | {::nomarkdown}<ul><li>Criteo unterstützt bis zu 1.000 Werbezielgruppen.</li><li>Die Mindestgröße einer Zielgruppe beträgt 500, empfohlen werden über 20.000.</li></ul>{:/} |
| [Facebook oder Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) | Bis zu 24 Stunden | 190.000 Werbekonten pro Stunde | Ja | {::nomarkdown}<ul><li>Facebook unterstützt bis zu 500 Werbezielgruppen.</li><li>Facebook setzt voraus, dass Zielgruppen mindestens 1.000 Nutzer:innen umfassen.</li></ul>{:/} |
| [Google Ads oder YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) | Zwischen 6 und 12 Stunden | Alle 5 Sekunden gebündelt mit automatischem Retry basierend auf Google-Feedback | Nein | {::nomarkdown}<ul><li><b>Customer Match:</b> Verwenden Sie entweder die mobile Werbe-ID oder E-Mail-Adresse bzw. Telefonnummer.</li><li>Google Audiences erfordern mindestens 5.000 Nutzer:innen, bevor Anzeigen ausgeliefert werden.</li><li>Die Zielgruppengröße wird als null angezeigt, bis mindestens 1.000 Nutzer:innen vorhanden sind.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync) | 48 Stunden | LinkedIn verarbeitet 10 Abfragen pro Sekunde und 100.000 Nutzer:innen pro Anfrage. Braze bündelt Nutzer:innen alle 5 Sekunden. | KI or künstliche Intelligenz-prädiktive Zielgruppen | {::nomarkdown}<ul><li>Die Mindestgröße der Zielgruppe beträgt 300 Mitglieder unter Berücksichtigung des Standort-Targetings.</li><li>LinkedIn zeigt die Übereinstimmungsrate im Braze-Dashboard an.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync) | Zwischen 24 und 48 Stunden | Pinterest verarbeitet 7 Abfragen pro Sekunde und 1.900 Nutzer:innen pro Anfrage. Braze bündelt Nutzer:innen alle 5 Sekunden. | Ja | Pinterest-Zielgruppen erfordern mindestens 100 Nutzer:innen. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync) | N/A | Snapchat verarbeitet 10 Abfragen pro Sekunde und 100.000 Nutzer:innen pro Anfrage. Braze bündelt Nutzer:innen alle 5 Sekunden. | Ja | Snapchat unterstützt bis zu 1.000 Werbezielgruppen. |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync) | Bis zu 24 Stunden | N/A | Ja | {::nomarkdown}<ul><li>Es gibt keine Mindestgröße für CRM or Customer-Relationship-Management [-System] (CRM)-Zielgruppen in The Trade Desk.</li><li>Es gibt kein Limit für die Anzahl der Zielgruppen, die The Trade Desk unterstützt.</li><li>Wenn Sie eine Zielgruppe mit einer auf EU gesetzten Region synchronisieren, wird Telefonnummer nicht unterstützt.</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync) | Zwischen 24 und 48 Stunden | TikTok verarbeitet 50 Abfragen pro Sekunde und 10.000 Nutzer:innen pro Anfrage. Braze bündelt Nutzer:innen alle 5 Sekunden. | Ja | {::nomarkdown}<ul><li>TikTok unterstützt bis zu 400 Werbezielgruppen.</li><li>TikTok-Zielgruppen erfordern mindestens 1.000 Nutzer:innen, bevor Anzeigen ausgeliefert werden.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Übersicht" }
<sup>Wenn das Rate-Limit erreicht ist, wiederholt Braze die Synchronisierung für 13 Stunden.</sup>

## So funktioniert es {#how-it-works}

Um Audience Sync mit Google oder Facebook zu verwenden, verbinden Sie Ihr Werbekonto, indem Sie auf der Seite **Technologie-Partner** nach dem Partner suchen.

![Facebook Technologie-Partner.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Google Ads Technologie-Partner.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

Nachdem Sie Ihr Werbekonto verbunden haben, können Sie einen Canvas mit einem Audience-Sync-Schritt erstellen.

![Menü für Canvas-Komponenten zum Hinzufügen des Audience-Sync-Schritts zur User Journey.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

Wählen Sie als Nächstes den Partner aus, mit dem die Zielgruppen synchronisiert werden sollen.

![Option zur Auswahl Ihres Audience-Sync-Partners im Audience-Sync-Schritt.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

Für jeden Partner müssen Sie im Rahmen Ihres Audience-Sync-Schritts Folgendes konfigurieren:

- Werbekonto
- Zielgruppe
- Aktion zum Hinzufügen oder Entfernen von Nutzer:innen
- Felder zum Abgleich

Beachten Sie, dass Braze Nutzer:innen synchronisiert, sobald sie den Audience-Sync-Schritt in Ihrem Canvas erreichen.

Für jedes Audience-Sync-Ziel kann der Partner unterschiedliche Anforderungen an die Felder haben, die Braze senden kann. Weitere Details finden Sie in der jeweiligen Partnerdokumentation.

### Audience Sync Pro

Um einen Audience-Sync-Pro-Partner wie TikTok, Pinterest, Snapchat oder Criteo zu verwenden, können Sie Ihre Partner basierend auf Ihren Audience-Sync-Pro-Kaufkontingenten im Abschnitt **Audience Sync Pro** auf der Seite **Technologie-Partner** auswählen.

![Audience Sync Pro ohne bisher ausgewählte Partner.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

Wählen Sie zunächst die Partner aus, die Sie verwenden möchten. Jeder Kauf von Audience Sync Pro bietet Ihnen 3 zugewiesene Audience-Sync-Pro-Ziele, die in jedem Ihrer Workspaces in Ihrem Dashboard verfügbar sind.

![Option zur Auswahl von bis zu drei Partnern für die Verbindung mit Braze.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Nachdem Sie Ihre Audience-Sync-Pro-Ziele ausgewählt haben, verbinden Sie das Werbekonto des ausgewählten Partners, indem Sie auf die Partner-Kachel klicken.

![Ein Beispiel mit Snapchat und TikTok als ausgewählte Partner für Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Snapchat Audience-Sync-Einstellungen mit der Nachricht: „Sie haben erfolgreich 1 Snapchat-Konto verbunden“.]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Erstellen Sie abschließend Ihren Audience-Sync-Schritt in Canvas unter Verwendung dieses Audience-Sync-Pro-Ziels.

### Batching und Latenz {#batching-and-latency}

Wenn Nutzer:innen einen Audience-Sync-Schritt in Canvas erreichen, reiht Braze sie in ein Batching-System ein, das Nutzeraktualisierungen aggregiert, bevor sie an die Partner-API gesendet werden. Ein Batch wird gesendet, wenn eine der folgenden Bedingungen eintritt:

- **Der Batch erreicht sein Größenlimit.** Dies variiert je nach Partner:
  - Standard unterstützt bis zu 2.000 Nutzer:innen
  - Google Ads unterstützt bis zu 10.000 Nutzer:innen
  - Facebook und TikTok unterstützen bis zu 2.000 Nutzer:innen
- **Der Batch-Latenz-Timer läuft ab.** Der Standardwert beträgt eine Stunde, ist aber pro Partner konfigurierbar. Beispielsweise verwendet The Trade Desk 10 Minuten.

Canvase mit hohem Volumen senden möglicherweise früher, da sich die Batches schneller füllen. Canvase mit geringerem Volumen warten, bis der Latenz-Timer abläuft. Braze garantiert keine feste Versandzeit; der Zeitpunkt hängt von der Batch-Größe und dem konfigurierten Latenzfenster ab.

Braze zeichnet Versandaktivitäten in internen Logs zur Überwachung und Fehlerbehebung auf, diese Zeitstempel sind jedoch nicht als abfragbare Felder verfügbar. Nachdem Braze einen Batch an die Partner-API gesendet hat, verarbeitet der Partner die Zielgruppenaktualisierung gemäß seinen eigenen Service Level Agreements – in der Regel 6–48 Stunden.

Braze erhält keine Bestätigung von Partnern, dass einzelne Nutzer:innen abgeglichen oder synchronisiert wurden. Partnerantworten sind HTTP-Empfangsbestätigungen, keine Abgleichbestätigungen. Um zu überprüfen, ob eine Zielgruppe befüllt wurde, prüfen Sie die Werbeplattform des Partners (z.&#160;B. Google Ads Audience Manager:in oder Meta Business Manager:in).

### Audience-Sync-Fehler-E-Mails {#audience-sync-error-emails}

Wenn der Fehler mit der allgemeinen Partnerintegration zusammenhängt (z.&#160;B. ein Autorisierungsproblem), wird eine E-Mail an die Person gesendet, die die Integration verbunden hat. Wenn diese Person nicht mehr existiert, erhalten die Administrator:innen die E-Mails.

Wenn der Fehler mit Problemen bei der Audience-Sync-Komponente zusammenhängt (z.&#160;B. „Zielgruppe existiert nicht“) in Canvas, wird eine E-Mail an die Person gesendet, die den Canvas eingerichtet hat. Wenn diese Person nicht mehr existiert, wird die E-Mail an die Unternehmensadministrator:innen weitergeleitet.

Um zu konfigurieren, wer diese E-Mails erhält, wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in, um Empfänger:innen unter **Benachrichtigungseinstellungen** hinzuzufügen. Diese Einstellung deckt sowohl Integrationsfehler als auch Fehler der Audience-Sync-Komponente ab. Empfänger:innen, die Sie hinzufügen, erhalten diese E-Mails zusätzlich zu der Person, die mit dem Fehler verknüpft ist.

## Datenschutzerwägungen {#data-privacy-considerations}

{% alert important %}
Diese Dokumentation ist nicht dazu gedacht, rechtliche Beratung zu bieten, und darf auch nicht als solche herangezogen werden. Die Nutzung von Audience Sync unterliegt bestimmten gesetzlichen Anforderungen. Um sicherzustellen, dass Sie diese Funktion im Einklang mit allen geltenden Gesetzen nutzen, sollten Sie sich an Ihre Rechtsberatung wenden.
{% endalert %}

Beim Erstellen von Zielgruppen für Ad-Tracking möchten Sie möglicherweise bestimmte Nutzer:innen auf Grundlage ihrer Präferenzen einschließen oder ausschließen und Datenschutzgesetze einhalten, wie z. B. das Recht auf „Do Not Sell or Share“ gemäß dem [CCPA](https://oag.ca.gov/privacy/ccpa). Marketer sollten die entsprechenden Filter für die Berechtigung von Nutzer:innen in ihren Canvas-Eintrittskriterien implementieren. Die folgenden Optionen können dabei helfen.

Wenn Sie die [iOS IDFA über das Braze SDK or Software-Development-Kit]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations) erfasst haben, können Sie den Filter „Ads Tracking Enabled“ verwenden. Wählen Sie den Wert `true`, um Nutzer:innen nur dann an Audience-Sync-Ziele zu senden, wenn sie ihr Opt-in gegeben haben.

![Ein Canvas mit einer Eintrittszielgruppe „Ad Tracking Enabled is true“.]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

Wenn Sie `opt-ins`, `opt-outs`, `Do Not Sell Or Share` oder andere relevante angepasste Attribute erfassen, sollten Sie diese als Filter in Ihre Canvas-Eintrittskriterien aufnehmen:

![Ein Canvas mit einer Eintrittszielgruppe „opted_in_marketing equals true“.]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Weitere Informationen darüber, wie Sie diese Datenschutzgesetze innerhalb der Braze-Plattform einhalten können, finden Sie unter [Technische Unterstützung zum Datenschutz]({{site.baseurl}}/dp-technical-assistance).

## Verwalten der Einwilligung für Anzeigen-Targeting {#managing-consent-for-ad-targeting}

Als Werbetreibende:r sind Sie dafür verantwortlich, die Einwilligung für Ad-Tracking oder Targeting Ihrer Nutzer:innen zu verwalten.

Um Anzeigen an Ihre Nutzer:innen auszuspielen, müssen Sie alle geltenden Gesetze und Vorschriften sowie die Richtlinien und Anforderungen der Werbeplattform einhalten. Verwenden Sie Braze nur, um Nutzer:innen zu targeten und zu synchronisieren, für die Sie deren Einwilligung eingeholt haben.

Um Ihre Zielgruppenlisten auf diesen Werbeplattformen aktuell zu halten und Nutzer:innen zu entfernen, die ihre Einwilligung widerrufen haben, richten Sie einen Canvas ein, der Nutzer:innen mithilfe eines Audience-Sync-Schritts aus bestehenden Zielgruppenlisten entfernt.
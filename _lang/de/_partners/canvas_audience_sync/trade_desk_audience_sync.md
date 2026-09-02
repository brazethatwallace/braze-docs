---
nav_title: The Trade Desk
article_title: Canvas Audience Sync mit The Trade Desk
description: "Dieser Referenzartikel beschreibt, wie Sie Braze Audience Sync mit The Trade Desk verwenden, um Werbung basierend auf Verhaltens-Trigger or triggern or triggern, Segmentierung und mehr auszuliefern."
alias: /trade_desk_audience_sync/
tool:
  - Canvas
page_order: 7
---

# Audience Sync mit The Trade Desk {#audience-sync-to-the-trade-desk}

> Mit Braze Audience Sync mit The Trade Desk können Sie Ihre First-Party-Nutzerdaten dynamisch von Braze direkt in The Trade Desk synchronisieren – für Retargeting, Lookalike-Modellierung und Ausschluss-Targeting.

**Häufige Anwendungsfälle für Audience Sync:**

- Retargeting Ihrer bestehenden Nutzer:innen auf The Trade Desk mit personalisierten Campaigns.
- Senden von First-Party-Daten an The Trade Desk für Ausschluss-Targeting.
- Synchronisierung von Nutzer:innen mit neuen oder bestehenden Zielgruppen oder CRM or Customer-Relationship-Management [-System] (CRM)-Datensegmenten.

## Voraussetzungen {#prerequisites}

Stellen Sie sicher, dass die folgenden Punkte erstellt, abgeschlossen oder akzeptiert wurden, bevor Sie den Audience Sync-Schritt mit The Trade Desk in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| API-Token / Textbaustein | [The Trade Desk](https://partner.thetradedesk.com/v3/portal/api/doc/Authentication#ui-method-create) | Ein Standard-API-Token / Textbaustein, das auf der The Trade Desk-Plattform erstellt wurde. Wir empfehlen, die Lifetime des API-Tokens auf bis zu ein Jahr festzulegen, um minimale Unterbrechungen Ihrer Canvase mit The Trade Desk Audience Sync zu vermeiden. |
| The Trade Desk Nutzungsbedingungen und Richtlinien | The Trade Desk | Sie müssen einer UID2/CRM or Customer-Relationship-Management [-System] (CRM)-Teilnahmerichtlinie zustimmen, bevor Sie Daten an The Trade Desk senden können. Kontaktieren Sie Ihre Vertretung bei The Trade Desk, um zu bestätigen, dass Sie die entsprechende Signatur haben, um die Datenzustellung an The Trade Desk zu aktivieren.<br><br> {::nomarkdown}<ul><li>Bestätigen Sie, dass der CRM or Customer-Relationship-Management [-System] (CRM)-Datenverwaltungszugriff in Ihrem Konto aktiviert ist&#8212;Ihre Vertretung bei The Trade Desk kann Ihnen dabei helfen. Sie benötigen Ihre Advertiser-ID.</li><li>Halten Sie Ihr Standard-API-Token / Textbaustein bereit. Sie können den Anweisungen auf dieser Seite folgen, um eines zu generieren.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: The Trade Desk-Konto verbinden {#step-1-connect-the-trade-desk-account}

Um zu beginnen, gehen Sie zu **Partnerintegrationen** > **Technologie-Partner** > **The Trade Desk**. Geben Sie die folgenden Details aus Ihrem Trade Desk-Konto an:

- **API-Token / Textbaustein**
- **Advertiser-ID-Name** (dieser optionale Name identifiziert das Advertiser-Konto, das im Audience Sync Canvas-Schritt referenziert werden soll)
- **Advertiser-ID**

Wählen Sie dann **Verbinden** aus.

![Ein Beispiel für einen nicht verbundenen Audience Sync für The Trade Desk.]({% image_buster /assets/img/audience_sync/trade_desk/connect_sync.png %}){: style="max-width:90%;"}

#### Mehrere The Trade Desk-Konten verbinden (optional) {#connect-multiple-the-trade-desk-accounts-optional}

Nachdem Sie Ihr erstes The Trade Desk-Konto verbunden haben, können Sie auf der The Trade Desk-Partnerseite weitere Advertiser-Konten hinzufügen, indem Sie **Weitere Advertiser verbinden** auswählen und dann den **Advertiser-ID-Namen** und die **Advertiser-ID** für jedes Konto angeben.

### 2. Schritt: Einen Audience Sync-Schritt mit The Trade Desk hinzufügen {#step-2-add-an-audience-sync-step-with-the-trade-desk}

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync** aus. Wählen Sie dann **The Trade Desk** als Audience Sync-Partner aus.

![Option zur Auswahl Ihres Partners für die Synchronisierung mit dem Audience Sync-Schritt.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step.png %}){: style="max-width:90%;"}

### 3. Schritt: Synchronisierung einrichten {#step-3-set-up-your-sync}

Konfigurieren Sie als Nächstes Ihre Synchronisierungsdetails:

1. Wählen Sie ein Werbekonto aus.
2. Wählen Sie eine bestehende Zielgruppe aus oder erstellen Sie eine neue Zielgruppe.

![Audience Sync-Einrichtung mit einem Zielgruppenfeld, das den Namen „valentines2025“ enthält.]({% image_buster /assets/img/audience_sync/trade_desk/choose_audience.png %}){: style="max-width:90%;"}

{: start="3"}
3. Wählen Sie eine Aktion aus: entweder **Nutzer:innen zur Zielgruppe hinzufügen** oder **Nutzer:innen aus der Zielgruppe entfernen**.

![Audience Sync-Einrichtung zum Hinzufügen von Nutzer:innen zur Zielgruppe.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step2.png %}){: style="max-width:90%;"}

{: start="4"}
4. Wählen Sie eines der folgenden Felder für den Abgleich aus: **E-Mail**, **Telefonnummer** oder **Mobile Advertiser-ID**.

{% alert note %}
Wenn Sie eine Zielgruppe in The Trade Desk mit einer auf EU eingestellten Region synchronisieren, wird die Telefonnummer von The Trade Desk nicht unterstützt. Wenden Sie sich an The Trade Desk für die Unterstützung von Telefonnummern in der EU-Region.
{% endalert %}

### 4. Schritt: Canvas starten {#step-4-launch-your-canvas}

Nachdem Sie Ihren Audience Sync mit The Trade Desk konfiguriert haben, können Sie den Canvas starten! Die neue Zielgruppe wird erstellt, und Nutzer:innen, die den Audience Sync-Schritt durchlaufen, werden in diese Zielgruppe auf The Trade Desk übertragen. Wenn Ihr Canvas nachfolgende Komponenten enthält, gehen Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey weiter.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie lange dauert es, bis die Zielgruppengrößen in The Trade Desk angezeigt werden? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-the-trade-desk}

Dies kann bis zu 24 Stunden dauern.

### Was ist die Mindestgröße einer Zielgruppe, damit The Trade Desk sie in Ihrem Werbekonto anzeigt? {#what-is-the-minimum-audience-size-for-the-trade-desk-to-populate-within-your-ad-account}

Es gibt keine Mindestgröße für CRM or Customer-Relationship-Management [-System] (CRM)-Zielgruppen in The Trade Desk.

### Wie erfahre ich, ob Nutzer:innen nach der Übertragung an The Trade Desk abgeglichen wurden? {#how-do-i-know-if-users-have-matched-after-passing-users-to-the-trade-desk}

In The Trade Desk werden empfangene IDs neben dem Segment angezeigt.

- Empfangene IDs sind die Anzahl der IDs, die in den letzten 30 Tagen empfangen wurden.
- Aktive IDs sind die Anzahl der IDs, die in den letzten sieben Tagen im Bidding gesehen wurden.

### Wie viele Zielgruppen kann The Trade Desk unterstützen? {#how-many-audiences-can-the-trade-desk-support}

Es gibt keine Begrenzung für die Anzahl der Zielgruppen, die auf The Trade Desk unterstützt werden können.
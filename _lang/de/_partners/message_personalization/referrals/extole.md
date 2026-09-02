---
nav_title: Extole
article_title: Extole
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Extole, einem Unternehmen für Empfehlungsmarketing, die es Ihnen erlaubt, Kunden-Events und -Attribute aus Empfehlungs- und Wachstumsprogrammen in Braze zu übernehmen."
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> [Extole](https://www.extole.com/), ein SaaS or Software-as-a-Service-Unternehmen, ist branchenführend im Empfehlungsmarketing und hilft bei der Erstellung und Optimierung effektiver Programme für das Empfehlungsmarketing, um die Kundenakquise zu steigern.

_Diese Integration wird von Extole gepflegt._

## Über die Integration {#about-the-integration}

Mit der Integration von Braze und Extole können Sie Kunden-Events und -Attribute aus den Freundschaftswerbungs- und Wachstumsprogrammen von Extole in Braze übernehmen und so personalisierte Marketingkampagnen erstellen, die die Kundenakquise, das Engagement und die Kundenbindung steigern. Sie können auch dynamisch Attribute von Extole-Inhalten, wie personalisierte Codes und Links, in die Braze-Kommunikation einbeziehen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Extole-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Extole-Konto. |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit der Berechtigung `users.track`. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-API-URL | Ihre Braze-API-URL ist spezifisch für Ihre [Braze-Instanz]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Die folgenden Anwendungsfälle zeigen Ihnen einige Möglichkeiten, wie Sie die Integration von Extole in Braze nutzen können. Arbeiten Sie mit Ihren Extole-Implementierungs- und Customer-Success-Managern zusammen, um eine Option zu entwickeln, die den speziellen Anforderungen Ihres Unternehmens entspricht.

- Verwenden Sie angepasste Events aus Ihren Empfehlungs- und Engagement-Programmen, um eine Braze-Campaign oder ein Canvas zu Trigger or triggern or triggern
- Erstellen Sie angepasste Segmente, Dashboards und Berichte mit Daten aus Ihren Extole-Programmen
- Melden Sie Nutzer:innen automatisch von Ihrer Marketing-Liste in Braze ab oder dafür an

## Integration

Führen Sie die folgenden Schritte aus, um Ihre Integration schnell zum Laufen zu bringen. Ihre Extole-Implementierungs- und CSM or Customer-Success-Manager or Customer-Success-Manager:in unterstützen Sie bei diesem Prozess und beantworten alle Ihre Fragen.

### Verbindung mit Ihrem Braze-Konto herstellen {#connect-to-your-braze-account}

1. Wählen Sie die Braze-Integration auf der [Partnerseite](https://my.extole.com/partners) Ihres My-Extole-Kontos aus.
2. Wählen Sie in der Braze-Integration **Install** aus, um die Verbindung zwischen Extole und Braze herzustellen.
3. Füllen Sie die erforderlichen Felder aus, beginnend mit Ihrem Braze Representational State Transfer-API-Schlüssel.
4. Geben Sie Ihre Braze-API-URL ein. Diese URL hängt davon ab, auf welcher Instanz Ihr Braze-Konto eingerichtet ist.
5. Fügen Sie alle Extole-Events hinzu, die Sie an Braze senden möchten. Die Standard-Events, Event-Eigenschaften und Nutzerattribute sind in der [Tabelle „Extole Events“](https://dev.extole.com/docs/braze#extole-program-events) beschrieben.
6. Fügen Sie alle Reward-Status hinzu, die Sie an Braze senden möchten, außer dem Status `FULFILLED`. In der [Tabelle „Extole Rewards“](https://dev.extole.com/docs/braze#extole-rewards) finden Sie Beschreibungen der verfügbaren Reward-Status.
7. Wählen Sie die Zuordnung Ihres externen Braze-ID-Schlüssels aus. So aktualisiert Extole die Nutzerprofile in Braze. Sie können den externen Braze-ID-Schlüssel der `email_address` oder `partner_user_id` von Extole für die Nutzer:innen zuordnen. Wir empfehlen die Verwendung von `external_id` anstelle von `email_address`, da dies sicherer ist.
8. Speichern Sie Ihre Einstellungen, um die Verbindung abzuschließen. Jetzt können Extole-Events in Ihr Braze-Konto fließen.

### Extole-Programm-Events {#extole-program-events}

Im Folgenden finden Sie die Standard-Events, Event-Eigenschaften und Nutzerattribute, die Extole an Braze sendet. Wenden Sie sich an Ihre Extole-Implementierungs- oder CSM or Customer-Success-Manager or Customer-Success-Manager:in, um zusätzliche Extole-Events zu identifizieren und zu Ihrer Integration hinzuzufügen.

| Event | Beschreibung | Event-Eigenschaften | Nutzerattribute |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | Ein:e Teilnehmer:in erstellt den Share-Link, indem die E-Mail-Adresse in der Extole Share Experience eingegeben wird. | Event-Name  <br>Event-Zeitpunkt  <br>Partner (Extole)  <br>Funnel (Fürsprecher:in oder Freund:in)  <br>Programm | <br>Externe ID <br>E-Mail  <br>Share-Link |
| `extole_shared` | Ein:e Teilnehmer:in teilt den Empfehlungslink mit einer/einem Freund:in. | Event-Name  <br>Event-Zeitpunkt  <br>Partner (Extole)  <br>Externe ID  <br>Funnel (Fürsprecher:in oder Freund:in)  <br>Programm  <br>Share-Kanal | E-Mail <br>Vorname <br>Nachname |
| `outcome` – Das Ergebnis ist dynamisch und hängt von der Konfiguration Ihres Programms ab (z. B. `extole_shipped`, `extole_converted`). | Ein:e Teilnehmer:in hat konvertiert oder das gewünschte Ergebnis-Event abgeschlossen, das für das Programm konfiguriert wurde. | Dynamisch pro Programm | E-Mail <br>Vorname <br>Nachname |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Extole-Programm-Events" }

### Extole-Abo-Status {#extole-subscription-states}

| Abo-Status | Beschreibung | Event-Eigenschaften | Nutzerattribute |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | Ein:e Teilnehmer:in hat sich für den Erhalt von Marketing-Nachrichten entschieden. | – | E-Mail  <br>Listentyp  <br>Externe ID  <br>E-Mail abonnieren (Opt-in) |
| `unsubscribed` | Ein:e Teilnehmer:in hat sich gegen den Erhalt von E-Mails von Extole entschieden. | E-Mail  <br>Externe ID  <br>Abo-Status (abgemeldet)  <br>Abo-Gruppen-ID  | Listentyp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Extole-Abo-Status" }

### Extole Rewards

Standardmäßig sendet Extole Reward-Events im Status `FULFILLED` an Braze, damit Sie Reward-Benachrichtigungen über eine Braze-Campaign oder ein Canvas Trigger or triggern or triggern können. In der folgenden Tabelle finden Sie weitere Reward-Status.

| Reward-Status | Beschreibung | Event-Eigenschaften | Nutzerattribute |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | Der Standardstatus. Der Prämie wurde von einem Extole-Prämienanbieter ein Wert zugewiesen (z. B. ein Gutschein oder eine Geschenkkarte). | E-Mail <br>Nennwert  <br>Gutscheincode  <br>Nennwerttyp  | E-Mail <br>Vorname  <br>Nachname |
| `EARNED` | Eine Prämie wurde erstellt und einer Person zugeordnet. | E-Mail <br>Nennwert  <br>Gutscheincode  <br>Nennwerttyp  | E-Mail <br>Vorname  <br>Nachname |
| `SENT` | Die Prämie wurde erfüllt und entweder per E-Mail oder auf einem Gerät an die/den Empfänger:in gesendet. | E-Mail <br>Nennwert  <br>Gutscheincode  <br>Nennwerttyp  | E-Mail <br>Vorname  <br>Nachname |
| `REDEEMED` | Die Prämie wurde von der/dem Empfänger:in eingelöst, was durch ein Konversions- oder Einlösungs-Event an Extole belegt wird. | E-Mail <br>Nennwert  <br>Gutscheincode  <br>Nennwerttyp  | E-Mail <br>Vorname  <br>Nachname |
| `FAILED` | Ein Problem hat die Ausgabe oder den Versand der Prämie verhindert und erfordert Aufmerksamkeit. | E-Mail <br>Nennwert  <br>Gutscheincode  <br>Nennwerttyp  | E-Mail <br>Vorname  <br>Nachname |
| `CANCELED` | Die Prämie wurde deaktiviert und kehrt ins Inventar zurück. | E-Mail <br>Nennwert  <br>Nennwerttyp  | E-Mail <br>Vorname  <br>Nachname |
| `REVOKED` | Die eingelöste Prämie wurde für ungültig erklärt. Extole hat zum Beispiel eine Geschenkkarte eines Anbieters angefordert und dann festgestellt, dass die Karte irrtümlich verschickt wurde. Wenn der Anbieter den Widerruf der Prämie unterstützt, wird Extole das Geld zurückfordern, und die Prämie ist nicht mehr gültig. | E-Mail <br>Nennwert   <br>Nennwerttyp  | E-Mail <br>Vorname  <br>Nachname |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Extole Rewards" }


## Anpassung {#customization}

### Nutzer:innen in Braze finden und erstellen {#find-and-create-users-in-braze}

Für bestimmte Anwendungsfälle, wie z. B. ein neues E-Mail- oder Kurzmitteilungsdienst or SMS-Abo, für das Extole keine externe ID (Nutzer-ID) hat, kann Extole über den Braze-Endpunkt [Kundenprofil or Nutzerprofil nach Bezeichner exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) nach dem Bezeichner der/des Nutzer:in suchen. Extole fügt alle Profilattribute hinzu und aktualisiert sie, wenn die/der Nutzer:in in Braze existiert. Wenn die Anfrage kein Kundenprofil or Nutzerprofil zurückgibt, verwendet Extole den Endpunkt `/users/track`, um einen Nutzer-Alias mit der E-Mail-Adresse der/des Nutzer:in als Alias-Namen zu erstellen.

## Verwendung dieser Integration {#using-this-integration}

Nachdem Sie Ihre Konten verbunden haben, fließen die Events automatisch von Extole zu Braze, ohne dass Sie etwas tun müssen. Eine Live-Ansicht der an Braze gesendeten Events finden Sie zur Fehlerbehebung im Outbound Webhook Center von Extole.
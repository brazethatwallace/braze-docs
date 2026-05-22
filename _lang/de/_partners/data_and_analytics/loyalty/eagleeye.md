---
nav_title: Eagle Eye
article_title: Eagle Eye
description: "Erfahren Sie, wie Sie Eagle Eye in Braze integrieren können."
alias: /partners/eagle_eye/
page_type: partner
search_tag: Partner
---

# Eagle Eye

> [Eagle Eye](https://eagleeye.com/) ist ein führendes SaaS- und KI-Technologieunternehmen, das Marken aus den Bereichen Einzelhandel, Reisen und Gastgewerbe dabei unterstützt, die Loyalität ihrer Endkund:innen zu gewinnen, indem es ihre Realtime-, Omnichannel- und personalisierten Marketing-Aktivitäten in großem Umfang ermöglicht.

_Diese Integration wird von Eagle Eye verwaltet._

## Übersicht {#overview}

Eagle Eye Connect ist eine bidirektionale Integration zwischen Braze und AIR, die es Marken ermöglicht, Treue- und Aktionsdaten direkt in Braze zu aktivieren. Clients können in AIR Rewards an Verbraucher:innen ausgeben, die eine Zielgruppe in AIR betreten. Dies erlaubt Marketern, das Customer-Engagement anhand von Echtzeitdaten wie Punktesalden, Aktionen und Reward-Aktivitäten zu personalisieren.

## Anwendungsfälle {#use-cases}

- Triggern Sie Braze-Campaigns auf der Grundlage von Treue-Events wie Punkteschwellen oder verdienten Rewards.
- Reichern Sie Braze-Nutzerprofile mit Realtime-Treuedaten an, um ein personalisierteres Targeting zu ermöglichen.
- Verfolgen Sie die Wirksamkeit von Campaigns in Verbindung mit der Einlösung von Rewards und erstellen Sie Berichte darüber.
- Geben Sie Rewards in AIR aus, wenn Nutzer:innen Campaigns in Braze beitreten.

## Voraussetzungen {#prerequisites}

| Anforderung              | Beschreibung |
|--------------------------|-------------|
| Eagle Eye AIR-Konto    | Sie benötigen ein aktives Eagle Eye AIR-Konto, um von dieser Partnerschaft zu profitieren. Wenden Sie sich an das Partnerships-Team von Eagle Eye unter [partnerships@eagleeye.com](mailto:partnerships@eagleeye.com), um loszulegen. |
| Braze REST-API-Schlüssel       | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen > API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt      | [Ihre REST-Endpunkt-URL](https://www.braze.com/docs/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Ausgehend vs. eingehend {#outbound-vs-inbound}

In den folgenden Tabellen werden die beiden Arten von Integrationen beschrieben, die zwischen Braze und Eagle Eye AIR unterstützt werden. Eagle Eye Connect ist die Middleware, die den Datenaustausch zwischen AIR und Partnersystemen wie Braze ermöglicht. Weitere Informationen finden Sie in der [Braze-Dokumentation von Eagle Eye](https://developer.eagleeye.com/docs/braze).

{% tabs local %}
{% tab Ausgehend %}
<table aria-label="Outbound vs. inbound">
  <caption>Ausgehend vs. eingehend</caption>
  <thead>
    <tr>
      <th>Richtung</th>
      <th>Initiiert von</th>
      <th>Datenfluss</th>
      <th>Zweck</th>
      <th>Beispiel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eagle Eye → Braze</td>
      <td>Eagle Eye</td>
      <td>Zur Braze API</td>
      <td>
        Senden Sie Kundenbindungsdaten als angepasste Attribute über angepasste Events in Braze-Nutzerprofile. Innerhalb von Braze können die aufgenommenen Daten verwendet werden, um:
        <ul>
          <li>Nutzer:innen zu segmentieren und Campaigns zu triggern</li>
          <li>Nachrichten zu personalisieren</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Senden von Treuepunkten oder Tier-Status an Braze (<code>ee_loyalty.points.current</code>, <code>ee_loyalty.tier.tierId</code>)</li>
          <li>Aktualisierung des Profils von Nutzer:innen, wenn sie einen Coupon erhalten oder einlösen.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Outbound vs. inbound" }
{% endtab %}

{% tab Eingehend %}
<table aria-label="Outbound vs. inbound">
  <caption>Ausgehend vs. eingehend</caption>
  <thead>
    <tr>
      <th>Richtung</th>
      <th>Initiiert von</th>
      <th>Datenfluss</th>
      <th>Zweck</th>
      <th>Beispiel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Braze → Eagle Eye</td>
      <td>Braze</td>
      <td>Zur Eagle Eye API über Webhook</td>
      <td>
        Wenn Verbraucher:innen in Braze aus einer beliebigen Quelle eine Zielgruppe betreten, kann Braze einen Webhook an EE Connect triggern, sodass EE ein Reward (Coupon oder Punkte) ausgeben kann.<br><br>
        Nach Abschluss der Aktion in AIR würde Braze ein ausgehendes Event von AIR erhalten.
      </td>
      <td>
        <ul>
          <li>Rewards (Coupon oder Punkte) werden an Verbraucher:innen für die Teilnahme am Kundenbindungs-Programm ausgegeben</li>
          <li>Rewards werden an Verbraucher:innen ausgegeben, die eine verspätete Zustellung hatten</li>
          <li>Geburtstags-Rewards</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Outbound vs. inbound" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Weitere Informationen zu den angepassten Daten, die Sie als angepasste Attribute oder Events an Braze senden können, finden Sie in der [Braze-Dokumentation von Eagle Eye](https://developer.eagleeye.com/docs/braze#data-model).
{% endalert %}

## Überblick über die Integration {#integration-overview}

Eingehende und ausgehende Konnektoren können derzeit nur über die API mit direkter Unterstützung durch das Eagle Eye Team eingerichtet werden – eine Self-Service-Option im AIR-Dashboard ist jedoch in Vorbereitung!

Wenn Sie mit Ihrem Eagle Eye Team zusammenarbeiten, werden Sie Folgendes erledigen:

### 1. Schritt: Konfigurationsdetails bereitstellen {#step-1-provide-configuration-details}

Zunächst geben Sie Ihrem Eagle Eye Team die folgenden Informationen:

| Sie liefern            | Beschreibung |
|------------------------|-------------|
| Braze-API-Zugangsdaten  | Teilen Sie Ihren Braze REST-Endpunkt, Ihren App-Bezeichner und Ihren API-Schlüssel sicher mit Ihrem Eagle Eye Kontakt. |
| Bezeichner-Abgleich    | Bestimmen und teilen Sie den primären Nutzer:innen-Bezeichner für Profil-Updates, der in AIR und Braze gemeinsam verwendet wird, z. B. externe ID oder E-Mail. |
| Authentifizierungsschlüssel               | Legen Sie für jeden eingehenden und ausgehenden Konnektor einen geheimen Authentifizierungsschlüssel fest und teilen Sie ihn. |
| Währungscode          | Geben Sie den 3-stelligen Währungscode für die Anzeige von Geldbeträgen an (z. B. USD). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Provide configuration details" }

### 2. Schritt: Eagle Eye Connect konfigurieren {#step-2-configure-eagle-eye-connect}

Ihr Eagle Eye Team konfiguriert Eagle Eye Connect unter Verwendung der von Ihnen bereitgestellten Details sowie der eindeutigen AIR-API-Zugangsdaten und ausgehenden Events für die Konnektoren.

### 3. Schritt: Social Behavioral Actions in AIR konfigurieren {#step-3-configure-social-behavioral-actions-in-air}

Als Nächstes richten Sie in AIR eine oder mehrere Social Behavioral Actions mit eindeutigen Aktionsreferenzen ein, um Punkte oder Coupons auszugeben.

### 4. Schritt: Braze konfigurieren {#step-4-configure-braze}

In Braze werden Sie Folgendes erledigen:

- Richten Sie Campaigns in Braze ein, um Rewards in AIR auszugeben.
- Richten Sie alle Mitteilungen an Verbraucher:innen ein, wenn AIR-Events empfangen werden.

### 5. Schritt: Ihre Integration testen {#step-5-test-your-integration}

Führen Sie API-Aufrufe in AIR durch und beobachten Sie den Fluss von Event-Daten in Ihren Braze-Workspace. Validieren Sie die von AIR empfangenen Daten und bestätigen Sie, dass die Attribute wie erwartet aktualisiert werden.

Fügen Sie außerdem Nutzer:innen zu Zielgruppen hinzu und bestätigen Sie, dass Rewards in AIR ausgegeben werden.

### 6. Schritt: Einführung in die Produktion {#step-6-launch-to-production}

Nachdem die Tests erfolgreich verlaufen sind, kann die Integration in Betrieb genommen werden, um kontinuierlich Daten an Braze zu senden. Die gleichen Konfigurationsschritte sind für Produktionsumgebungen in AIR und Braze erforderlich.

Wenden Sie sich an Ihren Eagle Eye Customer-Success-Manager, damit Ihnen eine Ressource zugewiesen wird, um EE Connect einzurichten.

## Support

Wenn Sie Unterstützung bei der Integration oder Fehlerbehebung benötigen, wenden Sie sich bitte an das Eagle Eye Support-Team unter [support@eagleeye.com](mailto:support@eagleeye.com).
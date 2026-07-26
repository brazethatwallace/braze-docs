---
nav_title: Kognitiv Inspire
article_title: Kognitiv Inspire
description: "Kognitiv Inspire ist ein Treuetechnologie-System, mit dem Sie Ihre Strategie zur Kundenbindung umsetzen und auswerten können. Es bietet innovative Funktionen und eine maßgeschneiderte Kommunikation mit den Mitgliedern, um die Effizienz des Programms zu steigern."
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# Kognitiv Inspire

> [Kognitiv Inspire](http://kognitiv.com) ist ein Treuetechnologie-System, das durch ergebnisorientierte Kundenbindungs-Programme, die das geschäftskunden-Engagement verstärken, die Ausgaben erhöhen und loyales Verhalten honorieren, unvergleichliche Kundenerlebnisse ermöglicht.

_Diese Integration wird von Kognitiv Inspire gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Kognitiv erlaubt es Ihnen, Ihre Strategie zur Kundenbindung zu implementieren und zu evaluieren. Sie bietet Ihnen innovative Funktionen und eine maßgeschneiderte Kommunikation mit Ihren Mitgliedern, um die Effizienz Ihres Programms zu steigern.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Kognitiv-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Kognitiv-Konto](http://kognitiv.com). |
| Kognitiv-API-Schlüssel | Ein Kognitiv-REST-API-Schlüssel. Dieser kann auf der Seite **API Security Tokens** erstellt werden. |
| Braze-REST-Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle {#use-cases}

- **Personalisierte Anmeldung für Kundenbindungs-Programme**: Bringen Sie Ihre Mitglieder auf ihrer Journey voran, indem Sie sie nahtlos in das Programm aufnehmen und ihnen eine angepasste Willkommensnachricht über den von ihnen bevorzugten Kanal zustellen.
- **Ausgabe von Rewards und Engagement-Benachrichtigungen**: Halten Sie den Funken der Loyalität am Leben, indem Sie Rewards und Benachrichtigungen ausgeben, die jeden Meilenstein eines Mitglieds feiern.
- **Strategische Einstufung und Segmentierung der Mitglieder**: Ermöglichen Sie ein stärker personalisiertes Engagement, indem Sie Mitglieder auf der Grundlage von Ausgaben, Engagement und einfachen oder komplexen Geschäftsregeln, die auf die spezifischen Bedürfnisse Ihrer Marke zugeschnitten sind, einteilen und segmentieren.
- **Realtime-Benachrichtigung über Aktionsteilnahme**: Geben Sie jedem Mitglied das Gefühl, etwas Besonderes zu sein, indem Sie es sofort über die Teilnahmeberechtigung an exklusiven Aktionen benachrichtigen.

## Integration

Verwenden Sie Kognitiv-Webhooks, um Anfragen an Braze zu senden, wenn Treueereignisse auftreten. Die folgenden Beispiele zeigen, wie Sie Kognitiv und Braze verwenden, um ein Reward auszustellen, Kognitiv-Nutzer:innen in Braze zu registrieren und ihnen eine Willkommens-E-Mail zu senden.

{% raw %}
### Braze – Reward-Ausgabe {#braze-issue-reward}

Das folgende Beispiel von Kognitiv gibt ein Mitglieder-Reward aus. Kognitiv Inspire leitet dieses Reward-Ausgabe-Ereignis als angepasstes Event über Webhooks an Braze weiter. Um eine Folge-E-Mail zur Mitteilung des Rewards zu senden, erstellen Sie eine Campaign oder ein Canvas, das durch dieses angepasste Event ausgelöst wird.

**Webhook-URL**: `<braze-api-rest-endpoint>`
**Anfragetext**: `Raw Text`

- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Anfragetext {#request-body}

```json
{
  "events" : [
    {
    "external_id" : "{{memberId}}",
    "app_id" : "93ec5a59-3752-4a45-8559-55b61209ba38",
    "name" : "rewards_issued",
    "time" : "{{issuedDate}}",
    "issued_date" : "{{issuedDate}}",
    "issued_location_name" : "{{issuedLocationName}}",
    "reward_type" : "{{rewardType}}"
    }
  ]
}
```

### Nutzer:in erstellen und Willkommens-E-Mail senden {#create-a-user-and-send-a-welcome-email}

Das folgende Kognitiv-Beispiel erstellt neue Nutzer:innen in Braze, wenn sie sich bei KLS anmelden. Um eine Willkommens-E-Mail für diese Nutzer:innen zu planen, erstellen Sie in Braze eine Campaign oder ein Canvas, das auf der Grundlage bestimmter angepasster Attribute ausgelöst wird.

**Webhook-URL**: `<braze-api-rest-endpoint>` <br>
**Anfragetext**: `Raw Text`

- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Anfragetext

```json
{
  "attributes": [
    {
      "app_id": "93ec5a59-3752-4a45-855b6109ba38",
      "bio": "Software Architect",
      "country": "{{memberAddressCO}}",
      "email": "{{memberEmail}}",
      "email_subscribe": "opted_in",
      "external_id": "{{memberId}}",
      "first_name": "{{memberFirstName}}",
      "home_city": "{{memberAddressCity}}",
      "time_zone": "America/Chicago",
      "total_points_balance": "{{memberPointsAvailable}}",
      "CreatedKLS": "{{issuedTimestamp}}",
      "email_contact_allowed" : "{{memberEmailContactAllowed}}",
      "sms_contact_allowed" : "{{memberSmsContactAllowed}}",
      "date_joined": "{{issuedDate}}"
    }
  ]
}
```
{% endraw %}

## Kognitiv Inspire – Dokumentation und Integrations-Features {#kognitiv-inspire-documentation-and-integration-features}

Nach der Integration von Braze in Kognitiv Inspire ermöglicht Ihnen Kognitiv den Zugriff auf sein umfangreiches API-Portfolio, innovative Webhook-Features und robuste Datenimport- und -exportfunktionen für nahtlose Massentransfers. Weitere Informationen zu den Features und Integrationsmöglichkeiten von Kognitiv Inspire finden Sie im [Kognitiv-Ressourcenhandbuch](https://info.kognitivloyalty.com) oder kontaktieren Sie Kognitiv für eine geführte Demonstration.

### Endpunkte {#endpoints}

**REST-API-Autorisierung**
- Region USA: `https://app.kognitivloyalty.com/Auth/connect/token`
- Region CA/EMEA: `https://ca.kognitivloyalty.com/Auth/connect/token`
- Region APAC: `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API (Basis-URL)**
- Region USA: `https://app.kognitivloyalty.com/api`
- Region CA/EMEA: `https://ca.kognitivloyalty.com/api`
- Region APAC: `https://aus.kognitivloyalty.com/api`

**Webservice-Endpunkte (Basis-URL)**
- Region USA: `https://app.kognitivloyalty.com/WS`
- Region CA/EMEA: `https://ca.kognitivloyalty.com/WS`
- Region APAC: `https://aus.kognitivloyalty.com/WS`

Weitere Informationen zur Konfiguration von Zugangstoken und SFTP-Endpunkten erhalten Sie bei Kognitiv im Rahmen einer Demonstration.
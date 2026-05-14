---
nav_title: API-Partnerintegration
alias: /api_partner_integration/
hidden: true
---

# API-Partnerintegration {#api-partner-integration}

> Erfahren Sie mehr über die Anforderungen für API-Partnerintegrationen, z. B. die Syntax für `User-Agent`-Header.

{% alert important %}
Bisher mussten Partner ihren Namen im Partnerfeld ihrer API-Anfragen angeben. Diese Formatierung wird nicht mehr unterstützt, und ein `User-Agent`-Header ist jetzt erforderlich.
{% endalert %}

## User-Agents

Sie müssen einen `User-Agent`-Header einfügen, der die Quelle des Datenverkehrs eindeutig identifiziert. So können unsere gemeinsamen Kund:innen den Partner-Datenverkehr in den API-Nutzungsberichten von Braze einsehen, und Braze-Ingenieur:innen können Integrationen identifizieren, die nicht den Best Practices entsprechen. Im Allgemeinen sollten Sie nur einen einzigen User-Agent für Ihren gesamten Datenverkehr verwenden.

### Syntax

Ihr `User-Agent`-Header muss dem folgenden Format entsprechen (das dem [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46)-Standard ähnelt):

```bash
User-Agent: partner-OrganizationName
```

Ersetzen Sie Folgendes:

| Platzhalter | Beschreibung |
|-------------|-------------|
| `OrganizationName` | Der Name Ihrer Organisation, formatiert in Pascal Case. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Syntax" }

### Beispiele {#examples}

Das folgende Beispiel zeigt einen korrekten User-Agent für die Cloud-Datenaufnahme von Snowflake:

```bash
User-Agent: partner-Snowflake
```

Das folgende Beispiel wäre hingegen falsch, da es die Quelle des Datenverkehrs nicht eindeutig identifiziert:

```bash
User-Agent: axios/1.4.0
```

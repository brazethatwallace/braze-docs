---
nav_title: "Nutzer-Alias-Objekt"
article_title: API-Nutzer-Alias-Objekt
page_order: 11
page_type: reference
description: "Dieser Referenzartikel erklärt die verschiedenen Komponenten des Nutzer-Alias-Objekts."

---

# Nutzer-Alias-Objekt {#user-alias-object}

> Ein Alias dient als alternativer eindeutiger Bezeichner für Nutzer:innen. Mithilfe eines Nutzer-Alias-Objekts können Sie einen konsistenten Bezeichner für Analytics festlegen, der eine:n bestimmte:n Nutzer:in sowohl vor als auch nach der Anmeldung bei einer mobilen App oder Website verfolgt. Sie können dieses Objekt auch verwenden, um die von einem Drittanbieter verwendeten Bezeichner zu Ihren Unternehmensnutzer:innen hinzuzufügen, um Ihre Daten extern einfacher abzugleichen.

Das Nutzer-Alias-Objekt besteht aus zwei Teilen: einem `alias_name` für den Bezeichner selbst und einem `alias_label`, das den Typ des Alias angibt. Nutzer:innen können mehrere Aliasse mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`.

Dieses Objekt wird häufig in allen unseren Endpunkten und oft auch in anderen Objekten verwendet.

## Objektstruktur {#object-body}

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

| Feld | Datentyp | Beispiel | Beschreibung |
|---|---|---|---|
| `alias_name` | String | `john_doe_123` | Ein eindeutiger Bezeichner für die:den Nutzer:in, z. B. eine ID aus einem Drittanbietersystem. Dieser Wert darf nicht leer sein und muss 236 Bytes oder weniger umfassen. |
| `alias_label` | String | `crm_id` | Ein nicht leerer angepasster String, der den Alias-Typ definiert. Dieser Wert ist nicht auf bestimmte Optionen beschränkt. Sie können jede sinnvolle Bezeichnung verwenden, z. B. `email_id`, `amplitude_id`, `salesforce_lead_id` oder einen anderen Wert, der zu Ihrem Anwendungsfall passt. Dieser Wert muss 236 Bytes oder weniger umfassen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }

### Beispiel {#example}

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "crm_id"
  },
  "external_id": "user_456"
}
```

In diesem Beispiel ist `crm_id` eine angepasste Bezeichnung, die angibt, dass der Alias einen CRM-System-Bezeichner darstellt.

### Weiteres Beispiel {#additional-example}

```json
{
  "user_alias": {
    "alias_name": "a9f3c102",
    "alias_label": "amplitude_id"
  }
}
```

In diesem Beispiel ist `amplitude_id` ein möglicher Bezeichnungswert. Sie können auch Bezeichnungen wie `email_id` oder `salesforce_lead_id` oder eine andere angepasste Bezeichnung verwenden, die zu Ihrem Bezeichnerschema passt.
---
nav_title: Kickbox
article_title: Kickbox
alias: /partners/kickbox/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Kickbox, einer Plattform zur E-Mail-Verifizierung, mit der Sie E-Mail-Listen validieren oder die Verifizierung in Ihre Anwendung integrieren können."
page_type: partner
search_tag: Partner
---

# Kickbox

> [Kickbox](https://kickbox.com/) ist eine All-in-One-Plattform zur E-Mail-Verifizierung, die mit den Features, Integrationen und Sicherheitsfunktionen ausgestattet ist, die Sie benötigen, um Ihre E-Mail-Daten sauber und zustellbar zu halten. Die Integration von Kickbox verbessert die Zustellbarkeit Ihrer Braze Campaigns, indem die E-Mail-Verifizierung von Kickbox verwendet wird, um unzustellbare und minderwertige E-Mail-Adressen zu identifizieren, bevor Sie auf „Senden“ klicken.

Mit Kickbox können Sie die Qualität der E-Mail-Adressen Ihrer Nutzer:innen in dem Moment überprüfen, in dem ein Nutzerprofil in Braze aktualisiert wird. Dies wird durch einen dedizierten Canvas- oder Campaign-Workflow erreicht, der durch die Belegung des Feldes `email` eines Profils getriggert wird.

Das Canvas oder die Campaign sendet einen Webhook an Kickbox, der die E-Mail-Adresse der Nutzer:innen weitergibt. Kickbox validiert die E-Mail-Adresse und verwendet den Braze-REST-API-Endpunkt, um das Nutzerprofil mit einem angepassten Attribut zu aktualisieren, das die Qualität beschreibt.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Kickbox-Konto | Für die Nutzung dieser Integration ist ein aktives Kickbox-Konto erforderlich. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel** erstellt werden. |
| Zugriff auf die Integration anfordern | Bitten Sie das Kickbox-Support-Team, Ihnen Zugriff auf die Braze-Integration zu gewähren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Um Kickbox zu integrieren, folgen Sie den Schritten unter [Integration mit Braze](https://docs.kickbox.com/docs/integrating-with-braze#/).

## Anwendungsfälle {#use-cases}

### Massenverifizierung {#bulk-verification}

Sie können Ihre gesamte Liste auch alle paar Monate oder vierteljährlich überprüfen, um sich vor E-Mails zu schützen, die durch Churn verloren gehen, oder vor Listen, die sich im Laufe der Zeit verschlechtern und Ihre Zustellbarkeit langsam herabsetzen.

Dazu müssen Sie, wie von Kickbox beschrieben, die **Eingangseinstellungen** des Workflows ändern. Anstatt **Aktionsbasierte Zustellung** auszuwählen, wählen Sie **Geplant**. Wählen Sie dann einen Zeitplan, zu dem Ihre Liste auf einmal überprüft werden soll.

### Verifizierte Segmente erstellen {#create-verified-segments}

Die angepassten Attribute von Kickbox haben ein einheitliches Schema, das den folgenden Beispielen entspricht.

{% raw %}
```json
   {
  "attributes": [
    {
      "email": "example1@kickbox.com",
      "_update_existing_only": true,
      "success": true,
      "code": null,
      "message": null,
      "result": "deliverable",
      "reason": "accepted_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": null,
      "sendex": 1,
      "user": "example1",
      "domain": "kickbox.com"
    },
    {
      "email": "example2@gamil.com",
      "_update_existing_only": true,
      "success": true,
      "code": "44312",
      "message": "SMTP verification",
      "result": "undeliverable",
      "reason": "rejected_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": "example2@gmail.com",
      "sendex": 0.23,
      "user": "example2",
      "domain": "gamil.com"
    }
  ]
}
```
{% endraw %}

Das bedeutet, dass Sie Zielgruppen-Segmente mit verifizierten E-Mail-Adressen erstellen können, sodass Ihre Campaigns und Canvases eine höhere Zustellerfolgsrate haben und Ihr Ruf bei den ESPs geschützt wird.

Gehen Sie dazu folgendermaßen vor:

1. Gehen Sie in Braze zu **Zielgruppe** > **Segments** > **Segment erstellen**.
2. Fügen Sie im Abschnitt **Filtergruppe** den Filter **Angepasstes Attribut** hinzu und wählen Sie in der Dropdown-Liste „result“ aus.

Je nach Anwendungsfall kann es sinnvoll sein, ein Segment zu erstellen, in dem das angepasste Kickbox-Attribut „result“ in einem Nutzerprofil vorhanden ist oder dessen Wert gleich „deliverable“ ist. Dieser Filter kann für sich allein verwendet werden, um ein Segment zu erstellen, oder er kann zu einem Teil aller zukünftigen Segmente gemacht werden, um alle darin enthaltenen Nutzer:innen zu validieren.
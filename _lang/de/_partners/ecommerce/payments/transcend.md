---
nav_title: Transcend
article_title: Transcend
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Transcend, einer Datenschutz-Infrastrukturplattform, die Braze-Nutzer:innen dabei hilft, die Erfüllung von Anfragen betroffener Personen zu automatisieren."
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcend ist ein Unternehmen für Datenschutz-Infrastruktur, das es Unternehmen einfach macht, ihren Nutzer:innen die Kontrolle über ihre Daten zu geben, indem es automatisch Anfragen betroffener Personen innerhalb von Unternehmen über alle ihre Datensysteme und Anbieter hinweg erfüllt.

_Diese Integration wird von Transcend gepflegt._

## Über die Integration {#about-the-integration}

Die Partnerschaft von Braze und Transcend hilft Nutzer:innen bei der Automatisierung von Datenschutzanfragen durch die Orchestrierung von Daten über Dutzende von Datensystemen hinweg und unterstützt Teams bei der Einhaltung von Vorschriften wie DSGVO und CCPA. Transcend stellt Endnutzer:innen ein Control Panel oder Privacy Center zur Verfügung, das unter `privacy.\<company\>.com` gehostet wird. Dort können Nutzer:innen ihre Datenschutzeinstellungen verwalten, ihre Daten exportieren oder löschen.

## Voraussetzungen {#prerequisites}

| Anforderungen | Beschreibung |
|---|---|
| Transcend-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Transcend-Konto](https://app.transcend.io/) mit Admin-Rechten. |
| Braze-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit den Berechtigungen `users.delete, users.alias.new, users.export.ids, email.unsubscribe,` und `email.blacklist`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Transcend ermöglicht es Ihnen, in Übereinstimmung mit den Datenschutzbestimmungen programmatisch auf Nutzer:innen in der Braze-Plattform zuzugreifen, sie zu löschen und von der Kommunikation abzumelden.

### 1. Schritt: Einrichten der Braze-Integration {#step-1-set-up-the-braze-integration}
Um loszulegen, melden Sie sich bei [Transcend](https://app.transcend.io/login) an.
1. Navigieren Sie zu **Data Map > Add Data Silo > Braze** und wählen Sie den Button **Connect**.<br><br>
2. Wenn Ihr Konto eingerichtet ist, melden Sie sich unter einer der entsprechenden URLs an: `https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`.<br> Verwenden Sie die folgende [Tabelle]({{site.baseurl}}/api/basics/#endpoints), um herauszufinden, welche Subdomain Sie auf der Grundlage Ihrer Dashboard-URL angeben sollten.<br><br>
3. Wenn Sie verbunden sind, navigieren Sie zum Tab **Privacy Center** in Transcend. Hier müssen Sie die Daten in Braze auf Ihre Datenpraktiken abbilden. Erstellen Sie dazu eine neue Kategorie und eine neue Datenerfassung mit der entsprechenden Namenskonvention (z. B. „Mailinglisten oder Kundenprofil or Nutzerprofil“). Wenn Sie fertig sind, wählen Sie **Publish**.<br><br>
4. Navigieren Sie zurück zu Ihrer Data Map und wählen Sie das Braze-Daten-Silo aus. Erweitern Sie **Manage Datapoints** und wählen Sie die Sammlungsbezeichnung (Kategorie), die Sie im vorherigen Schritt erstellt haben, aus der Dropdown-Liste aus. Sie können auch wählen, welche Datenaktionen (z. B. Zugriff oder Löschung) für welche Datenpunkte aktiviert sind. <br><br>
5. Erweitern Sie als Nächstes, während Sie sich noch im Braze-Daten-Silo befinden, **Manage Identifiers**. Markieren Sie die entsprechenden Kästchen für die Bezeichner, die Sie aktivieren möchten. Wenn Sie z. B. möchten, dass Transcend Nutzer:innen nach ihrer E-Mail-Adresse sucht, aktivieren Sie das Kästchen für den E-Mail-Adress-Bezeichner.

{% alert note %}
Wenn Bezeichner nicht korrekt aktiviert sind, kann Transcend Anfragen für bestimmte Nutzer:innen möglicherweise nicht bearbeiten.
{% endalert %}

### 2. Schritt: Anfragen testen {#step-2-test-requests}
Transcend empfiehlt, Anfragen über Ihre Data Map zu testen, bevor Sie mit der Verarbeitung von Anfragen von Endnutzer:innen beginnen.
1. Gehen Sie in Transcend zu **Privacy Center** und wählen Sie **View your Privacy Center**.<br><br>
2. Wählen Sie in Ihrem **Privacy Center** die Option **Take Control** und dann **Download my data**. Geben Sie Ihre E-Mail-Adresse ein oder melden Sie sich an, um sich vor dem Absenden der Anfrage zu authentifizieren.<br><br>
3. Prüfen Sie Ihre E-Mail auf eine Nachricht von Transcend. Sie werden aufgefordert, auf einen Verifizierungslink zu klicken, um die Anfrage zu bestätigen.<br><br>
4. Navigieren Sie als Nächstes zurück zum **Admin**-Dashboard, gehen Sie zum Tab **Incoming Requests** und wählen Sie Ihre Anfrage aus. Kontaktieren Sie Transcend unter [support@transcend.io](mailto:support@transcend.io), wenn Sie die Anfrage hier nicht sehen.<br><br>
5. Nachdem Sie auf Ihre Anfrage geklickt haben, navigieren Sie zum Tab **Data Silos** und wählen Sie **Braze** aus. Prüfen und bestätigen Sie die zurückgegebenen Daten.<br><br>
6. Navigieren Sie schließlich zum Tab **Report** und klicken Sie auf **Approve and Send**. Sie sollten den Bericht an die E-Mail-Adresse erhalten, die Sie bei der Anfrage angegeben haben.

## Braze-Integration entfernen {#remove-the-braze-integration}
So entfernen Sie das Braze-Daten-Silo aus Ihrer Transcend Data Map:
1. Navigieren Sie zu Ihrer **Data Map** und klicken Sie auf **Braze**. <br><br>
2. Erweitern Sie am unteren Rand des Bildschirms **Remove Braze** und klicken Sie auf **Remove Silo**. Sie werden aufgefordert zu bestätigen, dass Sie das Silo entfernen möchten. Klicken Sie auf **Ok**. <br><br>
3. Vergewissern Sie sich, dass das Silo entfernt wurde, indem Sie zurück zu Ihrer Data Map navigieren.
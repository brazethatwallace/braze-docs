---
nav_title: Justuno
article_title: Justuno
description: "Erfahren Sie, wie Sie Justuno mit Braze integrieren können, damit Sie Kundendaten auf beiden Plattformen nutzen können, um personalisierte Erlebnisse für alle Zielgruppen zu schaffen."

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> [Justuno](https://www.justuno.com/) ermöglicht es Ihnen, mit dynamischen Segmenten vollständig optimierte Besuchererlebnisse für alle Ihre Zielgruppen zu schaffen und bietet das fortschrittlichste verfügbare Targeting&#8212;und das alles, ohne die Geschwindigkeit der Website zu beeinträchtigen oder den Entwicklungsaufwand zu erhöhen. Analysieren Sie Konversionsraten, indem Sie angepasste Analytics wie die Anzahl der erstellten Profile, die beeinflusste Rate wiederkehrender Besucher:innen und die Seiten pro Sitzung anzeigen, um einen Marketing-Vorteil in Ihrer Branche zu erhalten. Justuno ermöglicht es Ihnen, den Umsatz pro Besucher:in zu steigern, sinnvolles Customer-Engagement aufzubauen und Ihr Geschäft auszubauen. Optimieren Sie die gesamte Zielgruppen-Journey End-to-End mit einer vernetzten Plattform.

## Anwendungsfälle {#use-cases}

Braze erlaubt es jedem Marketer, beliebige Datenmengen aus beliebigen Quellen zu sammeln und zu verarbeiten, sodass Sie von einer Plattform aus kreativ und kanalübergreifend in Echtzeit mit Ihren Kund:innen in Kontakt treten können.

Die Integration von Justuno und Braze bietet Ihnen das Beste aus beiden Welten. Sie können die in Braze gespeicherten Kundendaten mit den in Justuno gespeicherten Besucher- und Kundendaten kombinieren und personalisierte Erlebnisse für alle Zielgruppen schaffen. Dies erhöht die Effektivität Ihrer Marketingkampagnen und Ihres Customer-Engagements.

## Voraussetzungen {#prerequisites}

| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den Berechtigungen `users.track` und `custom_attributes.get`.<br><br>Dieser kann im Braze-Dashboard unter **Settings** > **API Keys** erstellt werden. |
| Braze-REST-Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration von Justuno mit Braze {#integrating-justuno-with-braze}

### 1. Schritt: Angepasste Attribute in Braze erstellen {#step-1-create-custom-attributes-in-braze}

Um Nutzer:innen-Attribute von Justuno mit Braze zu synchronisieren, müssen Sie diese Attribute in Braze erstellen, falls Sie dies nicht bereits getan haben. Gehen Sie dazu zu **Data Settings** > **Custom Attributes** und erstellen Sie dann Ihre angepassten Attribute. Eine vollständige Anleitung finden Sie unter [Angepasste Attribute in Braze verwalten]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).

### 2. Schritt: Die Braze-App zu Justuno hinzufügen {#step-2-add-the-braze-app-to-justuno}

#### Schritt 2.1: Zu Ihrem Konto hinzufügen {#step-21-add-it-to-your-account}

Um die Braze-App zu Ihrem Justuno-Konto hinzuzufügen, gehen Sie zu **Account Settings** > **Apps**, suchen Sie dann nach der Braze-App und wählen Sie sie aus.

![Die Seite „Apps verbinden“ in Justuno mit der Braze-App in der Liste der Suchergebnisse.]({% image_buster /assets/img/justuno/search-for-braze.png %})

Geben Sie den API-Schlüssel und die Basis-URL ein, [die Sie zuvor erstellt haben](#prerequisites), und wählen Sie dann **Connect**.

![Das Braze-Authentifizierungs-Popup-Fenster, in dem nach einem Braze-API-Schlüssel und der Basis-URL gefragt wird.]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### Schritt 2.2: Zu Ihrem Workflow hinzufügen {#step-22-add-it-to-your-workflow}

Um die Braze-App zu Ihrem [Justuno-Workflow](https://hub.justuno.com/knowledge/workflows-overview) hinzuzufügen, ziehen Sie die Aktion **Sync to App** per Drag-and-Drop in Ihren Workflow und wählen Sie dann **Select App** > **Braze**.

![Die Option „Select App“ befindet sich bei der Aktion „Sync to App“.]({% image_buster /assets/img/justuno/select-app.png %}){: style="max-width:45%;"}

### 3. Schritt: Ihre Braze-Abo-Gruppen verbinden {#step-3-connect-your-braze-subscription-groups}

Um Profildaten von Justuno an eine bestimmte E-Mail- oder SMS-Abo-Gruppe von Braze zu senden, müssen Sie deren ID in der Braze-App in Ihrem Justuno-Workflow hinzufügen.

| ID-Typ                          | Erforderlich? | Beschreibung                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| Braze-SMS-Abo-Gruppen-ID  | Ja       | Diese ID wird verwendet, um SMS-Einwilligungen von Nutzer:innen-Profilen zu erfassen. Wenn in Justuno keine ID eingegeben wird, haben die Profile keine Einwilligung, wenn Justuno dieses Profil an Braze überträgt. |
| Braze-E-Mail-Abo-Gruppen-ID | Nein        | Wenn diese ID nicht in Justuno eingegeben wird, sendet Justuno die Profildaten an Braze als Nutzer:in ohne zugehörige Abo-Gruppen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="3. Schritt: Ihre Braze-Abo-Gruppen verbinden" }

#### Schritt 3.1: Die IDs in Braze finden {#step-31-locate-the-ids-in-braze}

So finden Sie diese IDs im Braze-Dashboard:

1. Gehen Sie zu **Audience** > **Subscriptions**.
2. Notieren Sie sich für jede Abo-Gruppe die ID, die sich in der ID-Spalte befindet.

#### Schritt 3.2: Die IDs zur Braze-App hinzufügen {#step-32-add-the-ids-to-the-braze-app}

Öffnen Sie in Ihrem Justuno-Workflow die Braze-App und geben Sie dann die IDs für die einzelnen Abo-Gruppen ein.

![Die Braze-App geöffnet in einem Justuno-Workflow mit der Option, E-Mail- und SMS-Abo-Gruppen-IDs hinzuzufügen.]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### 4. Schritt: Ihre Attribute konfigurieren {#step-4-configure-your-attributes}

Die folgenden Attribute werden automatisch von Justuno mit Braze synchronisiert:

- E-Mail
- Telefon
- Vorname
- Nachname
- Sprache
- Geschlecht
- Land

Um zusätzliche Attribute zu synchronisieren:

1. Wählen Sie in der Braze-App innerhalb Ihres Workflows **Sync Another Property**.
    ![Die Braze-App geöffnet in einem Justuno-Workflow mit der Option „Sync Another Property“.]({% image_buster /assets/img/justuno/sync-another-property.png %}){: style="max-width:55%;"}
2. Wählen Sie die Braze-Attribute, die Sie synchronisieren möchten.
3. Gleichen Sie die Eigenschaften in Justuno mit ihren Entsprechungen in Braze ab (z. B. soziale Handles, Geburtstag, Einkaufspräferenzen, Antworten auf Umfragen und ähnliches). Beachten Sie, dass diese Eigenschaften als Zero-Party-Daten oder First-Party-Daten betrachtet werden. Weitere Informationen finden Sie unter [Justuno: Datenerfassung für Besucher](https://www.justuno.com/guides/zero-first-party-data/).
4. Wählen Sie im Workflow-Builder die Option **Save**, **Preview** oder **Publish** für Ihren Workflow.
    ![Das Menü „Publish“ mit den Optionen zum Speichern, zur Vorschau oder zum Anzeigen des Versionsverlaufs.]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## Wissenswertes {#things-to-know}

- Sie müssen die Abo-Gruppen-ID manuell in den App-Einstellungen eingeben.
- Die folgenden Braze-Datentypen werden **nicht unterstützt**: Objekt, Objekt-Array.
- Eine implizite SMS-Einwilligung wird erteilt, wenn das SMS-Einwilligungsfeld von Justuno nicht verwendet wird.
- Die explizite SMS-Einwilligung wird berücksichtigt, wenn das Justuno-Design das Einwilligungsfeld enthält.
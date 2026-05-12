---
nav_title: Digioh
article_title: Digioh
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Digioh, einer Umfrageplattform für die Erstellung von Pop-ups, Formularen, Umfragen und Kommunikationspräferenzzentren, die das Engagement in Ihren Braze-Campaigns fördern."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/) unterstützt das Listenwachstum, die Erfassung von First-Party-Daten und die Verwendung dieser Daten in Braze-Campaigns.

_Diese Integration wird von Digioh gepflegt._

## Über die Integration {#about-the-integration}

Mit der Integration von Braze und Digioh können Sie per Drag-and-Drop Formulare, Pop-ups, Präferenzzentren, Landing-Pages und Umfragen erstellen, die Sie mit Ihren Kund:innen verbinden. Digioh hilft Ihnen bei der Einrichtung der Integration und kann Ihre erste Campaign erstellen, entwerfen und starten.

![„Erstellen Sie mit Digioh flexible E-Mail- und Kommunikations-Präferenzzentren“]({% image_buster /assets/img/digioh/pref_pop_examples.png %}){: style="border:0"}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Digioh-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Digioh-Konto](https://www.digioh.com/). |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-API-`/users/track/`-Endpunkt | Ihre REST-Endpunkt-URL mit den angehängten `/users/track/`-Details. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab.<br><br>Wenn Ihr REST-API-Endpunkt z. B. `https://rest.iad-01.braze.com` lautet, wird Ihr `/users/track/`-Endpunkt `https://rest.iad-01.braze.com/users/track/` sein. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Um Digioh zu integrieren, müssen Sie zunächst den Braze-Konnektor konfigurieren. Anschließend müssen Sie die Integration auf eine Lightbox (Widget) anwenden. Besuchen Sie [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/), um mehr über die Grundlagen der Integration zu erfahren.

### 1. Schritt: Digioh-Integration erstellen {#step-1-create-digioh-integration}

Klicken Sie in Digioh auf den Tab **Integrations** und dann auf den Button **New Integration**. Wählen Sie **Braze** aus dem Dropdown **Integration** aus und benennen Sie die Integration.

![„Wählen Sie die richtige Integration aus dem Dropdown aus“]({% image_buster /assets/img/digioh/2.png %}){: style="max-width:50%;"}

Geben Sie als Nächstes den Braze-REST-API-Schlüssel und Ihren Braze-API-`/users/track/`-Endpunkt ein.

Verwenden Sie abschließend den Abschnitt „Felder zuordnen“, um weitere angepasste Felder neben E-Mail und Name zuzuordnen. Das folgende Code-Snippet zeigt eine Beispiel-Payload. Wenn Sie fertig sind, wählen Sie **Create Integration**.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### 2. Schritt: Eine Digioh-Lightbox erstellen {#step-2-create-a-digioh-lightbox}

Verwenden Sie den Digioh-[Design-Editor](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/), um eine Lightbox (Widget) zu erstellen. <br>
Möchten Sie eine Galerie sehen, wie Sie den Design-Editor nutzen können? Besuchen Sie die Digioh-[Themengalerie](https://www.digioh.com/theme-gallery).

### 3. Schritt: Integration anwenden {#step-3-apply-integration}

Um diese Integration auf eine Digioh-[Lightbox](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) anzuwenden, navigieren Sie zur Seite **Boxes** und wählen Sie den Link **Add** oder **Edit** in der Spalte **Integrations**. Dies kann auch über den Bereich **Integration** des Editors hinzugefügt werden.

![„Integration zu einer Lightbox hinzufügen“]({% image_buster /assets/img/digioh/3.png %}){: style="max-width:90%"}

Wählen Sie hier **Add Integration**, wählen Sie die gewünschte Integration aus und klicken Sie auf **Save**. Digioh leitet Ihre erfassten Leads nun in Realtime an Braze weiter.
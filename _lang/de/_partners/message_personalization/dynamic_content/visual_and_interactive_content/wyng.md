---
nav_title: Wyng
article_title: Wyng
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Wyng, einer Zero-Party-Datenplattform zur Erfassung, Nutzung und Integration von Kundenpräferenzen und -attributen über Micro-Experiences, Kundenpräferenzportale und eine API-Plattform."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng](https://wyng.com/) bietet Tools zum Aufbau interaktiver digitaler Erlebnisse (Quiz, Präferenzzentren, Aktionen), die Verbraucher:innen in Schlüsselmomenten einbinden, Präferenzen und andere Zero-Party-Daten erfassen und in Echtzeit personalisieren.

_Diese Integration wird von Wyng gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Wyng erlaubt es Ihnen, Zero-Party-Daten, die über Wyng-Erlebnisse gewonnen wurden, zu nutzen, um Interaktionen in Braze Campaigns und Braze-Canvas zu personalisieren. Wyng kann auch ein Präferenzzentrum betreiben, sodass Verbraucher:innen die Daten und Präferenzen (einschließlich der Kommunikationspräferenzen) kontrollieren können, die sie mit Ihrer Marke teilen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Wyng-Konto | Um diese Partnerschaft nutzen zu können, benötigen Sie ein Wyng-Konto. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Braze-Integration verbinden {#step-1-connect-the-braze-integration}

Gehen Sie in Wyng zu [**Integrations**](https://wyng.com/dashboard/integrations/) und wählen Sie den Tab **Add**. Bewegen Sie dann den Mauszeiger über **Braze** und klicken Sie auf **Connect** für die Integration.

![Die Braze-Partner-Kachel in der Wyng-Plattform.]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### 2. Schritt: Braze-Konnektor konfigurieren {#step-2-configure-the-braze-connector}

1. Geben Sie in dem sich öffnenden Konfigurationsfenster Ihren Braze REST-API-Schlüssel an.
![Ein Bild, das zeigt, wie die Eingabeaufforderung für die Zugangsdaten aussieht.]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. Wählen Sie dann aus der Dropdown-Liste die Wyng-Campaign aus, die Sie mit Braze teilen möchten.![Ein Bild des Braze-Konnektors, der Sie auffordert, eine bestehende Wyng-Campaign auszuwählen, die Sie mit Braze teilen möchten.]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. Als Nächstes müssen Sie Abos, Attribut- und Ereignisobjekte sowie angepasste Events einrichten.<br><br>
- **Einrichtung von Abos (erforderlich)**<br>
Um Nutzer:innen für Abo-Gruppen zu abonnieren, klicken Sie auf **Add Subscription** und fügen Sie den Namen und die ID Ihrer Abo-Gruppe hinzu. Um mehrere Gruppennamen und IDs hinzuzufügen, klicken Sie erneut auf den Button **Add Subscription**.<br>![Ein Bild, das Sie auffordert, den Namen und die ID einer Abo-Gruppe einzugeben.]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **Nutzer:innen-Tracking einrichten**<br>
Klicken Sie auf **Add custom property**, um Attribut- und Ereignisobjektpaare hinzuzufügen, die an den Endpunkt `/users/track` gesendet werden sollen. Verwenden Sie diese Option, um fest kodierte Attributwerte für jede Datentransaktion hinzuzufügen, die für die Integration gesendet wird. Um mehrere Eigenschaften hinzuzufügen, klicken Sie erneut auf den Button **Add custom property**.<br>![Ein Bild, das Sie auffordert, angepasste Attributeigenschaften hinzuzufügen.]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **Angepasstes Event senden**<br>
Optional können Sie **Sending custom event** aktivieren. Falls aktiviert, sollten Sie den Ereignisnamen und die entsprechende App-ID angeben.<br>![Ein Bild, das Sie auffordert, angepasste Events zu senden, falls erforderlich.]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. Schließlich müssen Sie die Wyng-Felder auf der Grundlage Ihres Anwendungsfalls den Braze-API-Feldern zuordnen. Klicken Sie auf **Select a field**, um die zuzuordnenden Felder auszuwählen, und klicken Sie anschließend auf **Save**, um Ihre Integration zu speichern. Nach dem Speichern finden Sie diese zugeordneten Felder unter **Integrations > Manage**.
![Ein Beispiel für die verschiedenen Wyng-Felder, die Sie bestimmten Braze-Feldern zuordnen können.]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![Eine Liste der verfügbaren Synchronisationsfelder.]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### 3. Schritt: Integration testen {#step-3-test-your-integration}

Testen Sie in Wyng das Absenden des Formulars in Ihrer Wyng-Campaign. Sie können es auch in der Vorschau-Campaign einreichen, wenn Sie der Hauptproduktions-Campaign keinen Datensatz hinzufügen möchten. Sie sollten im **Integration**-Dashboard eine erfolgreiche Transaktion sehen.

## Verwendung dieser Integration {#using-this-integration}

Sobald der Datenkonnektor eingerichtet ist, können alle in Wyng erstellten und zu Braze hinzugefügten Felder wie jedes andere Datenfeld verwendet werden, um Campaigns zu triggern, Zielgruppen zu segmentieren oder personalisierte Inhalte einzuspeisen.

Die Anwendungsmöglichkeiten sind breit gefächert, und spezifische Fragen können Sie an [contact@wyng.com](mailto:contact@wyng.com) oder an Ihre:n zuständige:n Account Manager:in:in richten.

## Fehlerbehebung {#troubleshooting}

### Fehlgeschlagene Übermittlung {#failed-submission}

Im Falle einer fehlgeschlagenen Übermittlung beim Senden von Daten an Braze klicken Sie auf den Link **View Log**, um die fehlgeschlagene Übermittlung und die zugehörige Fehlermeldung zu überprüfen.

![Der Link „View Log“ befindet sich unter der Überschrift „Actions“.]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

Auf der Protokollseite werden die fehlgeschlagene Übermittlung, die Anzahl der Wiederholungsversuche, die Daten der Übermittlung, der Fehler und ein Link zum erneuten Senden der Übermittlung angezeigt.

![Ein Beispiel dafür, was eine fehlgeschlagene Übermittlung anzeigt.]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

Im Abschnitt **View Error** werden der Fehlercode und einige zusätzliche Informationen über die Fehlerursache angezeigt. Sie können dann den Fehlercode mit Braze abgleichen, um die Ursache zu ermitteln.

![Ein Beispiel für ein Fehlerprotokoll auf der Wyng-Plattform.]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

Wenn Sie weitere Fragen haben, wenden Sie sich bitte an den Wyng-Support ([support@wyng.com](mailto:contact@wyng.com)), um Hilfe zu erhalten.
---
nav_title: Copy Pastd
article_title: Copy Pastd
alias: /partners/copy_pastd/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Copy Pastd, einem Drag-and-Drop-E-Mail-Builder, der Liquid-basierte Content Blocks und Templates direkt in Ihren Braze-Workspace überträgt."
page_type: partner
search_tag: Partner
---

# Copy Pastd

> [Copy Pastd](https://copypastd.com/) Building Blocks ist ein Drag-and-Drop-E-Mail-Builder, der Liquid-basierte Content Blocks und vollständige Templates direkt in Ihren Braze-Workspace überträgt. Einmal entwerfen, mit Braze synchronisieren und dieselben Komponenten in Campaigns, Canvases und getriggerten Flows wiederverwenden – ohne jedes Mal HTML neu erstellen zu müssen.

_Diese Integration wird von Copy Pastd gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Copy Pastd ermöglicht es Ihnen, E-Mails in Building Blocks zu erstellen – einem gehosteten E-Mail-Builder, der Braze-native Ausgaben mit sauberem Liquid, Content-Block-Referenzen und Templates erzeugt, die sich ohne Konvertierung in jede Campaign oder jeden Canvas einfügen lassen.

Sie können eine E-Mail aus wiederverwendbaren Blöcken zusammenstellen, sie mit einem Klick an Braze übertragen und darauf vertrauen, dass dieselben Markenstile, Komponenten und dynamischen Inhalte bei jedem Versand konsistent gerendert werden. Das Ergebnis: weniger handcodierte Templates, weniger Zeitaufwand für die Erstellung und den Versand von E-Mails und eine zentrale Bibliothek, die sich überall aktualisiert, wenn Änderungen vorgenommen werden.

## Voraussetzungen {#prerequisites}

Folgendes ist für die Nutzung dieser Integration erforderlich:

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Copy-Pastd-Konto | Erforderlich für die Nutzung von Building Blocks. Registrieren Sie sich unter [copypastd.com](https://copypastd.com). Jede:r geschäftskunden erhält einen Workspace, eine Stylesheet-Bibliothek, fünf Builder-Plätze und eine Block-Bibliothek. |
| Braze-REST-API-Schlüssel für E-Mail-Templates | Ein API-Schlüssel mit den Berechtigungen `templates.email.create`, `templates.email.update` und `templates.email.list`.<br><br>Erstellen Sie den Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| Braze-REST-API-Schlüssel für Content Blocks | Ein API-Schlüssel mit den Berechtigungen `content_blocks.create`, `content_blocks.update`, `content_blocks.info` und `content_blocks.list`.<br><br>Erstellen Sie den Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| Braze-REST-API-Schlüssel für Kataloge (optional) | Ein API-Schlüssel mit Lesezugriff auf `catalogs.get`, `catalogs.get_item` und `catalogs.get_selections`. Nur erforderlich, wenn Sie Blöcke an Braze-Kataloge binden möchten. |
| Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL Ihrer Instanz ab. Building Blocks wählt den Endpunkt automatisch basierend auf dem von Ihnen gewählten Cluster aus. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

* **Markenkonsistentes Erstellen im großen Maßstab.** Wenden Sie ein Building-Blocks-Stylesheet auf jedes Template an, und Farben, Schriftarten, Button-Stile und Padding-Skalierung werden über Hunderte von E-Mails hinweg identisch gerendert. Wenn sich die Marke ändert, aktualisieren Sie das Stylesheet einmal und synchronisieren erneut, um das Update auf alle Ihre E-Mails gleichzeitig auszurollen.
* **Connected-Content- und kataloggebundene Produkt-Templates.** Binden Sie E-Mail-Block-Felder direkt an Ihre [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)-Endpunkte und [Braze-Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs) innerhalb des Builders. Verwenden Sie dasselbe Template für neue Produkteinführungen, saisonale Kollektionen oder Content-Aktualisierungen wieder, ohne Liquid anfassen zu müssen.
* **Self-Service-E-Mail-Produktion für nicht-technische Marketer.** Erstellen Sie eine vollständige E-Mail aus genehmigten Blöcken – einschließlich Liquid-Personalisierung und -Logik – und übertragen Sie sie zur Überprüfung an Braze, ohne dass Entwickler:innen HTML oder Liquid schreiben oder Qualitätssicherung durchführen müssen.
* **Zentrale Header und Footer, mit einem Klick aktualisiert.** Erstellen Sie einen Header oder Footer einmal im Building-Blocks-Builder und übertragen Sie ihn an Braze. Jedes Template, das darauf verweist, bleibt synchron, sodass ein Logo-Tausch, eine Änderung des rechtlichen Texts oder ein neuer Social-Link nur ein einziges Update in Building Blocks erfordert, um in jeder E-Mail in Braze zu landen.
* **Zentralisierter Content über alle E-Mails hinweg.** Erstellen Sie einen Hero-, Footer- oder Promo-Card-Block einmal als Building-Blocks-Smart-Block. Aktualisieren Sie ihn, synchronisieren Sie, und jede E-Mail in Braze, die darauf verweist, übernimmt die Änderung beim nächsten Versand. Willkommens-Flows, wöchentliche Newsletter und getriggerte Journeys bleiben aktuell, ohne dass jede Campaign einzeln bearbeitet werden muss.
* **Gesperrte Templates für Mitwirkende im Self-Service.** Erstellen Sie Templates, sperren Sie ausgewählte Felder und laden Sie dann andere Teams ein, ihre eigenen E-Mails über eine Mitwirkenden-Oberfläche zu erstellen, ohne ihnen Zugriff auf nutzer:innenseitige Tools zu gewähren.

## Integration

### Schritt 1: Building Blocks mit Braze verbinden {#step-1-connect-building-blocks-to-braze}

{% alert note %}
Die Verbindung von Building Blocks mit Braze ist eine einmalige Einrichtung. Nachdem Ihre Zugangsdaten validiert wurden, speichert Building Blocks die Zugangsdaten für alle zukünftigen Synchronisierungen und Template-Übertragungen.
{% endalert %}

1. Melden Sie sich bei Building Blocks unter [blocks.copypastd.com](https://blocks.copypastd.com) an oder wählen Sie **Login** unter [copypastd.com](https://copypastd.com).
2. Wählen Sie im Dashboard **Set up your Braze connection**. (Diese Schaltfläche erscheint für Admins beim ersten Login und bis zur Fertigstellung. Sie können die Seite auch über **Team Settings** > **Connect** > **Braze API Keys** aufrufen.)
3. Wählen Sie Ihren Braze-Cluster aus dem Dropdown. Der passende REST-Endpunkt wird automatisch ausgefüllt.
4. Fügen Sie Ihren Templates-API-Schlüssel, Ihren Content-Blocks-API-Schlüssel und (optional) Ihren Katalog-API-Schlüssel in die entsprechenden Felder ein.
5. Wählen Sie **Validate and save**. Building Blocks ruft Braze auf, um zu bestätigen, dass die Schlüssel funktionieren und die Berechtigungsbereiche korrekt sind. Falls etwas fehlt, zeigt ein Inline-Fehler an, welcher Bereich falsch ist.

### Schritt 2: Ihre Bibliothek mit Braze synchronisieren {#step-2-sync-your-library-to-braze}

1. Nachdem die Schlüssel validiert wurden, wählen Sie **Sync now** im Einrichtungs-Modal. (Sie können jederzeit erneut synchronisieren über **Settings** > **Connect** > **Braze** > **Sync library**.) <br> Building Blocks überträgt Ihr Stylesheet und Ihre Blöcke als Braze Content Blocks in Ihren Braze-Workspace. Sie erscheinen in Braze unter Namen mit dem Präfix `CP_` (zum Beispiel `CP_Hero_1`) oder `cp_` für Stylesheets (zum Beispiel `cp_default_style`).
2. Nach Abschluss der Synchronisierung können Sie einzelne Templates aus dem Builder mit **Push to Braze** übertragen.

## Building Blocks anpassen {#customize-building-blocks}

### Schritt 1: Ihr Stylesheet einrichten {#step-1-set-up-your-stylesheet}

1. Navigieren Sie in Building Blocks zu **Settings** > **Build** > **Stylesheets**.
2. Bearbeiten Sie das Standard-Stylesheet oder erstellen Sie ein neues. Legen Sie Ihre Farbpalette (24 benannte Farben), Schriftarten (Google Fonts werden unterstützt), Button-Stile, Link-Stile, Radius und Padding-Skalierung fest.
3. Wählen Sie **Save**. Building Blocks generiert das Liquid für jeden Block, der dieses Stylesheet verwendet, neu.
4. Wählen Sie **Sync now**, um die aktualisierten Stile in Ihren Braze-Workspace zu übertragen.

### Schritt 2: Connected-Content-Endpunkte aktivieren (optional) {#step-2-enable-connected-content-endpoints-optional}

1. Navigieren Sie in Building Blocks zu **Settings** > **Connect** > **Connected Content endpoints**.
2. Fügen Sie die Endpunkt-URL hinzu, benennen Sie sie und speichern Sie. Building Blocks unterstützt neben dem Standard-JSON-Format auch ein Google-Sheets-Antwortformat.
3. Binden Sie im Builder ein beliebiges Text-, Bild- oder Link-Feld über das **Personalize**-Panel an eine Connected-Content-Variable. Das korrekte {% raw %}`{% connected_content %}`{% endraw %}-Liquid wird beim Export generiert.

### Schritt 3: An Braze-Kataloge binden (optional) {#step-3-bind-to-braze-catalogs-optional}

1. Navigieren Sie in Building Blocks zu **Settings** > **Connect** > **Catalogs**. Building Blocks liest Ihre Katalogliste mithilfe des Katalog-API-Schlüssels.
2. Öffnen Sie einen kompatiblen Block (zum Beispiel ein Produktraster).
3. Wählen Sie einen Katalog und eine Auswahl aus und ordnen Sie dann Block-Felder den Katalog-Artikelattributen zu.
4. Übertragen Sie das Template. Building Blocks gibt das korrekte {% raw %}`{% catalog_items %}`{% endraw %}- und {% raw %}`{% catalog_selection_items %}`{% endraw %}-Liquid aus, damit Braze es zum Sendezeitpunkt auflöst.

### Schritt 4: Ihre angepassten Braze-Attribute hinzufügen (optional) {#step-4-add-your-braze-custom-attributes-optional}

Building Blocks enthält die Standard-Braze-Nutzerattribute (`first_name`, `email`, `country` usw.). Um Blöcke an Ihre eigenen angepassten Attribute zu binden, importieren Sie diese einmalig in Building Blocks, und sie stehen in jedem **Personalize**-Dropdown zur Verfügung.

1. Navigieren Sie in Building Blocks zu **Team Settings** > **Connect** > **Custom Attributes**.
2. Importieren Sie Ihre angepassten Attribute mit einer der folgenden Methoden:
* **Massenimport (empfohlen).** Navigieren Sie in Braze zu **Data Settings** > **Custom Attributes** und wählen Sie **Export**. Laden Sie die CSV-Datei in Building Blocks hoch.
* **Attribute einzeln hinzufügen.** Geben Sie den Attributnamen ein (zum Beispiel `loyalty_tier`) und wählen Sie **Add**. Diese Methode ist nützlich, wenn Sie nur wenige Attribute hinzufügen oder ein neues Attribut zwischen Braze-Exporten ergänzen möchten.

Nach dem Speichern erscheinen Ihre angepassten Attribute im **Personalize**-Dropdown des Builders neben den Standardattributen. Beim Einfügen wird das korrekte {% raw %}`{{custom_attribute.${name}}}`{% endraw %}-Liquid beim Export gerendert, sodass Braze den Wert pro Empfänger:in zum Sendezeitpunkt auflöst.

## Die Integration verwenden {#use-the-integration}

### Schritt 1: Ein Template an Braze übertragen {#step-1-push-a-template-to-braze}

1. Öffnen Sie eine beliebige E-Mail im Building-Blocks-Builder.
2. Wählen Sie **Push to Braze** in der Aktionsleiste.
3. Wählen Sie den Workspace aus und bestätigen Sie. Building Blocks erstellt ein E-Mail-Template in Braze mit dem gerenderten Liquid.

Das Template erscheint in Braze unter **Templates und Medien** > **E-Mail-Templates**, benannt nach der E-Mail und dem ausgewählten Datum in den E-Mail-Einstellungen.

### Schritt 2: Das Template in einer Campaign oder einem Canvas verwenden {#step-2-use-the-template-in-a-campaign-or-canvas}

1. Erstellen Sie in Braze eine neue E-Mail-Campaign oder einen Canvas-Schritt.
2. Wählen Sie **Templates** und wählen Sie das Template, das Building Blocks übertragen hat.

Das Template enthält jede Building-Blocks-Referenz (Stylesheet, Content Blocks) als aktives {% raw %}`{{content_blocks.${...}}}`{% endraw %}-Liquid, sodass Aktualisierungen in Building Blocks ohne erneuten Import des Templates übernommen werden.

### Schritt 3: Content zentral aktualisieren {#step-3-update-content-centrally}

1. Bearbeiten Sie in Building Blocks den entsprechenden Block oder das Stylesheet.
2. Wählen Sie **Sync**, um den aktualisierten Content Block zurück an Braze zu übertragen.

Jede E-Mail in Braze, die darauf verweist (Evergreen, getriggert, Willkommens-Flows), übernimmt die neue Version beim nächsten Versand. Sie müssen nicht jede Campaign einzeln bearbeiten.

### Schritt 4: Content-Pools erstellen {#step-4-build-content-pools}

Content-Pools sind Tabellen mit Content-Zeilen, auf die E-Mails verweisen, anstatt statischen Text zu enthalten. Aktualisieren Sie den Pool in Building Blocks, und jede E-Mail in Braze, die ihn verwendet, liefert den neuen Content beim nächsten Versand aus. Verwenden Sie Content-Pools überall dort, wo derselbe Content über viele E-Mails hinweg aktuell bleiben muss – zum Beispiel in wöchentlichen Newslettern, Willkommens-Flows, Rückgewinnungs-Sequenzen, saisonalen Campaigns oder Post-Purchase-Journeys.

1. Wählen Sie in Building Blocks **Content** in der Hauptnavigation.
2. Wählen Sie **New Pool**. Geben Sie einen Namen an, der den Inhalt beschreibt (zum Beispiel Weekly Offers, Product Catalog, News Articles).
3. Wählen Sie den Block-Typ, den der Pool speist (zum Beispiel Hero, Grid, Card). Dadurch wird festgelegt, welche Felder für jede Zeile verfügbar sind.
4. Fügen Sie Zeilen hinzu. Jede Zeile ist ein Content-Element. Füllen Sie die Felder aus (Überschrift, Bild, CTA-Text, CTA-Link usw.).
5. Legen Sie die Prioritätsreihenfolge fest, indem Sie Zeilen nach oben oder unten ziehen. Schalten Sie jede Zeile aktiv oder inaktiv und legen Sie optionale Start- und Enddaten fest. Zum Sendezeitpunkt gewinnt die aktive Zeile mit der höchsten Priorität, deren Daten gültig sind.
6. Klicken Sie auf **Save**. Smart-Blöcke können jetzt auf diesen Pool verweisen.

### Schritt 5: Smart-Blöcke verwenden, um Pool-Content in Ihren E-Mails zu rendern {#step-5-use-smart-blocks-to-render-pool-content-in-your-emails}

Ein Smart-Block ist ein Block auf der Builder-Leinwand, der auf einen oder mehrere Content-Pools verweist, anstatt statischen Content zu enthalten. Zum Sendezeitpunkt rendert Braze die Pool-Zeile mit der höchsten Priorität, die aktiv und datumsgültig ist. Das exportierte Liquid übernimmt die Arbeit. Es ist kein zusätzliches Braze-Setup erforderlich.

1. Ziehen Sie in Building Blocks einen Smart-Block auf die Leinwand (jeder Block-Typ, der einen passenden Pool hat).
2. Öffnen Sie im Eigenschaften-Panel den Kaskaden-Editor.
3. Fügen Sie einen oder mehrere Content-Pools in Prioritätsreihenfolge hinzu. Dies ist die Wasserfall-Logik: Der erste Pool mit einer aktiven, datumsgültigen Zeile wird gerendert. Wenn er nichts Aktives hat, fällt der Smart-Block zum nächsten Pool durch, dann zum nächsten. Ein gängiges Muster ist Flash Sale > Weekly Offers > Evergreen Favorites, sodass immer etwas verfügbar ist.
4. Übertragen Sie das Template an Braze. Das exportierte Liquid enthält die vollständige Kaskade, sodass Braze die Pool-Priorität und Daten bei jedem Versand auswertet.

Ab jetzt aktualisieren Sie den Pool, nicht die E-Mail. Getriggerte Flows, Evergreen-Newsletter und saisonale Campaigns bleiben alle aktuell, solange der Pool aktuell ist.

Finden Sie Ihre hochgeladenen Building-Blocks-Templates in Braze unter **Templates und Medien** > **E-Mail-Templates**. Synchronisierte Stylesheets und Blöcke erscheinen unter **Templates und Medien** > **Content Blocks**.

## Hinweise {#considerations}

- **Eine Braze-Instanz pro Building-Blocks-Team-Space.** Jedes Building-Blocks-Team verbindet sich mit einer einzelnen Braze-Instanz. Kund:innen, die mehrere Workspaces betreiben (separate Marken, Regionen oder Umgebungen), können diese demselben Team hinzufügen, was das Teilen von Blöcken ermöglicht.
- **API-Schlüssel-Berechtigungen sind separat begrenzt.** Templates-Schlüssel und Content-Blocks-Schlüssel werden getrennt gehalten. Die Validierung schlägt schnell fehl, wenn einem Schlüssel ein erforderlicher Bereich fehlt, sodass Sie genau wissen, welche Berechtigung Sie in Braze hinzufügen müssen.
- **Content-Block-Namen sind mit Namensräumen versehen.** Building Blocks überträgt Content Blocks mit den Präfixen `CP_` (Blöcke) und `cp_` (Stylesheets), um Kollisionen mit direkt in Braze erstellten Content Blocks zu vermeiden.
- **Stylesheet-Änderungen aktualisieren jede E-Mail.** Stylesheets werden als einzelner Braze Content Block gerendert, auf den jedes Template verweist. Eine Änderung in Building Blocks aktualisiert jede E-Mail in Braze, die es verwendet, einschließlich bereits geplanter. Testen Sie Stylesheet-Änderungen in einem Entwurfs-Template, bevor Sie synchronisieren.
- **Katalogbindung ist schreibgeschützt.** Building Blocks liest Kataloge, um die Bindungs-UI zu befüllen. Es schreibt nicht in Braze-Kataloge. Die gesamte Katalogverwaltung erfolgt weiterhin im Braze-Dashboard.
- **Rate-Limits und Wiederholungsversuche.** Alle ausgehenden Anfragen respektieren die Rate-Limits von Braze mit exponentiellem Backoff, Jitter und Retry-After-Handling. Ein `User-Agent: partner-CopyPastd`-Header wird bei jedem Aufruf zur Partner-Attribution gesendet.
- **Es werden keine Nutzerdaten übertragen.** Building Blocks ist ein Content-Authoring-Tool. Es überträgt keine Nutzerattribute, Ereignisse, Käufe oder Segmentdaten an Braze und verbraucht keine Braze-Datenpunkte.

## Fehlerbehebung {#troubleshooting}

- **API-Schlüssel-Validierung schlägt fehl.** Überprüfen Sie, ob jeder Schlüssel die genauen Berechtigungen trägt, die unter „Voraussetzungen“ aufgeführt sind. Templates- und Content-Blocks-Bereiche werden separat geprüft. Wenn Sie einen Schlüssel in Braze neu generieren, fügen Sie den neuen Wert in Building Blocks ein und validieren Sie erneut.
- **REST-Endpunkt-Abweichung.** Templates- und Content-Blocks-Schlüssel müssen aus demselben Braze-Workspace stammen, und der REST-Endpunkt muss zum Cluster passen. Das Building-Blocks-Dropdown stellt dies für Sie ein – überprüfen Sie also die Cluster-Auswahl, wenn die Validierung fehlschlägt.
- **Push to Braze gibt einen Fehler zurück.** Öffnen Sie **Settings** > **Build** > **Activity log**, um den letzten Synchronisierungsversuch und die von Braze zurückgegebene Antwort zu sehen. Die meisten Fehler sind berechtigungsbezogen (fehlender Bereich) oder kontingentbezogen (Rate-Limit, wird automatisch wiederholt).
- **Content Block wird in Braze nicht aktualisiert.** Lösen Sie eine manuelle Neusynchronisierung über **Settings** > **Connect** > **Braze** > **Sync library** aus. Building Blocks führt einen Compare-and-Swap durch, sodass unveränderte Blöcke übersprungen werden.
- **Template verweist auf einen Content Block, der in Braze noch nicht existiert.** Übertragen Sie zuerst die Abhängigkeiten (Stylesheet, Smart-Blöcke) über **Sync library** und dann das Template.
- **Für alles andere.** Kontaktieren Sie Copy Pastd unter [help@copypastd.com](mailto:help@copypastd.com). Geben Sie Ihren Team-Namen und den Zeitpunkt der fehlgeschlagenen Aktion an, damit Copy Pastd das passende Aktivitätsprotokoll abrufen kann.
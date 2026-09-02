---
nav_title: Bynder
article_title: Bynder
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Bynder, einer Digital-Asset-Management-Plattform (DAM), mit der Sie über die Universal Compact View Chrome-Erweiterung genehmigte Asset-URLs in Braze Campaigns und Canvases suchen und einfügen können."
alias: /partners/bynder/
page_type: partner
search_tag: Partner
---

# Bynder

> [Bynder](https://www.bynder.com) ist eine Digital-Asset-Management-Plattform (DAM), die Kund:innen dabei unterstützt, genehmigte digitale Assets (Bilder, Videos und andere Kreativmaterialien) aus einer einzigen zentralen Quelle zu erstellen, zu verwalten, zu finden und zu verteilen. Durch die Integration mit Braze können Marketer über die Universal Compact View (UCV) Google-Chrome-Erweiterung von Bynder nach Bynder-Assets suchen und diese auswählen, ohne das Braze-Dashboard zu verlassen. Fügen Sie Links zu diesen Assets direkt in Campaigns und Canvases ein.

_Diese Integration wird von Bynder gepflegt._

## Über diese Integration {#about-this-integration}

Durch die Verbindung von Bynder mit Braze über die UCV-Chrome-Erweiterung erhalten Marketer Zugriff auf ihre Bynder-Asset-Bibliothek innerhalb des Braze-Content-Editors. Öffnen Sie die Universal Compact View als Overlay auf einem beliebigen Browser-Tab, einschließlich des Braze-Dashboards. Suchen oder filtern Sie nach dem passenden Kreativmaterial und fügen Sie dann die URL des Assets in Ihre Campaign ein.

So bleiben Braze Campaigns mit Bynders zentraler Quelle der Wahrheit abgestimmt: die richtigen Berechtigungen, die aktuellste Dateiversion und die korrekten Nutzungsrechte.

## Anwendungsfälle {#use-cases}

- Marketer, die eine E-Mail, In-App-Nachricht oder einen Content Block in Braze erstellen, können Hero-Bilder, Banner oder Links zu Werbevideos direkt aus Bynder einfügen, sodass Campaigns die neueste genehmigte Version eines Assets verwenden.
- Campaign-Manager:in:innen können die Such- und Filterleiste der Universal Compact View nutzen, um genehmigte regionale oder lokalisierte Kreativmaterialien für ein bestimmtes Zielgruppen-Segment zu finden, bevor sie diese einem Canvas-Schritt hinzufügen.
- Kreativteams können Bynders Dynamic Asset Transformation verwenden, um ein Asset für einen bestimmten Kanal in der Größe anzupassen oder umzuformatieren, bevor der Link in Braze kopiert wird. Verwenden Sie beispielsweise einen kompakten Zuschnitt für eine Push-Benachrichtigung oder ein Banner in voller Größe für E-Mails.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
| --- | --- |
| Ein Bynder-Konto | Ein Bynder-Konto mit Zugriff auf die DAM-Assets, die Sie in Braze referenzieren möchten. |
| Bynder Universal Compact View (UCV) Chrome-Erweiterung | Installiert aus dem Chrome Web Store und mit Ihrem Bynder-Portal verbunden. Nur für Google Chrome verfügbar. |
| Öffentliche Assets und Derivate | Jedes Asset und das spezifische Derivat, auf das Sie verlinken möchten, muss in Bynder als öffentlich markiert sein, damit die URL für Nachrichtenempfänger:innen korrekt aufgelöst wird. |
| Ein Braze-Konto | Zugriff auf den Messaging-Kanal (E-Mail, Content Block, In-App-Nachricht, Canvas usw.), in dem das Asset verwendet wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Bynder UCV Chrome-Erweiterung installieren und verbinden {#step-1-install-and-connect-the-bynder-ucv-chrome-extension}

1. Rufen Sie die [Bynder UCV-Erweiterung](https://chromewebstore.google.com/detail/bynders-universal-compact/ilghhphnbdblpbdhmbdfiaidganphema) im Chrome Web Store auf.
2. Klicken Sie auf **Zu Chrome hinzufügen**, überprüfen Sie die angeforderten Berechtigungen und klicken Sie dann auf **Erweiterung hinzufügen**.
3. Wählen Sie in der Chrome-Symbolleiste das Bynder-UCV-Symbol aus (heften Sie es zuerst an die Symbolleiste an, falls es noch nicht sichtbar ist).
4. Geben Sie Ihre Bynder-Portal-Domain ein (ohne `https://`) und klicken Sie dann auf **Connect**.
5. Melden Sie sich im sich öffnenden Fenster mit Ihren üblichen Zugangsdaten bei Ihrem Bynder-Portal an.

### Schritt 2: Ein Bynder-Asset suchen und auswählen {#step-2-search-for-and-select-a-bynder-asset}

1. Öffnen Sie bei verbundener Erweiterung die Universal Compact View von einem beliebigen Browser-Tab aus, einschließlich Ihres Braze-Dashboards.
2. Verwenden Sie den Smart-Filter und die Suchleiste, um das benötigte Bild, Video, Dokument oder Audio-Asset zu finden.
3. Wählen Sie das Asset aus und wählen Sie dann das Derivat (oder die Originaldatei, falls diese öffentlich ist), das Sie verwenden möchten.
4. Klicken Sie auf **Add Asset**, um die URL des ausgewählten Assets in Ihre Zwischenablage zu kopieren.

### Schritt 3: Die Asset-URL zu Ihrer Braze Campaign hinzufügen {#step-3-add-the-asset-url-to-your-braze-campaign}

1. Öffnen Sie in Braze die E-Mail, den Content Block, die In-App-Nachricht oder den Canvas-Schritt, in dem Sie das Asset hinzufügen möchten.
2. Fügen Sie die kopierte Bynder-Asset-URL in das entsprechende Feld ein. Verwenden Sie beispielsweise ein `<img src="">`-Tag oder das Bild-URL-Feld eines Content Blocks.

   Beispiel-Bild-URL:

   ```html
   <img src="https://your-portal.bynder.com/m/abcdef123456/original/campaign-banner.jpg" alt="Summer Campaign">
   ```

{: start="3"}
3. Speichern Sie Ihre Nachricht und zeigen Sie eine Vorschau an, um zu bestätigen, dass das Asset wie erwartet dargestellt wird.

## Tipps {#tips}

### Dynamic Asset Transformations vor dem Kopieren der URL anwenden {#apply-dynamic-asset-transformations-before-copying-the-url}

Verwenden Sie innerhalb der Universal Compact View die verfügbaren Transformationsoptionen, um ein Asset für den gewünschten Kanal in der Größe anzupassen, zuzuschneiden oder umzuformatieren. So vermeiden Sie das Hochladen separater zugeschnittener Versionen in Bynder.

### Kanalspezifische Derivat-URLs generieren {#generate-channel-specific-derivative-urls}

Jede Transformation oder jedes Derivat erzeugt eine eigene eindeutige URL. Generieren Sie eine Version in der Größe für E-Mail, eine weitere für Push und eine weitere für In-App-Nachrichten und fügen Sie dann jede in den entsprechenden Braze-Kanal oder Canvas-Schritt ein.

### Eine Asset-URL kanalübergreifend wiederverwenden {#reuse-one-asset-url-across-channels}

Da ein eingefügter Link auf ein bestimmtes Asset und Derivat in Bynder verweist, kann dasselbe URL-Format in E-Mails, Content Blocks, In-App-Nachrichten und Canvas-Schritten wiederverwendet werden. So bleibt das Kreativmaterial überall dort konsistent, wo es in einer Campaign verwendet wird.

### Das Quell-Asset aktualisieren, ohne Ihre Campaigns zu bearbeiten {#update-the-source-asset-without-editing-your-campaigns}

Wenn die zugrunde liegende Datei in Bynder ersetzt wird und dabei die gleichen öffentlichen Asset- und Derivat-Einstellungen beibehalten werden, spiegelt jede aktive Braze-Nachricht, die auf diese URL verweist, die Aktualisierung automatisch wider. Sie müssen die Campaign selbst nicht bearbeiten.

## Hinweise {#considerations}

- Die Bynder UCV Chrome-Erweiterung ist nur für Google Chrome verfügbar. In anderen Browsern kopieren Sie Asset-URLs direkt aus dem vollständigen Bynder-Portal.
- Nur Assets (und die spezifischen Derivate, auf die verlinkt wird), die in Bynder als öffentlich markiert sind, werden aufgelöst, wenn sie in Braze eingefügt werden. Private Assets geben einen Zugriffsfehler für Empfänger:innen zurück.
- Wenn Pop-up-Fenster nicht erlaubt sind oder das Portal bereits in einem anderen Tab geöffnet ist, wird das Anmeldefenster möglicherweise nicht korrekt geöffnet. Stellen Sie vor dem Verbinden sicher, dass Pop-up-Fenster erlaubt sind, und schließen Sie alle anderen Tabs, in denen das Portal geöffnet ist.
- Der Zugriff innerhalb der Erweiterung folgt den bestehenden Berechtigungen der Nutzer:innen im Bynder-DAM, sodass sie nur Assets sehen und auswählen können, für die sie bereits autorisiert sind.

## Fehlerbehebung {#troubleshooting}

| Problem | Lösung |
| --- | --- |
| Das Erweiterungssymbol ist nicht sichtbar | Heften Sie die Bynder UCV-Erweiterung über das Erweiterungsmenü an die Chrome-Symbolleiste an. |
| **Connect** öffnet kein Anmeldefenster | Stellen Sie sicher, dass Chrome-Pop-ups für Ihre Bynder-Portal-Domain erlaubt sind, und schließen Sie alle anderen Tabs, in denen das Portal bereits geöffnet ist. |
| Die Asset-URL wird in Braze nicht dargestellt | Bestätigen Sie, dass das Asset und das verwendete spezifische Derivat im Bynder-Portal als öffentlich markiert sind. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

Weitere Informationen finden Sie in Bynders [Universal Compact View Dokumentation](https://support.bynder.com/hc/en-us/sections/16936397091858-Universal-Compact-View-UCV) oder kontaktieren Sie den Bynder-Support.
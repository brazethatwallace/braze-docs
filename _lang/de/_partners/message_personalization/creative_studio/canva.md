---
nav_title: Canva
article_title: Canva
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Canva, mit der Sie Medien-Assets in die Braze-Medienbibliothek übertragen und Canva-E-Mail-Designs als Braze-E-Mail-Templates veröffentlichen können."
alias: /partners/canva/
page_type: partner
search_tag: Partner

---

# Canva

> [Canva](https://www.canva.com/) ist eine Grafikdesign-Plattform und ein Tool, mit dem Sie visuelle Inhalte für Social-Media-Beiträge, Präsentationen, Videos und mehr erstellen können. Die Braze-App in Canva unterstützt außerdem den Export von **E-Mail**-Designs als Braze-E-Mail-Templates sowie das Senden statischer Designs an Ihre Medienbibliothek.

## Über die Integration {#about-the-integration}

Die Integration von Braze und Canva unterstützt zwei Exportpfade:

| Exporttyp | Beschreibung |
| --- | --- |
| **Bild oder Design in die Medienbibliothek** | Sendet Ihr Design als Asset an die Braze-Medienbibliothek. |
| **E-Mail-Design an Braze** | Veröffentlicht ein Canva-**E-Mail**-Dokument als Braze-E-Mail-Template, einschließlich Betreffzeilen-Metadaten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Über die Integration" }

## Braze mit Canva integrieren {#integrate-braze-with-canva}

### 1. Schritt: Die Braze-App in Canva installieren {#step-1-install-the-braze-app-in-canva}

Sie finden die Braze-App im [Canva Apps Marketplace](https://www.canva.com/your-apps/AAG1cO7kIyc).

Nach der Installation der App ist sie innerhalb eines Designs im Menü **Apps** verfügbar.

![Braze-App im Canva-Apps-Menü.]({% image_buster /assets/img/canva_integration/braze-canva-app.png %}){: style="max-width:50%;"}

### 2. Schritt: Ihr Braze-Konto autorisieren {#step-2-authorize-your-braze-account}

Wenn Sie die Braze-App zum ersten Mal verwenden – egal ob Sie sie über das Menü **Apps** (Medienbibliothek-Export) oder über das Menü **Share** (E-Mail-Export) öffnen – wählen Sie **Connect**, um die Autorisierung zu starten. Dadurch kann Canva die Braze-Workspaces auflisten, auf die Sie Zugriff haben, und Medienbibliothek-Assets in Ihrem Namen erstellen.

Für **E-Mail**-Exporte fordert Canva Sie möglicherweise auf, sich erneut anzumelden und zusätzlichen Zugriff zu genehmigen, einschließlich der Berechtigung zum **Erstellen von E-Mail-Templates**. Akzeptieren Sie diese Berechtigungen, um die Veröffentlichung von E-Mail-Designs an Braze abzuschließen.

![„Connect“-Button und Autorisierungsablauf zum Verknüpfen von Canva mit Braze.]({% image_buster /assets/img/canva_integration/canva-connect-panel.jpg %})

## Bilder in die Medienbibliothek exportieren {#export-images-to-the-media-library}

Verwenden Sie diesen Ablauf für Standard-Canva-Designs, wenn Sie eine Datei in der Braze-Medienbibliothek benötigen.

Die folgenden Videos zeigen, wie Sie Designs von Canva an Ihre Braze-Medienbibliothek senden.

Video: Öffnen Sie die Braze-App in Canva und starten Sie einen Medienbibliothek-Export.

{% multi_lang_include video.html id="uf5krks2cx" source="wistia" %}

Video: Wählen Sie einen Braze-Workspace und schließen Sie den Export in die Medienbibliothek ab.
{% multi_lang_include video.html id="3d09tafx7c" source="wistia" %}

1. Öffnen Sie im Menü **Apps** in Ihrem Design die Braze-App. Falls Sie noch nicht verbunden sind, wählen Sie **Connect** und führen Sie die Schritte unter [Ihr Braze-Konto autorisieren](#step-2-authorize-your-braze-account) aus.
2. Wählen Sie Ihren Ziel-Workspace aus, geben Sie optional einen Dateinamen ein und wählen Sie **Start Export**.

![Canva-Exportbildschirm mit Ziel-Workspace und „Start Export“-Button.]({% image_buster /assets/img/canva_integration/canva-upload-screen.jpg %})

{: start="3"}
3. Wenn Ihr Export abgeschlossen ist, ist Ihr neues Asset in der **Medienbibliothek** mit der Quelle „Canva“ verfügbar.

![Exportiertes Canva-Asset in der Braze-Medienbibliothek.]({% image_buster /assets/img/canva_integration/media-library-source.jpg %})

## E-Mail-Designs als Braze-Templates exportieren {#export-email-designs-as-braze-templates}

Verwenden Sie diesen Ablauf, wenn Ihre Canva-Datei ein **E-Mail**-Designtyp ist. Dabei wird HTML als Template an Braze veröffentlicht (ähnliche Metadaten wie beim Bild-Ablauf, aber Sie starten über **Share** statt über **Apps**).

1. Erstellen oder öffnen Sie in Canva ein **E-Mail**-Design. Erstellen Sie Ihre Nachricht von Grund auf oder verwenden Sie ein Canva-E-Mail-Template.
2. Klicken Sie oben rechts im Editor auf **Share** und wählen Sie **Braze**. Falls Braze nicht aufgelistet ist, öffnen Sie **See more** und scrollen Sie zu **More options**, um Braze zu finden.

![Weitere Veröffentlichungsoptionen in Canva mit Braze unter „More options“.]({% image_buster /assets/img/canva_integration/canva-share-more-options-braze.png %})

{: start="3"}
3. Falls Sie aufgefordert werden, sich zu verbinden oder erneut anzumelden, wählen Sie **Connect** im Braze-Panel (oder schließen Sie den Browser-Anmeldevorgang ab), damit Canva Templates in Ihrem Workspace erstellen kann.

![Braze-Seitenleiste in Canva mit Aufforderung zur Verbindung für den E-Mail-Export.]({% image_buster /assets/img/canva_integration/canva-email-connect-sidebar.png %})

{: start="4"}
4. Wählen Sie im Braze-Panel aus, welche **E-Mail**-Seite veröffentlicht werden soll (falls das Design mehrere Seiten hat), wählen Sie Ihren **Braze-Workspace**, geben Sie einen **Template-Namen** und eine **Betreffzeile** ein und wählen Sie dann **Publish now**. Canva zeigt den Fortschritt an, während Ihr Design veröffentlicht wird.

![Braze-Panel in Canva mit Workspace, Template-Name, Betreffzeile und „Publish now“.]({% image_buster /assets/img/canva_integration/canva-email-publish-fields.png %})

{: start="5"}
5. Wenn die Veröffentlichung abgeschlossen ist, erscheint eine Erfolgsmeldung. Wählen Sie **Check it out**, um das E-Mail-Template in Braze zu öffnen.

![Erfolgsmeldung nach der Veröffentlichung eines Canva-E-Mail-Designs an Braze mit „Check it out“.]({% image_buster /assets/img/canva_integration/canva-email-publish-success.png %})

{: start="6"}
6. Vervollständigen Sie in Braze alle erforderlichen E-Mail-Einstellungen – wie **Absender**-Adresse, Preheader und einen Abmeldelink – bevor Sie das Template in einer Kampagne oder einem Canvas verwenden.

![E-Mail-Template in Braze, geöffnet aus Canva, mit Versandinformationen und Vorschau.]({% image_buster /assets/img/canva_integration/braze-email-template-from-canva.png %})
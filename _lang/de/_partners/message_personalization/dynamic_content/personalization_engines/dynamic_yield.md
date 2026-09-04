---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Dynamic Yield. Diese Partnerschaft erlaubt es Ihnen, die Empfehlungs- und Segmentierungs-Engine von Dynamic Yield zu nutzen, um Experience Blocks zu erstellen, die in Nachrichten von Braze eingebettet werden können."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Dynamic Yield

> [Dynamic Yield](https://www.dynamicyield.com/), ein Unternehmen von Mastercard, unterstützt Unternehmen aller Branchen bei der Bereitstellung digitaler Kundenerlebnisse, die personalisiert, optimiert und synchronisiert sind. Mit dem [Experience OS](http://www.dynamicyield.com/experience-os) von Dynamic Yield können Marketer, Produktmanager:innen, Entwickler:innen und digitale Teams Inhalte, Produkte und Angebote algorithmisch an jede Kund:in anpassen, um den Umsatz zu steigern und die Kundenbindung zu erhöhen.

_Diese Integration wird von Dynamic Yield gepflegt._

## Über die Integration {#about-the-integration}

Die Partnerschaft zwischen Braze und Dynamic Yield ermöglicht es Ihnen, die Empfehlungs- und Segmentierungs-Engine von Dynamic Yield zu nutzen, um Experience Blocks zu erstellen, die in Braze-Nachrichten eingebettet werden können. Experience Blocks können bestehen aus:
{% multi_lang_include partners/message_personalization/dynamic_yield_experience_blocks.md %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Dynamic Yield-Konto | Ein [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard)-Konto ist erforderlich, um diese Partnerschaft nutzen zu können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Einen Experience Block erstellen {#step-1-create-an-experience-block}

Um einen Experience Block in Dynamic Yield zu erstellen, navigieren Sie zu **Email > Experience Emails > Create New**.

Wählen Sie als Nächstes **Create Experience Block**, um einen Block mit dynamischem Content oder Empfehlungen zu entwerfen, der in ein Braze E-Mail-Template eingebettet werden soll.<br>![Dynamic Yield Experience Emails-Seite mit ausgewählter Option „Create Experience Block“.]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### Schritt 2: Ihre Nachricht entwerfen {#step-2-draft-your-messaging}

Das folgende Bild zeigt eine E-Mail, die von Grund auf im Builder erstellt wird.<br>![Dynamic Yield E-Mail-Builder mit einem Entwurf für ein Experience-E-Mail-Layout.]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. Geben Sie einen Kampagnennamen, eine Notiz und Bezeichnungen für die Kampagne im Kopfbereich ein.<br><br>
2. Fügen Sie einen Experience Block ein. Diese Blöcke umfassen:
  - [Empfehlungen](#configure-a-recommendations-block): Ein Widget, das Nutzer:innen vollständig personalisierte Empfehlungen bietet.
  - [Dynamischer Content](#configure-a-dynamic-content-block): Richten Sie verschiedene Aktionen und Nachrichten an verschiedene Zielgruppen.<br><br>
3. Einstellungen aktualisieren:
  - Verwenden Sie die URL-Parameter zum Tracking von Klicks in Ihrer Analytics-Software (optional). Fügen Sie bei Bedarf Parameter zu den Standardanzeigen hinzu.
  - Wählen Sie ein Attribut-Fenster aus, entweder sieben Tage (Standard) oder einen Tag.<br><br>
4. Speichern und beenden. Sie können jederzeit zurückkehren, um alle Elemente Ihrer E-Mail zu bearbeiten, bevor der Code generiert wird. Nachdem der Code generiert wurde, können Sie alles bearbeiten, was [sich nicht auf den Code auswirkt](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Einen Empfehlungsblock konfigurieren {#configure-a-recommendations-block}

Mit dem Empfehlungsblock können Sie Algorithmen und Filter festlegen, um personalisierte Inhalte für Nutzer:innen bereitzustellen, die beim Öffnen der E-Mail geladen werden.

1. Ziehen Sie einen Empfehlungsblock aus dem Bearbeitungsbereich in den Textkörper Ihrer E-Mail.<br><br>
2. Wählen Sie den gewünschten Algorithmus aus (Popularität, Nutzer:innen-Affinität, Ähnlichkeit und mehr). Je nach ausgewähltem Algorithmus werden zusätzliche Optionen angezeigt:
  - Wenn Ihre Empfehlung auf Popularität basiert, können Sie die Ergebnisse mischen, um zu vermeiden, dass dieselbe Empfehlung aus verschiedenen E-Mails angezeigt wird, die die betrachtende Person öffnet.
  - Andere Algorithmen, wie z. B. Ähnlichkeit, stützen sich auf den Kontext, um Empfehlungen auszusprechen, und erfordern, dass Sie Artikel zur Einbeziehung auswählen. Diese Artikel können im Builder hinzugefügt werden, oder Sie können [dem Einbettungscode einen Merge-Tag hinzufügen](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced), um ihn dynamisch zu gestalten – z. B. um ähnliche Artikel in Versandbestätigungs-E-Mails einzufügen. <br><br>
3. Sie können Produkte ausschließen, die Nutzer:innen bereits gekauft haben, um diese Produkte nicht erneut zu empfehlen.<br><br>
4. Sie können eine [angepasste Filterregel](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) hinzufügen, um bestimmte Produkte an Slots zu binden oder Produkte nach Produkteigenschaften ein- und auszuschließen. Zeigen Sie z. B. keine Produkte an, die weniger als 5 $ kosten, oder nur Produkte aus der Kategorie Shorts.<br><br>
5. Zum Schluss konfigurieren Sie das Design des Empfehlungsblocks. Wählen Sie dazu ein Artikel-Template aus, legen Sie die Anzahl der anzuzeigenden Artikel fest und bestimmen Sie, in wie vielen Zeilen diese angezeigt werden sollen.

### Einen dynamischen Content-Block konfigurieren {#configure-a-dynamic-content-block}
Verwenden Sie dynamischen Content, um verschiedene Aktionen und Nachrichten an verschiedene Nutzer:innen zu richten. Das Targeting kann entweder auf Affinität oder auf Zielgruppe basieren. Dynamic Yield bestimmt, welches personalisierte Erlebnis beim Öffnen der E-Mail angezeigt werden soll.

1. Ziehen Sie einen dynamischen Content-Block aus dem Bearbeitungsbereich in den Textkörper Ihrer E-Mail.<br><br>
2. Wählen Sie ein Template für die erste Variante aus. Sie können jetzt Design- und Inhaltsvariablen definieren. Speichern Sie die Variante, wenn Sie fertig sind. <br>![Dynamic Yield Template-Editor für dynamische Content-Varianten.]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br>
3. Legen Sie die Zielgruppe im Bereich „Dynamischer Content“ fest.<br>![Dynamic Yield Zielgruppen-Targeting-Einstellungen für eine dynamische Content-Variante.]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br>
4. Fügen Sie eine weitere Variante hinzu, um eine andere spezifische Zielgruppe oder alle Nutzer:innen anzusprechen. Wiederholen Sie den Vorgang nach Bedarf.<br><br>
5. Legen Sie die Prioritäten für Ihre Varianten mithilfe der Pfeile nach oben und unten fest. <br><br>
6. Die Prioritäten bestimmen, welche Variante angezeigt wird, wenn Nutzer:innen für mehr als ein Erlebnis infrage kommen.

### Schritt 3: Ihre E-Mail mit Braze integrieren {#step-3-integrate-your-email-with-braze}

Diese Integration erlaubt es Ihnen, personalisierte Empfehlungs-Widgets und dynamischen Content von Dynamic Yield in Ihre Braze E-Mail-Campaigns einzubetten. Das Einbetten in Braze Campaigns erfolgt über einen einfachen Einbettungscode, den Sie in den E-Mail-Editor von Braze einfügen.

1. Klicken Sie auf das Symbol für die E-Mail-Anbieter-Integration auf der Seite der Experience-E-Mail-Liste.<br><br>
2. Geben Sie das entsprechende Token von Braze ein, das die CUID und die E-Mail-ID der Nutzer:innen einfügt.<br>![Dynamic Yield ESP-Integrations-Dialog mit Braze-Nutzer:innen-Token-Feldern.]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})

Wenn Sie mit Ihrer E-Mail zufrieden sind, generieren Sie im nächsten Schritt den Code zum Einbetten in Braze.
1. Klicken Sie unter **Experience Emails** auf **Generate Code**.<br><br>
2. Klicken Sie anschließend auf **Copy to Clipboard**.<br>![Dynamic Yield Panel mit generiertem Einbettungscode und der Aktion „Copy to Clipboard“.]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br>
3. Fügen Sie den Code in Ihre Braze E-Mail-Campaign ein und fahren Sie dann mit dem Entwerfen, Testen und Veröffentlichen Ihrer E-Mail-Campaign fort.
---
nav_title: Adobe
article_title: Adobe
description: "Diese Seite beschreibt die Partnerschaft zwischen Braze und Adobe, einer Customer Data Platform, die es Marken erlaubt, ihre Adobe-Daten (angepasste Attribute und Segmente) mit Braze in Echtzeit zu verbinden und abzubilden. Marken können dann auf Basis dieser Daten handeln und diesen Nutzer:innen personalisierte, zielgerichtete Erlebnisse bieten."
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Die Customer Data Platform (CDP) von Adobe basiert auf der Adobe Experience Platform und führt bekannte und anonyme Daten aus verschiedenen Unternehmensquellen zusammen, um Kundenprofile zu erstellen. Diese Profile können dann verwendet werden, um über alle Kanäle und Geräte hinweg personalisierte Erlebnisse in Realtime zu bieten.

Die Integration von Braze und Adobe Customer Data Platform (CDP) verbindet die Adobe-Daten Ihrer Marke (angepasste Attribute und Segmente) mit Braze und bildet sie in Echtzeit ab. Sie können dann auf diese Daten reagieren und Ihren Nutzer:innen personalisierte, zielgerichtete Erlebnisse zustellen. Bei Adobe ist die Integration intuitiv. Nehmen Sie einfach eine beliebige [Adobe-Identität](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en), bilden Sie sie auf eine externe ID von Braze ab und senden Sie sie an die Braze-Plattform. Alle gesendeten Daten werden in Braze über ein neues Attribut `AdobeExperiencePlatformSegments` zugänglich sein.

{% alert important %}
Die Integration der Adobe Experience Platform unterstützt derzeit keine dynamische Zielgruppenmitgliedschaft. Das bedeutet, dass sie nur Werte zu Nutzerprofilen hinzufügen, nicht aber entfernen kann.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Adobe-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Adobe-Konto](https://account.adobe.com/). |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze Onboarding Manager:in oder auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics#endpoints). |
| Braze REST-Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% alert important %}
Das Senden zusätzlicher angepasster Attribute erhöht Ihre Datenpunkt-Nutzung. Wir empfehlen Ihnen, mit Ihrem CSM zu sprechen, um diesen potenziellen Anstieg der Datenpunkte besser zu verstehen.
{% endalert %}

## Integration

### 1. Schritt: Braze-Ziel konfigurieren {#step-1-configure-braze-destination}

Wählen Sie auf der Adobe-Seite **Settings** unter **Collections** die Option **Destinations** aus. Suchen Sie von dort aus die Kachel **Braze** und wählen Sie **Configure**.

![Adobe-Zielkatalog mit der Braze-Zielkachel und der Aktion „Configure“.]({% image_buster /assets/img/adobe/braze-destination-configure.png %})

{% alert note %}
Wenn bereits eine Verbindung mit Braze besteht, sehen Sie auf der Zielkarte einen Button **Activate**. Weitere Informationen zum Unterschied zwischen „Activate“ und „Configure“ finden Sie im Abschnitt „Catalog“ in der [Dokumentation](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog) zum Adobe Workspace für Ziele.
{% endalert %}

### 2. Schritt: Braze-Token / Textbaustein bereitstellen {#step-2-provide-braze-token}

Geben Sie im Schritt **Account** Ihren Braze-API-Schlüssel an und wählen Sie **Connect to destination** aus.

![Adobe-Braze-Ziel – Schritt „Account“ mit API-Schlüssel-Eingabe und Verbindungsaktion.]({% image_buster /assets/img/adobe/braze-destination-account.png %}){: style="max-width:60%"}

### 3. Schritt: Authentifizierung {#step-3-authentication}

Als Nächstes geben Sie im Schritt **Authentication** Ihre Braze-Verbindungsdaten ein:
- **Name**: Geben Sie den Namen ein, unter dem Sie dieses Ziel in Zukunft wiedererkennen möchten.
- **Destination**: Geben Sie eine Beschreibung ein, mit deren Hilfe Sie dieses Ziel identifizieren können.
- **Endpoint instance**: Geben Sie Ihre Braze-Endpunkt-Instanz ein.
- **Marketing use case**: Anwendungsfälle im Marketing geben die Absicht an, für die Daten an das Ziel exportiert werden sollen. Sie können aus den von Adobe definierten Anwendungsfällen für das Marketing auswählen oder Ihren eigenen Anwendungsfall erstellen. Wenn Sie mehr über Anwendungsfälle im Marketing von Adobe erfahren möchten, besuchen Sie [Data Governance in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

![Adobe-Ziel – Schritt „Authentication“ mit Feldern für Name, Ziel und Endpunkt.]({% image_buster /assets/img/adobe/braze-destination-authentication.png %}){: style="max-width:60%;"}

### 4. Schritt: Ziel erstellen {#step-4-create-destination}
Wählen Sie **Create destination**. Ihr Ziel wurde erstellt. Sie können **Save & Exit** wählen, um Segmente später zu aktivieren, oder **Next**, um den Workflow fortzusetzen und Segmente zur Aktivierung auszuwählen.

### 5. Schritt: Segmente aktivieren {#step-5-activate-segments}
Aktivieren Sie die Daten, die Sie in der Adobe Realtime Customer Data Platform (CDP) haben, indem Sie Segmente auf das Braze-Ziel abbilden.

In der folgenden Liste finden Sie die allgemeinen Schritte, die zur Aktivierung eines Segments erforderlich sind. Eine ausführliche Anleitung zu den Segmenten von Adobe und dem Workflow zur Segmentaktivierung finden Sie unter [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Wählen Sie das Braze-Ziel aus und aktivieren Sie es.
2. Wählen Sie die zutreffenden Segmente aus.
4. Konfigurieren Sie die Zeitpläne und Dateinamen für jedes Segment, das Sie exportieren.
5. Wählen Sie die Attribute aus, die Sie an Braze senden möchten.
6. Überprüfen und bestätigen Sie die Aktivierung.

### 6. Schritt: Abbildung der Felder {#step-6-field-mapping}

Um Ihre Zielgruppendaten von der Adobe Experience Platform korrekt an Braze zu senden, müssen Sie den Schritt der Abbildung der Felder abschließen. Die Abbildung stellt eine Verbindung zwischen den Feldern des Adobe Experience-Datenmodells und den entsprechenden Feldern der Braze-Plattform her.

1. Wählen Sie im Schritt „Abbildung“ die Option **Add new mapping**.<br>![Adobe-Seite für die Abbildung der Felder mit dem Button „Add new mapping“.]({% image_buster /assets/img/adobe/braze-destination-mapping.png %}){: style="max-width:50%;"}<br><br>
2. Wählen Sie im Bereich „Quellfeld“ den Pfeil-Button neben dem leeren Feld, um das Fenster „Quellfeld auswählen“ zu öffnen.<br>![Adobe-Quellfeldauswahl für die Zielabbildung.]({% image_buster /assets/img/adobe/braze-destination-mapping-source.png %})<br><br>
3. Wählen Sie in dem Fenster die Adobe-Attribute aus, die Sie Ihren Braze-Attributen zuordnen möchten. <br>![Adobe-Attributauswahl mit Quellattributen für die Abbildung.]({% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}){: style="max-width:70%;"}<br><br>Wählen Sie dann den Identitäts-Namensraum aus. Mit dieser Option können Sie einen Namensraum für die Plattformidentität auf einen Braze-Namensraum abbilden.<br>![Adobe-Auswahl des Identitäts-Namensraums für die Braze-Abbildung.]({% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}){: style="max-width:80%;"}<br> Wählen Sie Ihre Quellfelder aus und wählen Sie dann **Select**.<br><br>
4. Wählen Sie im Abschnitt „Zielfeld“ das Symbol für die Abbildung neben dem Feld aus.<br>![Adobe-Panel für die Zielfeld-Abbildung mit ausgewähltem Abbildungssymbol.]({% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}){: style="max-width:90%;"} <br><br>
5. Im Fenster „Zielfeld auswählen“ können Sie zwischen drei Kategorien von Zielfeldern wählen:<br><br>• **Select identity namespace**: Verwenden Sie diese Option, um Identitäts-Namensräume der Plattform auf Identitäts-Namensräume von Braze abzubilden.<br>• **Select custom attributes**: Verwenden Sie diese Option, um Adobe-XDM-Attribute auf angepasste Braze-Attribute abzubilden, die Sie in Ihrem Braze-Konto definiert haben. <br><br>![Adobe-Zielfeldauswahl mit Optionen für Identitäts-Namensraum und angepasste Attribute.]({% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}){: style="max-width:60%;"}<br><br>**Sie können diese Option auch verwenden, um bestehende XDM-Attribute in Braze umzubenennen.** Wenn Sie beispielsweise ein `lastname`-XDM-Attribut auf ein angepasstes `Last_Name`-Attribut in Braze abbilden, wird das `Last_Name`-Attribut in Braze erstellt, falls es noch nicht vorhanden ist, und das `lastname`-XDM-Attribut wird diesem zugeordnet. <br><br> Wählen Sie Ihre Zielfelder und wählen Sie dann **Select**.<br><br>
6. Ihre Abbildung der Felder sollte in der Liste erscheinen.<br>![Abgeschlossene Adobe-zu-Braze-Feldabbildungen, aufgelistet im Schritt „Zielabbildung“.]({% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %})<br><br>
7. Wenn Sie weitere Abbildungen hinzufügen möchten, wiederholen Sie die Schritte 1 bis 6 nach Bedarf.

## Anwendungsfall {#use-case}

Nehmen wir an, Ihr XDM-Profilschema und Ihre Braze-Instanz enthalten die folgenden Attribute und Identitäten:

|     | XDM-Profilschema | Braze-Instanz |
| --- | ------------------ | -------------- |
| Attribute | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| Identitäten | - `Email`<br>- Google Ad ID (`GAID`)<br>- Apple ID für Werbetreibende (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Anwendungsfall" }

Die korrekte Abbildung würde wie folgt aussehen:

![Ziel-Abbildungen: IdentityMap:IDFA abgebildet auf IdentityMap:external_id, IdentityMap:GAID abgebildet auf IdentityMap:external_id, IdentityMap:Email abgebildet auf IdentityMap:external_id, xdm:mobilePhone.number abgebildet auf CustomAttribute:PhoneNumber, xdm:person.name.lastName abgebildet auf CustomAttribute:LastName, xdm:person.name.firstName abgebildet auf CustomAttribute:FirstName]({% image_buster /assets/img/adobe/braze-destination-mapping-example.png %})

## Exportierte Daten {#exported-data}
Um zu überprüfen, ob die Daten erfolgreich nach Braze exportiert wurden, sehen Sie in Ihrem Braze-Konto nach. Adobe Experience Platform Segmente werden unter dem Attribut `AdobeExperiencePlatformSegments` nach Braze exportiert.

## Nutzung und Verwaltung von Daten {#data-usage-and-governance}
Alle Ziele von Adobe Experience Platform halten sich beim Umgang mit Ihren Daten an die Richtlinien zur Datennutzung. Unter [Data Governance in Realtime Customer Data Platform (CDP)](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) finden Sie detaillierte Informationen darüber, wie die Adobe Experience Platform Data Governance durchsetzt.
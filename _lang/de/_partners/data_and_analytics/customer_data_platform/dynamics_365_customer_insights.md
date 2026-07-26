---
nav_title: Dynamics 365 geschäftskunden Insights
article_title: Dynamics 365 geschäftskunden Insights
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Dynamics 365 geschäftskunden Insights, einer führenden geschäftskunden Data Platform (CDP) für Unternehmen, mit der Sie Kundensegmente nach Braze exportieren können, um sie in Kampagnen oder Canvases zu verwenden."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 geschäftskunden Insights

> [Dynamics 365 geschäftskunden Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) ist eine führende geschäftskunden Data Platform (CDP) für Unternehmen, die personalisierte Kundenerlebnisse mit einer 360-Grad-Sicht auf Ihre Kund:innen ermöglicht.

_Diese Integration wird von Dynamics 365 geschäftskunden Insights gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Dynamics 365 geschäftskunden Insights ermöglicht es Ihnen, Kundensegmente nach Braze zu exportieren, um sie in Kampagnen oder Canvases zu verwenden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Dynamics 365 geschäftskunden Insights-Konto | Um die Vorteile dieser Partnerschaft nutzen zu können, benötigen Sie ein [Dynamics 365 geschäftskunden Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/)-Konto. Sie benötigen Zugriff als Administrator:in, um Verbindungen innerhalb Ihres Dynamics 365 geschäftskunden Insights-Kontos anzuzeigen und zu bearbeiten und auf die erforderlichen Plugins zuzugreifen. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit den Berechtigungen `users.track` und `users.export.segment` ist erforderlich. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Übereinstimmende Profilbezeichner | Vereinheitlichte Kundenprofile in den exportierten Segmenten enthalten ein Feld für eine E-Mail-Adresse und eine Braze `external_id`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### 1. Schritt: Braze-Verbindung einrichten {#step-1-set-up-braze-connection}

Navigieren Sie in geschäftskunden Insights zu **Admin > Connections**. Wählen Sie dann **Add connections** und wählen Sie **Braze**, um die Verbindung zu konfigurieren.

1. Geben Sie Ihrer Verbindung im Feld **Display name** einen erkennbaren Namen.
2. Wählen Sie, wer diese Verbindung nutzen kann. Wenn Sie dieses Feld leer lassen, ist der Standardwert „Administrators“. Weitere Informationen finden Sie unter [Beitragenden erlauben, eine Verbindung für Exporte zu verwenden](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. Geben Sie Ihren Braze-API-Schlüssel und den REST-Endpunkt im Format `rest.iad-03.braze.com` an.
4. Wählen Sie **I agree**, um die Einhaltung der Daten- und Datenschutzrichtlinien zu bestätigen.
5. Wählen Sie **Connect**, um die Verbindung zu Braze zu initialisieren.
6. Wählen Sie **Add yourself as export user** und geben Sie Ihre geschäftskunden Insights-Zugangsdaten an.
7. Wählen Sie **Save**, um die Verbindung abzuschließen.

### 2. Schritt: Ein Braze Segment erstellen {#step-2-create-a-braze-segment}

1. Gehen Sie in Braze zu **Audience** > **Segments**.
2. Erstellen Sie ein Segment der Nutzer:innen, die Microsoft über Dynamics 365 geschäftskunden Insights aktualisieren soll.
3. Erfassen Sie den **API-Bezeichner** des Segments.

### 3. Schritt: Einen Export konfigurieren {#step-3-configure-an-export}

Sie können diesen Export konfigurieren, wenn Sie Zugang zu einer Verbindung dieses Typs haben. Weitere Informationen finden Sie in der [Übersicht über Exporte](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. Gehen Sie in geschäftskunden Insights zu **Data > Exports**. Um einen neuen Export zu erstellen, wählen Sie **Add destination**.
2. Wählen Sie im Feld **Connection for export** eine Verbindung für den Abschnitt „Braze“ aus. Wenn Sie diesen Abschnittsnamen nicht sehen, stehen Ihnen keine Verbindungen dieses Typs zur Verfügung.
3. Geben Sie den Segment-API-Bezeichner des Segments in Braze an.
4. Wählen Sie im Abschnitt **Data matching** im Feld **Email** das Feld aus, das die E-Mail-Adresse einer geschäftskunden darstellt. Wählen Sie dann im Feld **Braze geschäftskunden ID** das Feld aus, das die Braze-ID der geschäftskunden darstellt. Sie können auch ein zusätzliches, optionales Feld für den Datenabgleich auswählen.
  a. Wenn Sie die `external_id` in Braze dem Feld „Braze geschäftskunden ID“ in geschäftskunden Insights zuordnen, werden die vorhandenen Datensätze beim Exportieren in Braze aktualisiert.
  b. Wenn Sie ein anderes ID-Feld zuordnen, das nicht der `external_id` eines Datensatzes in Braze entspricht, oder ein leeres Feld, werden beim Exportieren neue Datensätze in Braze erstellt.
5. Wählen Sie abschließend die Segmente aus, die Sie exportieren möchten, und wählen Sie **Save**.

Beachten Sie, dass durch das Speichern eines Exports der Export nicht sofort ausgeführt wird. Dieser Export wird bei jeder [geplanten Aktualisierung](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab) ausgeführt. Sie können auch [Daten bei Bedarf exportieren](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand).


### Verwendung dieser Integration {#using-this-integration}

Nachdem Ihre Segmente erfolgreich nach Braze exportiert wurden, finden Sie sie als angepasste Attribute in den Nutzerprofilen. Das angepasste Attribut wird mit dem Braze Segment-API-Bezeichner benannt, der bei der Konfiguration der Exportverbindung eingegeben wurde. Zum Beispiel: `"Segment_API_Identifier": "0000-0000-0000"`

Um ein Segment dieser Nutzer:innen in Braze zu erstellen, navigieren Sie zu **Segments**, erstellen Sie ein neues Segment und wählen Sie **Custom Attributes** als Filter. Von hier aus können Sie das mit Dynamics 365 synchronisierte angepasste Attribut auswählen. Nachdem das Segment erstellt wurde, können Sie es als Zielgruppen-Filter auswählen, wenn Sie eine Campaign oder ein Canvas erstellen.

{% alert note %}
Weitere Informationen zu dieser Integration finden Sie im [Integrationsartikel](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze) zu Braze von Microsoft.
{% endalert %}
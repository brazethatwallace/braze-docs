---
nav_title: Shopify für Currents
article_title: Shopify für Currents
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze-Currents und Shopify, einem globalen Handelsunternehmen, mit dem Sie Braze nahtlos mit Ihrem Shopify-Shop verbinden können, um internes Reporting zu unterstützen und die Last-Touch-Attribution für Käufe besser zu verfolgen."
page_type: partner
tool: Currents
search_tag: Partner
alias: /shopify_for_currents/
hidden: true
noindex: true

---

# Shopify für Currents {#shopify-for-currents}

> [Shopify](https://www.shopify.com/) ist ein führendes globales Handelsunternehmen, das vertrauenswürdige Tools bereitstellt, um ein Unternehmen jeder Größe zu starten, auszubauen, zu vermarkten und zu verwalten. Die Plattform und Dienste von Shopify sind auf Zuverlässigkeit ausgelegt und bieten Verbraucher:innen überall ein besseres Einkaufserlebnis.

{% alert important %}
Diese Integration befindet sich derzeit in der Beta-Phase. Für weitere Informationen wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

Die Braze-Integration mit Shopify bietet eine leistungsstarke Lösung für E-Commerce-Unternehmen, die ihr Customer-Engagement verbessern und personalisierte Marketingmaßnahmen vorantreiben möchten. Mit [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) können Sie Daten mit Shopify verbinden, um internes Reporting zu unterstützen und die Last-Touch-Attribution für Käufe besser zu verfolgen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Currents | Um Daten nach Shopify zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
| Shopify-Shop | Stellen Sie sicher, dass Sie bereits [mindestens einen Shopify-Shop mit Braze eingerichtet]({{site.baseurl}}/shopify_standard_integration/) haben. |
| Shopify-Shop-Inhaber:in oder Mitarbeiter:innen-Berechtigungen | {::nomarkdown}<ul><li>Zugriff auf alle Einstellungen unter <b>General</b> und <b>Online Store</b>.</li><li> Zusätzliche Administrator-Berechtigungen:</li><ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### 1. Schritt: Ihren Shopify-Shop einrichten {#step-1-set-up-your-shopify-store}

Falls noch nicht geschehen, folgen Sie den Schritten zur [Shopify-Standardintegration]({{site.baseurl}}/shopify_standard_integration/), um mindestens einen Shopify-Shop mit Braze einzurichten.

### 2. Schritt: Braze-Current erstellen {#step-2-create-braze-current}

1. Gehen Sie in Braze zu **Partner Integrations** > **Currents** > **+ Create New Current** > **Shopify Export**.
2. Geben Sie einen Integrationsnamen und eine Kontakt-E-Mail-Adresse an.
3. Wählen Sie im Abschnitt **Credentials** den Shopify-Shop aus, den Sie in [Schritt 1](#step-1-set-up-your-shopify-store) eingerichtet haben.
4. Wählen Sie die Ereignisse aus, die Sie verfolgen möchten. Eine Liste der verfügbaren Ereignisse wird bereitgestellt.
5. Wählen Sie **Launch Current** aus.

![Die Braze-Shopify-Currents-Seite. Diese Seite enthält Felder für den Integrationsnamen, die Kontakt-E-Mail-Adresse und den Shopify-Shop.]({% image_buster /assets/img/shopify/shopify_currents.png %})
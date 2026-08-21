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

Die Braze-Integration mit Shopify bietet eine leistungsstarke Lösung für E-Commerce-Unternehmen, die ihr Customer-Engagement verbessern und personalisierte Marketingmaßnahmen vorantreiben möchten. Mit [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) können Sie Daten mit Shopify verbinden, um internes Reporting zu unterstützen und die Last-Touch-Attribution für Käufe besser zu verfolgen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Currents | Um Daten nach Shopify zu exportieren, muss [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) für Ihr Konto eingerichtet sein. |
| Shopify-Shop | Stellen Sie sicher, dass Sie bereits [mindestens einen Shopify-Shop mit Braze eingerichtet]({{site.baseurl}}/shopify_standard_integration) haben. |
| Berechtigungen als Shopify-Shop-Inhaber:in oder Mitarbeiter:in | {::nomarkdown}<ul><li>Zugriff auf alle Einstellungen unter <b>General</b> und <b>Online Store</b>.</li><li> Zusätzliche Administratorberechtigungen:</li><ul><li>Bestellungen: Anzeigen</li><li>Kund:in: Lesen/Schreiben</li><li>Kundenereignisse anzeigen (Web Pixels)</li><li>Einstellungen verwalten</li><li>Von Mitarbeiter:innen/Mitarbeitenden entwickelte Apps anzeigen</li><li>Apps und Kanäle verwalten/installieren</li><li>Angepasste Pixels verwalten/hinzufügen</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### 1. Schritt: Ihren Shopify-Shop einrichten {#step-1-set-up-your-shopify-store}

Falls noch nicht geschehen, folgen Sie den Schritten zur [Shopify-Standardintegration]({{site.baseurl}}/shopify_standard_integration), um mindestens einen Shopify-Shop mit Braze einzurichten.

### 2. Schritt: Braze-Current erstellen {#step-2-create-braze-current}

1. Gehen Sie in Braze zu **Partner Integrations** > **Currents** > **+ Create New Current** > **Shopify Export**.
2. Geben Sie einen Integrationsnamen und eine Kontakt-E-Mail-Adresse an.
3. Wählen Sie im Abschnitt **Credentials** den Shopify-Shop aus, den Sie in [Schritt 1](#step-1-set-up-your-shopify-store) eingerichtet haben.
4. Wählen Sie die Ereignisse aus, die Sie verfolgen möchten. Eine Liste der verfügbaren Ereignisse wird bereitgestellt.
5. Wählen Sie **Launch Current** aus.

![Die Braze-Shopify-Currents-Seite. Diese Seite enthält Felder für den Integrationsnamen, die Kontakt-E-Mail-Adresse und den Shopify-Shop.]({% image_buster /assets/img/shopify/shopify_currents.png %})

## Nutzerprofil-Synchronisierung {#user-profile-sync}

Zusätzlich zu Ereignisdaten kann die Shopify-Integration Nutzerprofil-Aktualisierungen von Braze mit Ihrem Shopify-Shop synchronisieren. Wenn das Profil einer Nutzerin oder eines Nutzers in Braze aktualisiert wird, erstellt oder aktualisiert Currents den entsprechenden Kunden in Ihrem Shop.

{% alert note %}
Die Nutzerprofil-Synchronisierung wird bei [Test-Currents-Konnektoren]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#testing-currents-connectors) nicht unterstützt. Andere Ereignis-Exporte sind davon nicht betroffen. Um Nutzerprofile zu synchronisieren, verwenden Sie einen [Standard-Shopify-Currents-Konnektor](#step-2-create-braze-current).
{% endalert %}

### Nutzer:innen-Zuordnung {#user-matching}

Braze ordnet Shopify-Kunden anhand der Braze-`user_id` als Shopify-[Custom Identifier](https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerSet) (`customId`) mit dem Namespace `braze` und dem Schlüssel `user_id` zu. Wenn in Ihrem Shop kein Kunde mit diesem Bezeichner existiert, wird ein neuer Kunde erstellt. Anonyme Nutzer:innen werden nicht synchronisiert.

### Feldzuordnung {#field-mapping}

Die folgenden Braze-Profilfelder werden mit Shopify synchronisiert:

| Braze-Feld | Shopify-Kundenfeld | Hinweise |
| ----------- | ---------------------- | ----- |
| `first_name` | `firstName` | Wird unverändert übernommen. Wird nur gesendet, wenn im Profil-Update vorhanden. |
| `last_name` | `lastName` | Wird unverändert übernommen. Wird nur gesendet, wenn im Profil-Update vorhanden. |
| `email_address` | `email` | Wird vor dem Senden getrimmt und in Kleinbuchstaben umgewandelt. |
| `phone_number` | `phone` | Wird im [E.164](https://en.wikipedia.org/wiki/E.164)-Format gesendet. |
| `language` | `locale` | Wird in ein von Shopify unterstütztes Gebietsschema konvertiert. Portugiesisch und Chinesisch erhalten eine regionale Variante (z. B. `pt-BR`) basierend auf dem Land der Nutzerin oder des Nutzers. Wenn die Sprache nicht von Shopify unterstützt wird, wird dieses Feld ausgelassen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Es werden nur die Felder gesendet, die in einem Profil-Update enthalten sind. Felder, die in einem Update nicht enthalten sind, bleiben in Shopify unverändert – eine Synchronisierung löscht oder entfernt niemals ein Feld bei Ihrem Shopify-Kunden.

### Felder, die nicht synchronisiert werden {#fields-that-are-not-synced}

Die Integration schreibt derzeit keine Shopify-Metafelder. Daher werden Profilfelder, die ein Metafeld erfordern würden, nicht synchronisiert. Insbesondere werden angepasste Attribute nicht an Shopify gesendet. Weitere nicht gesendete Felder sind `external_user_id`, `gender`, `dob` (Geburtsdatum), `timezone`, `home_city`, `country` und `archived`.

Braze kann in Ihrem Shop Metafeld-Definitionen unter dem Namespace `braze` erstellen (z. B. `braze.gender`). Diese Definitionen sind für eine mögliche zukünftige Nutzung reserviert – Braze schreibt derzeit keine Werte in sie. Die Ausnahme ist `braze.user_id`, das den Bezeichner speichert, der zur Zuordnung Ihrer Kunden verwendet wird.
---
nav_title: Merkury
article_title: Merkury
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Merkury, einer Unternehmensidentitätsplattform für Ihre Apps, die es Ihnen erlaubt, die `MerkuryID` zu nutzen, um die Erkennungsrate von Website-Besucher:innen für Braze-Kund:innen zu erhöhen."
page_type: partner
search_tag: Partner

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/) ist die Identitätsplattform von Merkle für Unternehmen, die Marken dabei hilft, das Engagement, die Erfahrung und den Umsatz ihrer Verbraucher:innen durch cookielose First-Party-Identitätsfunktionen zu maximieren. Die `MerkuryID` vereinigt die bekannten und unbekannten Datensätze von Kund:innen und Interessent:innen einer Marke, Website-/App-Besuche und Verbraucher:innen-Daten zu einer einzigen, persistenten Personen-ID.

_Diese Integration wird von Merkury gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Merkury erlaubt es Ihnen, die `MerkuryID` zu nutzen, um die Erkennungsrate von Website-Besucher:innen für Braze-Kund:innen zu erhöhen. Wenn Merkury erkennt, dass Besucher:innen E-Mail-Abonnent:innen der Marke sind, aktualisiert es das Braze-Profil und fügt die E-Mail-Adresse der Abonnent:innen hinzu. Die verbesserten Erkennungsmöglichkeiten der `MerkuryID` steigern das Engagement und die Personalisierungschancen und erhöhen sofort die Anzahl der gesendeten E-Mails bei Website-Abbrüchen sowie den damit verbundenen Umsatz.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Merkle-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Merkle-Konto. |
| Merkle-Client-ID | Erhalten Sie Ihre Client-ID von Ihrer Merkle-Vertretung. |
| Merkury-Tag | Platzieren Sie den Merkle-Merkury-Tag auf Ihrer Website. |
| Braze-REST- und SDK-Endpunkt | Ihre REST- oder SDK-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den Berechtigungen `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Dieser kann über **Braze-Dashboard > Entwicklungskonsole > REST-API-Schlüssel > Neuen API-Schlüssel erstellen** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% alert important %}
Die Anfragen des Merkury-Identitätskonnektors an Braze bewegen sich im Rahmen der Braze-API-Rate-Limits. Kontaktieren Sie Braze oder Ihre:n Merkle-Account-Manager:in, wenn Sie Fragen haben.<br><br>Merkury sendet mindestens eine Anfrage am Ende einer qualifizierten Sitzung.
{% endalert %}

## Side-by-side-SDK-Integration

Verwendet den clientseitigen Merkury-Tag von Merkle, um Braze-Geräte zu erfassen, und leitet sie zur Identifizierung an den Endpunkt des Merkury-Identitätskonnektors weiter.

### 1. Schritt: Braze-Web-SDK-Tag einrichten {#step-1-setup-braze-web-sdk-tag}

Sie müssen das [Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) auf Ihrer Website installiert haben, um diese Integration nutzen zu können.

### 2. Schritt: Merkury-Tag von Merkle bereitstellen {#step-2-deploy-merkles-merkury-tag}

Setzen Sie den Merkury-Tag auf Ihrer Website ein, um den Merkury-Identitätskonnektor auf Ihrer Website verfügbar zu machen. Ihre:r Merkle-Account-Manager:in wird Ihnen einen detaillierten Leitfaden mit Anweisungen zur Verfügung stellen.

### 3. Schritt: Angepasste Attribute erstellen {#step-3-create-custom-attributes}

Der Merkury-Identitätskonnektor füllt die folgenden Felder auf, die Sie in Braze als [angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes) erstellen müssen.

| Attributname | Datentyp | Beschreibung |
| --- | --- | --- |
| `hmid` | String | Merkury-ID von Merkle |
| `confidence_score` | Zahl | Wie sicher Merkury bei der Identifizierung war (1–8, niedriger ist besser) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="3. Schritt: Angepasste Attribute erstellen" }

### 4. Schritt: Merkle mit dem E-Mail-Universum der Nutzer:innen versorgen {#step-4-provide-merkle-with-user-email-universe}

Merkle empfiehlt einen Segmentierungsexport Ihres zulässigen E-Mail-Universums. Dies kann durch tägliche Exporte aktiver zulässiger Nutzer:innen ergänzt werden.

Die folgenden Felder sind erforderlich:

- `braze_id`
- `external_id`
- E-Mail-Adresse

Wenden Sie sich für weitere Informationen an Ihre Braze-Vertretung.
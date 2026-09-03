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

Die Integration von Braze und Merkury ermöglicht es Ihnen, die `MerkuryID` zu nutzen, um die Erkennungsraten von Website-Besucher:innen für Braze-Kund:innen zu erhöhen. Wenn Besucher:innen erkannt werden, die E-Mail-Abonnent:innen der Marke sind, aktualisiert Merkury das Braze-Profil und fügt die E-Mail-Adresse der Abonnent:innen hinzu. Die verbesserten Erkennungsfähigkeiten der `MerkuryID` steigern die Möglichkeiten für Engagement und Personalisierung und erhöhen unmittelbar die Versandmengen von E-Mails bei Website-Abbrüchen sowie den damit verbundenen Umsatz.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Merkle-Konto | Ein Merkle-Konto ist erforderlich, um diese Partnerschaft zu nutzen. |
| Merkle Client-ID | Erhalten Sie Ihre Client-ID von Ihrer Merkle-Vertretung. |
| Merkury-Tag | Platzieren Sie den Merkury-Tag von Merkle auf Ihrer Website. |
| Braze REST- und SDK-Endpunkt | Ihre REST- oder SDK-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics#endpoints) ab. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit den Berechtigungen `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Dieser kann unter **Braze-Dashboard > Entwicklungskonsole > REST-API-Schlüssel > Neuen API-Schlüssel erstellen** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% alert important %}
Die Anfragen des Merkury-Identitätskonnektors an Braze erfolgen innerhalb der Braze-API-Rate-Limits. Wenden Sie sich an Braze oder Ihre:n Merkle Account Manager:in, wenn Sie Fragen haben.<br><br>Merkury sendet mindestens eine Anfrage am Ende einer qualifizierten Sitzung.
{% endalert %}

## Side-by-Side-SDK-Integration

Nutzt Merkles clientseitigen Merkury-Tag, um Braze-Geräte zu erfassen und an den Merkury-Identity-Konnektor-Endpunkt zur Identifizierung weiterzuleiten.

### Schritt 1: Braze Web SDK-Tag einrichten {#step-1-setup-braze-web-sdk-tag}

Sie müssen das [Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-gtm) auf Ihrer Website bereitgestellt haben, um diese Integration nutzen zu können.

### Schritt 2: Merkles Merkury-Tag bereitstellen {#step-2-deploy-merkles-merkury-tag}

Stellen Sie den Merkury-Tag auf Ihrer Website bereit, um den Merkury-Identity-Konnektor auf Ihrer Website verfügbar zu machen. Ihr Merkle Account Manager:in stellt Ihnen eine detaillierte Anleitung mit Anweisungen zur Verfügung.

### Schritt 3: Angepasste Attribute erstellen {#step-3-create-custom-attributes}

Der Merkury-Identity-Konnektor befüllt die folgenden Felder, die Sie in Braze als [angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) erstellen müssen.

| Attributname | Datentyp | Beschreibung |
| --- | --- | --- |
| `hmid` | String | Merkles Merkury-ID |
| `confidence_score` | Zahl | Wie sicher Merkury die Identifizierung vornehmen konnte (1–8, niedriger ist besser) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 3: Angepasste Attribute erstellen" }

### Schritt 4: Merkle das E-Mail-Universum der Nutzer:innen bereitstellen {#step-4-provide-merkle-with-user-email-universe}

Merkle empfiehlt einen Segmentierungsexport Ihres zulässigen E-Mail-Universums. Darauf können tägliche Exporte aktiver zulässiger Nutzer:innen folgen.

Die folgenden Felder sind erforderlich:

- `braze_id`
- `external_id`
- E-Mail-Adresse

Wenden Sie sich an Ihre Braze-Vertretung für weitere Informationen.
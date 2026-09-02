---
nav_title: Importieren Sie Ihre E-Mail-Liste
article_title: Importieren Sie Ihre E-Mail-Liste in Braze
page_order: 4
page_type: reference
description: "In diesem Referenzartikel erfahren Sie Best Practices zum Importieren Ihrer E-Mail-Liste in Braze."
channel: email

---

# Importieren Sie Ihre E-Mail-Liste in Braze {#importing-email-lists}

> Ein wichtiger Schritt, um ein erfolgreicher E-Mail-Sender zu werden, ist die Sicherstellung einer hochwertigen E-Mail-Liste. Die richtige Verwaltung von E-Mail-Listen kann Ihre Zustellbarkeit verbessern und Ihnen präzisere und saubere Campaign-Ergebnisse liefern.

## Überlegungen vor dem Importieren {#considerations-before-importing}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Validieren Sie Ihre E-Mail-Listen {#validate-your-email-lists}

Bevor Sie Ihre E-Mail-Liste in Braze importieren, vergewissern Sie sich, dass Ihre Liste nur echte E-Mail-Adressen enthält. Eine hohe Bounce-Rate kann Ihrer Absender-Reputation schaden.

E-Mail-Listenbereinigungsdienste können dies für Sie übernehmen, indem sie feststellen, ob die E-Mail-Adresse der korrekten Syntax folgt und die physischen Eigenschaften einer E-Mail-Adresse aufweist, die E-Mail-Domain überprüfen und eine Verbindung zum E-Mail-Server herstellen, um zu verifizieren, ob die E-Mail-Adresse dort existiert.

### Prüfen Sie, ob eine E-Mail-Adresse bereits mit einem Kundenprofil verknüpft ist {#check-if-an-email-address-is-already-associated-with-a-user}

Bevor Sie eine Nutzer:in über die API oder das SDK anlegen, rufen Sie den Endpunkt [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) auf und geben Sie die `email_address` der Nutzer:in an. Wenn ein Kundenprofil zurückgegeben wird, ist diese Braze-Nutzer:in bereits mit dieser E-Mail-Adresse verknüpft.

Wir empfehlen dringend, bei der Erstellung neuer Nutzer:innen auf eindeutige E-Mail-Adressen zu achten und zu vermeiden, Nutzer:innen mit derselben E-Mail-Adresse zu übergeben oder zu importieren. Andernfalls können unbeabsichtigte Auswirkungen auf den Nachrichtenversand, das Targeting, das Reporting und andere Features auftreten.

Nehmen wir zum Beispiel an, Sie haben doppelte Profile, aber bestimmte angepasste Attribute oder Ereignisse befinden sich nur in einem Profil. Wenn Sie versuchen, Campaigns oder Canvases mit mehreren Kriterien zu triggern, kann Braze die Nutzer:in nicht als berechtigt identifizieren, da zwei Nutzerprofile vorhanden sind. Oder wenn eine Campaign eine E-Mail-Adresse anspricht, die von zwei Nutzer:innen geteilt wird, zeigt die Seite **Nutzer:innen suchen** beide Nutzerprofile als Empfänger:innen der Campaign an.

### Identifizieren Sie Ihre engagierten Nutzer:innen {#identify-your-engaged-users}

Um Ihre am stärksten engagierten Nutzer:innen zu identifizieren, entfernen Sie zunächst seit Langem inaktive Nutzer:innen. Es ist eine Best Practice, Nutzer:innen, die seit über sechs Monaten nicht mit einer E-Mail interagiert haben, nicht per E-Mail zu kontaktieren, da dies Ihrer Absender-Reputation schaden kann. Stellen Sie beim Importieren Ihrer E-Mail-Liste sicher, dass Sie nur Nutzer:innen einschließen, die innerhalb der letzten sechs Monate eine E-Mail von Ihnen geöffnet haben.

Langfristig sollten Sie auch die Implementierung einer [Sunset-Richtlinie]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) in Betracht ziehen.

### Vermeiden Sie Unterdrückungslisten {#avoid-suppression-lists}

Wenn Sie von einem bestehenden E-Mail-Anbieter wechseln, stellen Sie sicher, dass Sie keine Nutzer:innen aus einer Unterdrückungsliste importieren. Unterdrückungslisten enthalten E-Mail-Adressen, die sich entweder abgemeldet haben, Ihre E-Mails als Spam markiert haben oder einen Hard Bounce verursacht haben.

## Methoden für den Import {#methods-for-importing}

Sobald Sie Ihre E-Mail-Liste vorbereitet haben, gibt es mehrere Möglichkeiten, Nutzer:innen in Braze zu importieren, beispielsweise über die Braze REST API oder CSV-Dateien. Lesen Sie mehr in unserem speziellen Artikel zum [Nutzerimport]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).
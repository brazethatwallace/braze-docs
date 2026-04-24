---
nav_title: E-Mail-Liste importieren
article_title: E-Mail-Liste in Braze importieren
page_order: 4
page_type: reference
description: "Dieser Referenzartikel behandelt Best Practices für den Import Ihrer E-Mail-Liste in Braze."
channel: email

---

# E-Mail-Liste in Braze importieren {#importing-email-lists}

> Ein wichtiger Schritt auf dem Weg zum erfolgreichen E-Mail-Versender ist es, sicherzustellen, dass Sie über eine hochwertige E-Mail-Liste verfügen. Eine ordnungsgemäße Verwaltung der E-Mail-Liste kann Ihre Zustellbarkeit verbessern und Ihnen genauere und sauberere Kampagnenergebnisse liefern.

## Überlegungen vor dem Import

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### E-Mail-Listen validieren

Bevor Sie Ihre E-Mail-Liste in Braze importieren, stellen Sie sicher, dass Ihre Liste nur echte E-Mail-Adressen enthält. Eine hohe Bounce-Rate kann Ihre Absender-Reputation beschädigen.

E-Mail-Listen-Bereinigungsdienste können dies für Sie übernehmen, indem sie prüfen, ob die E-Mail-Adresse der korrekten Syntax folgt und die physischen Eigenschaften einer E-Mail-Adresse aufweist, die E-Mail-Domain verifizieren und eine Verbindung zum E-Mail-Server herstellen, um zu authentifizieren, ob die E-Mail-Adresse dort existiert.

### Prüfen, ob eine E-Mail-Adresse bereits mit einer Nutzer:in verknüpft ist

Bevor Sie über die API oder das SDK Nutzer:innen erstellen, rufen Sie den Endpunkt [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) auf und geben Sie die `email_address` der Nutzer:in an. Wenn ein Nutzerprofil zurückgegeben wird, ist diese Braze-Nutzer:in bereits mit dieser E-Mail-Adresse verknüpft.

Wir empfehlen dringend, bei der Erstellung neuer Nutzer:innen auf eindeutige E-Mail-Adressen zu achten und zu vermeiden, Nutzer:innen mit derselben E-Mail-Adresse zu übergeben oder zu importieren. Andernfalls können unbeabsichtigte Auswirkungen auf den Nachrichtenversand, das Targeting, das Reporting und andere Features auftreten.

Nehmen wir zum Beispiel an, Sie haben doppelte Profile, aber bestimmte angepasste Attribute oder Events befinden sich nur in einem Profil. Wenn Sie versuchen, Kampagnen oder Canvases mit mehreren Kriterien zu triggern, kann Braze die Nutzer:in nicht als berechtigt identifizieren, da zwei Nutzerprofile vorhanden sind. Oder wenn eine Kampagne eine E-Mail-Adresse anspricht, die von zwei Nutzer:innen geteilt wird, zeigt die Seite **Nutzer:innen suchen** beide Nutzerprofile als Empfänger:innen der Kampagne an.

### Engagierte Nutzer:innen identifizieren

Um Ihre am stärksten engagierten Nutzer:innen zu identifizieren, entfernen Sie zunächst seit Langem inaktive Nutzer:innen. Es ist eine Best Practice, Nutzer:innen, die seit über sechs Monaten nicht mit einer E-Mail interagiert haben, nicht per E-Mail zu kontaktieren, da dies Ihre Absender-Reputation beschädigen kann. Stellen Sie beim Import Ihrer E-Mail-Liste sicher, dass Sie nur Nutzer:innen einschließen, die innerhalb der letzten sechs Monate eine E-Mail von Ihnen geöffnet haben.

Langfristig sollten Sie auch die Implementierung einer [Sunset-Richtlinie]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/) in Betracht ziehen.

### Unterdrückungslisten vermeiden

Wenn Sie von einem bestehenden E-Mail-Anbieter wechseln, stellen Sie sicher, dass Sie keine Nutzer:innen aus einer Unterdrückungsliste importieren. Unterdrückungslisten enthalten E-Mail-Adressen, die sich entweder abgemeldet haben, Ihre E-Mails als Spam markiert haben oder einen Hard Bounce verursacht haben.

## Methoden für den Import

Sobald Sie Ihre E-Mail-Liste vorbereitet haben, gibt es mehrere Möglichkeiten, Nutzer:innen in Braze zu importieren, beispielsweise über die Braze REST API oder CSV-Dateien. Lesen Sie mehr in unserem speziellen Artikel zum [Nutzerimport]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/).
---
nav_title: Angepasste Daten
article_title: Angepasste Daten
page_order: 0
page_type: landing
description: "Angepasste Daten sind die Grundlage Ihrer Engagement-Strategie in Braze. Erfahren Sie mehr über angepasste Attribute, Events, Kataloge, Datentypen und wie Sie Ihre Datenintegrität sicherstellen."
---

# Angepasste Daten {#custom-data}

> Angepasste Daten sind der Treibstoff für Ihre Engagement-Strategie. Während Standardattribute wie Vorname und Land bereits integriert sind, können Sie mit angepassten Daten die einzigartigen Details erfassen, die Ihre Beziehung zu Ihren Kund:innen ausmachen – vom Lieblingsfilmgenre bis zum genauen Zeitpunkt eines abgeschlossenen Kaufs.

Indem Sie diese Informationen in Braze einbringen, können Sie über generisches Messaging hinausgehen und Erlebnisse schaffen, die sich persönlich, zeitnah und relevant anfühlen. Sie können diese Daten nutzen, um präzise Segmente zu erstellen, Nachrichteninhalte mit Liquid zu personalisieren und automatisierte Journeys basierend auf Realtime-Verhalten zu triggern.

## Attribute und Events {#attributes-and-events}

Die wichtigste Entscheidung, die Sie bei der Einrichtung Ihrer Daten treffen, ist die Wahl zwischen einem Attribut und einem Event.

### Angepasste Attribute: Wer Ihre Nutzer:innen sind {#custom-attributes-who-your-users-are}

Stellen Sie sich angepasste Attribute als die persistenten Merkmale oder Eigenschaften Ihrer Nutzer:innen vor. Sie eignen sich am besten zum Speichern von Informationen, die einen aktuellen Zustand darstellen oder sich selten ändern.

- **Anwendungsfall:** Sie könnten ein `loyalty_tier`-Attribut verwenden, um zwischen Ihren „Silver“- und „Gold“-Mitgliedern zu unterscheiden.
- **Personalisierung:** Attribute eignen sich hervorragend für die Personalisierung. Sie können die `favorite_category` einer Nutzerin oder eines Nutzers in eine E-Mail-Betreffzeile einfügen, um Aufmerksamkeit zu erzeugen.
- **Speicherung:** Diese Daten bleiben dauerhaft im Nutzerprofil gespeichert, solange das Profil aktiv ist.

Weitere Informationen finden Sie unter [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).

### Angepasste Events: Was Ihre Nutzer:innen tun {#custom-events-what-your-users-do}

Angepasste Events erfassen bestimmte Aktionen, die Ihre Nutzer:innen zu einem bestimmten Zeitpunkt ausführen. Es handelt sich um wertvolle Interaktionen, die Ihnen helfen, das „Wann“ und „Wie oft“ des Nutzerverhaltens zu verstehen.

- **Anwendungsfall:** Wenn eine Nutzerin oder ein Nutzer eine Registrierung abschließt, können Sie ein `completed_registration`-Event protokollieren.
- **Triggern:** Events sind die primäre Methode, um eine aktionsbasierte Zustellung zu triggern. Sie können eine „Willkommen“-Push-Benachrichtigung genau in dem Moment senden, in dem das `completed_registration`-Event protokolliert wird.
- **Metadaten:** Sie können einem Event mithilfe von Event-Eigenschaften zusätzliche Details hinzufügen, z. B. den Namen des Artikels, der in den Warenkorb gelegt wurde.
- **Analytics:** Events ermöglichen Segmentierung, Berichte und Analytics, sodass Sie Engagement messen und Ihr Messaging optimieren können.

Weitere Informationen finden Sie unter [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/).

## Kataloge {#catalogs}

Während sich Attribute und Events auf Ihre Nutzer:innen konzentrieren, ermöglichen Ihnen Kataloge, nicht-nutzerbezogene Daten wie Produktbestände, Kursdetails oder Veranstaltungslisten einzubringen.

Indem Sie diese Metadaten per CSV oder API importieren, können Sie Ihre Nachrichten mit Informationen anreichern, die nicht im Nutzerprofil gespeichert sind. Sie können beispielsweise einen Katalog verwenden, um Kund:innen automatisch zu benachrichtigen, wenn ein zuvor angesehener Artikel wieder auf Lager ist oder im Preis gesunken ist.

Weitere Informationen finden Sie unter [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs/).

## Datentypen {#data-types}

Braze unterstützt mehrere Datentypen für Ihre angepassten Daten – darunter Boolescher Wert, Zahl, String, Array, Zeit und Objekt – jeweils mit spezifischem Verhalten und Segmentierungsoptionen. Der gewählte Datentyp beeinflusst, wie Sie in Campaigns und Segments filtern und personalisieren können.

Eine vollständige Referenz der unterstützten Datentypen für angepasste Attribute, Event-Eigenschaften und Kataloge finden Sie unter [Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/).

## Datenintegrität verwalten {#managing-your-data-integrity}

Braze bietet mehrere Tools, die Ihnen helfen, Ihre angepassten Daten zu verwalten, während sich Ihre Strategie weiterentwickelt.

### Datentyp-Erkennung und -Änderungen {#data-type-detection-and-changes}

Braze erkennt automatisch den Datentyp (z. B. eine Zahl oder einen String) für den ersten Wert, den es für ein Attribut erhält. Um die Genauigkeit zu gewährleisten, sollte Ihr Team konsistente Datentypen über alle Umgebungen hinweg senden. Wenn Sie einen Datentyp ändern müssen, beachten Sie, dass bestehende Daten in Nutzerprofilen nicht rückwirkend aktualisiert werden, was sich auf Ihre Segmente auswirken kann.

### Blocklist und Löschen {#blocklist-and-delete}

Wenn Sie feststellen, dass bestimmte Attribute oder Events nicht mehr nützlich sind oder versehentlich hinzugefügt wurden, können Sie sie aus Ihrem Workspace entfernen.

- **Blocklist:** Dies verhindert, dass Braze neue Daten für dieses Objekt erfasst. Die Daten erscheinen nicht mehr in Filtern oder Grafiken, bleiben aber in den bestehenden Profilen erhalten.
- **Löschen:** Dies entfernt die Daten dauerhaft aus allen Nutzerprofilen. Sie müssen ein Datenobjekt 7 Tage lang auf die Blocklist setzen, bevor es zum Löschen freigegeben wird.

Weitere Informationen finden Sie unter [Angepasste Daten verwalten]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/) und [Angepasste Daten auf die Blocklist setzen]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).
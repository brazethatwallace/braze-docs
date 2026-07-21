---
nav_title: Datenaufbewahrung
article_title: Datenaufbewahrung
alias: /data_retention/
description: "Dieser Referenzartikel enthält allgemeine Informationen zur Datenaufbewahrung bei Braze."
page_type: reference
page_order: 2.5

---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Informationen zur Datenaufbewahrung bei Braze {#braze-data-retention-information}

*Zuletzt überarbeitet am 1. April 2024*

> Dieser Artikel enthält allgemeine Informationen zur Datenaufbewahrung bei Braze.<br><br>Die in Braze gespeicherten Daten werden aufbewahrt und können für die Segmentierung, Personalisierung und das Targeting während der Lifetime des Kundenkontos verwendet werden. Das bedeutet, dass Daten wie Nutzerprofil-Attribute, angepasste Attribute, angepasste Events und Käufe für aktive Nutzer:innen auf unbestimmte Zeit gespeichert werden, sofern sie nicht von der Kund:in entfernt werden, und zwar für die Dauer des Vertrages.<br><br>Braze verfügt über Features, Prozesse und APIs, um automatisch gute Datenhygienepraktiken zur Einhaltung der DSGVO und anderer bewährter Praktiken zu implementieren. Die folgenden Abschnitte beschreiben, wie die Datenaufbewahrung gehandhabt wird.

## Von Kund:innen verwaltete Datenaufbewahrung über das Braze-Dashboard oder die API {#data-retention-handled-by-customers-through-brazes-dashboard-or-api}

Braze ermöglicht es seinen Kund:innen, komplette Nutzerprofile und Attribut-Daten selbst aus ihrem Workspace zu löschen.

Das heißt, Sie können:
- Nutzerprofile mit dem Braze-Endpunkt [Delete user API]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) löschen
- Attribute in Nutzerprofilen über den Braze-Endpunkt [Track user API]({{site.baseurl}}/api/endpoints/user_data/post_user_track) löschen (null) oder ändern

Verhaltensbezogene Events können nicht aus einem Nutzerprofil gelöscht werden (angepasste Events, Sitzungen, Campaigns, Käufe). Um diese Events zu entfernen, müssen Sie das gesamte Nutzerprofil löschen.

Um den Datenschutz zu gewährleisten, müssen Sie möglicherweise auf Anfrage einer Nutzer:in alle personenbezogenen Daten löschen, die sich auf diese Nutzer:in beziehen. Eine Anleitung finden Sie auf unserer Seite für [technische Unterstützung zum Datenschutz]({{site.baseurl}}/help/dp-technical-assistance#the-right-to-erasure).

{% alert note %}
Eine Nutzer:in kann mehrere Profile haben, und Sie müssen möglicherweise mehrere Profile löschen, um alle Daten einer einzelnen Nutzer:in zu löschen. Befolgen Sie die Anweisungen auf der Seite der technischen Unterstützung zum Datenschutz, um alle Daten einer Nutzer:in vollständig zu löschen.
{% endalert %}

## Von Braze verwaltete Datenaufbewahrung für bestimmte Features der Braze-Dienste {#data-retention-handled-by-braze-for-specific-features-of-the-braze-services}

### Braze-Datenbank: Automatische Archivierung/Löschung abgewanderter Nutzer:innen {#braze-database-automatic-archivingdeletion-of-churned-users}

Jede Woche führt Braze einen Prozess durch, um inaktive und ruhende Nutzer:innen aus den Braze-Diensten zu entfernen. Im Allgemeinen handelt es sich dabei um Nutzer:innen, die nicht erreichbar sind (z. B. keine E-Mail-Adresse, keine Telefonnummer, kein Push-Token haben, Ihre Apps nicht nutzen oder Ihre Websites nicht besuchen), die keine Aktivitäten in ihrem Nutzerprofil aufgezeichnet haben und mit denen kein Messaging oder Engagement über Braze stattgefunden hat. Dies geschieht, um die Grundsätze der DSGVO und bewährte Verfahren einzuhalten. Mehr über diesen Prozess erfahren Sie auf unserer Seite <a href="/docs/user_archival">Definitionen der Nutzerarchivierung</a>.

{% alert note %}
Kund:innen haben die volle Kontrolle darüber, ob eine Nutzer:in inaktiv oder ruhend ist, und können die Archivierung von Nutzerprofilen verhindern, indem sie in regelmäßigen Abständen einen Datenpunkt aufzeichnen. Braze Canvas bietet die Möglichkeit, dies automatisch zu tun, sodass Sie diese Funktion für einige oder alle Ihrer inaktiven oder ruhenden Nutzer:innen effektiv ausschalten können.
{% endalert %}

### Daten zu Campaign- und Canvas-Interaktionen {#campaign-and-canvas-interactions-data}

Messaging-Interaktionsdaten beschreiben, wie Nutzer:innen mit einer Campaign oder einem Canvas interagieren, die/den sie erhalten haben (zum Beispiel, wenn Nutzer:innen Campaign A öffnen oder Variante A erhalten). Diese Daten werden für Retargeting verwendet. Weitere Informationen über die Verfügbarkeit von Messaging-Interaktionsdaten finden Sie unter [Über die Verfügbarkeit von Messaging-Interaktionsdaten]({{site.baseurl}}/messaging_interaction_data).

## Von Braze verwaltete Datenaufbewahrung {#data-retention-handled-by-braze}

Die folgenden Aufbewahrungsrichtlinien beziehen sich auf die Einhaltung der DSGVO und der Datenschutzbestimmungen durch Braze und betreffen die vorübergehende Speicherung von Daten, die unsere internen Systeme durchlaufen. Diese Aufbewahrungsrichtlinien haben keine Auswirkungen auf die Braze-Dienste und dienen der Information Ihrer Teams für Recht und Datenschutz.

### Braze-Server: Kurzfristige Aufbewahrung für Wiederherstellungszwecke {#braze-servers-short-term-retention-for-recovery-purposes}

Daten, die von Braze an bestimmte Unterauftragsverarbeiter gesendet werden, können noch bis zu 90 Tage in den internen Systemen von Braze vorhanden sein.

### Braze Data Lake – Datenaufbewahrung {#braze-data-lake-data-retention}

Die Daten, die Kund:innen im Braze-Dashboard zur Verfügung stehen, sind größtenteils aggregiert. Detaillierte Protokolle werden in einer separaten, von Braze erstellten Datenbank (dem „Data Lake“) gespeichert. Data-Lake-Daten werden für aggregierte Berichte und andere erweiterte Funktionen verwendet. Braze entfernt persönlich identifizierbare Informationen aus den im Data Lake gespeicherten Ereignisdaten nach zwei Jahren (weitere Informationen finden Sie auf unserer Seite [Snowflake Datenaufbewahrung]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention#snowflake-data-retention)).

Wenn Sie unsere APIs verwenden, um Nutzerprofile zu löschen oder Attribute von Nutzerprofilen zu löschen oder zu ändern, kann es bis zu drei Wochen dauern, bis diese Daten aus dem Data Lake von Braze gelöscht werden. Das Löschen von Daten im Data Lake hat keinen Einfluss auf die Segmentierung oder Personalisierung, sondern stellt sicher, dass die Daten aus allen Braze-Systemen entfernt werden.

### Braze-Backup-Server {#braze-backup-servers}

Wenn Daten aus Ihrer Produktionsinstanz gelöscht werden, verbleiben die Daten sechs Monate lang auf den Backup-Servern von Braze und werden dann gemäß unseren internen Verfahren gelöscht.
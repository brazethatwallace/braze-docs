---
nav_title: Datenaufbewahrung
article_title: "Informationen zur Datenaufbewahrung bei Braze"
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

## Von Kund:innen über das Braze-Dashboard oder die API verwaltete Datenaufbewahrung {#data-retention-handled-by-customers-through-brazes-dashboard-or-api}

Braze ermöglicht es seinen Kund:innen, vollständige Nutzerprofile und Attributdaten selbst aus ihrem Workspace zu löschen.

Das bedeutet, Sie können:
- Nutzerprofile mit dem Braze-[Endpunkt zum Löschen von Nutzer:innen]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) löschen
- Attribute in Nutzerprofilen mit dem Braze-[Endpunkt zum Tracken von Nutzer:innen]({{site.baseurl}}/api/endpoints/user_data/post_user_track) löschen (auf null setzen) oder ändern

Verhaltensbezogene Events können nicht aus einem Nutzerprofil gelöscht werden (angepasste Events, Sitzungen, Campaigns, Käufe). Um diese Events zu entfernen, müssen Sie das gesamte Nutzerprofil löschen.

Zur Einhaltung des Datenschutzes müssen Sie möglicherweise auf Anfrage einer/eines Nutzer:in alle personenbezogenen Daten löschen, die sich auf diese:n Nutzer:in beziehen. Anweisungen dazu finden Sie auf unserer Seite zur [technischen Unterstützung zum Datenschutz]({{site.baseurl}}/help/dp-technical-assistance#the-right-to-erasure).

{% alert note %}
Eine/ein Nutzer:in kann mehrere Profile haben, und Sie müssen möglicherweise mehrere Profile löschen, um alle Daten zu entfernen, die sich auf eine:n einzelne:n Nutzer:in beziehen. Folgen Sie den Anweisungen auf der Seite zur technischen Unterstützung zum Datenschutz, um alle Daten einer/eines Nutzer:in vollständig zu löschen.
{% endalert %}

## Von Braze verwaltete Datenaufbewahrung für bestimmte Features der Braze-Dienste {#data-retention-handled-by-braze-for-specific-features-of-the-braze-services}

### Braze-Datenbank: Automatische Archivierung/Löschung abgewanderter Nutzer:innen {#braze-database-automatic-archivingdeletion-of-churned-users}

Braze führt jede Woche einen Prozess durch, um inaktive und inaktive Nutzer:innen aus den Braze-Diensten zu entfernen. Im Allgemeinen handelt es sich dabei um Nutzer:innen, die nicht erreichbar sind (z. B. keine E-Mail-Adresse, keine Telefonnummer, kein Push-Token haben, Ihre Apps nicht nutzen oder Ihre Websites nicht besuchen), bei denen keine Aktivität in ihrem Nutzerprofil aufgezeichnet wurde und die nicht über Braze kontaktiert oder angesprochen wurden. Dies geschieht in Übereinstimmung mit den Grundsätzen und Best Practices der DSGVO. Weitere Informationen zu diesem Prozess finden Sie auf unserer Seite zu den <a href="/docs/user_archival">Definitionen der Nutzerarchivierung</a>.

{% alert note %}
Kund:innen haben die volle Kontrolle darüber, ob Nutzer:innen als inaktiv eingestuft werden, und können die Archivierung von Nutzerprofilen verhindern, indem sie in regelmäßigen Abständen einen Datenpunkt aufzeichnen. Braze Canvas bietet die Möglichkeit, dies automatisch zu tun, sodass Sie diese Funktionalität für einige oder alle Ihrer inaktiven Nutzer:innen effektiv deaktivieren können.
{% endalert %}

### Interaktionsdaten von Campaigns und Canvases {#campaign-and-canvas-interactions-data}

Messaging-Interaktionsdaten beziehen sich darauf, wie Nutzer:innen mit einer Campaign oder einem Canvas interagieren, die sie erhalten haben (zum Beispiel, wenn Nutzer:innen Campaign A öffnen oder Variante A erhalten). Diese Daten werden für Retargeting verwendet. Weitere Informationen zur Verfügbarkeit von Messaging-Interaktionsdaten finden Sie unter [Über die Verfügbarkeit von Messaging-Interaktionsdaten]({{site.baseurl}}/messaging_interaction_data).

## Von Braze verwaltete Datenaufbewahrung {#data-retention-handled-by-braze}

Die folgenden Aufbewahrungsrichtlinien beziehen sich auf die Einhaltung der DSGVO und der Datenschutzvorschriften durch Braze und betreffen die vorübergehende Datenspeicherung, während Daten unsere internen Systeme durchlaufen. Diese Aufbewahrungsrichtlinien haben keine Auswirkungen auf die Braze-Dienste und dienen der Information Ihrer Rechts- und Datenschutzteams.

### Braze-Server: Kurzfristige Aufbewahrung zu Wiederherstellungszwecken {#braze-servers-short-term-retention-for-recovery-purposes}

Daten, die von Braze an bestimmte Unterauftragsverarbeiter gesendet werden, können noch bis zu 90 Tage in den internen Systemen von Braze vorhanden sein.

### Datenaufbewahrung im Braze Data Lake {#braze-data-lake-data-retention}

Die Daten, die Kund:innen im Braze-Dashboard zur Verfügung stehen, sind größtenteils aggregiert. Detaillierte Protokolle werden in einer separaten, von Braze erstellten Datenbank (dem „Data Lake“) aufbewahrt. Data-Lake-Daten werden für aggregierte Berichterstattung und andere erweiterte Funktionen verwendet. Braze entfernt persönlich identifizierbare Informationen aus Ereignisdaten, die im Data Lake gespeichert sind, nach zwei Jahren (weitere Informationen finden Sie auf unserer Seite zur [Snowflake Datenaufbewahrung]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_retention)).

Wenn Sie unsere APIs verwenden, um Nutzerprofile zu löschen oder Attribute aus Nutzerprofilen zu löschen oder zu ändern, kann es bis zu drei Wochen dauern, bis diese Daten aus dem Data Lake von Braze gelöscht werden. Die Löschung von Daten im Data Lake wirkt sich nicht auf die Segmentierung oder Personalisierung aus, sondern stellt sicher, dass die Daten aus allen Braze-Systemen entfernt werden.

### Braze-Backup-Server {#braze-backup-servers}

Wenn Daten aus Ihrer Produktionsinstanz gelöscht werden, verbleiben die Daten sechs Monate lang auf den Backup-Servern von Braze und werden dann gemäß unseren internen Prozessen gelöscht.
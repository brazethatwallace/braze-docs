---
nav_title: Erste Schritte
article_title: "Erste Schritte&#58; Braze Übersicht"
page_order: 1
page_type: reference
description: "Machen Sie sich mit den wichtigsten Konzepten vertraut, die Sie bei der Arbeit mit Braze kennen müssen."

---

# Erste Schritte: Braze Übersicht {#get-started-braze-overview}

> Willkommen bei Braze! Diese Artikelsammlung hilft Ihnen beim Einstieg in unsere Plattform und macht Sie mit den wichtigsten Begriffen, Features und Funktionalitäten von Braze vertraut. Auf dieser Seite werden die grundlegenden Konzepte vorgestellt, die Sie bei der Arbeit mit Braze kennen müssen.

{% alert tip %}
Wir empfehlen Ihnen, neben diesen Artikeln auch unseren kostenlosen [Practitioner Learning Path](https://learning.braze.com/page/practitioner) zu absolvieren. Dafür ist keine spezielle Anmeldung oder ein Konto erforderlich. Wenn Sie Entwickler:in sind und einen technischen Überblick über Braze suchen, schauen Sie sich auch <a href="/docs/developer_guide/getting_started/platform_overview">Erste Schritte für Entwickler:innen</a> an.
{% endalert %}

In den Abschnitten zu den ersten Schritten konzentrieren wir uns auf die gängigen Implementierungen von Braze. Braze ist jedoch unglaublich flexibel und kann so angepasst werden, dass es Ihrem Unternehmen auf vielfältige Weise Mehrwert bietet. Aus Gründen der Übersichtlichkeit und Kürze haben wir einen beschreibenden Überblick über die Standardeinrichtung gegeben, anstatt starre Anweisungen zu liefern. Wir wissen, dass jedes Unternehmen seine eigenen Bedürfnisse hat, und Braze ist so konzipiert, dass es eine Vielzahl von Anpassungsmöglichkeiten bietet, die auf Ihre speziellen Anforderungen zugeschnitten werden können.

Lassen Sie uns gemeinsam die Möglichkeiten von Braze entdecken.

## So funktioniert Braze {#how-braze-works}

Braze ist eine geschäftskunden-Engagement-Plattform, die Marken jeder Größe dabei hilft, personalisierte und gezielte Kampagnen über verschiedene Kanäle zu erstellen. Braze gibt Ihnen die Möglichkeit, Ihren Kund:innen zuzuhören, zu verstehen, was ihr Verhalten signalisiert, und dann zu handeln, indem Sie die richtige Nachricht über den richtigen Kanal zur richtigen Zeit senden.

{% alert tip %}
Stellen Sie sicher, dass Sie [Ihre Kolleg:innen zu Braze hinzufügen]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users), damit sie die Plattform gemeinsam mit Ihnen erkunden können.
{% endalert %}

## Nutzer:innen und Segmente {#users-and-segments}

Nutzer:innen sind Ihre Kund:innen – die Personen, die die Nachrichten erhalten, die Sie mit Braze versenden. Alle Daten, die Sie über eine:n Nutzer:in sammeln und in Braze aufnehmen, werden in deren Nutzerprofil gespeichert, z. B. demografische Daten, persönliche Informationen, Vorlieben und Verhaltensweisen. Diese Informationen bilden die Grundlage für Ihr Messaging und ermöglichen es Ihnen, Ihre Nachrichten auf die richtigen Nutzer:innen zuzuschneiden.

![Screenshot eines Nutzerprofils in Braze.]({% image_buster /assets/img/getting_started/user_profile.png %})

Segmente unterteilen Ihren Kundenstamm in kleinere Gruppen, die Sie dann mit spezifischem Messaging ansprechen können. Sie können verschiedene Variablen verwenden, um Segmente zu erstellen – von Merkmalen wie Geschlecht, Standort und Alter bis hin zu Verhaltensweisen wie Interaktionsmustern mit früheren Kampagnen oder der Position in der geschäftskunden Journey.

Segmente sind dynamisch – Nutzer:innen können in Echtzeit in Segmente ein- und ausgegliedert werden, basierend auf ihrem Verhalten und ihrer Beziehung zu Ihrer Marke. So stellen Sie sicher, dass Ihre Kund:innen jederzeit die für sie relevantesten Nachrichten erhalten. Sie können so viele Segmente erstellen, wie Sie für Ihr Targeting und Messaging benötigen.

![Segmente sind dynamisch – Nutzer:innen können in Echtzeit in Segmente ein- und ausgegliedert werden, basierend auf ihrem Verhalten und ihrer Beziehung zu Ihrer Marke. So stellen Sie sicher, dass Ihre Kund:innen jederzeit die für sie relevantesten Nachrichten erhalten. Sie können so viele Segmente erstellen, wie Sie für Ihr Targeting und Messaging benötigen.]({% image_buster /assets/img/getting_started/segment.png %})

Mehr dazu finden Sie hier: [Erste Schritte: Nutzer:innen und Segmente]({{site.baseurl}}/user_guide/get_started/users_and_segments).

## Campaigns und Canvases {#campaigns-and-canvases}

Campaigns und Canvases sind die Werkzeuge, mit denen Sie Nachrichten an Ihre Nutzer:innen senden.

Campaigns eignen sich am besten für einzelne Nachrichten, die über verschiedene Kanäle an ein bestimmtes Zielgruppen-Segment gesendet werden. Sie können jeden unserer unterstützten Messaging-Kanäle in Ihrer Campaign nutzen (E-Mail, Push, In-App-Nachrichten, SMS und mehr).

Canvases sind fortschrittliche Campaign-Workflows, mit denen Sie personalisierte geschäftskunden Journeys über mehrere Kanäle hinweg automatisieren und orchestrieren können. Innerhalb eines Canvas können Sie Verzweigungslogiken, Verzögerungen, Entscheidungspunkte und Konversions-Events einrichten, um Kund:innen durch eine Reihe von Interaktionen zu führen. Canvases sorgen für eine konsistente und nahtlose Kommunikation über verschiedene Touchpoints hinweg und erhöhen so die Chancen auf Engagement und Conversion.

Mehr dazu finden Sie hier: [Erste Schritte: Campaigns und Canvases]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases).

## Workspaces {#workspaces}

Workspaces fassen Ihre Daten – Nutzer:innen, Segmente, Campaigns und Canvases – an einem Ort zusammen. Informationen werden nicht zwischen Workspaces geteilt. Behalten Sie das im Hinterkopf, wenn Sie Websites und Apps zu Ihren Workspaces hinzufügen. Als Best Practice empfehlen wir, nur verschiedene Versionen derselben oder sehr ähnlicher Apps in einem Workspace zusammenzufassen.

Beispiele für die Verwendung von Workspaces:

- Verschiedene Produktlinien oder Apps
- Unterschiedliche Zielgruppen (z. B. Lieferfahrer:innen und Kund:innen)
- Separate Unternehmen
- Testumgebung

Mehr dazu finden Sie hier: [Erste Schritte: Workspaces]({{site.baseurl}}/user_guide/get_started/workspaces).

## Integration von Braze {#integrating-braze}

Braze ist so konzipiert, dass Sie schnell und einfach loslegen können. Unsere durchschnittliche Time-to-Value beträgt sechs Wochen bei unserem Kundenstamm von Hunderten von Marken.

![Grafik zur Time-to-Value bei der Integration von Braze.]({% image_buster /assets/img/getting_started/timetovalue.png %})

Hier ist das Braze-Framework zur Einschätzung der Dauer Ihrer Integration, basierend auf vier Komponenten, an denen Sie parallel arbeiten können. Die typische Spanne liegt zwischen 30 und 180 Tagen, wobei die meisten Konten ihre Integration innerhalb von 45 bis 60 Tagen abschließen.

- **Komplexitätsgrad der Campaign-Migration:** Die Zeit für die Migration von Campaigns hängt davon ab, wie viele Sie haben, wie personalisiert sie sind und welche Ressourcen Ihnen zur Verfügung stehen. Wenn Sie weniger als zehn Campaigns migrieren müssen, dauert es weniger als 60 Tage. Bei mehr als 100 Campaigns wird es komplizierter. Wenn nur eine Person 100 Campaigns migriert, ist das etwas anderes, als wenn 10 Personen 100 migrieren.

{% alert tip %}
Benötigen Sie Hilfe bei Ihrer Migration? Unsere [zertifizierten Braze-Partner](https://www.braze.com/partners/solutions-partners) können Sie unterstützen!
{% endalert %}

- **E-Mail-Volumen:** Um E-Mails zu versenden, müssen Sie Ihre IPs aufwärmen. [IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) ist der Prozess des Aufbaus einer Absender-Reputation mit Ihren neu zugewiesenen IP-Adressen. Wenn Sie weniger als 2–3 Millionen E-Mails pro Tag versenden, sollte Ihr IP-Warming 30 Tage oder weniger dauern. Beachten Sie dabei Ihre Spitzenvolumen. Wenn Sie normalerweise 2 Millionen E-Mails pro Tag versenden, aber für einen saisonalen Zeitraum 7 Millionen planen, sollten Sie auf dieses „Spitzen“-Volumen aufwärmen. Absender mit hohem Volumen können mehrere IPs verwenden, um den Warming-Prozess zu beschleunigen.
- **Organisatorische Komplexität:** Unser Onboarding-Prozess kann an die Bedürfnisse Ihres Unternehmens angepasst werden. Ob Sie eine einzelne Geschäftseinheit, ein Center of Excellence, mehrere unabhängige Einheiten oder Agenturen zur Verstärkung Ihrer Teams einsetzen – Braze hat Erfahrung mit allen Szenarien.
- **Komplexität der Dateninfrastruktur:** Wenn Sie nur das Braze SDK implementieren oder bereits über eine geschäftskunden Data Platform (CDP) verfügen, ist es möglich, alles in nur 30 Tagen einzurichten. Die Verwendung einer modernen CDP kann den Prozess beschleunigen. Wenn Sie jedoch viele Backend-Systeme, Tools oder Datenbanken mit Braze verbinden müssen, kann es länger dauern und mehr dedizierte Ressourcen erfordern, um die Einrichtung abzuschließen.

Mehr dazu finden Sie hier: [Erste Schritte: Übersicht über die Integration]({{site.baseurl}}/user_guide/get_started/integrations).
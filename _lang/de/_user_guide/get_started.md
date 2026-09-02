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

Braze ist eine Customer-Engagement-Plattform, die Marken jeder Größe dabei unterstützt, personalisierte und zielgerichtete Campaigns über verschiedene Kanäle zu erstellen. Braze gibt Ihnen die Möglichkeit, Ihren Kund:innen zuzuhören, zu verstehen, was ihr Verhalten signalisiert, und dann zu handeln, indem Sie Kund:innen die richtige Nachricht über den richtigen Kanal zum richtigen Zeitpunkt senden.

{% alert tip %}
Vergessen Sie nicht, [Ihre Kolleg:innen zu Braze hinzuzufügen]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users), damit sie die Plattform gemeinsam mit Ihnen erkunden können.
{% endalert %}

## Nutzer:innen und Segments {#users-and-segments}

Nutzer:innen sind Ihre Kund:innen – die Personen, die die Nachrichten erhalten, die Sie mit Braze versenden. Alle Daten, die Sie über Nutzer:innen sammeln und in Braze einspeisen, werden in deren Kundenprofil gespeichert, z. B. demografische Angaben, persönliche Informationen, Präferenzen und Verhaltensweisen. Diese Informationen bilden die Grundlage für Ihr Messaging und ermöglichen es Ihnen, Ihre Nachrichten auf die richtigen Nutzer:innen zuzuschneiden.

![Screenshot zu Nutzer:innen und Segments.]({% image_buster /assets/img/getting_started/user_profile.png %})

Segments unterteilen Ihren Kundenstamm in kleinere Gruppen, die Sie dann mit spezifischem Messaging ansprechen können. Sie können verschiedene Variablen verwenden, um Segments zu erstellen – von Merkmalen wie Geschlecht, Standort und Alter bis hin zu Verhaltensweisen wie Interaktionsmustern mit früheren Campaigns oder der aktuellen Position in der Customer Journey.

Segments sind dynamisch – Nutzer:innen können in Echtzeit in Segments aufgenommen oder daraus entfernt werden, basierend auf ihrem Verhalten und ihrer Beziehung zu Ihrer Marke. So wird sichergestellt, dass Ihre Kund:innen jederzeit die für sie relevantesten Nachrichten erhalten. Sie können so viele Segments erstellen, wie Sie für Ihr Targeting und Messaging benötigen.

![Segments sind dynamisch – Nutzer:innen können in Echtzeit in Segments aufgenommen oder daraus entfernt werden, basierend auf ihrem Verhalten und ihrer Beziehung zu Ihrer Marke. So wird sichergestellt, dass Ihre Kund:innen jederzeit die für sie relevantesten Nachrichten erhalten. Sie können so viele Segments erstellen, wie Sie für Ihr Targeting und Messaging benötigen.]({% image_buster /assets/img/getting_started/segment.png %})

Weitere Informationen finden Sie unter: [Erste Schritte: Nutzer:innen und Segments]({{site.baseurl}}/user_guide/get_started/users_and_segments).

## Campaigns und Canvases {#campaigns-and-canvases}

Campaigns und Canvases sind die Werkzeuge, mit denen Sie Nachrichten an Ihre Nutzer:innen senden.

Campaigns eignen sich am besten für einzelne Nachrichten, die an ein bestimmtes Zielgruppensegment über verschiedene Kanäle gesendet werden. Sie können jeden unserer unterstützten Messaging-Kanäle in Ihrer Campaign nutzen (E-Mail, Push, In-App-Nachrichten, SMS und mehr).

Canvases sind erweiterte Campaign-Workflows, mit denen Sie personalisierte Customer Journeys über mehrere Kanäle automatisieren und orchestrieren können. Innerhalb eines Canvas können Sie Verzweigungslogiken, Verzögerungen, Entscheidungspunkte und Konversions-Events einrichten, um Kund:innen durch eine Reihe von Interaktionen zu führen. Canvases sorgen für eine konsistente und nahtlose Kommunikation über verschiedene Touchpoints hinweg und erhöhen so die Chancen auf Customer-Engagement und Konversion.

Weitere Informationen finden Sie unter: [Erste Schritte: Campaigns und Canvases]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases).

## Workspaces {#workspaces}

Workspaces bündeln Ihre Daten – Nutzer:innen, Segments, Campaigns und Canvases – an einem zentralen Ort. Informationen werden nicht zwischen Workspaces geteilt. Beachten Sie dies, wenn Sie Websites und Apps zu Ihren Workspaces hinzufügen. Als Best Practice empfehlen wir, nur verschiedene Versionen derselben oder sehr ähnlicher Apps in einem Workspace zusammenzufassen.

Beispielhafte Anwendungsfälle für Workspaces:

- Verschiedene Produktlinien oder Apps
- Verschiedene Zielgruppen (z. B. Lieferfahrer:innen im Vergleich zu Kund:innen)
- Separate Geschäftsbereiche
- Testumgebungen

Weitere Informationen finden Sie unter: [Erste Schritte: Workspaces]({{site.baseurl}}/user_guide/get_started/workspaces).

## Braze integrieren {#integrating-braze}

Braze ist so konzipiert, dass es schnell und einfach einsatzbereit ist. Unsere durchschnittliche Time-to-Value beträgt sechs Wochen – über unseren Kundenstamm von Hunderten von Marken hinweg.

![Screenshot zur Integration von Braze.]({% image_buster /assets/img/getting_started/timetovalue.png %})

Hier ist das Braze-Framework zur Schätzung der Dauer Ihrer Integration, basierend auf vier Komponenten, an denen Sie parallel arbeiten können. Der typische Zeitrahmen liegt zwischen 30 und 180 Tagen, wobei die meisten Accounts ihre Integration innerhalb von 45 bis 60 Tagen abschließen.

- **Komplexitätsstufe der Campaign-Migration:** Die Zeit für die Migration von Campaigns hängt davon ab, wie viele Sie haben, wie personalisiert sie sind und welche Ressourcen Ihnen zur Verfügung stehen. Wenn Sie weniger als zehn Campaigns migrieren müssen, dauert es weniger als 60 Tage. Aber bei über 100 Campaigns wird es komplizierter. Ob eine einzelne Person 100 Campaigns migriert oder zehn Personen, macht einen großen Unterschied.

{% alert tip %}
Brauchen Sie Hilfe bei Ihrer Migration? Unsere [zertifizierten Braze-Partner](https://www.braze.com/partners/solutions-partners) können Sie unterstützen!
{% endalert %}

- **E-Mail-Volumen:** Um E-Mails zu versenden, müssen Sie Ihre IPs aufwärmen. [IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) ist der Prozess, bei dem Sie die Absender-Reputation mit Ihren neu zugewiesenen IP-Adressen aufbauen. Wenn Sie weniger als 2–3 Millionen E-Mails pro Tag versenden, sollte Ihr IP-Warming 30 Tage oder weniger dauern. Berücksichtigen Sie dabei Ihre Spitzenversandzeiten. Wenn Sie normalerweise 2 Millionen E-Mails pro Tag versenden, aber zu einer saisonalen Hochphase 7 Millionen versenden möchten, ist dieses „Spitzenvolumen“ das Ziel, auf das Sie aufwärmen sollten. Versender mit hohem Volumen können mehrere IPs nutzen, um den Aufwärmprozess zu beschleunigen.
- **Organisatorische Komplexität:** Unser Onboarding-Prozess lässt sich an Ihre geschäftlichen Anforderungen anpassen. Ob Sie eine einzelne Geschäftseinheit sind, ein Center of Excellence haben, mehrere unabhängige Einheiten betreiben oder Agenturen zur Verstärkung Ihrer Teams einsetzen – Braze hat Erfahrung mit all diesen Szenarien.
- **Ausgereiftheit der Dateninfrastruktur:** Wenn Sie nur das Braze SDK implementieren oder bereits eine Customer Data Platform (CDP) nutzen, ist es möglich, alles in nur 30 Tagen einzurichten. Eine moderne Customer Data Platform (CDP) kann den Prozess beschleunigen. Wenn Sie jedoch viele Backend-Systeme, Tools oder Datenbanken mit Braze verbinden müssen, kann es länger dauern und mehr dedizierte Ressourcen erfordern, um die Einrichtung abzuschließen.

Weitere Informationen finden Sie unter: [Erste Schritte: Übersicht zur Integration]({{site.baseurl}}/user_guide/get_started/integrations).
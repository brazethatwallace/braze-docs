---
nav_title: API- und SDK or Software-Development-Kit-Endpunkte
article_title: API- und SDK or Software-Development-Kit-Endpunkte
page_order: 5
page_type: reference
description: "Finden Sie die richtige Dashboard-URL, den Representational State Transfer API-Endpunkt und den SDK or Software-Development-Kit-Endpunkt für Ihre Braze-Instanz."

---

# API- und SDK or Software-Development-Kit-Endpunkte {#api-and-sdk-endpoints}

> Finden Sie die richtige Dashboard-URL, den Representational State Transfer API-Endpunkt und den SDK or Software-Development-Kit-Endpunkt für Ihre Braze-Instanz. Sie benötigen diese URLs, um sich anzumelden, API-Aufrufe durchzuführen und das SDK or Software-Development-Kit zu integrieren.

Braze verwaltet eine Reihe verschiedener Instanzen für unser Dashboard, SDK or Software-Development-Kit und Representational State Transfer-Endpunkte, die wir „Cluster“ nennen. Ihr Braze-Onboarding-Manager:in wird Ihnen mitteilen, auf welchem Cluster Sie sich befinden. Um mehr über das Braze SDK or Software-Development-Kit zu erfahren, besuchen Sie den [Braze 101](https://learning.braze.com/braze-101) Braze-Lernkurs.

Wenn Sie sich unter [dashboard.braze.com](https://dashboard.braze.com) anmelden, werden Sie automatisch an die richtige Cluster-Adresse weitergeleitet.

{% multi_lang_include administer/data_centers.md datacenters='instances' %}

{% alert important %}
Verwenden Sie bei der Integration Ihres SDK or Software-Development-Kit den SDK or Software-Development-Kit-Endpunkt. Verwenden Sie bei Aufrufen an unsere Representational State Transfer API den Representational State Transfer-Endpunkt.
{% endalert %}

Weitere Informationen zum Zugriff auf die API finden Sie in unserem [Artikel zur API-Übersicht]({{site.baseurl}}/api/basics).
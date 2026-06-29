---
nav_title: API- und SDK-Endpunkte
article_title: API- und SDK-Endpunkte
page_order: 5
page_type: reference
description: "Finden Sie die richtige Dashboard-URL, den REST API-Endpunkt und den SDK-Endpunkt für Ihre Braze-Instanz."

---

# API- und SDK-Endpunkte {#api-and-sdk-endpoints}

> Finden Sie die richtige Dashboard-URL, den REST API-Endpunkt und den SDK-Endpunkt für Ihre Braze-Instanz. Sie benötigen diese URLs, um sich anzumelden, API-Aufrufe durchzuführen und das SDK zu integrieren.

Braze verwaltet eine Reihe verschiedener Instanzen für unser Dashboard, SDK und REST-Endpunkte, die wir „Cluster“ nennen. Ihre Braze-Onboarding-Manager:in wird Ihnen mitteilen, auf welchem Cluster Sie sich befinden. Um mehr über das Braze SDK zu erfahren, besuchen Sie den [Braze 101](https://learning.braze.com/braze-101) Braze-Lernkurs.

Wenn Sie sich unter [dashboard.braze.com](https://dashboard.braze.com) anmelden, werden Sie automatisch an die richtige Cluster-Adresse weitergeleitet.

{% multi_lang_include administer/data_centers.md datacenters='instances' %}

{% alert important %}
Verwenden Sie bei der Integration Ihres SDK den SDK-Endpunkt. Verwenden Sie bei Aufrufen an unsere REST API den REST-Endpunkt.
{% endalert %}

Weitere Informationen zum Zugriff auf die API finden Sie in unserem [Artikel zur API-Übersicht]({{site.baseurl}}/api/basics/).
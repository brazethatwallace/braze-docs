---
nav_title: Pypestream
article_title: Pypestream
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Pypestream, einer umfassenden KI or künstliche Intelligenz-Plattform für Konversationen, mit der Sie das digitale Engagement Ihrer Marke verbessern können."
alias: /partners/pypestream/
page_type: partner
search_tag: Partner

---

# Pypestream

> [Pypestream](https://www.pypestream.com) ist eine umfassende KI or künstliche Intelligenz-Plattform für Konversationen, die patentiertes, All-in-One-Cloud-Messaging anbietet, um Marken in „always-on“ digitale Einheiten zu transformieren. Mit Pypestream können Marken jetzt Omnichannel-Konversationen in großem Umfang mit allen Kund:innen führen und dabei ein immersives Nutzererlebnis, fortschrittliche NLU-Funktionen und Realtime-Integrationen in Backend-Systeme nutzen.

_Diese Integration wird von Pypestream gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Pypestream ermöglicht es Ihnen, den End-to-End-Kundenlebenszyklus nahtlos zu orchestrieren – von der ersten Kontaktaufnahme über ein konversationsbasiertes Erlebnis bis hin zu Omnichannel-Follow-up(s) durch intelligentes Retargeting.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Pypestream-Konto | Ein [Pypestream-Konto](https://www.pypestream.com/contact-us/) ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen.<br><br>Sobald Sie registriert sind, hilft Ihnen das Pypestream-Team bei der Einrichtung Ihrer dedizierten Umgebung, damit Sie mit dem Aufbau Ihrer KI or künstliche Intelligenz-Lösung für die Integration mit Braze beginnen können. |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze Representational State Transfer-Endpunkt  | Ihre Representational State Transfer-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Die Partnerschaft zwischen Braze und Pypestream kann in Ihren Canvase genutzt werden, um gängige Anwendungsfälle zu realisieren:
* **Intelligentes Retargeting**: Retargeten Sie Nutzer:innen mit Braze Canvas nach deren konversationsbasiertem Engagement mit Ihrer Marke, indem Sie alle über Pypestream erfassten Datenpunkte nutzen.
* **Dynamisches Targeting**: Kontaktieren Sie bestehende und potenzielle Kund:innen auf Basis ihrer spezifischen Kohorten und Segmente und bieten Sie ihnen über Pypestream maßgeschneiderte Konversationserlebnisse.
* **Kontextuelle Kund:innen-Insights**: Nachdem sich Endnutzer:innen (bestehende oder potenzielle Kund:innen) auf Ihrer Website engagiert haben, kombinieren Sie die vom Pypestream Event Listener aufgenommenen Webseiten-Tags mit den in Braze gespeicherten Kundendaten, um eine vollständig personalisierte und kontextuelle Konversationsinteraktion zu ermöglichen.

## Integration

Pypestream nutzt eine serverlose Integrationsebene, um angepasste Integrationen in verschiedene Plattformen durchzuführen. Diese Schicht dient als Schnittstelle zu Diensten oder Systemen, um die Datenanforderungen des zu erstellenden Konversationsflusses zu unterstützen. Diese Integrationen, die als Action-Node-Integrationen bezeichnet werden, sind in der Regel in Python geschrieben und werden über die Pypestream-Plattform bereitgestellt. Nachdem ein Action Node instanziiert wurde, bietet er die Flexibilität, sich in jeden beliebigen Braze-API-Endpunkt zu integrieren, und erlaubt die Auswertung der Ergebnisse auf vielfältige Weise.

{% alert note %}
In diesem [Pypestream-Artikel](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) finden Sie eine Übersicht und Konfigurationsschritte für Pypestream-Action-Nodes. Sie müssen Kund:in von Pypestream sein, um auf diese Dokumentation zugreifen zu können.
{% endalert %}

### 1. Schritt: Endpunkt-Konfigurationen festlegen {#step-1-set-endpoint-configurations}

Die primären Konfigurationswerte, wie die URL des Braze Representational State Transfer-Endpunkts und die Braze-API-Schlüssel, sollten in der Datei `app.py` der Lösung festgelegt werden:

```
import os

NAME = '{ CUSTOMER NAME }'
BOTS = []
CSV_BOTS = ['{ SOLUTION NAME }']
PATH = os.path.dirname(__file__)

PARAMS = {
    'sandbox': {
        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
    'prod': {

        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
}
```

### 2. Schritt: Action-Node-Template entwickeln {#step-2-develop-action-node-template}

Action Nodes nutzen die Umgebung, in der die Lösung bereitgestellt wird, um mit den entsprechenden Braze-Endpunkten zu interagieren, die im vorherigen Schritt festgelegt wurden. In diesem Schritt wird ein Action Node entwickelt, um bestimmte Braze-Endpunkte zu integrieren. Verwenden Sie das folgende Template als Leitfaden für die Entwicklung der Integrationen:

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Authorization": "{YOUR-REST-API-KEY}"
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ]
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)

            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```
### 3. Schritt: Lösungsdesigns Update or aktualisieren or aktualisieren {#step-3-update-the-solution-designs}

Der letzte Schritt der Integration mit der Braze Representational State Transfer API besteht darin, die Abläufe im [Design Studio](https://platform.pypestream.com/design-studio/) von Pypestream so zu konfigurieren, dass sie den Action Node verwenden, der im vorherigen Schritt entwickelt wurde.

{% alert note %}
In diesem [Pypestream-Artikel](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) finden Sie eine Übersicht darüber, wie Sie Modi im Design Studio konfigurieren können. Sie müssen Kund:in von Pypestream sein, um auf diese Dokumentation zugreifen zu können.
{% endalert %}

## Anwendungsfall der Integration {#integration-use-case}

Nachdem die Voraussetzungen erfüllt sind und eine Action-Node-Struktur erstellt wurde, steht Entwickler:innen ein leeres Canvas zur Verfügung, um mit den Braze-API-Endpunkten zu arbeiten. Dieses Beispiel zeigt die Schritte, die für die Integration eines Action Nodes in den Braze-[`/user/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) erforderlich sind – insbesondere für die Erstellung eines Nutzerprofils zum Tracking von Nutzer:innen, die einen Pypestream-Konversationsfluss betreten.

### 1. Schritt: Daten von Nutzer:innen im Gespräch erfassen {#step-1-collect-data-from-the-user-in-conversation}

Wenn Nutzer:innen eine Pypestream-Sitzung betreten, hängt die Art der erfassten Daten ganz vom jeweiligen Anwendungsfall ab. Um ein Kundenprofil or Nutzerprofil innerhalb von Braze erstellen zu können, muss die Konversation die erforderlichen Felder erfassen, die für den gewünschten Endpunkt benötigt werden.

Wenn die Lösung beispielsweise während der Konversation für den Braze-`/user/track`-Endpunkt die folgenden Informationen von Nutzer:innen gesammelt hat:

* Vorname
* Nachname
* E-Mail-Adresse
* Geburtsdatum
* Wohnort
* Betriebssystem

Diese Daten können nun an die Braze-Plattform gesendet werden, um das Engagement dieser Nutzer:innen zu verfolgen und sie möglicherweise in Zukunft zu retargeten. Sehen Sie sich die [Liste der Anwendungsfälle](#use-cases) an, um häufige Anwendungen zu entdecken.

### 2. Schritt: Daten in die Action-Node-Struktur einfügen {#step-2-populate-data-in-the-action-node-structure}

Unter Verwendung derselben Struktur für die Entwicklung von Action Nodes können die von Nutzer:innen gesammelten Daten in den Action Node eingefügt werden, um sie über den `/user/track`-Endpunkt an Braze zu senden.

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ],
        "partner" : 'pypestream'
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    "first_name": "{ FIRST_NAME }",
                    "last_name": "{ LAST_NAME }",
                    "email": "{ EMAIL_ADDRESS }",
                    "dob": "{ DATE_OF_BIRTH }",
                    "home_city": "{ CITY_OF_RESIDENCE }",
                    "operating_system": "{ OPERATING_SYSTEM }" #custom attributes can be added here as well
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [{
                    "external_id": "{ USER_ID }",
                    "name": "{ NAME_OF_EVENT }",
                    "time": "{ EVENT_TIME }"
                }],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)

            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```

### 3. Schritt: Lösungsabläufe für Weiterleitung bei Erfolg/Fehler des Action Nodes Update or aktualisieren or aktualisieren {#step-3-update-solution-flows-to-redirect-upon-successfailure-of-action-node}

Abschließend können Sie im Design jeder Lösung Nutzer:innen basierend darauf zu Knoten weiterleiten, ob der API-Aufruf des Action Nodes erfolgreich war. Wenn der Action Node eine Fehlermeldung erhält, sollten Endnutzer:innen mit besonderer Sorgfalt behandelt werden.
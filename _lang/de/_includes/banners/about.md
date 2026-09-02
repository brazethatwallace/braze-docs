# Banner {#banners}

> Mit Bannern können Sie personalisierte Nachrichten für Ihre Nutzer:innen erstellen und gleichzeitig die Reichweite Ihrer anderen Kanäle, wie E-Mail oder Push-Benachrichtigungen, erhöhen. Sie können Banner direkt in Ihre App oder Website einbetten, wodurch Sie Nutzer:innen durch ein natürliches Erlebnis ansprechen können.

## Voraussetzungen {#prerequisites}

Die Verfügbarkeit von Bannern hängt von Ihrem Braze-Paket ab. Kontaktieren Sie Ihren Account Manager:in oder CSM or Customer-Success-Manager or Customer-Success-Manager:in, um loszulegen.

Bevor Sie beginnen, stellen Sie sicher, dass Sie [Banner-Platzierungen]({{site.baseurl}}/developer_guide/banners/placements) in Ihrer App oder Website erstellt haben.

![Ein Beispiel-Banner, das auf einem Gerät dargestellt wird.]({% image_buster /assets/img/banners/sample_banner.png %})

## Warum Banner verwenden? {#why-use-banners}

Banner ermöglichen es Marketing- und Produktteams, App- oder Website-Inhalte dynamisch zu personalisieren und dabei die Berechtigung und das Verhalten der Nutzer:innen in Echtzeit widerzuspiegeln. Sie zeigen Nachrichten dauerhaft inline an und bieten nicht-aufdringliche, kontextuell relevante Erlebnisse, die zu Beginn einer Sitzung oder während einer Sitzung aktualisiert werden können, wenn Ihre App oder Website dies explizit anfordert.

Nachdem Banner in eine App oder Website integriert wurden, können Marketer Banner mithilfe eines Drag-and-Drop-Editors oder eines vollständigen HTML-Editors gestalten und starten – ohne fortlaufende Unterstützung durch Entwickler:innen, was die Komplexität reduziert und die Effizienz verbessert.

| Anwendungsfall | Erklärung |
| --- | --- |
| Ankündigungen | Halten Sie Ankündigungen wie bevorstehende Veranstaltungen oder Richtlinienänderungen im Vordergrund Ihres App-Erlebnisses. |
| Personalisierte Angebote | Zeigen Sie personalisierte Aktionen und Anreize basierend auf dem Browserverlauf, dem Warenkorbinhalt, der Abo-Stufe und dem Treueprogramm-Status jeder:jedes Nutzer:in an. |
| Engagement neuer Nutzer:innen | Führen Sie neue Nutzer:innen durch Onboarding-Flows und die Kontoeinrichtung. |
| Verkäufe und Aktionen | Heben Sie vorgestellte Inhalte, Trendprodukte und laufende Markenkampagnen dauerhaft und direkt auf Ihrer Startseite hervor, ohne das Nutzererlebnis zu beeinträchtigen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Warum Banner verwenden?" }

## Features

Zu den Features für Banner gehören:

- **Einfache Erstellung von Inhalten:** Erstellen Sie Ihr Banner mit einem visuellen Drag-and-Drop-Editor, der Bilder, Text, Buttons, Formulare zur Erfassung von E-Mails, angepassten Code und vieles mehr unterstützt, und zeigen Sie eine Vorschau an. Teams, die ihr eigenes Markup verwalten möchten, können stattdessen den HTML-Editor für die volle Kontrolle über HTML und Stile des Banners verwenden, oder [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages) bitten, HTML aus einer Beschreibung zu generieren.
- **Flexible Platzierungen:** Definieren Sie mehrere Standorte innerhalb Ihrer Anwendung oder Website, an denen Banner erscheinen können, und ermöglichen Sie so ein präzises Targeting auf bestimmte Kontexte oder Nutzererlebnisse.
- **Dynamische Personalisierung:** Banner berechnen die Personalisierung (Liquid-Logik) und Segmentierung bei jeder Aktualisierung des Banners neu. Wenn Nutzer:innen ihr Profil Update or aktualisieren or aktualisieren oder sich ein angepasstes Attribut ändert, spiegelt die nächste Banner-Aktualisierung diese Änderungen wider.
- **Native Priorisierung:** Legen Sie die Anzeigepriorität fest, wenn mehrere Banner auf dieselbe Platzierung abzielen, um sicherzustellen, dass die richtige Nachricht die Nutzer:innen zur richtigen Zeit erreicht.
- **Editor-Block für angepassten Code:** Verwenden Sie den Editor-Block für angepassten Code, um angepasstes HTML für erweiterte Anpassungen oder eine nahtlose Integration in Ihre bestehenden Webstile hinzuzufügen.

## Über Banner {#about-banners}

### Platzierungs-IDs {#placement-id}

Bannerplatzierungen sind bestimmte Standorte in Ihrer App oder Website, [die Sie mit dem Braze SDK or Software-Development-Kit erstellen]({{site.baseurl}}/developer_guide/banners/placements) und die festlegen, wo Banner erscheinen können.

Zu den üblichen Standorten gehören der obere Teil Ihrer Homepage, Produktdetailseiten und Checkout-Abläufe. Nachdem die Platzierungen erstellt wurden, können Banner [in Ihrer Banner-Campaign zugewiesen]({{site.baseurl}}/user_guide/channels/banners/create_a_banner) werden.

Es gibt keine feste Begrenzung für die Anzahl der Platzierungen, die Sie pro Workspace erstellen können, und Sie können so viele Platzierungs-IDs erstellen, wie es Ihre Anforderungen erfordern. Jede Platzierung muss innerhalb eines Workspaces eindeutig sein. Eine einzelne Platzierungs-ID kann gleichzeitig von bis zu 25 aktiven Nachrichten referenziert werden.

{% alert important %}
Vermeiden Sie die Änderung von Platzierungs-IDs nach dem Starten einer Banner-Campaign.
{% endalert %}

### Bannerpriorität {#priority}

Wenn mehrere Banner-Nachrichten auf dieselbe Platzierungs-ID referenzieren, werden die Banner in der Reihenfolge ihrer Priorität angezeigt: hoch, mittel oder niedrig. Standardmäßig sind Banner auf „mittel“ eingestellt, Sie können jedoch [die Priorität manuell festlegen]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#set-banner-priority-optional), wenn Sie Ihre Banner-Campaign erstellen oder bearbeiten.

Wenn mehrere Banner auf dieselbe Priorität eingestellt sind, wird das neueste Banner, für das der/die Nutzer:in berechtigt ist, zuerst angezeigt.

### Platzierungsanfragen {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Zustellung von Nachrichten {#message-delivery}

Banner-Nachrichten werden Ihrer App oder Website als HTML-Inhalt zugestellt, der in der Regel innerhalb eines iFrames gerendert wird. Dadurch wird sichergestellt, dass Ihre Banner auf allen Geräten konsistent dargestellt werden, und Sie können deren Stile und Skripte vom Representational State Transfer Ihres Codes trennen.

iFrames ermöglichen dynamische und personalisierte Inhaltsaktualisierungen, ohne dass Änderungen an Ihrer Codebasis erforderlich sind. Jeder iFrame ruft den HTML-Code für jede Nutzersitzung ab und zeigt ihn mithilfe der Logik für das Campaign-Targeting und die Personalisierung an.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

### Abmessungen und Größenangaben {#dimensions-and-sizing}

Hier erfahren Sie, was Sie über die Abmessungen und die Größe von Bannern wissen müssen:

- Der Composer erlaubt Ihnen zwar die Vorschau von Bannern in verschiedenen Abmessungen, aber diese Informationen werden nicht gespeichert oder an das SDK or Software-Development-Kit gesendet.
- Der HTML-Code nimmt die gesamte Breite des Containers ein, in dem er gerendert wird.
- Wir empfehlen, ein Element mit festen Abmessungen zu erstellen und diese Abmessungen im Composer zu testen.

### Connected Content {#connected-content}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content for Banners' %}

Sie können [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) verwenden, um Echtzeitdaten von externen APIs in Ihr Banner einzubinden. Da Banner inline während einer Sitzungsaktualisierung gerendert werden, gelten für Connected Content in diesem Kanal bestimmte Einschränkungen:

- **Nur GET-Anfragen:** Banner rendern nur `GET`-Connected-Content-Anfragen. `POST`-Anfragen werden nicht unterstützt.
- **Gemeinsames Rendering-Budget:** Alle Platzierungen, die in einer einzelnen Aktualisierungsanfrage zurückgegeben werden (bis zu 10), teilen sich ein Rendering-Budget von etwa zwei Sekunden. Jeder Connected-Content-Aufruf wird auf dieses gemeinsame Budget angerechnet, sodass eine Platzierung mit langsamen oder zahlreichen Aufrufen Zeit verbrauchen kann, die andere Platzierungen benötigen.
- **Keine Wiederholungsversuche:** Wenn ein Connected-Content-Aufruf fehlschlägt, das Zeitlimit überschreitet oder das Rendering-Budget überschritten wird, wird das Connected-Content-Ergebnis für diese Platzierung als null behandelt. Im Gegensatz zu anderen Kanälen wiederholen Banner die Anfrage nicht und verzögern die Zustellung nicht.

## Einschränkungen {#limitations}

Jeder Workspace unterstützt bis zu 200 aktive Banner-Campaigns. Wenn dieses Limit erreicht ist, müssen Sie eine bestehende Campaign [archivieren oder deaktivieren]({{site.baseurl}}/user_guide/messaging/governance/statuses#changing-the-status), bevor Sie eine neue erstellen können.

Darüber hinaus unterstützen Banner-Nachrichten die folgenden Features nicht:

- API-getriggerte und aktionsbasierte Campaigns
- [Connected-Content](#connected-content) (im Early Access)
- Aktionscodes
- `catalog_items` mit dem [`:rerender`-Tag]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid)

## Nächste Schritte {#next-steps}

- [Banner-Platzierungen in Ihrer App oder Website erstellen]({{site.baseurl}}/developer_guide/banners/placements)
- [Eine Banner-Campaign in Braze erstellen]({{site.baseurl}}/user_guide/channels/banners/create_a_banner)
- [Tutorial: Ein Banner anhand der Platzierungs-ID anzeigen]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)

{% alert tip %}
Möchten Sie mitbestimmen, was als Nächstes kommt? Kontaktieren Sie [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}
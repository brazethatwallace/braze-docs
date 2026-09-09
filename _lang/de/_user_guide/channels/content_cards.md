---
nav_title: Content Cards
article_title: Content Cards
page_order: 2
page_type: landing
description: "Senden Sie Ihren Nutzer:innen einen dynamischen Stream mit reichhaltigen Inhalten über Content Cards, die direkt in Ihre App oder Website eingebettet sind."
channel:
  - content cards
search_rank: 5
---

# Content Cards {#content-cards}

> Mit Content Cards können Sie Ihren Kund:innen einen hochgradig zielgerichteten, dynamischen Stream mit reichhaltigen Inhalten innerhalb der Apps senden, die sie lieben – ohne ihr Erlebnis zu unterbrechen. Content Cards werden direkt in Ihre App oder Website eingebettet und ermöglichen es Ihnen, Nachrichten-Posteingänge und angepasste Oberflächen zu erstellen, die die Reichweite anderer Kanäle wie E-Mail oder Push-Benachrichtigungen erweitern.

## Voraussetzungen {#prerequisites}

Die Verfügbarkeit von Content Cards hängt von Ihrem Braze-Paket ab. Wenden Sie sich an Ihren Account Manager oder Customer-Success-Manager, um loszulegen.

Bevor Sie Content Cards verwenden können, müssen Sie das [Braze SDK]({{site.baseurl}}/developer_guide/content_cards) in Ihre App oder Website integrieren. Es ist keine zusätzliche Einrichtung erforderlich. Wenn Sie stattdessen eine eigene UI erstellen möchten, lesen Sie den [Leitfaden zur Anpassung von Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards).

## Vorteile der Verwendung von Content Cards {#benefits-of-using-content-cards}

Hier sind einige Vorteile der Verwendung von Content Cards im Vergleich dazu, Inhalte von Ihren Entwickler:innen direkt in Ihre App einbauen zu lassen:

- **Einfachere Segmentierung und Personalisierung:** Ihre Nutzerdaten befinden sich in Braze, sodass Sie Ihre Zielgruppe einfach definieren und Ihre Nachrichten mit Content Cards personalisieren können.
- **Zentralisiertes Reporting:** Content-Card-Analytics werden in Braze erfasst, sodass Sie Einblick in alle Ihre Campaigns an einem Ort haben.
- **Zusammenhängende Customer Journeys:** Sie können Content Cards mit anderen Kanälen in Braze kombinieren, um konsistente Kundenerlebnisse zu schaffen. Ein beliebter Anwendungsfall ist das Senden einer Push-Benachrichtigung und anschließendes Speichern dieser Benachrichtigung als Content-Card in Ihrer App für alle, die nicht auf den Push reagiert haben. Wenn der Inhalt direkt von Ihren Entwickler:innen in Ihre App eingebaut wird, ist er vom Rest Ihres Messagings isoliert.
- **Kein erforderliches Opt-in:** Ähnlich wie In-App-Nachrichten erfordern Content Cards kein Opt-in und keine Berechtigungen von Ihren Nutzer:innen. Aber während In-App-Nachrichten keine Berechtigung erfordern und kurzlebig sind, sind Content Cards berechtigungsfrei und dauerhaft. Das bedeutet, dass Messaging-Strategien, die In-App-Nachrichten und Content Cards miteinander kombinieren, eine hervorragende Balance bieten.
- **Mehr Kontrolle über das Messaging-Erlebnis:** Auch wenn Sie Ihre Entwickler:innen für die Ersteinrichtung von Content Cards benötigen, können Sie danach die Nachricht, die Empfänger:innen, das Timing und mehr direkt über Ihr Braze-Dashboard steuern.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Content Cards in Zahlen {#content-cards-by-the-numbers}

Wenn Sie Content Cards in Braze erstellen, können Sie Nachrichten aktualisieren und die Wirkung messen, ohne Ihre App oder Website grundlegend überarbeiten zu müssen. Highlights aus der Braze-Forschung:

- Content Cards sind **38-mal** effektiver als E-Mail bei der Umsatzsteigerung innerhalb eines 72-Stunden-Fensters.[^1]
- Der Einsatz von Content Cards in Kundenbindungs-Registrierungskampagnen steigert Konversionen um das **5-Fache**.[^1]
- Ansprache über Push-Benachrichtigungen, In-App Messages und Content Cards führt zu **6,9-mal** mehr Sitzungen als Push allein.[^2]
- Ansprache über E-Mail, In-App Messages und Content Cards führt zu einer **3,6-mal** längeren durchschnittlichen Nutzer:innen-Lifetime als E-Mail allein.[^2]

## Anwendungsfälle {#use-cases}

In diesem Abschnitt finden Sie einige gängige Anwendungsfälle für Content Cards.

{% alert tip %}
Weitere Inspiration finden Sie im [Content Cards Inspiration Guide](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), der über 20 anpassbare Campaigns enthält, darunter Empfehlungsprogramme, Produkteinführungen und Abo-Verlängerungen.
{% endalert %}

{% tabs %}
{% tab Onboarding und nächste Schritte %}

Wenn neue Nutzer:innen Ihre App und Website erkunden, führen Sie sie mit strategisch platzierten Content Cards durch den Nutzen und die Vorteile Ihres Angebots. Ermutigen Sie Nutzer:innen, sich für weitere Kommunikationskanäle zu entscheiden, indem Sie eine Content-Card auf Ihrer Startseite platzieren, und speichern Sie ausstehende Onboarding-Aufgaben in einem eigenen Onboarding-Tab, der von Content Cards unterstützt wird. Vergessen Sie nicht, eine Card zu entfernen, nachdem Nutzer:innen die gewünschte Aufgabe abgeschlossen haben!

![Beispiel für einen Onboarding-Anwendungsfall mit Content Cards.]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab Veranstaltungsteilnahme %}

Präsentieren Sie Content Cards oben auf der Startseite von Nutzer:innen, um die Teilnahme an Veranstaltungen zu fördern, und nutzen Sie Standort-Targeting, um potenzielle Nutzer:innen dort zu erreichen, wo sie sich befinden. Wenn Sie Nutzer:innen zu relevanten physischen Veranstaltungen einladen, fühlen sie sich wertgeschätzt – besonders mit personalisierten Nachrichten, die ihre bisherigen Aktivitäten mit Ihrer Marke nutzen.

![Beispiel für einen Anwendungsfall zur Veranstaltungsteilnahme mit Content Cards.]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab Empfehlungen %}

Nutzen Sie die Daten, die Sie über das Verhalten und die Präferenzen von Nutzer:innen haben, um relevante Inhalte in Echtzeit über Content Cards auf der Startseite oder im Posteingang anzuzeigen und Nutzer:innen zurück zu Ihrem Produktangebot zu führen.

![Beispiel für einen Empfehlungs-Anwendungsfall mit Content Cards.]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab Aktionen und Angebote %}

Nutzen Sie Content Cards, um Werbebotschaften und nicht eingelöste Angebote direkt auf Ihrer Startseite oder in einem speziellen Aktions-Posteingang hervorzuheben. Zeigen Sie relevante Inhalte basierend auf den bisherigen Käufen jeder Kund:in an, um aufmerksamkeitsstarke personalisierte Aktionen bereitzustellen.

![Beispiel für einen Anwendungsfall zu Aktionen und Angeboten mit Content Cards.]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### Weitere Anwendungsfälle {#other-use-cases}

Abgesehen von diesen Hauptanwendungsfällen setzen Kund:innen Content Cards auf vielfältige Weise ein. Die Stärke von Content Cards liegt in ihrer Flexibilität. Wenn der gewünschte Anwendungsfall hier nicht aufgeführt ist, können Sie [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) einrichten und die Payloads an Ihre App oder Website senden.

Einen Überblick darüber, wie Sie Content-Card-Platzierungen in Ihrer App oder auf Ihrer Website implementieren, finden Sie unter [Angepasste Content Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

## Nächste Schritte {#next-steps}

{% article_tiles %}
- name: Content-Card erstellen
  link: /docs/user_guide/channels/content_cards/create_a_content_card
- name: Kreativdetails
  link: /docs/user_guide/channels/content_cards/creative_details
{% endarticle_tiles %}

[^1]: [8 Tipps, um das Beste aus Ihren Kundenbindungskampagnen herauszuholen](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Bericht: Der Unterschied durch kanalübergreifendes Marketing](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)
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

Die Verfügbarkeit von Content Cards hängt von Ihrem Braze-Paket ab. Kontaktieren Sie Ihren Account Manager oder Customer-Success-Manager, um loszulegen.

Bevor Sie Content Cards verwenden können, müssen Sie das [Braze SDK]({{site.baseurl}}/developer_guide/content_cards) in Ihre App oder Website integrieren. Es ist kein zusätzliches Setup erforderlich. Wenn Sie stattdessen eine eigene UI erstellen möchten, lesen Sie den [Leitfaden zur Anpassung von Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards).

## Vorteile von Content Cards {#benefits-of-using-content-cards}

Hier sind einige Vorteile von Content Cards im Vergleich dazu, Ihre Entwickler:innen Inhalte direkt in Ihre App einbauen zu lassen:

- **Einfachere Segmentierung und Personalisierung:** Ihre Nutzerdaten befinden sich in Braze, sodass Sie Ihre Zielgruppe einfach definieren und Ihre Nachrichten mit Content Cards personalisieren können.
- **Zentralisiertes Reporting:** Content-Card-Analytics werden in Braze erfasst, sodass Sie Insights zu all Ihren Campaigns an einem Ort haben.
- **Zusammenhängende Customer Journeys:** Sie können Content Cards mit anderen Kanälen in Braze kombinieren, um konsistente Kundenerlebnisse zu schaffen. Ein beliebter Anwendungsfall ist das Senden einer Push-Benachrichtigung und das anschließende Speichern dieser Benachrichtigung als Content Card in Ihrer App für alle, die nicht auf den Push reagiert haben. Wenn der Inhalt direkt von Ihren Entwickler:innen in die App eingebaut wird, ist er vom Rest Ihres Messagings isoliert.
- **Kein Opt-in erforderlich:** Ähnlich wie In-App Messages erfordern Content Cards kein Opt-in oder Berechtigungen von Ihren Nutzer:innen. Während In-App Messages jedoch keine Berechtigung erfordern und kurzlebig sind, erfordern Content Cards ebenfalls keine Berechtigung, sind aber dauerhaft. Das bedeutet, dass Messaging-Strategien, die In-App Messages und Content Cards kombinieren, eine hervorragende Balance bieten.
- **Mehr Kontrolle über das Messaging-Erlebnis:** Auch wenn Sie für das initiale Setup von Content Cards noch die Hilfe Ihrer Entwickler:innen benötigen, können Sie danach die Nachricht, Empfänger:innen, das Timing und mehr direkt über Ihr Braze-Dashboard steuern.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Content Cards in Zahlen {#content-cards-by-the-numbers}

Wenn Sie Content Cards in Braze erstellen, können Sie Messaging aktualisieren und die Wirkung messen, ohne Ihre App oder Website grundlegend überarbeiten zu müssen. Highlights aus der Braze-Forschung:

- Content Cards sind **38-mal** effektiver als E-Mail bei der Steigerung von Verkäufen innerhalb eines 72-Stunden-Fensters.[^1]
- Der Einsatz von Content Cards in Campaigns zur Anmeldung für Treueprogramme steigert Conversions um das **5-Fache**.[^1]
- Die Ansprache über Push-Benachrichtigungen, In-App Messages und Content Cards führt zu **6,9-mal** mehr Sessions als Push allein.[^2]
- Die Ansprache über E-Mail, In-App Messages und Content Cards führt zu einer **3,6-mal** längeren durchschnittlichen Nutzer-Lifetime als E-Mail allein.[^2]

[^1]: [8 Tipps, um aus Kundenbindungskampagnen das Maximum herauszuholen](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Report: Der Unterschied beim kanalübergreifenden Marketing](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)

## Anwendungsfälle {#use-cases}

In diesem Abschnitt finden Sie einige gängige Anwendungsfälle für Content Cards.

{% alert tip %}
Für weitere Inspiration lesen Sie den [Content Cards Inspiration Guide](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), der über 20 anpassbare Campaigns enthält, darunter Empfehlungsprogramme, neue Produkteinführungen und Abo-Verlängerungen.
{% endalert %}

{% tabs %}
{% tab Onboarding und nächste Schritte %}

Wenn neue Nutzer:innen Ihre App und Website erkunden, führen Sie sie mit strategisch platzierten Content Cards durch die Werte und Vorteile Ihres Angebots. Ermutigen Sie Nutzer:innen, sich für andere Kommunikationskanäle zu entscheiden, mit einer Content Card auf Ihrer Startseite, und speichern Sie ausstehende Onboarding-Aufgaben in einem dedizierten Onboarding-Tab, der von Content Cards unterstützt wird. Vergessen Sie nicht, eine Card zu entfernen, nachdem ein:e Nutzer:in die gewünschte Aufgabe abgeschlossen hat!

![Beispiel für einen Content-Card-Onboarding-Anwendungsfall.]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab Veranstaltungsteilnahme %}

Präsentieren Sie Content Cards oben auf der Startseite Ihrer Nutzer:innen, um die Teilnahme an Veranstaltungen zu fördern, und nutzen Sie Standort-Targeting, um potenzielle Nutzer:innen dort zu erreichen, wo sie sich befinden. Nutzer:innen zu relevanten physischen Veranstaltungen einzuladen, gibt ihnen ein besonderes Gefühl – insbesondere mit personalisiertem Messaging, das ihre bisherige Aktivität mit Ihrer Marke nutzt.

![Beispiel für einen Content-Card-Anwendungsfall zur Veranstaltungsteilnahme.]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab Empfehlungen %}

Nutzen Sie die Daten, die Sie über das Verhalten und die Präferenzen Ihrer Nutzer:innen haben, um relevante Inhalte in Echtzeit über Content Cards auf der Startseite oder im Posteingang anzuzeigen und sie zurück zu Ihrem Produktangebot zu führen.

![Beispiel für einen Content-Card-Anwendungsfall für Empfehlungen.]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab Verkäufe und Aktionen %}

Nutzen Sie Content Cards, um Werbebotschaften und nicht eingelöste Angebote direkt auf Ihrer Startseite oder in einem dedizierten Aktions-Posteingang hervorzuheben. Ziehen Sie relevante Inhalte basierend auf den bisherigen Käufen jedes Kunden bzw. jeder Kundin heran, um aufmerksamkeitsstarke, personalisierte Aktionen zu liefern.

![Beispiel für einen Content-Card-Anwendungsfall für Verkäufe und Aktionen.]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### Weitere Anwendungsfälle {#other-use-cases}

Abgesehen von diesen Hauptanwendungsfällen nutzen Kund:innen Content Cards auf viele verschiedene Arten. Die Stärke von Content Cards liegt in ihrer Flexibilität. Wenn der gewünschte Anwendungsfall hier nicht aufgeführt ist, können Sie [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) einrichten und die Payloads an Ihre App oder Website senden.

Einen Überblick darüber, wie Sie Content-Card-Platzierungen in Ihrer App oder Website implementieren, finden Sie unter [Angepasste Content Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

## Nächste Schritte {#next-steps}

- [Content-Card erstellen]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card)
- [Kreativdetails]({{site.baseurl}}/user_guide/channels/content_cards/creative_details)
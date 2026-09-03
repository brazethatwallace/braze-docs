---
nav_title: A/B-Tests
article_title: A/B-Tests
page_order: 6
layout: dev_guide
guide_top_header: "A/B-Tests"
guide_top_text: "Führen Sie Experimente durch, um Ihr Messaging zu optimieren. Ein A/B-Test vergleicht die Reaktionen von Nutzer:innen auf mehrere Versionen derselben Campaign, während ein multivariater Test dies auf zwei oder mehr Variablen erweitert. In Braze werden die Begriffe synonym verwendet, da der Einrichtungsprozess identisch ist. Nutzen Sie <a href=\"/docs/user_guide/brazeai/intelligence_suite/variant_selection\">Optimierung mit BrazeAI<sup>TM</sup></a> um Ihre Ergebnisse automatisch zu optimieren."

page_type: landing
description: "Richten Sie A/B-Tests und multivariate Experimente in Braze ein und analysieren Sie diese."

guide_featured_title: "Artikel in diesem Abschnitt"
guide_featured_list:
  - name: Konzepte
    link: /docs/user_guide/messaging/ab_testing/concepts
    image: /assets/img/braze_icons/lightbulb-02.svg
  - name: Tests erstellen
    link: /docs/user_guide/messaging/ab_testing/create_tests
    image: /assets/img/braze_icons/plus-circle.svg
  - name: Optimierungen
    link: /docs/user_guide/messaging/ab_testing/optimizations
    image: /assets/img/braze_icons/settings-01.svg
  - name: Analytics
    link: /docs/user_guide/messaging/ab_testing/analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: FAQ
    link: /docs/user_guide/messaging/ab_testing/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

## Wann Sie A/B-Tests einsetzen sollten {#when-to-use-ab-tests}

- **Ausprobieren eines neuen Nachrichtentyps:** Experimentieren Sie und lernen Sie, was bei Ihren Nutzer:innen ankommt.
- **Onboarding-Campaigns oder wiederkehrende Sendungen:** Stellen Sie sicher, dass Campaigns mit hohem Traffic so effektiv wie möglich sind.
- **Mehrere Nachrichtenideen:** Führen Sie einen Test durch und treffen Sie eine datengestützte Entscheidung.
- **Annahmen hinterfragen:** Testen Sie, ob konventionelle Marketing-Taktiken tatsächlich für Ihre spezifische Zielgruppe funktionieren.

## Tipps für effektive Tests {#tips-for-running-effective-tests}

- **Verwenden Sie große Stichproben**, um sicherzustellen, dass die Ergebnisse Ihre durchschnittlichen Nutzer:innen widerspiegeln und nicht durch Ausreißer verzerrt werden.
- **Randomisieren Sie die Testgruppen**, damit unterschiedliche Antwortraten auf Nachrichtenunterschiede zurückzuführen sind und nicht auf Unterschiede in der Stichprobe.
- **Wissen Sie, was Sie testen.** Die Isolation einer einzelnen Änderung zeigt, welches Element die größte Wirkung hatte. Das Testen mehrerer Unterschiede ermöglicht den Vergleich umfassenderer Ansätze.
- **Legen Sie die Testdauer im Voraus fest** und beenden Sie den Test nicht vorzeitig, selbst wenn frühe Ergebnisse vielversprechend aussehen.
- **Fügen Sie Tests vor dem Start hinzu.** Das Hinzufügen eines Tests zu einer laufenden Campaign führt zu ungenauen Ergebnissen. Klonen Sie die Campaign, stoppen Sie das Original und fügen Sie den Test dem Klon hinzu.
- **Schließen Sie eine [Kontrollgruppe]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#including-a-control-group) ein**, um die Wirkung im Vergleich zum vollständigen Verzicht auf eine Nachricht zu messen.
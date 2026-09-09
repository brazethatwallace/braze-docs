---
nav_title: Optimierungen
article_title: A/B-Tests optimieren
page_order: 1
page_type: reference
description: "Erfahren Sie, wie Sie Multivariate- und A/B-Campaign-Tests mit BrazeAI optimieren können."
---

# A/B-Tests optimieren {#optimizing-ab-tests}

> Verwenden Sie **Optimieren mit BrazeAI<sup>TM</sup>**, um eine Campaign mit mehreren Varianten automatisch zu optimieren.

Gehen Sie im Schritt **Zielgruppen** zu **A/B-Tests** und aktivieren Sie dann **Optimieren mit BrazeAI<sup>TM</sup>**.

Bei einer einmalig versendeten Campaign sendet BrazeAI<sup>TM</sup> einen ersten Test und versendet dann die Variante mit der besten Performance an die verbleibende Zielgruppe. Bei einer mehrfach versendeten Campaign überprüft BrazeAI<sup>TM</sup> die Performance alle 12 Stunden und verschiebt mehr Nutzer:innen in Richtung der besser performenden Varianten.

Voraussetzungen, Konfigurationsoptionen und Details zur Berichterstellung finden Sie unter [A/B-Tests mit BrazeAI optimieren]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

{% alert note %}
Bestehende Campaigns, die Personalisierte Variante verwenden, unterstützen diese Optimierung und die zugehörigen Analytics weiterhin. Personalisierte Variante ist beim Erstellen einer neuen Campaign nicht verfügbar.
{% endalert %}

Braze prüft die Berechtigung der Nutzer:innen vor dem zweiten Versand bei einer Optimierung mit einmaligem Versand erneut. Nutzer:innen, die für den ersten Test nicht berechtigt waren, können in die verbleibende Zielgruppe aufgenommen werden, während Nutzer:innen, die nicht mehr berechtigt sind, den Folgeversand nicht erhalten.

Informationen zu den Campaign-Ergebnissen finden Sie unter [Analytics für A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).
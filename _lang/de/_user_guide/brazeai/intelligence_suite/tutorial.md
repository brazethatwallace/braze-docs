---
nav_title: "Anleitung: Schnellrestaurant"
article_title: Intelligence Suite-Anleitung
page_order: 10
search_rank: 12
description: "Sind Sie neu in der Braze Intelligence Suite? Beginnen Sie mit dieser Anleitung."
tool:
  - Dashboard
---

# Intelligence Suite-Anleitung {#intelligence-suite-tutorial}

> Sind Sie neu in der Braze Intelligence Suite? Beginnen Sie mit dieser Anleitung! Weitere allgemeine Informationen finden Sie unter [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/).

## Anleitung: Schnellrestaurant {#tutorial-quick-service-restaurant}

Stellen wir uns vor, wir arbeiten bei SandwichEmperor, einem Schnellrestaurant, das ein neues, zeitlich begrenztes Menüangebot hat: den Royal Roast. Wir werden zwei Features der Intelligence Suite verwenden, um personalisierte Aktionen in einem Canvas zu versenden.

### 1. Schritt: Intelligentes Timing für den Versand von Benachrichtigungen verwenden {#step-1-use-intelligent-timing-for-when-to-send-notifications}

Wir verwenden intelligentes Timing, um die vergangenen Interaktionen unserer Nutzer:innen mit unserer App und den einzelnen Messaging-Kanälen zu analysieren und dann automatisch den besten Zeitpunkt auszuwählen, um den Royal Roast bei jeder Nutzerin und jedem Nutzer zu bewerben. Einige Nutzer:innen erhalten die Aktion vielleicht am Nachmittag, andere am Abend.

Für Nutzer:innen, die nicht über genügend frühere Interaktionen verfügen, die analysiert werden können, bieten wir einen Fallback-Zeitpunkt an: die beliebteste Zeit für die Nutzung der App unter allen Nutzer:innen.

![Einstellungen für intelligentes Timing bei der Zustellung eines Nachrichtenschritts.]({% image_buster /assets/img/intelligence_suite1.png %})

### 2. Schritt: Intelligente Auswahl für die Aktion verwenden {#step-2-use-intelligent-selection-to-select-the-promotion}

Für die eigentlichen Werbebotschaften verwenden wir die intelligente Auswahl, um drei verschiedene Nachrichten (Push-Benachrichtigung, E-Mail und SMS) für den Royal Roast zu testen. Die intelligente Auswahl analysiert die Performance aller unserer Werbebotschaften zweimal täglich und sendet dann nach und nach mehr von den leistungsstärksten Nachrichten und weniger von den anderen.

Nachdem die intelligente Auswahl genügend Daten gesammelt hat, um die Nachricht mit der besten Performance zu ermitteln, wird diese Nachricht bei 100 % aller zukünftigen Sendungen verwendet.

![A/B-Test-Abschnitt eines Canvas mit aktivierter intelligenter Auswahl.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### 3. Schritt: Canvas starten {#step-3-launch-the-canvas}

Mit intelligentem Timing und intelligenter Auswahl haben wir unsere Royal-Roast-Aktionen so eingerichtet, dass sie hinsichtlich Timing und Messaging optimiert sind. Wir können unseren Canvas starten und beobachten, wie sich unsere Sendungen an die Vorlieben der Nutzer:innen anpassen.
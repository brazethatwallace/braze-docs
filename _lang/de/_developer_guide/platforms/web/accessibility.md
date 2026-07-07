---
nav_title: Barrierefreiheit
article_title: Barrierefreiheit
platform: Web
page_order: 22
page_type: reference
description: "Dieser Artikel beschreibt, wie Braze die Barrierefreiheit unterstützt."

---

# Barrierefreiheit {#accessibility}

> Dieser Artikel bietet eine Übersicht darüber, wie Braze die Barrierefreiheit innerhalb Ihrer Integration unterstützt.

Das Braze Web SDK unterstützt die Standards der [Web Content Accessibility Guidelines (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). Wir halten bei allen unseren neuen Versionen einen [Lighthouse-Score von 100/100](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) für Content Cards und In-App-Nachrichten ein, um unseren Standard für Barrierefreiheit aufrechtzuerhalten.

## Voraussetzungen {#prerequisites}

Die Mindest-SDK-Version, die WCAG 2.1 erfüllt, liegt nahe an v3.4.0. Wir empfehlen jedoch, auf mindestens Version 6.0.0 zu upgraden, um wichtige Fehlerbehebungen bei Bild-Tags zu erhalten.

### Wichtige Verbesserungen der Barrierefreiheit {#notable-accessibility-fixes}

| Version | Typ | Wichtige Änderungen |
|---------|------|-------------|
| **6.0.0** | **Major** | Bilder als `<img>`-Tags, `imageAltText`- oder `language`-Felder, allgemeine Verbesserungen der Barrierefreiheit der UI |
| **3.5.0** | Geringfügig | Verbesserungen der Barrierefreiheit für scrollbaren Text |
| **3.4.0** | Behebung | Content Cards `article`-Rollenanpassung |
| **3.2.0** | Geringfügig | Mindestgröße von 45 x 45 Pixel für Touch-Ziele bei Buttons |
| **3.1.2** | Geringfügig | Standard-Alt-Text für Bilder |
| **2.4.1** | **Major** | Semantisches HTML (`h1` oder `button`), ARIA-Attribute, Tastaturnavigation, Fokusverwaltung |
| **2.0.5** | Geringfügig | Fokusverwaltung, Tastaturnavigation, Beschriftungen |
{: .reset-td-br-1, .reset-td-br-2 aria-label="Wichtige Verbesserungen der Barrierefreiheit" }

## Unterstützte Barrierefreiheitsfeatures {#supported-accessibility-features}

Wir unterstützen die folgenden Features für Content Cards und In-App-Nachrichten:

- ARIA-Rollen und -Labels
- Unterstützung der Tastaturnavigation
- Fokusverwaltung
- Screenreader-Ankündigungen
- Alt-Text-Unterstützung für Bilder

## Richtlinien zur Barrierefreiheit für SDK-Integrationen {#accessibility-guidelines-for-sdk-integrations}

Allgemeine Richtlinien zur Barrierefreiheit finden Sie unter [Barrierefreie Nachrichten in Braze erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility). Dieser Leitfaden enthält Tipps und bewährte Verfahren für maximale Barrierefreiheit bei der Integration des Braze Web SDK in Ihre Webanwendung.

### Content Cards

#### Festlegen einer maximalen Höhe {#setting-a-maximum-height}

Um zu verhindern, dass Content Cards zu viel vertikalen Platz einnehmen, und um die Barrierefreiheit zu verbessern, können Sie eine maximale Höhe für den Feed-Container festlegen, wie in diesem Beispiel:

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### Überlegungen zum Darstellungsbereich {#viewport-considerations}

Bei Content Cards, die inline angezeigt werden, sollten Sie die Einschränkungen des Darstellungsbereichs berücksichtigen, wie in diesem Beispiel dargestellt.

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### In-App-Nachrichten {#in-app-messages}

{% alert warning %}
Fügen Sie keine wichtigen Informationen in Slide-up-In-App-Nachrichten ein, da diese für Screenreader nicht zugänglich sind.
{% endalert %}

### Überlegungen für Mobilgeräte {#mobile-considerations}

#### Responsives Design {#responsive-design}

Das SDK enthält responsive Haltepunkte. Stellen Sie sicher, dass Ihre Anpassungen auf allen Bildschirmgrößen funktionieren, wie in diesem Beispiel:

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }

  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### Prüfung der Barrierefreiheit {#testing-accessibility}

#### Manuelle Test-Checkliste {#manual-test-checklist}

Überprüfen Sie die Barrierefreiheit manuell, indem Sie die folgenden Aufgaben ausführen:

- Navigieren Sie ausschließlich mit der Tastatur (Tab, Enter, Leertaste) durch Content Cards und In-App-Nachrichten.
- Testen Sie mit einem Screenreader (NVDA, JAWS, VoiceOver).
- Überprüfen Sie, ob alle Bilder über Alt-Text verfügen.
- Überprüfen Sie die Farbkontrastverhältnisse (verwenden Sie dazu Tools wie den WebAIM Contrast Checker).
- Testen Sie auf Mobilgeräten mit Touchscreen.
- Überprüfen Sie, ob die Fokusindikatoren sichtbar sind.
- Testen Sie das Fokus-Trapping bei modalen Nachrichten.
- Überprüfen Sie, ob alle interaktiven Elemente über eine Tastatur erreichbar sind.

### Häufige Probleme bei der Barrierefreiheit {#common-accessibility-issues}

Um häufige Probleme mit der Barrierefreiheit zu vermeiden, gehen Sie wie folgt vor:

1. **Fokusstile beibehalten:** Die Fokusindikatoren des SDK sind für Tastaturnutzer:innen von entscheidender Bedeutung.
2. **Verwenden Sie `display: none` nur für nicht-interaktive Elemente:** Verwenden Sie `visibility: hidden` oder `opacity: 0` zum Ausblenden interaktiver Elemente.
3. **Überschreiben Sie keine ARIA-Attribute:** Das SDK legt geeignete ARIA-Rollen und -Labels fest.
4. **Verwenden Sie `tabindex`-Attribute:** Diese steuern die Reihenfolge der Tastaturnavigation.
5. **Stellen Sie eine Bildlaufleiste bereit, wenn Sie `overflow: hidden` festlegen:** Stellen Sie sicher, dass scrollbare Inhalte weiterhin zugänglich sind.
6. **Greifen Sie nicht in die integrierten Tastatur-Handler ein:** Stellen Sie sicher, dass die vorhandene Tastaturnavigation ordnungsgemäß funktioniert.
---
nav_title: CSS-Inlining
article_title: CSS-Inlining
page_order: 5.1
description: "Dieser Referenzartikel behandelt, wie Sie CSS-Inlining aktivieren können, und einige Best Practices."
channel:
  - email

---

# CSS-Inlining

> CSS-Inlining ist eine Form der E-Mail-Vorverarbeitung, bei der Styles aus einem CSS-Stylesheet in den Body einer HTML-E-Mail verschoben werden. Der Begriff „Inlining" bezieht sich darauf, dass Styles „inline" auf einzelne HTML-Elemente angewendet werden.

Bei einigen E-Mail-Clients kann CSS-Inlining das Rendering von E-Mails verbessern und dazu beitragen, dass Ihre E-Mails so aussehen, wie Sie es erwarten. Wenn Sie bereits den Großteil des CSS inline eingebunden haben oder sicher sind, dass Ihr HTML und CSS mit den Anforderungen der meisten E-Mail-Clients kompatibel sind, ist es möglicherweise nicht notwendig, dieses Feature zu aktivieren. Es kann dazu führen, dass dynamisch eingebettete Styles mit Ihren bestehenden Inline-Styles in Konflikt geraten und Ihre erwartete Vorschau und das E-Mail-Rendering verändern.

## CSS-Inlining verwenden

Sie können steuern, ob CSS-Inlining für jede E-Mail-Nachricht ein- oder ausgeschaltet ist, indem Sie den Schalter **Inline-CSS aktivieren** im Tab **Versandinformationen** des HTML-Editors verwenden.

![Kontrollkästchen zum Verwalten von CSS-Inlining im HTML-Composer.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Standard-Inlining-Status

Sie können einen globalen Standard-Ein- oder -Aus-Status unter **Einstellungen** > **E-Mail-Präferenzen** festlegen. Suchen Sie die Einstellung für **CSS-Inlining**. Diese Einstellung bestimmt den gewünschten Standardwert, mit dem alle neuen E-Mail-Nachrichten beginnen. Beachten Sie, dass eine Änderung dieser Einstellung keine Auswirkungen auf Ihre bestehenden E-Mail-Nachrichten hat. Sie können diesen Standard jederzeit beim Verfassen von E-Mail-Nachrichten überschreiben.

![Option „Inline-CSS bei neuen E-Mails standardmäßig aktivieren" in den E-Mail-Einstellungen.]({% image_buster /assets/img_archive/css-inline1.png %})
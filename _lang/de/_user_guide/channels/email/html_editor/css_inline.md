---
nav_title: CSS-Inlining
article_title: CSS-Inlining
page_order: 5.1
description: "In diesem Referenzartikel erfahren Sie, wie Sie das CSS-Inlining aktivieren können und welche Best Practices es gibt."
channel:
  - email

---

# CSS-Inlining {#css-inlining}

> CSS-Inlining ist eine Form der E-Mail-Vorverarbeitung, bei der Stile aus einem CSS-Stylesheet in den Textkörper einer HTML-E-Mail verschoben werden. Der Begriff „Inlining“ bezieht sich darauf, dass Stile „inline“ auf einzelne HTML-Elemente angewendet werden.

Bei einigen E-Mail-Clients kann das CSS-Inlining die Darstellung von E-Mails verbessern und dazu beitragen, dass Ihre E-Mails so aussehen, wie Sie es erwarten. Wenn Sie bereits einen Großteil des CSS inlined haben oder sicher sind, dass Ihr HTML und CSS mit den Anforderungen der meisten Mail-Clients kompatibel sind, ist es möglicherweise nicht notwendig, dieses Feature zu aktivieren. Es kann dazu führen, dass dynamisch eingebettete Stile mit Ihren bestehenden Inline-Stilen in Konflikt geraten und die erwartete Vorschau und das Rendering von E-Mails verändern.

## CSS-Inlining verwenden {#using-css-inlining}

Mit dem Umschalter **Inline-CSS aktivieren** auf dem Tab **Versandinformationen** des HTML-Editors können Sie festlegen, ob das CSS-Inlining für jede E-Mail-Nachricht ein- oder ausgeschaltet wird.

![Kontrollkästchen zur Verwaltung des CSS-Inlinings im HTML-Composer.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Standard-Inlining-Status {#default-inlining-state}

Sie können unter **Einstellungen** > **E-Mail-Präferenzen** einen Standardstatus für die Aktivierung oder Deaktivierung festlegen. Suchen Sie die Einstellung für **CSS-Inlining**. Diese Einstellung bestimmt den gewünschten Standardwert, mit dem alle neuen E-Mail-Nachrichten beginnen. Beachten Sie, dass eine Änderung dieser Einstellung keine Auswirkungen auf Ihre bestehenden E-Mail-Nachrichten hat. Sie können diesen Standard jederzeit beim Verfassen von E-Mail-Nachrichten überschreiben.

![Option „Inline-CSS bei neuen E-Mails standardmäßig aktivieren“ in den E-Mail-Einstellungen.]({% image_buster /assets/img_archive/css-inline1.png %})

## Connected-Content und CSS-Inlining {#connected-content-and-css-inlining}

CSS-Inlining wird **vor** der Auswertung von [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) ausgeführt. HTML, das von Connected-Content zurückgegeben wird, durchläuft **nicht** denselben Inlining-Schritt. Fügen Sie Stile, die Sie aus Connected-Content benötigen, direkt in die Antwort ein (Inline-`style`-Attribute oder eingebettete Regeln), oder deaktivieren Sie das Inlining für die Nachricht, wenn das besser zu Ihrem Template passt.

## Content Blocks in benutzerdefinierten HTML-Templates {#content-blocks-in-custom-html-templates}

Wenn Sie einen [Content-Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) mit Liquid in ein **benutzerdefiniertes HTML**-E-Mail-Template oder eine Campaign einbinden, können CSS-Regeln im übergeordneten Template die im Content-Block definierten Stile überschreiben. Prüfen Sie, ob es im Template-Wrapper widersprüchliche Selektoren oder globale Regeln gibt.

## CSS-Einschränkungen bei Gmail {#gmail-css-limitations}

Gmail hat bestimmte CSS-Einschränkungen, die dazu führen können, dass E-Mails in der Gmail-App in der Desktop-Ansicht statt in der mobilen Ansicht angezeigt werden. Dies kann aus folgenden Gründen auftreten:

- **Zu viel CSS:** Wenn Ihre E-Mail übermäßig viel CSS enthält, kann Gmail den gesamten Style-Block entfernen.
- **Inkompatibles CSS:** Jedes CSS, das nicht mit Gmail kompatibel ist (einschließlich gültigem CSS, das Gmail nicht unterstützt), kann dazu führen, dass der Style-Block entfernt wird.
- **Nicht-Gmail-Konten in der Gmail-App:** CSS im `<head>` wird nicht unterstützt.

### Media-Queries in Gmail {#media-queries-in-gmail}

CSS-Media-Queries funktionieren in Gmail-Apps im Allgemeinen, es gibt jedoch Einschränkungen. Wenn Sie Probleme damit haben, dass Media-Queries in Gmail nicht korrekt funktionieren:

- Überprüfen Sie die [von Gmail unterstützte CSS-Referenz](https://developers.google.com/gmail/design/reference/supported_css), um sicherzustellen, dass Ihr CSS kompatibel ist.
- Lesen Sie die [Gmail-CSS-Designrichtlinien](https://developers.google.com/gmail/design/css) für Best Practices.
- Erwägen Sie Mobile-First-responsive-Designmuster, die sich für die mobile Darstellung nicht ausschließlich auf Media-Queries verlassen.
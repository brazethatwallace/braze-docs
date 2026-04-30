---
nav_title: Landing-Pages personalisieren
article_title: Landing-Pages personalisieren
description: "Dieser Artikel beschreibt, wie Sie Braze-Landing-Pages mit dem Drag-and-Drop-Editor personalisieren können."
page_order: 4
---

# Landing-Pages personalisieren {#personalize-landing-pages}

> Verwenden Sie Liquid-Personalisierung in Landing-Pages, um den Inhalt dynamisch mit Nutzerprofildaten anzupassen. So können Sie beispielsweise Überschriften basierend auf verschiedenen Nutzerattributen personalisieren, ohne mehrere statische Landing-Pages verwalten zu müssen.

{% alert important %}
Liquid-Personalisierung für Landing-Pages ist nur im Pro-Tier der Landing-Pages verfügbar. Derzeit werden [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), [Mehrsprachigkeit]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/) und [Aktionscodes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/) nicht mit Liquid-Personalisierung in Landing-Pages unterstützt.
{% endalert %}

## Liquid einfügen {#inserting-liquid}

Im Drag-and-Drop-Editor können Sie Liquid-Personalisierung sowohl im Editor als auch in den Seiten- oder Block-Einstellungen im rechten Panel einfügen. Anleitungen zur Implementierung von Liquid finden Sie in unserer speziellen [Liquid-Dokumentation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#using-liquid).

![Landing-Page-Editor mit hinzugefügter Liquid-Personalisierung.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Vorschau und Testen {#previewing-and-testing}

Wenn Sie eine Landing-Page im Editor in der Vorschau anzeigen, können Sie die Seite als zufällige:r Nutzer:in, als bestehende:r Nutzer:in oder als benutzerdefinierte:r Nutzer:in betrachten.

Wenn Sie die Landing-Page jedoch über die Datentabelle oder die Seite **Landing-Page-Details** in der Vorschau anzeigen, können Sie sie nur als zufällige:r Nutzer:in betrachten.

## Hinweise zur Personalisierung {#personalization-considerations}

Um eine optimale Performance bei personalisierten Landing-Pages zu gewährleisten, beachten Sie die folgenden Größenbeschränkungen:

- **Speichern einer Landing-Page:** Wenn die Größe 500&nbsp;KB überschreitet, erhalten Sie möglicherweise eine Warnmeldung, die darauf hinweist, dass die Seite unsere Größenbeschränkungen überschritten hat, was die Veröffentlichung verhindern kann.
- **Rendering mit Liquid-Personalisierung:** Die Gesamtgröße darf 1&nbsp;MB nicht überschreiten. Andernfalls kann die Seite automatisch von Braze zurückgezogen werden.

### Zurückziehen von Landing-Pages vermeiden {#avoid-unpublishing-landing-pages}

Wenn Ihre Seite diese Größenbeschränkungen überschreitet, erhalten Sie eine E-Mail, dass sie möglicherweise zurückgezogen wird, wenn sie die Grenze weiterhin überschreitet. Wenn der Schwellenwert erreicht ist, wird die Seite automatisch zurückgezogen, und Sie erhalten eine Benachrichtigung.

Um zu verhindern, dass Ihre Seite die Größenbeschränkungen überschreitet oder langsame Ladezeiten auftreten, stellen Sie sicher, dass die Liquid-Personalisierung:

- Nicht kontinuierlich durch große Datensätze iteriert oder diese referenziert.
- Nicht auf umfangreiche mathematische oder bedingte Logik innerhalb des Liquid-Blocks angewiesen ist.

Vermeiden Sie außerdem das direkte Einbetten großer Skripte, Stylesheets und Base64-kodierter Assets in Ihren Landing-Page-Code. Diese Inline-Assets zählen zur Seitengrößenbeschränkung und können das Rendering verlangsamen. Laden Sie stattdessen Schriftarten, Bilder, Stylesheets und Skripte in die [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) hoch. Assets, die über die Medienbibliothek bereitgestellt werden, werden auf dem CDN von Braze gehostet, sodass sie nicht für das Liquid-Rendering verarbeitet werden und nicht zur Seitengrößenbeschränkung zählen.

### Liquid für identifizierte und anonyme Nutzer:innen verwenden {#use-liquid-for-identified-and-anonymous-users}

Liquid kann das Landing-Page-Erlebnis sowohl für identifizierte als auch für anonyme Besucher:innen anpassen.

- **Identifizierte Nutzer:innen:** Verlinken Sie die Landing-Page aus einer Braze-Nachricht und fügen Sie den [Landing-Page-Liquid-Tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users/#using-landing-page-liquid-tags) hinzu. Dadurch wird die Person mit ihrem Braze-Profil verknüpft und das Seitenerlebnis personalisiert.
- **Anonyme Besucher:innen:** Verwenden Sie Liquid für kontextuelle, nicht profilbasierte Inhalte, wie z. B. eine Zufallszahl oder eine tageszeitabhängige Begrüßung.

## Fallback-Seiten {#fallback-pages}

Wenn Ihre Nutzer:innen versuchen, auf eine Seite zuzugreifen, die zurückgezogen wurde, sehen sie eine Meldung, dass die Seite derzeit nicht geladen werden kann. Gründe für das Zurückziehen einer Seite sind unter anderem:

- Komplexes oder fehlerhaftes Liquid, das zu langen Renderzeiten führen kann
- Netzwerkprobleme der Nutzer:innen
- Überschreitung der maximalen Landing-Page-Größenbeschränkungen
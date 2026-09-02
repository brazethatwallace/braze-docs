---
nav_title: Attribut-Trigger or triggern
article_title: Attribut-Trigger or triggern
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Dieser Referenzartikel gibt einen Überblick über Attribut-Trigger or triggern und wie Sie diese nutzen können, um aktionsbasierte Nachrichten an Nutzer:innen zu senden."
tool:
  - Campaigns

---

# Attribut-Trigger or triggern {#attribute-triggers}

> Mit Attribut-Trigger or triggern or triggern können Sie aktionsbasierte Nachrichten senden, wenn sich der Abo-Status oder die Werte angepasster Attribute einer Nutzerin oder eines Nutzers ändern.

Attribut-Trigger or triggern sind für die folgenden Szenarien verfügbar:

- Aktualisierungen des Abo-Status.
- Änderungen von booleschen, Zahl-, String- oder Zeittyp-Werten angepasster Attribute auf einen beliebigen Wert.
- Änderungen von booleschen, Zahl- oder String-Werten angepasster Attribute auf einen bestimmten Wert.

{% alert important %}
Im Dashboard verwenden ganzzahlige Attribute den Typ **Zahl**, und Datums- oder Zeitstempelwerte verwenden den Typ **Time** (diese werden in der UI nicht als „Integer“ oder „Date“ bezeichnet). Attribute vom Typ **Time** unterstützen **Change Custom Attribute Value** nur mit der Option **any new value** – sie unterstützen nicht die Option **specific value**.
{% endalert %}

Um Attribut-Trigger or triggern zu verwenden, erstellen Sie eine Campaign oder Canvas-Komponente und wählen Sie **Aktionsbasierte Zustellung** als Zustellungsmethode. Wählen Sie dann den Attribut-Trigger or triggern aus, den Sie verwenden möchten.

![Abschnitt „Aktionsbasierte Zustellung“ mit einem Dropdown zur Auswahl eines Triggers.]({% image_buster /assets/img_archive/trigger_attribute.png %})

## Abo-Status Update or aktualisieren or aktualisieren {#update-subscription-status}

Verwenden Sie den Trigger or triggern `Update Subscription Status`, um Nutzer:innen anzusprechen, wenn ihr Abo-Status aktualisiert wird.

Sie können beispielsweise Nutzer:innen ansprechen, wenn sich ihr E-Mail- oder Push-Abo-Status auf „Opted-in“ ändert, und ihnen für die Anmeldung danken. Sie können auch einen Webhook an Ihre Systeme senden, wenn sich Nutzer:innen von E-Mails abmelden, damit Ihre internen Systeme stets über die aktuellen Abo-Statusinformationen verfügen.

{% alert important %}
Dieser Trigger or triggern greift nicht, wenn neue Nutzer:innen mit dem globalen Standard-E-Mail-Status `subscribed` erstellt werden und eine nachfolgende Anfrage den Status auf `subscribed` aktualisiert, da sich der Abo-Status nicht geändert hat.
{% endalert %}

## Abo-Gruppenstatus Update or aktualisieren or aktualisieren {#update-subscription-group-status}

Verwenden Sie den Trigger or triggern `Update Subscription Group Status`, um Nutzer:innen anzusprechen, wenn ihr Abo-Gruppenstatus für E-Mail, Kurzmitteilungsdienst or SMS oder WhatsApp aktualisiert wird.

Sie können beispielsweise Nutzer:innen mit einer Willkommens-Kurzmitteilungsdienst or SMS ansprechen, wenn sie sich für Ihr Programm anmelden. Sie können auch die Quelle des Updates angeben, um eine genauere Kontrolle darüber zu haben, wann eine Nachricht ausgelöst wird.

Die verfügbaren Update or aktualisieren-Quellen variieren je nach Kanal:
- Canvas-Nutzeraktualisierung-Schritt
- CSV-Import
- List-Unsubscribe
- Präferenzzentrum
- Representational State Transfer API
- SDK or Software-Development-Kit
- Shopify (E-Mail, Kurzmitteilungsdienst or SMS)
- Eingehende Nachricht (Kurzmitteilungsdienst or SMS)

Beispielsweise möchten Sie Ihre Willkommens-Kurzmitteilungsdienst or SMS möglicherweise nur senden, wenn das Update or aktualisieren über die Representational State Transfer API kommt und nicht über eine eingehende Nachricht, da Braze bereits automatisch auf bestimmte eingehende Kurzmitteilungsdienst or SMS antwortet.

## Wert eines angepassten Attributs ändern {#change-custom-attribute-value}

Bei der Änderung eines Attributs wird zuerst der Trigger or triggern ausgewertet und dann die Zielgruppenkriterien. Dies unterscheidet sich vom Standardverhalten, bei dem zuerst die Zielgruppenkriterien und dann der Trigger or triggern ausgewertet werden. Um eine Race-Condition zu vermeiden, stellen Sie sicher, dass das als Trigger or triggern verwendete Attribut nicht dasselbe ist wie das Attribut, das zur Qualifizierung Ihrer Zielgruppe verwendet wird.

### Option „Beliebiger neuer Wert“ {#any-new-value-option}

Verwenden Sie den Trigger or triggern `Change Custom Attribute Value` mit der Option `any new value`, um Nutzer:innen anzusprechen, wenn sich ein boolescher, Zahl-, String- oder Zeittyp-Wert auf einen beliebigen neuen Wert ändert.

Sprechen Sie beispielsweise Nutzer:innen an, wenn sich ihre Anzahl an Rewards-Punkten ändert, um ihnen mitzuteilen, wie viele Punkte sie jetzt haben. Nehmen wir in diesem Beispiel an, dass eine Nutzerin oder ein Nutzer 85 Rewards-Punkte hat und Sie eine Campaign eingerichtet haben, die ausgelöst wird, wenn sich das Rewards-Punkte-Attribut auf einen beliebigen neuen Wert ändert. Wenn sich der Wert des Rewards-Punkte-Attributs auf einen beliebigen neuen Wert ändert (z. B. 83, 84, 86 usw.), wird die Campaign ausgelöst.

Betrachten Sie den nächsten Anwendungsfall mit einer Benachrichtigung über ein Stufen-Update or aktualisieren. Möglicherweise möchten Sie Nutzer:innen benachrichtigen, wenn sich ihre Rewards-Stufe ändert. Um diesen Anwendungsfall umzusetzen, richten Sie eine Campaign ein, die durch `Change Custom Attribute Value` getriggert wird, und konfigurieren Sie sie so, dass sie ausgelöst wird, wenn sich das angepasste Attribut „Rewards-Stufe“ auf einen beliebigen neuen Wert ändert.

{% alert important %}
Attribut-Trigger or triggern sind derzeit nicht für Array-Attribute verfügbar.
{% endalert %}

![Ein „Change Custom Attribute Value“-Trigger or triggern für „AA_current_rewards_tier“, der bei einer Änderung auf einen beliebigen Wert ausgelöst wird.]({% image_buster /assets/img_archive/any_value.png %})

Sie können auch Liquid verwenden, um den Nachrichtentext mit der neuen Rewards-Stufe der Kundin oder des Kunden zu personalisieren und weitere Informationen über die Änderung bereitzustellen.

{% raw %}
```liquid
Your rewards tier was just changed to {{custom_attribute.${AA_current_rewards_tier}}}
```
{% endraw %}

### Bestimmter Wert {#specific-value}

Verwenden Sie den Trigger or triggern `Change Custom Attribute Value` mit der Option `specific value`, um Nutzer:innen anzusprechen, wenn sich ein boolesches, Zahl- oder String-Attribut auf einen bestimmten Wert ändert.

Sprechen Sie beispielsweise Nutzer:innen an, wenn sich ihre Rewards-Stufe auf die beste Stufe ändert. Nehmen wir in diesem Beispiel an, dass die beste Rewards-Stufe „Super VIP“ ist. Sie können eine Campaign einrichten, die ausgelöst wird, wenn sich das angepasste Attribut „Rewards-Stufe“ auf `Super VIP` ändert, um der Nutzerin oder dem Nutzer zum Super-VIP-Status zu gratulieren.

![Ein „Change Custom Attribute Value“-Trigger or triggern für „AA_current_rewards_tier“, der bei einer Änderung auf den bestimmten Wert „super vip“ ausgelöst wird.]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Attribut-Trigger or triggern für bestimmte Werte angepasster Attribute sind nicht für Array- und Zeittyp-Attribute verfügbar.
- Der Trigger or triggern für die Änderung angepasster Attributwerte wird nicht ausgelöst, wenn der Wert des angepassten Attributs auf null aktualisiert wird.
- Der Trigger or triggern für die Änderung angepasster Attributwerte wird nur ausgelöst, wenn sich der Wert eines angepassten Attributs tatsächlich ändert. Wenn der aktuelle Wert eines angepassten Attributs erneut an Braze gesendet wird (z. B. der Wert für das Lieblingsfarbe-Attribut ist „Rot“ und Sie senden den Wert „Rot“ erneut an Braze), wird der Trigger or triggern für die Änderung angepasster Attributwerte nicht ausgelöst.
- Der Trigger or triggern für die Änderung angepasster Attributwerte gilt auch für neu erstellte Nutzer:innen.
{% endalert %}
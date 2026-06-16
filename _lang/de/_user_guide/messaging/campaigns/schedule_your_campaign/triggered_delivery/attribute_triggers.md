---
nav_title: Attribut-Trigger
article_title: Attribut-Trigger
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Dieser Referenzartikel gibt einen Überblick über Attribut-Trigger und wie Sie diese nutzen können, um aktionsbasierte Nachrichten an Nutzer:innen zu senden."
tool:
  - Campaigns

---

# Attribut-Trigger {#attribute-triggers}

> Mit Attribut-Triggern können Sie aktionsbasierte Nachrichten senden, wenn sich der Abo-Status oder die Werte angepasster Attribute einer Nutzerin oder eines Nutzers ändern.

Attribut-Trigger sind für die folgenden Szenarien verfügbar:

- Aktualisierungen des Abo-Status.
- Änderungen von booleschen, ganzzahligen oder String-Werten angepasster Attribute auf einen beliebigen oder einen bestimmten Wert.

{% alert important %}
Angepasste Attribute vom Typ „Datum“ sind im Dashboard nicht als Attribut-Trigger-Optionen verfügbar. Verwenden Sie einen anderen Zustellungs-Trigger oder Kanal-Workflow, um auf Datumsänderungen zu reagieren.
{% endalert %}

Um Attribut-Trigger zu verwenden, erstellen Sie eine Campaign oder Canvas-Komponente und wählen Sie **Aktionsbasierte Zustellung** als Zustellungsmethode. Wählen Sie dann den Attribut-Trigger aus, den Sie verwenden möchten.

![Abschnitt „Aktionsbasierte Zustellung“ mit einem Dropdown zur Auswahl eines Triggers.]({% image_buster /assets/img_archive/trigger_attribute.png %})

## Abo-Status aktualisieren {#update-subscription-status}

Verwenden Sie den Trigger `Update Subscription Status`, um Nutzer:innen anzusprechen, wenn ihr Abo-Status aktualisiert wird.

Sie können beispielsweise Nutzer:innen ansprechen, wenn sich ihr E-Mail- oder Push-Abo-Status auf „Opted-in“ ändert, und ihnen für die Anmeldung danken. Sie können auch einen Webhook an Ihre Systeme senden, wenn sich Nutzer:innen von E-Mails abmelden, damit Ihre internen Systeme stets über die aktuellen Abo-Statusinformationen verfügen.

{% alert important %}
Dieser Trigger greift nicht, wenn neue Nutzer:innen mit dem globalen Standard-E-Mail-Status `subscribed` erstellt werden und eine nachfolgende Anfrage den Status auf `subscribed` aktualisiert, da sich der Abo-Status nicht geändert hat.
{% endalert %}

## Abo-Gruppenstatus aktualisieren {#update-subscription-group-status}

Verwenden Sie den Trigger `Update Subscription Group Status`, um Nutzer:innen anzusprechen, wenn ihr Abo-Gruppenstatus für E-Mail, SMS oder WhatsApp aktualisiert wird.

Sie können beispielsweise Nutzer:innen mit einer Willkommens-SMS ansprechen, wenn sie sich für Ihr Programm anmelden. Sie können auch die Quelle des Updates angeben, um eine genauere Kontrolle darüber zu haben, wann eine Nachricht ausgelöst wird.

Die verfügbaren Update-Quellen variieren je nach Kanal:
- Canvas-Nutzeraktualisierung-Schritt
- CSV-Import
- List-Unsubscribe
- Präferenzzentrum
- REST API
- SDK
- Shopify (E-Mail, SMS)
- Eingehende Nachricht (SMS)

Beispielsweise möchten Sie Ihre Willkommens-SMS möglicherweise nur senden, wenn das Update über die REST API kommt und nicht über eine eingehende Nachricht, da Braze bereits automatisch auf bestimmte eingehende SMS antwortet.

## Wert eines angepassten Attributs ändern {#change-custom-attribute-value}

Bei der Änderung eines Attributs wird zuerst der Trigger ausgewertet und dann die Zielgruppenkriterien. Dies unterscheidet sich vom Standardverhalten, bei dem zuerst die Zielgruppenkriterien und dann der Trigger ausgewertet werden. Um eine Race-Condition zu vermeiden, stellen Sie sicher, dass das als Trigger verwendete Attribut nicht dasselbe ist wie das Attribut, das zur Qualifizierung Ihrer Zielgruppe verwendet wird.

### Option „Beliebiger neuer Wert“ {#any-new-value-option}

Verwenden Sie den Trigger `Change Custom Attribute Value` mit der Option `any new value`, um Nutzer:innen anzusprechen, wenn sich ein boolescher, ganzzahliger oder String-Wert auf einen beliebigen neuen Wert ändert.

Sprechen Sie beispielsweise Nutzer:innen an, wenn sich ihre Anzahl an Rewards-Punkten ändert, um ihnen mitzuteilen, wie viele Punkte sie jetzt haben. Nehmen wir in diesem Beispiel an, dass eine Nutzerin oder ein Nutzer 85 Rewards-Punkte hat und Sie eine Campaign eingerichtet haben, die ausgelöst wird, wenn sich das Rewards-Punkte-Attribut auf einen beliebigen neuen Wert ändert. Wenn sich der Wert des Rewards-Punkte-Attributs auf einen beliebigen neuen Wert ändert (z. B. 83, 84, 86 usw.), wird die Campaign ausgelöst.

Betrachten Sie den nächsten Anwendungsfall mit einer Benachrichtigung über ein Stufen-Update. Möglicherweise möchten Sie Nutzer:innen benachrichtigen, wenn sich ihre Rewards-Stufe ändert. Um diesen Anwendungsfall umzusetzen, richten Sie eine Campaign ein, die durch `Change Custom Attribute Value` getriggert wird, und konfigurieren Sie sie so, dass sie ausgelöst wird, wenn sich das angepasste Attribut „Rewards-Stufe“ auf einen beliebigen neuen Wert ändert.

{% alert important %}
Attribut-Trigger sind derzeit nicht für Array-Attribute verfügbar.
{% endalert %}

![Ein „Change Custom Attribute Value“-Trigger für „AA_current_rewards_tier“, der bei einer Änderung auf einen beliebigen Wert ausgelöst wird.]({% image_buster /assets/img_archive/any_value.png %})

Sie können auch Liquid verwenden, um den Nachrichtentext mit der neuen Rewards-Stufe der Kundin oder des Kunden zu personalisieren und weitere Informationen über die Änderung bereitzustellen.

{% raw %}
```liquid
Your rewards tier was just changed to {{custom_attribute.${AA_current_rewards_tier}}}
```
{% endraw %}

### Bestimmter Wert {#specific-value}

Verwenden Sie den Trigger `Change Custom Attribute Value` mit der Option `specific value`, um Nutzer:innen anzusprechen, wenn sich ein boolesches, ganzzahliges oder String-Attribut auf einen bestimmten Wert ändert.

Sprechen Sie beispielsweise Nutzer:innen an, wenn sich ihre Rewards-Stufe auf die beste Stufe ändert. Nehmen wir in diesem Beispiel an, dass die beste Rewards-Stufe „Super VIP“ ist. Sie können eine Campaign einrichten, die ausgelöst wird, wenn sich das angepasste Attribut „Rewards-Stufe“ auf `Super VIP` ändert, um der Nutzerin oder dem Nutzer zum Super-VIP-Status zu gratulieren.

![Ein „Change Custom Attribute Value“-Trigger für „AA_current_rewards_tier“, der bei einer Änderung auf den bestimmten Wert „super vip“ ausgelöst wird.]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Attribut-Trigger für bestimmte Werte angepasster Attribute sind nicht für Array- und Datums-Attribute verfügbar.
- Der Trigger für die Änderung angepasster Attributwerte wird nicht ausgelöst, wenn der Wert des angepassten Attributs auf null aktualisiert wird.
- Der Trigger für die Änderung angepasster Attributwerte wird nur ausgelöst, wenn sich der Wert eines angepassten Attributs tatsächlich ändert. Wenn der aktuelle Wert eines angepassten Attributs erneut an Braze gesendet wird (z. B. der Wert für das Lieblingsfarbe-Attribut ist „Rot“ und Sie senden den Wert „Rot“ erneut an Braze), wird der Trigger für die Änderung angepasster Attributwerte nicht ausgelöst.
- Der Trigger für die Änderung angepasster Attributwerte gilt auch für neu erstellte Nutzer:innen.
{% endalert %}
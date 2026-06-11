---
nav_title: Shopify checkout und Liquid
page_order: 7
description: "Dieser Artikel erklärt die Abschaffung von Shopify checkout&#46;liquid, einschließlich der Auswirkungen auf Ihre Shopify-Integration und der Anleitung für Entwickler:innen."
page_type: update

---

# Abschaffung von Shopify checkout&#46;liquid {#shopify-checkout46liquid-deprecation}

Shopify hat alle Händler über die Abschaffung von `checkout.liquid` und die Migration zu [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions) informiert, einer neuen Grundlage für den Aufbau angepasster Checkout-Erlebnisse.

Shopify wird `checkout.liquid` in zwei Phasen abschaffen:

1. **[13. August 2024](#phase-one-august-13-2024):** Deadline für das Upgrade Ihrer Informations-, Versand- und Zahlungsseiten.
2. **[28. August 2025](#phase-two-august-28-2025):** Deadline für das Upgrade Ihrer Dankes- und Auftragsstatus-Seiten, einschließlich Ihrer Apps mit Script-Tags und zusätzlichen Scripts.

Allgemeine Informationen zum Upgrade auf Checkout Extensibility finden Sie in [der Upgrade-Anleitung von Shopify](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility).

## Auswirkungen auf Ihre Integration {#impact-to-your-integration}

Die Braze- und Shopify-Integration verwendet [Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy), um das Braze Web SDK für nicht-headless Websites zu laden. Wir planen, eine neue Version der Integration vor der Frist 2025 zu veröffentlichen, um alle Kund:innen zu unterstützen, bevor `checkout.liquid` vollständig abgeschafft wird.

Für die bevorstehenden Änderungen am 13. August 2024 prüfen Sie bitte anhand der nachstehenden Details, ob Ihr Entwickler:innen-Team davon betroffen sein wird.

### Phase eins: 13. August 2024 {#phase-one-august-13-2024}

Bei der Standard-Integration von Braze und Shopify werden die Informations-, Versand- und Zahlungsseiten innerhalb der Kaufabwicklung nicht verwendet. Die Standard-Integration ist daher nicht betroffen.

#### Shopify Plus

Für Shopify-Plus-Kund:innen werden alle angepassten SDK-Code-Snippets, die `checkout.liquid` für die Informations-, Versand- oder Zahlungsseiten ändern, nach diesem Datum inaktiv. Angepasster Code, der Ereignisse von diesen Seiten protokolliert, wird zum Beispiel nicht mehr funktionieren. Wenn Sie angepassten SDK-Code haben, lesen Sie unsere [Anleitung für Entwickler:innen](#developer-guidance) zur Migration.

#### Nicht-Shopify Plus {#non-shopify-plus}

Für Kund:innen ohne Shopify Plus müssen Sie, wenn Sie die Informations-, Zahlungs- und Versandseiten anpassen möchten, [auf Shopify Plus upgraden](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) und dann der [Anleitung für Entwickler:innen](#developer-guidance) folgen.

### Phase zwei: 28. August 2025 {#phase-two-august-28-2025}

Shopify wird die Unterstützung für [ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) auf `checkout.liquid`-Seiten, die in der Integration verwendet werden, abschaffen. Als Reaktion darauf arbeiten wir aktiv an einer neuen Version der Shopify-Integration, die wir rechtzeitig vor dem Stichtag im August 2025 veröffentlichen wollen. Bleiben Sie dran für weitere Informationen vom Braze-Produktteam.

## Anleitung für Entwickler:innen {#developer-guidance}

Diese Anleitung gilt für Shopify-Plus-Kund:innen, die angepasste SDK-Code-Snippets zu den Informations-, Versand- oder Zahlungsseiten in `checkout.liquid` hinzugefügt haben. Wenn Sie diese Anpassungen nicht vorgenommen haben, können Sie diese Anleitung ignorieren.

Sie können keine angepassten SDK-Code-Snippets mehr zu den Informations-, Versand- oder Zahlungsseiten in `checkout.liquid` hinzufügen. Stattdessen müssen Sie angepasste SDK-Code-Snippets zu den Dankes- oder Auftragsstatus-Seiten hinzufügen. Damit können Sie Nutzer:innen, die den Checkout abgeschlossen haben, abgleichen.
1. Laden Sie das Braze Web SDK auf den Dankes- und Auftragsstatus-Seiten.
2. Rufen Sie die E-Mail-Adresse der Nutzer:innen ab.
3. Rufen Sie `setEmail` auf.

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4. Führen Sie auf Braze die Nutzerprofile per E-Mail zusammen.

Wenn Sie auf doppelte Nutzerprofile stoßen, können Sie unser [Tool zur Massenzusammenführung]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging) verwenden, um Ihre Daten zu bereinigen.
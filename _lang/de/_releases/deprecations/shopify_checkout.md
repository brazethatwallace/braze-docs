---
nav_title: Shopify checkout und Liquid
page_order: 7
description: "Dieser Artikel erklärt die Abschaffung von Shopify checkout&#46;liquid, einschließlich der Auswirkungen auf Ihre Shopify-Integration und der Anleitung für Entwickler:innen."
page_type: update

---

# Abschaffung von Shopify checkout&#46;liquid {#shopify-checkout46liquid-deprecation}

Shopify hat alle Händler über die Abschaffung von `checkout.liquid` und die Migration zu [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions) informiert, einer neuen Grundlage für den Aufbau angepasster Checkout-Erlebnisse.

Shopify wird `checkout.liquid` in zwei Phasen abschaffen:

1. **[13. August 2024](#phase-one-august-13-2024):** Deadline für das Upgrade or upgraden Ihrer Informations-, Versand- und Zahlungsseiten.
2. **[28. August 2025](#phase-two-august-28-2025):** Deadline für das Upgrade or upgraden Ihrer Dankes- und Auftragsstatus-Seiten, einschließlich Ihrer Apps mit Script-Tags und zusätzlichen Scripts.

Allgemeine Informationen zum Upgrade or upgraden auf Checkout Extensibility finden Sie in [der Upgrade or upgraden-Anleitung von Shopify](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility).

## Auswirkungen auf Ihre Integration {#impact-to-your-integration}

Die Integration von Braze und Shopify nutzt [Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy), um das Braze Web SDK or Software-Development-Kit für Websites ohne Headless-Architektur zu laden. Wir planen, vor der Frist 2025 eine neue Version der Integration bereitzustellen, um alle Kund:innen zu unterstützen, bevor `checkout.liquid` vollständig eingestellt wird.

Prüfen Sie für die anstehenden Änderungen am 13. August 2024 die folgenden Details, um festzustellen, ob Ihr Entwicklungsteam betroffen ist.

### Phase eins: 13. August 2024 {#phase-one-august-13-2024}

Die Standard-Integration von Braze und Shopify verwendet nicht die Informations-, Versand- und Zahlungsseiten innerhalb des Checkout-Erlebnisses. Daher ist die Standardintegration nicht betroffen.

#### Shopify Plus

Für Shopify-Plus-Kund:innen werden alle angepassten SDK or Software-Development-Kit-Code-Snippets, die `checkout.liquid` für die Informations-, Versand- oder Zahlungsseiten modifizieren, nach diesem Datum inaktiv. Zum Beispiel funktioniert angepasster Code, der Ereignisse von diesen Seiten protokolliert, nicht mehr. Wenn Sie angepassten SDK or Software-Development-Kit-Code verwenden, lesen Sie unsere [Entwickler:innen-Anleitung](#developer-guidance) zur Migration.

#### Ohne Shopify Plus {#non-shopify-plus}

Wenn Sie kein Shopify Plus nutzen und die Informations-, Zahlungs- und Versandseiten anpassen möchten, müssen Sie [ein Upgrade or upgraden auf Shopify Plus durchführen](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) und anschließend der [Entwickler:innen-Anleitung](#developer-guidance) folgen.

### Phase zwei: 28. August 2025 {#phase-two-august-28-2025}

Shopify wird die Unterstützung für [ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) auf `checkout.liquid`-Seiten einstellen, die in der Integration verwendet werden. Als Reaktion darauf arbeiten wir aktiv an einer neuen Version der Shopify-Integration, die wir rechtzeitig vor der Frist im August 2025 veröffentlichen möchten. Bleiben Sie auf dem Laufenden für weitere Informationen vom Braze-Produktteam.

## Entwickler:innen-Hinweise {#developer-guidance}

Diese Hinweise gelten für Shopify Plus-Kund:innen, die angepasste SDK or Software-Development-Kit-Code-Snippets zu den Informations-, Versand- oder Zahlungsseiten in `checkout.liquid` hinzugefügt haben. Wenn Sie diese Anpassungen nicht vorgenommen haben, können Sie diese Hinweise ignorieren.

Sie können keine angepassten SDK or Software-Development-Kit-Code-Snippets mehr zu den Informations-, Versand- oder Zahlungsseiten in `checkout.liquid` hinzufügen. Stattdessen müssen Sie angepasste SDK or Software-Development-Kit-Code-Snippets zu den Dankes- oder Auftragsstatusseiten hinzufügen. Dadurch können Sie Nutzer:innen abgleichen, die den Checkout abgeschlossen haben.
1. Laden Sie das Braze Web SDK or Software-Development-Kit auf den Dankes- und Auftragsstatusseiten.
2. Rufen Sie die E-Mail-Adresse der Nutzer:innen ab.
3. Rufen Sie `setEmail` auf.

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4. Führen Sie in Braze die Zusammenführung der Nutzerprofile anhand der E-Mail-Adresse durch.

Wenn Sie auf doppelte Nutzerprofile stoßen, können Sie unser [Tool zur Massenzusammenführung]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#bulk-merging) verwenden, um Ihre Daten zu optimieren.
---
nav_title: Features auswählen
article_title: Features für Decisioning Studio auswählen
page_order: 7
page_type: reference
description: "Dieser Referenzartikel behandelt, wie Sie effektive Kund:innen-Features für BrazeAI Decisioning Studio erstellen, einschließlich Feature-Typen, allgemeiner Richtlinien, Konstruktion von Verhaltens-Features und der Beziehung zwischen Features und dem Aktionsraum."
---

# Gute Features auswählen {#choose-good-features}

> Das Decisioning-Studio-Modell verwendet Kund:innen-Features als Eingaben, um individualisierte Empfehlungen zu erstellen. Hochwertige Features, die gut auf Ihren Entscheidungsraum abgestimmt sind, gehören zu den wirkungsvollsten Hebeln zur Verbesserung der Modell-Performance. Dieser Artikel behandelt die Arten von Features, die Sie bereitstellen können, wie Sie diese gut konstruieren und wie Sie Features mit den Aktionen in Einklang bringen, zwischen denen Ihr Agent wählt.

Wenn Sie interne Data-Science- oder Data-Engineering-Teams haben, sind diese am besten geeignet, Features zu konstruieren und zu kuratieren, da sie den meisten Kontext darüber haben, welche Signale in Ihren Daten aussagekräftig sind.

{% alert note %}
Für Braze-Kund:innen werden Kund:innen-Features typischerweise über angepasste Attribute in Nutzerprofilen an Decisioning Studio übergeben. Details zu angepassten Attributen im Vergleich zu angepassten Events und deren jeweiligen Update-Strategien finden Sie unter [Snapshots versus Event-Streams]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams).
{% endalert %}

## Typen von Kund:innen-Features {#types-of-customer-features}

Es gibt vier gängige Kategorien von Kund:innen-Features:

| Feature-Typ | Was er erfasst | Beispiele |
|-------------|-----------------|---------|
| **Nutzerprofil** | Objektive Fakten über den Status der geschäftskunden | `age`, `loyalty_tier`, `days_enrolled`, `city`, `acquisition_channel` |
| **Nutzerneigung** | Modellbasierte Scores für die Wahrscheinlichkeit, dass Kund:innen etwas tun | `churn_risk_score`, `purchase_intent_score`, `upsell_affinity` |
| **Nutzerverhalten** | Zusammenfassungen der Kund:innenaktivität über ein Zeitfenster | `clicks_past_30d`, `purchases_past_7d`, `app_logins_past_14d` |
| **Umgebung** | Kontextuelle Signale außerhalb der geschäftskunden | `is_promotional_period`, `is_holiday`, `regional_economic_index` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Typen von Kund:innen-Features" }

Zusammen geben diese Feature-Typen dem Modell die Informationen, die es benötigt, um Segmente zu identifizieren, zwischen Kund:innen zu unterscheiden und Empfehlungen entsprechend anzupassen.

## Allgemeine Richtlinien {#general-guidelines}

Beachten Sie Folgendes bei der Auswahl und Konstruktion von Features:

- **Abdeckung:** Features sollten alle Kund:innen in Ihrer Zielgruppe abdecken. Ein Feature, das für einen großen Teil Ihrer Zielgruppe fehlt oder null ist, gibt dem Modell für diese Kund:innen weniger Informationen.
- **Granularität:** Alle Features sollten auf Kund:innenebene aggregiert sein. Siehe [Externe Braze-ID verwenden]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/braze_external_id) für Hinweise, was „Kund:innenebene“ in der Praxis bedeutet.
- **Aktualität:** Features sollten nach einem zeitgesteuerten Zeitplan aktualisiert werden, nicht nach einem eventgesteuerten. Siehe [Snapshots versus Event-Streams]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams) für die Gründe.
- **Gültigkeit:** Feature-Werte sollten in Bereichen liegen, die angesichts der Definition sinnvoll sind. Ein Feature für „Käufe in den letzten 30 Tagen“ sollte niemals negativ sein.
- **Spärlichkeit:** Vermeiden Sie Features, die für die überwiegende Mehrheit der Kund:innen null oder leer sind, es sei denn, es gibt einen klaren geschäftlichen Grund. Spärliche Features fügen Rauschen hinzu, ohne Signal beizutragen.
- **Korrelation:** Vermeiden Sie Features, die stark miteinander korreliert sind. Redundante Features können Verzerrungen einführen und das Training verlangsamen, ohne die Prognosen zu verbessern.

## Verhaltens-Features konstruieren {#construct-behavioral-features}

Verhaltens-Features fassen die Aktionshistorie von Kund:innen über ein definiertes Zeitfenster zusammen (zum Beispiel „Anzahl der Käufe in den letzten 28 Tagen“). Diese gehören zu den wertvollsten Features für ein Empfehlungssystem, da sie erfassen, wie sich Kund:innen tatsächlich verhalten – und nicht nur statische Profilmerkmale.

### Zeitfenster wählen {#choose-time-windows}

Das richtige Zeitfenster hängt davon ab, wie häufig Kund:innen die gemessene Aktion ausführen:

- **Kurze Fenster (7–28 Tage):** Verwenden Sie diese für hochfrequente Aktivitäten wie App-Anmeldungen, E-Mail-Öffnungen oder Website-Besuche.
- **Lange Fenster (90–365 Tage):** Verwenden Sie diese für seltene Aktivitäten wie Produktkäufe, Abo-Verlängerungen oder Kundenservice-Kontakte.

Eine nützliche Diagnose: Wenn ein großer Prozentsatz Ihrer Feature-Werte null ist, ist das Zeitfenster wahrscheinlich zu kurz. Erweitern Sie es, bis Sie eine aussagekräftige Varianz über die Kund:innen hinweg sehen.

### Aggregationen wählen {#choose-aggregations}

- **Für Events ohne Wert** (etwas ist entweder passiert oder nicht): Verwenden Sie **Count**-Aggregationen. Zum Beispiel `email_opens_past_30d`.
- **Für Events mit einem zugehörigen Wert** (Umsatz, Dauer, Menge): Verwenden Sie sowohl **Summen**- als auch **Durchschnitts**-Aggregationen. Zum Beispiel `purchase_value_sum_past_90d` und `purchase_value_avg_past_90d`. Diese liefern komplementäre Informationen über das Gesamtvolumen und die Größenordnung pro Event.

## Features mit dem Aktionsraum abstimmen {#align-features-with-the-action-space}

Decisioning Studio ist kein Propensity-Modell, sondern ein Ranking-System. Sein Ziel ist es, für jede geschäftskunden zu identifizieren, welche Aktion aus einer definierten Menge von Optionen am wahrscheinlichsten das beste Ergebnis erzielt. Dies schafft eine spezifische Anforderung: **Features sollten dem Modell, wo möglich, Informationen liefern, die ihm helfen, zwischen den verfügbaren Optionen für eine bestimmte geschäftskunden zu unterscheiden.**

### Warum das wichtig ist {#why-this-matters}

Angenommen, der Aktionsraum Ihres Agents besteht darin, eines von drei Menüartikeln zu empfehlen: Kaffee, Schwarztee oder Bubble Tea.

Wenn Ihre Features Kund:innen auf einer hohen Ebene beschreiben („bestellt häufig Getränke“ oder „hohes E-Mail-Engagement“), kann das Modell Kund:innen in breite Gruppen segmentieren. Aber wenn es darum geht, Kaffee versus Bubble Tea für eine bestimmte geschäftskunden zu ranken, helfen breite Features nicht viel. Zwei Kund:innen können bei allgemeinen Features identisch aussehen, aber völlig entgegengesetzte Präferenzen haben.

Wenn das Modell auf widersprüchliche Signale stößt – etwa wenn es zwei scheinbar ähnlichen Kund:innen Kaffee empfiehlt, aber nur eine konvertiert –, kann es nicht effektiv lernen. Das Rauschen reduziert seine Fähigkeit, genaue Rankings zu erstellen.

### Features erstellen, die zum Aktionsraum passen {#build-features-that-match-the-action-space}

Features, die auf derselben Granularität wie Ihr Aktionsraum abgebildet sind, geben dem Modell deutlich stärkere Ranking-Signale. Im Café-Beispiel sagt ein Feature wie `coffee_orders_past_14d` dem Modell direkt, ob eine geschäftskunden Kaffee bevorzugt. Ein Feature wie `black_tea_orders_past_14d` leistet dasselbe für Schwarztee. Das Modell kann nun eine fundierte Ranking-Entscheidung treffen.

Mit aktionsausgerichteten Features kann das Modell auch Sättigung und Ermüdung erkennen. Wenn eine geschäftskunden einen hohen `coffee_orders_past_14d`-Wert hat, aber bei einer kürzlichen Kaffee-Empfehlung nicht konvertiert hat, lernt das Modell, dass eine erneute Kaffee-Empfehlung möglicherweise nicht die beste Wahl ist, und beginnt, Alternativen zu testen.

### Wenn eine exakte Abstimmung nicht möglich ist {#when-exact-alignment-isnt-available}

Eine exakte Feature-zu-Aktion-Abstimmung ist das Ideal, wird aber oft durch die Datenverfügbarkeit eingeschränkt. Zwei Ansätze können helfen, wenn Sie keine perfekt abgestimmten Features erstellen können:

**Datenzusammenfassung:** Wenn Sie nicht zwischen Schwarztee- und Bubble-Tea-Käufen unterscheiden können, verwenden Sie ein aggregiertes Feature `tea_orders_past_14d`. Dies verliert etwas Präzision, hilft dem Modell aber dennoch, Tee-bevorzugende Kund:innen von Kaffee-bevorzugenden zu unterscheiden.

**Indirekte Signale:** Features, die nicht direkt im Aktionsraum liegen, können dennoch wertvoll sein, wenn sie eine logische Beziehung dazu haben. Zum Beispiel ist `dessert_purchased_past_30d` ein vernünftiger Proxy für die Präferenz für süße Artikel, die wahrscheinlich mit der Bubble-Tea-Präferenz korreliert. Das Modell kann aus diesen indirekten Signalen lernen, auch ohne ein direktes Feature-Match.

Das zugrunde liegende Prinzip ist, dass relevantere und granularere Informationen immer helfen, das Modell aber auch aus unvollkommenen Features lernen kann. Beginnen Sie mit dem, was Sie haben, und verfeinern Sie es im Laufe der Zeit, wenn mehr Daten verfügbar werden.
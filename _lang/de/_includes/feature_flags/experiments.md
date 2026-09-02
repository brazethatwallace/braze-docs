# Feature-Flag-Experimente {#feature-flag-experiments}

> Mit Feature-Flag-Experimenten können Sie A/B-Tests mit Anwendungsänderungen durchführen, um die Konversionsraten zu optimieren. Marketer können Feature-Flags verwenden, um herauszufinden, ob sich ein neues Feature positiv oder negativ auf die Konversionsraten auswirkt, oder welche Feature-Flag-Eigenschaften am besten geeignet sind.

## Voraussetzungen {#prerequisites}

Bevor Sie Nutzerdaten im Experiment erfassen können, muss Ihre App aufzeichnen, wann Nutzer:innen mit einem Feature-Flag interagieren. Dies wird als Feature-Flag-Impression bezeichnet. Stellen Sie sicher, dass Sie eine Feature-Flag-Impression protokollieren, wann immer Nutzer:innen das zu testende Feature sehen oder hätten sehen können – auch wenn sie sich in der Kontrollgruppe befinden.

Weitere Informationen zum Protokollieren von Feature-Flag-Impressionen finden Sie unter [Feature-Flags erstellen]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#impressions).

{% tabs %}
{% tab Web %}

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewFeature();
} else {
  return new ExistingFeature();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("my-new-feature")
braze.logFeatureFlagImpression("my-new-feature")
if (featureFlag?.enabled == true) {
  return NewFeature()
} else {
  return ExistingFeature()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Erstellen eines Feature-Flag-Experiments {#creating-a-feature-flag-experiment}

### Schritt 1: Experiment erstellen {#step-1-create-an-experiment}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **+ Create Campaign** aus.
2. Wählen Sie **Feature Flag Experiment** aus.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.

### Schritt 2: Experimentvarianten hinzufügen {#step-2-add-experiment-variants}

Erstellen Sie als Nächstes Variationen. Wählen Sie für jede Variante das Feature-Flag aus, das Sie ein- oder ausschalten möchten, und überprüfen Sie dann die zugewiesenen Eigenschaften.

Um die Auswirkung Ihres Features zu testen, verwenden Sie Varianten, um den Traffic in zwei oder mehr Gruppen aufzuteilen. Benennen Sie eine Gruppe „Meine Kontrollgruppe“ und schalten Sie deren Feature-Flags aus.

Feature-Flag-Experimente unterstützen bis zu neun Gruppen insgesamt: eine Kontrollgruppe plus bis zu acht Varianten.

### Schritt 3: Eigenschaften überschreiben (optional) {#step-3-overwrite-properties-optional}

Sie können die Standardeigenschaften überschreiben, die Sie ursprünglich für Nutzer:innen eingerichtet haben, die eine bestimmte Kampagnenvariante erhalten.

Um zusätzliche Standardeigenschaften zu bearbeiten, hinzuzufügen oder zu entfernen, bearbeiten Sie das Feature-Flag selbst unter **Messaging** > **Feature Flags**. Wenn eine Variante deaktiviert ist, gibt das SDK or Software-Development-Kit ein leeres Eigenschaftsobjekt für das entsprechende Feature-Flag zurück.

![Der Abschnitt „Experimentvarianten“ mit dem überschriebenen Variablenschlüssel „link“ mit dem Wert „/sales“.]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### Schritt 4: Zielgruppe zusammenstellen {#step-4-choose-users-to-target}

Verwenden Sie eines Ihrer Segments oder Filter, um Ihre [Zielgruppe zusammenzustellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users). Sie können beispielsweise den Filter **Received Feature Flag Variant** verwenden, um Nutzer:innen erneut anzusprechen, die bereits einen A/B-Test erhalten haben.

![Die Seite „Zielgruppe“ in einem Feature-Flag-Experiment mit „Received Feature Flag Variant“ hervorgehoben in der Suchleiste der Filtergruppe.]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
Die Segment-Zugehörigkeit wird berechnet, wenn Feature-Flags für bestimmte Nutzer:innen aktualisiert werden. Änderungen werden verfügbar, nachdem Ihre App die Feature-Flags aktualisiert hat oder eine neue Sitzung gestartet wurde.
{% endalert %}

### Schritt 5: Varianten verteilen {#step-5-distribute-variants}

Wählen Sie die prozentuale Verteilung für Ihr Experiment. Als Best Practice sollten Sie die Verteilung nicht mehr ändern, nachdem Ihr Experiment gestartet wurde.

### Schritt 6: Konversionen zuweisen {#step-6-assign-conversions}

Mit Braze können Sie verfolgen, wie oft Nutzer:innen bestimmte Aktionen – [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) – nach Erhalt einer Campaign durchführen. Legen Sie ein Zeitfenster von bis zu 30 Tagen fest, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

### Schritt 7: Überprüfen und starten {#step-7-review-and-launch}

Nachdem Sie den letzten Teil Ihres Experiments fertiggestellt haben, überprüfen Sie die Details und wählen Sie dann **Launch Experiment** aus.

## Überprüfung der Ergebnisse {#reviewing-the-results}

Nachdem Ihr Feature-Flag-Experiment abgeschlossen ist, können Sie die Impressionsdaten für Ihr Experiment überprüfen. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie die Campaign mit Ihrem Feature-Flag-Experiment aus.

### Campaign Analytics

**Campaign Analytics** bietet eine allgemeine Übersicht über die Performance Ihres Experiments, wie zum Beispiel:

- Die Gesamtzahl der Impressionen
- Die Anzahl der eindeutigen Impressionen
- Die primäre Konversionsrate
- Der durch die Nachricht generierte Gesamtumsatz
- Die geschätzte Zielgruppe

Sie können auch die Einstellungen des Experiments für Zustellung, Zielgruppe und Konversion einsehen.

### Feature-Flag-Experiment-Performance

**Feature Flags Experiments Performance** zeigt, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die spezifischen Metriken, die Sie sehen, variieren je nach gewähltem Messaging-Kanal und ob Sie einen multivariaten Test durchführen. Um die Feature-Flag-Werte zu sehen, die mit jeder Variante verknüpft sind, wählen Sie **Preview** aus.
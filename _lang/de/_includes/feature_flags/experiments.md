# Feature-Flag-Experimente {#feature-flag-experiments}

> Mit Feature-Flag-Experimenten können Sie A/B-Tests mit Anwendungsänderungen durchführen, um die Konversionsraten zu optimieren. Marketer können Feature-Flags verwenden, um herauszufinden, ob sich ein neues Feature positiv oder negativ auf die Konversionsraten auswirkt, oder welche Feature-Flag-Eigenschaften am besten geeignet sind.

## Voraussetzungen {#prerequisites}

Bevor Sie Nutzerdaten im Experiment tracken können, muss Ihre App aufzeichnen, wann Nutzer:innen mit einem Feature-Flag interagieren. Dies wird als Feature-Flag-Impression bezeichnet. Vergewissern Sie sich, dass Sie jedes Mal eine Feature-Flag-Impression protokollieren, wenn Nutzer:innen das zu testende Feature sehen oder gesehen haben könnten, auch wenn sie in der Kontrollgruppe sind.

Weitere Informationen zur Protokollierung von Feature-Flag-Impressionen finden Sie unter [Feature-Flags erstellen]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#impressions).

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

## Ein Feature-Flag-Experiment erstellen {#creating-a-feature-flag-experiment}

### Schritt 1: Ein Experiment erstellen {#step-1-create-an-experiment}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **+ Create Campaign**.
2. Wählen Sie **Feature Flag Experiment**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.

### Schritt 2: Experimentiervarianten hinzufügen {#step-2-add-experiment-variants}

Als Nächstes erstellen Sie Variationen. Wählen Sie für jede Variante das Feature-Flag, das Sie ein- oder ausschalten möchten, und überprüfen Sie dann die zugewiesenen Eigenschaften.

Um die Wirkung Ihres Features zu testen, verwenden Sie Varianten, um den Traffic in zwei oder mehr Gruppen aufzuteilen. Nennen Sie eine Gruppe „Meine Kontrollgruppe“ und deaktivieren Sie die Feature-Flags.

Feature-Flag-Experimente unterstützen insgesamt bis zu neun Gruppen: eine Kontrollgruppe plus bis zu acht Varianten.

### Schritt 3: Eigenschaften überschreiben (optional) {#step-3-overwrite-properties-optional}

Sie können die Standard-Eigenschaften, die Sie ursprünglich für Nutzer:innen mit einer bestimmten Kampagnenvariante eingerichtet haben, überschreiben.

Um zusätzliche Standardeigenschaften zu bearbeiten, hinzuzufügen oder zu entfernen, bearbeiten Sie das Feature-Flag selbst unter **Messaging** > **Feature Flags**. Wenn eine Variante deaktiviert ist, gibt das SDK ein leeres Eigenschaften-Objekt für das angegebene Feature-Flag zurück.

![Der Abschnitt „Experimentvarianten“ mit dem Variablenschlüssel „link“, der mit „/sales“ überschrieben wurde.]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### Schritt 4: Zielgruppe auswählen {#step-4-choose-users-to-target}

Verwenden Sie eines Ihrer Segmente oder Filter, um Ihre [Zielgruppe zusammenzustellen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users). Sie können zum Beispiel den Filter **Received Feature Flag Variant** verwenden, um Nutzer:innen, die bereits einen A/B-Test erhalten haben, erneut anzusprechen.

![Die Seite „Zielgruppe“ in einem Feature-Flag-Experiment, wobei „Received Feature Flag Variant“ in der Suchleiste der Filtergruppe hervorgehoben ist.]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
Die Segmentzugehörigkeit wird berechnet, wenn die Feature-Flags für bestimmte Nutzer:innen aktualisiert werden. Die Änderungen werden bereitgestellt, wenn Ihre App die Feature-Flags aktualisiert oder wenn eine neue Sitzung gestartet wird.
{% endalert %}

### Schritt 5: Varianten verteilen {#step-5-distribute-variants}

Wählen Sie die prozentuale Verteilung für Ihr Experiment. Es empfiehlt sich, die Verteilung nach dem Starten des Experiments nicht mehr zu ändern.

### Schritt 6: Konversionen zuweisen {#step-6-assign-conversions}

Mit Braze können Sie nachverfolgen, wie oft Nutzer:innen nach Erhalt einer Campaign bestimmte Aktionen, d. h. [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events), durchführen. Geben Sie ein Zeitfenster von bis zu 30 Tagen an, in dem eine Konversion gezählt wird, wenn Nutzer:innen die angegebene Aktion durchführen.

### Schritt 7: Überprüfung und Start {#step-7-review-and-launch}

Nachdem Sie den letzten Teil Ihres Experiments fertiggestellt haben, überprüfen Sie dessen Details und wählen dann **Launch Experiment**.

## Überprüfung der Ergebnisse {#reviewing-the-results}

Nachdem Ihr Feature-Flag-Experiment abgeschlossen ist, können Sie die Impressions-Daten für Ihr Experiment überprüfen. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie die Campaign mit Ihrem Feature-Flag-Experiment.

### Campaign Analytics

**Campaign Analytics** bietet eine Übersicht über die Performance Ihres Experiments, z. B.:

- Die Gesamtzahl der Impressionen
- Die Anzahl der eindeutigen Impressionen
- Die primäre Konversionsrate
- Der Gesamtumsatz, der durch die Nachricht generiert wurde
- Die geschätzte Zielgruppe

Sie können auch die Einstellungen des Experiments für Zustellung, Zielgruppe und Konversion einsehen.

### Feature-Flag-Experiment-Performance

**Feature Flags Experiments Performance** zeigt, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die spezifischen Metriken, die Sie sehen, hängen von dem von Ihnen gewählten Messaging-Kanal ab und davon, ob Sie einen multivariaten Test durchführen. Um die mit jeder Variante verbundenen Feature-Flag-Werte zu sehen, wählen Sie **Vorschau**.
# Expériences d'indicateurs de fonctionnalité {#feature-flag-experiments}

> Les expériences d'indicateurs de fonctionnalités vous permettent d'effectuer des tests A/B sur les modifications apportées à vos applications afin d'optimiser les taux de conversion. Les marketeurs peuvent utiliser les indicateurs de fonctionnalité pour déterminer si une nouvelle fonctionnalité a un impact positif ou négatif sur les taux de conversion, ou quel ensemble de propriétés d'indicateurs de fonctionnalité est le plus optimal.

## Prérequis {#prerequisites}

Avant de pouvoir suivre les données utilisateur dans l'expérience, votre application doit enregistrer le moment où un utilisateur interagit avec un indicateur de fonctionnalité. C'est ce qu'on appelle une impression d'indicateur de fonctionnalité. Veillez à enregistrer une impression d'indicateur de fonctionnalité chaque fois qu'un utilisateur voit ou aurait pu voir la fonctionnalité que vous testez, même s'il fait partie du groupe de contrôle.

Pour en savoir plus sur l'enregistrement des impressions d'indicateurs de fonctionnalité, consultez [Créer des indicateurs de fonctionnalité]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#impressions).

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

## Créer une expérience d'indicateur de fonctionnalité {#creating-a-feature-flag-experiment}

### Étape 1 : Créer une expérience {#step-1-create-an-experiment}

1. Allez dans **Messaging** > **Campaigns**, puis sélectionnez **+ Create Campaign**.
2. Sélectionnez **Feature Flag Experiment**.
3. Donnez à votre campagne un nom clair et significatif.

### Étape 2 : Ajouter des variantes d'expérience {#step-2-add-experiment-variants}

Ensuite, créez des variations. Pour chaque variante, choisissez l'indicateur de fonctionnalité que vous souhaitez activer ou désactiver, puis examinez ses propriétés assignées.

Pour tester l'impact de votre fonctionnalité, utilisez des variantes pour diviser le trafic en deux groupes ou plus. Nommez un groupe « Mon groupe de contrôle » et désactivez ses indicateurs de fonctionnalité.

Les expériences d'indicateurs de fonctionnalité prennent en charge jusqu'à neuf groupes au total : un groupe de contrôle plus jusqu'à huit variantes.

### Étape 3 : Remplacer les propriétés (facultatif) {#step-3-overwrite-properties-optional}

Vous pouvez choisir de remplacer les propriétés par défaut que vous avez initialement configurées pour les utilisateurs qui reçoivent une variante de campagne spécifique.

Pour modifier, ajouter ou supprimer des propriétés par défaut supplémentaires, modifiez l'indicateur de fonctionnalité lui-même depuis **Messaging** > **Feature Flags**. Lorsqu'une variante est désactivée, le SDK renvoie un objet de propriétés vide pour l'indicateur de fonctionnalité concerné.

![La section « Variantes d'expérience » avec la clé de variable « link » remplacée par « /sales ».]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### Étape 4 : Choisir les utilisateurs à cibler {#step-4-choose-users-to-target}

Utilisez l'un de vos Segments ou filtres pour choisir vos [utilisateurs cibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users). Par exemple, vous pouvez utiliser le filtre **Received Feature Flag Variant** pour recibler les utilisateurs qui ont déjà reçu un test A/B.

![La page « Cible » dans une expérience d'indicateur de fonctionnalité avec « Received Feature Flag Variant » mis en évidence dans la barre de recherche du groupe de filtres.]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
L'appartenance à un Segment est calculée lorsque les indicateurs de fonctionnalité sont actualisés pour un utilisateur donné. Les modifications sont disponibles après que votre application a actualisé les indicateurs de fonctionnalité, ou lorsqu'une nouvelle session est démarrée.
{% endalert %}

### Étape 5 : Distribuer les variantes {#step-5-distribute-variants}

Choisissez le pourcentage de distribution pour votre expérience. En tant que bonne pratique, vous ne devriez pas modifier la distribution après le lancement de votre expérience.

### Étape 6 : Assigner les conversions {#step-6-assign-conversions}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), après avoir reçu une campagne. Spécifiez une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

### Étape 7 : Vérifier et lancer {#step-7-review-and-launch}

Une fois que vous avez terminé la construction de votre expérience, vérifiez ses détails, puis sélectionnez **Launch Experiment**.

## Examen des résultats {#reviewing-the-results}

Une fois votre expérience d'indicateur de fonctionnalité terminée, vous pouvez examiner les données d'impressions de votre expérience. Accédez à **Messaging** > **Campaigns** et sélectionnez la campagne contenant votre expérience d'indicateur de fonctionnalité.

### Analyse de la campagne {#campaign-analytics}

**Campaign Analytics** offre un aperçu général des performances de votre expérience, notamment :

- Le nombre total d'impressions
- Le nombre d'impressions uniques
- Le taux de conversion principal
- Le chiffre d'affaires total généré par le message
- L'audience estimée

Vous pouvez également consulter les paramètres de l'expérience concernant la réception, l'audience et la conversion.

### Performance de l'expérience d'indicateur de fonctionnalité {#feature-flag-experiment-performance}

**Feature Flags Experiments Performance** indique les performances de votre message selon différentes dimensions. Les indicateurs spécifiques affichés varient en fonction du canal de communication choisi et selon que vous effectuez un test multivariante ou non. Pour voir les valeurs d'indicateur de fonctionnalité associées à chaque variante, sélectionnez **Preview**.
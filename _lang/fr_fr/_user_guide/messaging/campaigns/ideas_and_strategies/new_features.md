---
nav_title: Découverte des fonctionnalités et nouvelle version de l'application
article_title: Découverte des fonctionnalités et nouvelle version de l'application
page_order: 9
page_type: reference
description: "Cet article de référence explique comment tenir vos utilisateurs informés et enthousiastes lors de la publication de nouvelles fonctionnalités ou versions."
tool: Campaigns

---

# Découverte des fonctionnalités et nouvelle version de l'application {#feature-awareness-and-new-app-version}

> Cet article de référence explique comment utiliser la plateforme Braze pour tenir vos clients informés des nouvelles fonctionnalités et versions de votre application.

Vous travaillez sans relâche pour mettre à jour et améliorer votre application, et vous souhaitez que vos utilisateurs profitent de ces nouvelles fonctionnalités et versions. Découvrez comment faire connaître à vos utilisateurs les fonctionnalités qu'ils n'ont pas encore utilisées et les encourager à explorer l'application pour tirer le meilleur parti de ce que vous avez à offrir.

Les campagnes de découverte des fonctionnalités sont un excellent moyen d'encourager vos utilisateurs à rester engagés avec votre application à mesure que vous en améliorez les capacités. Tenir vos utilisateurs informés est un excellent moyen de les garder actifs, d'améliorer les évaluations et de garantir leur engagement.

## Filtrer par versions les plus récentes de l'application {#filtering-by-most-recent-app-versions}

Les SDK Braze suivent automatiquement la version la plus récente de l'application d'un utilisateur. Ces versions peuvent être utilisées dans des filtres et des segments pour déterminer quels utilisateurs doivent recevoir un message ou une Campaign.

![Le panneau Options de ciblage dans l'étape Cibler les utilisateurs du workflow de création de Campaign. La section Filtres supplémentaires inclut le filtre suivant : « Le numéro de version d'application le plus récent pour Android Stopwatch (Android) est inférieur à 3.7.0 (134.0.0.0) ».]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
Il peut s'écouler un certain temps avant que les versions actuelles de l'application ne soient renseignées. La version de l'application sur le profil utilisateur est mise à jour lorsque l'information est capturée par le SDK, ce qui dépend du moment où les utilisateurs ouvrent leur application. Si l'utilisateur n'ouvre pas l'application, la version actuelle ne sera pas mise à jour. <br><br> Ces filtres ne s'appliquent pas non plus de manière rétroactive. Il est recommandé d'utiliser « supérieur à » ou « égal à » pour les versions actuelles et futures, car l'utilisation de filtres sur des versions passées peut entraîner des comportements inattendus.
{% endalert %}

### Numéro de version de l'application {#app-version-number}

Utilisez le filtre **Numéro de version de l'application** pour segmenter les utilisateurs par la version et le numéro de build de l'application.

Ce filtre prend en charge les comparaisons numériques pour cibler une plage de versions d'application. Par exemple, vous pouvez cibler les utilisateurs dont l'application est « inférieure à », « supérieure à » ou « égale à » la version « 1.2.3 », ce qui peut être utile pour promouvoir une nouvelle fonctionnalité nécessitant une mise à jour de l'application.

Ce nouveau filtre peut remplacer l'ancien filtre « Nom de version de l'application » qui nécessitait de lister explicitement chaque ancienne version ou d'utiliser une expression régulière.

**Fonctionnement**

* Chaque partie de la version `major.minor.patch` envoyée par votre application est comparée en tant qu'entier
* Si les numéros majeurs sont égaux, les numéros mineurs sont comparés, et ainsi de suite.

**Important**

* Les applications Android possèdent à la fois un [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) lisible par l'utilisateur et un [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) interne. Le filtre Numéro de version de l'application utilise le `versionCode` car il est garanti d'être incrémenté à chaque publication sur la boutique d'applications.
* Cela peut prêter à confusion lorsque le `versionName` et le `versionCode` de votre application ne sont plus synchronisés, d'autant plus que les deux champs sont visibles depuis le tableau de bord de Braze. Il est recommandé de vérifier que le `versionName` et le `versionCode` de votre application sont incrémentés ensemble.
* Si vous devez filtrer par le champ `versionName` lisible par l'utilisateur (cas peu fréquent), utilisez le filtre Nom de version de l'application.

#### Prérequis SDK {#sdk-requirements}

Les valeurs de ce filtre sont collectées à partir du SDK Braze pour Android v3.6.0+ et du SDK iOS v3.21.0+. Même si ce filtre a des prérequis SDK, vous pourrez tout de même cibler les utilisateurs qui utilisent des versions plus anciennes de votre application grâce à cette fonctionnalité !

Pour Android, ce numéro de version est basé sur le [Package Long Version Code](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) de l'application.

Pour iOS, ce numéro de version est basé sur le [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) de l'application.

{% alert tip %}
Ce filtre ne sera renseigné qu'après la mise à jour de l'application par les utilisateurs vers les versions du SDK Braze prises en charge. En attendant, le filtre n'affichera aucune version lorsqu'il sera sélectionné.
{% endalert %}

#### Cas d'usage {#use-case}

Dans le scénario suivant, supposons que vous avez effectué la première mise à jour vers les SDK Braze prenant en charge ce filtre dans la version `2.0.0` de votre application.

Une fois que Braze reçoit des données de la version 2.0.0 de votre application, vous pouvez cibler les utilisateurs ayant des versions antérieures ou ultérieures.

| Filtre  | Version de l'application de l'utilisateur  | Résultat |
| :------------- | :----------- | :--------- |
| Inférieur à 2.0.0 | 1.0.0 | L'utilisateur fait partie du segment, même si son SDK Braze ne prenait pas en charge le filtre « Numéro de version de l'application ». |
| Supérieur à 2.0.0 | 2.5.1 | L'utilisateur et toutes les futures installations feront partie du segment. |
| Supérieur à 2.0.0 | 1.9.9 | L'utilisateur ne fait pas partie du segment. |
| Inférieur ou égal à 2.0.0 | 3.0.1 | L'utilisateur ne fait pas partie du segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cas d'usage" }

### Nom de version de l'application {#app-version-name}

Utilisez le filtre « Nom de version de l'application » pour segmenter les utilisateurs par le nom de build visible par l'utilisateur.

Ce filtre prend en charge la correspondance avec « est », « n'est pas » et les expressions régulières. Par exemple, vous pouvez cibler les utilisateurs dont l'application n'est pas la version « 1.2.3-test-build ».

Pour Android, ce nom de version est basé sur le [Package Version Name](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) de l'application. Pour iOS, ce nom de version est basé sur le [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) de l'application.

### Fonctionnalité non utilisée {#have-not-used-feature}

Lorsque vous publiez une nouvelle version de votre application avec de nouvelles fonctionnalités, les utilisateurs ne remarquent pas toujours le nouveau contenu. Lancer une campagne de découverte des fonctionnalités est un excellent moyen de faire connaître aux utilisateurs les nouvelles fonctionnalités ou celles qu'ils n'ont jamais utilisées. Pour ce faire, vous devez créer un [attribut personnalisé]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#custom-data) attribué aux utilisateurs qui n'ont jamais effectué une certaine action dans votre application, ou utiliser un [événement personnalisé]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#custom-data) pour suivre une action particulière. Vous pouvez ensuite utiliser cet attribut (ou événement) pour segmenter les utilisateurs auxquels vous souhaitez envoyer la Campaign.

{% alert tip %}
Vous souhaitez recibler une portion spécifique de votre audience ? Consultez [Campaigns de reciblage]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns) pour découvrir comment recibler des campagnes en exploitant les actions précédentes de vos utilisateurs.
{% endalert %}
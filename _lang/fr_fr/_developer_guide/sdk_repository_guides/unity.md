---
nav_title: SDK Unity
article_title: Guide du dépôt du SDK Unity
page_order: 9
description: "Référence du README du SDK Unity Braze, reproduite depuis GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## À propos du SDK Unity Braze {#about-the-braze-unity-sdk}

Le SDK Unity Braze vous aide à intégrer les fonctionnalités d'envoi de messages, d'analyse et d'engagement utilisateur de Braze dans votre application.

Pour commencer, consultez les ressources suivantes :

- [Guide de l'utilisateur Braze]({{site.baseurl}}/user_guide/introduction)
- [Guide du développeur Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity)

## Configuration du plugin {#plugin-setup}

Avant de pouvoir commencer à utiliser Braze dans les scripts Unity, vous devez importer les fichiers du plugin dans votre projet Unity.

**Recommandé :** Les plugins Android et iOS sont regroupés dans un package Unity disponible au téléchargement depuis la [page des versions du SDK][1].

**Configuration manuelle du plugin :** Vous pouvez également copier les plugins dans votre projet Unity :
  1. Commencez par cloner ce dépôt.
  2. Si vous n'utilisez aucun autre plugin, il vous suffit de copier le répertoire `Plugins` de ce dépôt dans le dossier `Assets` de votre projet Unity.
  3. Si vous disposez déjà d'un répertoire `/<your-project>/Assets/Plugins` (probablement parce que vous utilisez déjà un autre plugin), copiez `Plugins/Appboy/AppboyBinding.cs` dans `/<your-project>/Assets/Plugins`. Copiez ensuite le contenu de `Plugins/iOS` et `Plugins/Android` de ce dépôt dans `/<your-project>/Assets/Plugins/iOS` et `/<your-project>/Assets/Plugins/Android` respectivement.

## Configuration de l'intégration {#integration-setup}

Pour intégrer Braze dans votre application Unity, suivez nos instructions pour l'[intégration du SDK Unity Braze][2].

[1]: https://github.com/braze-inc/braze-unity-sdk/releases
[2]: {{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity

## Contact {#contact}

Si vous avez des questions, veuillez contacter [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Pour les détails du dépôt et les exemples de projets, consultez [https://github.com/braze-inc/braze-unity-sdk](https://github.com/braze-inc/braze-unity-sdk).
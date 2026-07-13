---
nav_title: Thèmes en mode sombre
article_title: Thèmes en mode sombre
page_order: 2
description: "Cet article de référence couvre la prise en charge du mode sombre pour les messages in-app de Braze, y compris comment définir un thème en mode sombre et les considérations de compatibilité."
channel:
  - in-app messages

---

# Thèmes en mode sombre {#dark-mode-themes}

> Cet article s'applique à l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional). Le mode sombre offre aux utilisateurs la possibilité de définir une préférence de couleur à l'échelle du système (introduite sur [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) et [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). Les thèmes « sombres » sont conçus pour économiser la batterie et réduire la fatigue oculaire des utilisateurs, tout en offrant aux développeurs d'applications un moyen d'implémenter des thèmes de couleurs sombres.

Les messages in-app de Braze prennent en charge l'ajout d'un thème sombre alternatif pour délivrer le bon message en termes de couleurs à vos utilisateurs en fonction de leurs préférences et maintenir la cohérence avec le design de votre application.

## Comment fonctionne le mode sombre {#how-dark-mode-works}

Les utilisateurs disposant au minimum d'Android 10 ou d'iOS 13 et versions ultérieures peuvent activer ou désactiver le mode sombre dans les paramètres de leur appareil.

Lorsque le mode sombre est activé, les menus et écrans natifs de l'appareil (notifications push, paramètres de l'appareil, etc.) passent en gris foncé. Les applications peuvent également choisir de prendre en charge le mode sombre en spécifiant les thèmes alternatifs dans le code de l'application.

## Définir un thème en mode sombre {#setting-a-dark-mode-theme}

Le mode sombre, situé dans l'onglet **Conception** lors de la [création d'un message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional), vous permet d'ajouter un thème de couleurs alternatif pour les utilisateurs qui sont en mode sombre sur leur appareil.

![Un utilisateur basculant entre les styles du mode clair et du mode sombre dans l'onglet Style lors de la création d'un message in-app.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

Lorsque cette option est activée, vous pouvez choisir les couleurs du thème sombre pour votre message in-app à l'aide du sélecteur de couleurs, ou en sélectionnant des [profils de couleurs]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#color-profile) existants pour réutiliser des thèmes sombres ou clairs existants.

{% alert note %}
Vous pouvez toujours utiliser cette fonctionnalité même si votre application ne propose pas son propre thème sombre. Cependant, les appareils qui ne prennent pas en charge le mode sombre afficheront le thème clair par défaut. Changer le thème de l'appareil sur Android pendant qu'un message in-app est affiché ne modifiera pas le thème utilisé pour ce message in-app.
{% endalert %}

### Utiliser le mode sombre de manière cohérente {#using-dark-mode-consistently}

Pour utiliser le mode sombre pour tous les messages in-app, commencez par créer un profil de couleurs correspondant à votre thème en mode sombre.

1. Accédez à **Contenu** > **Message in-app**.
2. Sélectionnez **Créer des modèles** et choisissez [Profil de couleurs]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#color-profile) dans le menu déroulant.
3. Créez et enregistrez votre profil de couleurs.

Lors de la création d'une version en mode sombre d'un message in-app, vous pouvez sélectionner ce profil de couleurs pour conserver une apparence cohérente pour vos messages in-app.

## Compatibilité {#compatibility}

- Vos utilisateurs doivent disposer d'appareils iOS version 13 ou supérieure, ou d'appareils Android version 10 ou supérieure.
- Le SDK Braze pour iOS v3.21.0+ et le SDK Braze pour Android v3.8.0+ sont requis.

{% alert note %}
Les applications en mode sombre ont été introduites avec Android 10 et iOS 13. Les utilisateurs qui n'ont pas mis à jour leur téléphone vers au moins ces versions ne verront que le thème clair. <br><br>Les campagnes seront toujours diffusées à tous les utilisateurs éligibles pour l'audience que vous avez sélectionnée, indépendamment du paramètre de mode sombre ou de la version du système d'exploitation des utilisateurs.
{% endalert %}

## Utiliser des messages in-app HTML {#using-html-in-app-messages}

Pour créer un thème sombre et un thème clair pour les messages in-app HTML, vous pouvez utiliser la fonctionnalité média CSS [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) pour détecter la préférence de l'utilisateur.

Par exemple :

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```


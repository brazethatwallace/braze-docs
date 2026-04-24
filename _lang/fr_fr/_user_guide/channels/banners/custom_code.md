---
nav_title: Code personnalisé et pont JavaScript
article_title: Code personnalisé et pont JavaScript pour les Bannières
page_order: 2
page_type: reference
description: "Découvrez comment utiliser du HTML personnalisé dans les Bannières et le pont JavaScript pour enregistrer les clics et déclencher des actions Braze."
channel:
  - banners
---

# Code personnalisé et pont JavaScript pour les Bannières

> Lorsque vous utilisez le bloc éditeur **Code personnalisé** dans le compositeur de Bannière, vous devez appeler `brazeBridge.logClick()` depuis votre HTML personnalisé pour enregistrer les clics. Les Bannières utilisent le même pont JavaScript que les messages in-app HTML : les mêmes méthodes et schémas s'appliquent donc.

Si vous utilisez du HTML personnalisé dans la conception de votre Bannière, le SDK Braze ne peut pas attacher automatiquement des écouteurs de clics aux éléments de votre code personnalisé. Vous devez appeler explicitement `brazeBridge.logClick()` pour tous les éléments cliquables (liens, boutons, etc.) que vous souhaitez suivre dans l'analytique de campagne.

Par exemple, pour enregistrer un clic lorsqu'un utilisateur appuie sur un bouton dans votre HTML personnalisé :

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Pour la référence complète du pont JavaScript, y compris toutes les méthodes disponibles et les options de suivi des clics, consultez la section ci-dessous.

## Pont JavaScript {#javascript-bridge}

{% include javascript_bridge/reference.md %}
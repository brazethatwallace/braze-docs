---
nav_title: Code personnalisé et pont JavaScript
article_title: Code personnalisé et pont JavaScript pour les bannières
page_order: 2
page_type: reference
description: "Découvrez comment utiliser le code HTML personnalisé dans les bannières et le pont JavaScript pour enregistrer les clics et déclencher des actions Braze."
channel:
  - banners
---

# Code personnalisé et pont JavaScript pour les bannières {#custom-code-and-javascript-bridge-for-banners}

> Lorsque vous utilisez le bloc éditeur **Code personnalisé** dans le générateur de bannières, ou lorsque vous créez une bannière avec l'**éditeur HTML**, vous devez appeler `brazeBridge.logClick()` depuis votre code HTML personnalisé pour enregistrer les clics. Les bannières utilisent le même pont JavaScript que les messages in-app HTML : les mêmes méthodes et modèles s'appliquent donc.

Si vous utilisez du code HTML personnalisé dans votre conception de bannière — que ce soit via un bloc Code personnalisé dans le générateur ou via l'éditeur HTML complet — le SDK Braze ne peut pas associer automatiquement des écouteurs de clic aux éléments de votre code personnalisé. Vous devez appeler explicitement `brazeBridge.logClick()` pour tout élément cliquable (liens, boutons et autres éléments similaires) que vous souhaitez suivre dans les analyses de la campagne.

Par exemple, pour enregistrer un clic lorsqu'un utilisateur appuie sur un bouton dans votre code HTML personnalisé :

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Pour obtenir la référence complète du pont JavaScript, y compris toutes les méthodes disponibles et les options de suivi des clics, consultez la section [Pont JavaScript](#javascript-bridge).

## Pont JavaScript {#javascript-bridge}

{% include javascript_bridge/reference.md %}
---
nav_title: Accessibilité
article_title: Accessibilité
platform: Web
page_order: 22
page_type: reference
description: "Cet article décrit comment Braze prend en charge l'accessibilité."

---

# Accessibilité {#accessibility}

> Cet article présente un aperçu de la manière dont Braze prend en charge l'accessibilité au sein de votre intégration.

Le SDK Web Braze est conforme aux normes définies par les [directives d'accessibilité du contenu Web (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). Nous maintenons un [score Lighthouse de 100/100](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) pour les Content Cards et les messages in-app sur toutes nos nouvelles versions afin de respecter notre norme d'accessibilité.

## Conditions préalables {#prerequisites}

La version minimale du SDK conforme à la norme WCAG 2.1 est proche de la version 3.4.0. Cependant, nous recommandons de procéder à une mise à niveau vers la version 6.0.0 au minimum afin de bénéficier des corrections majeures apportées aux balises d'image.

### Corrections notables en matière d'accessibilité {#notable-accessibility-fixes}

| Version | Type | Principaux changements |
|---------|------|-------------|
| **6.0.0** | **Majeur** | Images en tant que balises `<img>`, champs `imageAltText` ou `language`, améliorations générales de l'accessibilité de l'interface utilisateur |
| **3.5.0** | Mineur | Améliorations de l'accessibilité du texte défilable |
| **3.4.0** | Correctif | Correction du rôle `article` des Content Cards |
| **3.2.0** | Mineur | Cibles tactiles minimales de 45x45 px pour les boutons |
| **3.1.2** | Mineur | Texte alternatif par défaut pour les images |
| **2.4.1** | **Majeur** | HTML sémantique (`h1` ou `button`), attributs ARIA, navigation au clavier, gestion du focus |
| **2.0.5** | Mineur | Gestion du focus, navigation au clavier, étiquettes |
{: .reset-td-br-1, .reset-td-br-2 aria-label="Notable accessibility fixes" }

## Fonctionnalités d'accessibilité prises en charge {#supported-accessibility-features}

Nous prenons en charge les fonctionnalités suivantes pour les Content Cards et les messages in-app :

- Rôles et étiquettes ARIA
- Prise en charge de la navigation au clavier
- Gestion du focus
- Annonces du lecteur d'écran
- Prise en charge du texte alternatif pour les images

## Directives d'accessibilité pour les intégrations SDK {#accessibility-guidelines-for-sdk-integrations}

Consultez [Créer des messages accessibles dans Braze]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/) pour obtenir des directives générales en matière d'accessibilité. Ce guide fournit des conseils et des bonnes pratiques pour optimiser l'accessibilité lors de l'intégration du SDK Web Braze dans votre application web.

### Content Cards

#### Définition d'une hauteur maximale {#setting-a-maximum-height}

Afin d'éviter que les Content Cards n'occupent trop d'espace vertical et d'améliorer l'accessibilité, vous pouvez définir une hauteur maximale pour le conteneur du flux, comme dans l'exemple suivant :

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### Considérations relatives à la fenêtre d'affichage {#viewport-considerations}

Pour les Content Cards affichées en ligne, tenez compte des contraintes de la fenêtre d'affichage, comme dans cet exemple.

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### Messages in-app {#in-app-messages}

{% alert warning %}
Ne placez pas d'informations importantes dans les messages in-app de type slide up, car ils ne sont pas accessibles aux lecteurs d'écran.
{% endalert %}

### Considérations relatives aux appareils mobiles {#mobile-considerations}

#### Conception réactive {#responsive-design}

Le SDK comprend des points d'arrêt réactifs. Vérifiez que vos personnalisations s'adaptent à toutes les tailles d'écran, comme dans l'exemple suivant :

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }

  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### Tests d'accessibilité {#testing-accessibility}

#### Liste de contrôle pour les tests manuels {#manual-test-checklist}

Testez manuellement l'accessibilité en effectuant les tâches suivantes :

- Naviguez dans les Content Cards et les messages in-app à l'aide du clavier uniquement (Tab, Entrée, Espace)
- Testez avec un lecteur d'écran (NVDA, JAWS, VoiceOver)
- Vérifiez que toutes les images disposent d'un texte alternatif
- Vérifiez les rapports de contraste des couleurs (utilisez des outils tels que WebAIM Contrast Checker)
- Testez sur les appareils mobiles avec écran tactile
- Vérifiez que les indicateurs de focus sont visibles
- Testez le piégeage du focus des messages dans les fenêtres modales
- Vérifiez que tous les éléments interactifs sont accessibles au clavier

### Problèmes courants d'accessibilité {#common-accessibility-issues}

Pour éviter les problèmes courants d'accessibilité, suivez ces recommandations :

1. **Conservez les styles de focus :** les indicateurs de focus du SDK sont essentiels pour les utilisateurs de clavier.
2. **N'utilisez `display: none` que sur des éléments non interactifs :** utilisez `visibility: hidden` ou `opacity: 0` pour masquer les éléments interactifs.
3. **Ne remplacez pas les attributs ARIA :** le SDK définit les rôles et les étiquettes ARIA appropriés.
4. **Utilisez les attributs `tabindex` :** ils contrôlent l'ordre de navigation au clavier.
5. **Fournissez un défilement si vous définissez `overflow: hidden` :** vérifiez que le contenu défilable reste accessible.
6. **N'interférez pas avec les gestionnaires de clavier intégrés :** vérifiez que la navigation au clavier existante fonctionne correctement.
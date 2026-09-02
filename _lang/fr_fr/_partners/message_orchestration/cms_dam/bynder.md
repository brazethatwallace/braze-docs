---
nav_title: Bynder
article_title: Bynder
description: "Cet article de référence décrit le partenariat entre Braze et Bynder, une plateforme de gestion des ressources numériques (DAM) qui vous permet de rechercher et d'insérer des URL de ressources approuvées dans les Campaigns et Canvas Braze via l'extension Chrome Universal Compact View."
alias: /partners/bynder/
page_type: partner
search_tag: Partner
---

# Bynder

> [Bynder](https://www.bynder.com) est une plateforme de gestion des ressources numériques (DAM) qui aide les clients à créer, gérer, trouver et distribuer des ressources numériques approuvées (images, vidéos et autres contenus créatifs) à partir d'une source unique de vérité. Lorsqu'elle est intégrée à Braze, l'extension Google Chrome Universal Compact View (UCV) de Bynder permet aux marketeurs de rechercher et de sélectionner des ressources Bynder sans quitter le tableau de bord de Braze. Insérez des liens vers ces ressources directement dans vos Campaigns et Canvas.

_Cette intégration est maintenue par Bynder._

## À propos de cette intégration {#about-this-integration}

Connecter Bynder à Braze via l'extension Chrome UCV donne aux marketeurs accès à leur bibliothèque de ressources Bynder depuis l'éditeur de contenu Braze. Ouvrez l'Universal Compact View en superposition sur n'importe quel onglet du navigateur, y compris le tableau de bord de Braze. Recherchez ou filtrez le bon contenu créatif, puis collez l'URL de la ressource dans votre Campaign.

Cela permet de garder les Campaigns Braze alignées avec la source unique de vérité de Bynder : les bonnes autorisations, la version de fichier la plus récente et les droits d'utilisation appropriés.

## Cas d'usage {#use-cases}

- Les marketeurs qui créent un e-mail, un message in-app ou un Content Block dans Braze peuvent insérer des images principales, des bannières ou des liens vers des vidéos promotionnelles provenant directement de Bynder afin que les Campaigns utilisent la dernière version approuvée d'une ressource.
- Les gestionnaires de Campaigns peuvent utiliser la barre de recherche et de filtrage de l'Universal Compact View pour localiser des contenus créatifs régionaux ou localisés approuvés pour un Segment d'audience spécifique avant de les ajouter à une étape du Canvas.
- Les équipes créatives peuvent appliquer la transformation dynamique des ressources (Dynamic Asset Transformation) de Bynder pour redimensionner ou reformater une ressource pour un canal spécifique avant de copier le lien dans Braze. Par exemple, utilisez un recadrage compact pour une notification push ou une bannière pleine taille pour un e-mail.

## Prérequis {#prerequisites}

Avant de commencer, vous avez besoin des éléments suivants :

| Condition | Description |
| --- | --- |
| Un compte Bynder | Un compte Bynder avec accès aux ressources DAM que vous souhaitez référencer dans Braze. |
| Extension Chrome Bynder Universal Compact View (UCV) | Installée depuis le Chrome Web Store et connectée à votre portail Bynder. Disponible uniquement pour Google Chrome. |
| Ressources et dérivés publics | Toute ressource, ainsi que le dérivé spécifique vers lequel vous prévoyez de créer un lien, doit être marquée comme publique dans Bynder afin que son URL soit correctement résolue pour les destinataires du message. |
| Un compte Braze | Accès au canal de communication (e-mail, Content Block, message in-app, Canvas, etc.) où la ressource est utilisée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Installer et connecter l'extension Chrome Bynder UCV {#step-1-install-and-connect-the-bynder-ucv-chrome-extension}

1. Accédez à l'[extension Bynder UCV](https://chromewebstore.google.com/detail/bynders-universal-compact/ilghhphnbdblpbdhmbdfiaidganphema) dans le Chrome Web Store.
2. Cliquez sur **Ajouter à Chrome**, vérifiez les autorisations demandées, puis cliquez sur **Ajouter l'extension**.
3. Dans la barre d'outils Chrome, sélectionnez l'icône Bynder UCV (épinglez-la d'abord à la barre d'outils si elle n'est pas déjà visible).
4. Saisissez le domaine de votre portail Bynder (sans `https://`), puis cliquez sur **Connect**.
5. Dans la fenêtre qui s'ouvre, connectez-vous à votre portail Bynder avec vos identifiants habituels.

### Étape 2 : Rechercher et sélectionner une ressource Bynder {#step-2-search-for-and-select-a-bynder-asset}

1. Une fois l'extension connectée, ouvrez l'Universal Compact View depuis n'importe quel onglet du navigateur, y compris votre tableau de bord de Braze.
2. Utilisez le filtre intelligent et la barre de recherche pour localiser l'image, la vidéo, le document ou la ressource audio dont vous avez besoin.
3. Sélectionnez la ressource, puis sélectionnez le dérivé (ou le fichier original, s'il est public) que vous souhaitez utiliser.
4. Cliquez sur **Add Asset** pour copier l'URL de la ressource sélectionnée dans votre presse-papiers.

### Étape 3 : Ajouter l'URL de la ressource à votre Campaign Braze {#step-3-add-the-asset-url-to-your-braze-campaign}

1. Dans Braze, ouvrez l'e-mail, le Content Block, le message in-app ou l'étape du Canvas où vous souhaitez ajouter la ressource.
2. Collez l'URL de la ressource Bynder copiée dans le champ approprié. Par exemple, utilisez une balise `<img src="">` ou le champ d'URL d'image d'un Content Block.

   Exemple d'URL d'image :

   ```html
   <img src="https://your-portal.bynder.com/m/abcdef123456/original/campaign-banner.jpg" alt="Summer Campaign">
   ```

{: start="3"}
3. Enregistrez et prévisualisez votre message pour confirmer que la ressource s'affiche comme prévu.

## Conseils {#tips}

### Appliquer les transformations dynamiques de ressources avant de copier l'URL {#apply-dynamic-asset-transformations-before-copying-the-url}

Dans l'Universal Compact View, utilisez les options de transformation disponibles pour redimensionner, recadrer ou reformater une ressource pour le canal que vous ciblez. Cela évite de télécharger des versions recadrées séparées dans Bynder.

### Générer des URL de dérivés spécifiques à chaque canal {#generate-channel-specific-derivative-urls}

Chaque transformation ou dérivé produit sa propre URL distincte. Générez une version dimensionnée pour l'e-mail, une autre pour les notifications push et une autre pour les messages in-app, puis collez chacune dans le canal Braze ou l'étape du Canvas correspondant.

### Réutiliser une même URL de ressource sur plusieurs canaux {#reuse-one-asset-url-across-channels}

Comme un lien collé pointe vers une ressource et un dérivé spécifiques dans Bynder, le même format d'URL peut être réutilisé dans les e-mails, les Content Blocks, les messages in-app et les étapes du Canvas. Cela garantit la cohérence des contenus créatifs partout où ils sont utilisés dans une Campaign.

### Mettre à jour la ressource source sans modifier vos Campaigns {#update-the-source-asset-without-editing-your-campaigns}

Si le fichier sous-jacent dans Bynder est remplacé tout en conservant les mêmes paramètres de ressource publique et de dérivé, tout message Braze en direct or en ligne/en production/instantané référençant cette URL reflète automatiquement la mise à jour. Vous n'avez pas besoin de modifier la Campaign elle-même.

## Considérations {#considerations}

- L'extension Chrome Bynder UCV est disponible uniquement pour Google Chrome. Dans les autres navigateurs, copiez les URL des ressources directement depuis le portail Bynder complet.
- Seules les ressources (et les dérivés spécifiques liés) marquées comme publiques dans Bynder sont résolues lorsqu'elles sont collées dans Braze. Les ressources privées renvoient une erreur d'accès aux destinataires.
- Si les fenêtres pop-up ne sont pas autorisées ou si le portail est déjà ouvert dans un autre onglet, la fenêtre de connexion peut ne pas s'ouvrir correctement. Avant de vous connecter, confirmez que les fenêtres pop-up sont autorisées et fermez tout autre onglet où le portail est ouvert.
- L'accès au sein de l'extension suit les autorisations existantes de l'utilisateur dans le DAM Bynder : il ne voit et ne peut sélectionner que les ressources auxquelles il est déjà autorisé à accéder.

## Résolution des problèmes {#troubleshooting}

| Problème | Résolution |
| --- | --- |
| L'icône de l'extension n'est pas visible | Épinglez l'extension Bynder UCV à la barre d'outils Chrome depuis le menu Extensions. |
| **Connect** n'ouvre pas de fenêtre de connexion | Confirmez que les pop-ups Chrome sont autorisés pour le domaine de votre portail Bynder, et fermez tout autre onglet où le portail est déjà ouvert. |
| L'URL de la ressource ne s'affiche pas dans Braze | Confirmez que la ressource et le dérivé spécifique utilisé sont marqués comme publics dans le portail Bynder. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

Pour plus d'informations, consultez la [documentation Universal Compact View](https://support.bynder.com/hc/en-us/sections/16936397091858-Universal-Compact-View-UCV) de Bynder ou contactez le support Bynder.
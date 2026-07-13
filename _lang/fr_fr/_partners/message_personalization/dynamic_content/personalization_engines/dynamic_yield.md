---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "Cet article de référence décrit le partenariat entre Braze et Dynamic Yield. Ce partenariat vous permet d'utiliser le moteur de recommandation et de segmentation de Dynamic Yield pour créer des blocs d'expérience qui peuvent être intégrés dans les messages de Braze."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Dynamic Yield

> [Dynamic Yield](https://www.dynamicyield.com/), une entreprise Mastercard, aide les entreprises de divers secteurs à offrir des expériences client numériques personnalisées, optimisées et synchronisées. Avec l'[Experience OS](http://www.dynamicyield.com/experience-os) de Dynamic Yield, les marketeurs, les chefs de produit, les développeurs et les équipes digitales peuvent faire correspondre algorithmiquement le contenu, les produits et les offres à chaque client pour accélérer le chiffre d'affaires et la fidélité des clients.

_Cette intégration est maintenue par Dynamic Yield._

## À propos de l'intégration {#about-the-integration}

Le partenariat entre Braze et Dynamic Yield vous permet d'utiliser le moteur de recommandation et de segmentation de Dynamic Yield pour créer des blocs d'expérience qui peuvent être intégrés dans les messages de Braze. Les blocs d'expérience peuvent être composés de :
- **Blocs de recommandations** : définissez des algorithmes et des filtres pour obtenir le contenu personnalisé des utilisateurs qui se propage lorsque l'e-mail est ouvert.
- **Blocs de contenu dynamique** : ciblez différentes promotions et messages vers différents utilisateurs. Le ciblage peut être basé soit sur l'affinité, soit sur l'audience. Dynamic Yield détermine quelle expérience personnalisée servir lorsque l'e-mail est ouvert.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Dynamic Yield | Un compte [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer un bloc d'expérience {#step-1-create-an-experience-block}

Pour créer un bloc d'expérience dans Dynamic Yield, accédez à **Email > Experience Emails > Create New**.

Ensuite, sélectionnez **Create Experience Block** pour concevoir un bloc de contenu dynamique ou de recommandations à intégrer dans un modèle d'e-mail Braze.<br>![Page Experience Emails de Dynamic Yield avec l'option Create Experience Block sélectionnée.]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### Étape 2 : Rédigez le brouillon de votre message {#step-2-draft-your-messaging}

L'image suivante montre un e-mail créé à partir de zéro dans le générateur.<br>![Générateur d'e-mails Dynamic Yield avec une mise en page d'e-mail d'expérience en brouillon.]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. Entrez un nom de campagne, une note et des étiquettes pour la campagne dans la zone d'en-tête.<br><br>
2. Insérez un bloc d'expérience. Ces blocs incluent :
  - [Recommandations](#configure-a-recommendations-block) : un widget offrant aux utilisateurs des recommandations entièrement personnalisées.
  - [Contenu dynamique](#configure-a-dynamic-content-block) : ciblez différentes promotions et messages vers différentes audiences.<br><br>
3. Mettez à jour les paramètres :
  - Utilisez les paramètres d'URL pour suivre les clics dans votre logiciel d'analyse (facultatif). Ajoutez des paramètres aux affichages par défaut selon les besoins.
  - Sélectionnez une fenêtre d'attributs, soit sept jours (par défaut), soit un jour.<br><br>
4. Enregistrez et quittez. Vous pouvez revenir pour modifier tous les éléments de votre e-mail à tout moment avant que le code ne soit généré. Après la génération du code, vous pouvez modifier tout ce qui [n'affecte pas le code](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Configurer un bloc de recommandations {#configure-a-recommendations-block}

Le bloc de recommandations vous permet de définir des algorithmes et des filtres pour obtenir le contenu personnalisé des utilisateurs qui se propage à l'ouverture de l'e-mail.

1. Faites glisser un bloc de recommandations depuis le volet d'édition dans le corps de votre e-mail.<br><br>
2. Sélectionnez l'algorithme souhaité (popularité, affinité utilisateur, similarité, et plus). En fonction de l'algorithme sélectionné, des options supplémentaires sont affichées :
  - Si votre recommandation est basée sur la popularité, vous pouvez mélanger les résultats pour éviter de servir la même recommandation à partir de différents e-mails que le destinataire ouvre.
  - D'autres algorithmes, tels que la similarité, s'appuient sur le contexte pour fournir des recommandations nécessitant que vous sélectionniez des éléments à inclure. Ces éléments peuvent être ajoutés dans le générateur ou vous pouvez [ajouter une balise de fusion au code d'intégration](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced) pour le rendre dynamique, par exemple, pour ajouter des éléments similaires dans les e-mails de confirmation d'expédition. <br><br>
3. Vous pouvez exclure les produits que l'utilisateur a déjà achetés pour éviter de les recommander.<br><br>
4. Vous pouvez ajouter une [règle de filtre personnalisé](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) pour épingler des produits spécifiques à des emplacements, ou inclure et exclure des produits par propriétés de produit. Par exemple, ne montrez pas de produits qui coûtent moins de 5 $ ou uniquement des produits de la catégorie shorts.<br><br>
5. Enfin, configurez la conception du bloc de recommandation. Pour ce faire, sélectionnez un modèle d'élément, définissez le nombre d'éléments à afficher et en combien de lignes.

### Configurer un bloc de contenu dynamique {#configure-a-dynamic-content-block}
Utilisez le contenu dynamique pour cibler différentes promotions et messages vers différents utilisateurs. Le ciblage peut être basé soit sur l'affinité, soit sur l'audience. Dynamic Yield détermine quelle expérience personnalisée servir lorsque l'e-mail est ouvert.

1. Faites glisser un bloc de contenu dynamique depuis le volet d'édition dans le corps de votre e-mail.<br><br>
2. Sélectionnez un modèle pour la première variation. Vous pouvez maintenant définir des variables de conception et de contenu. Enregistrez la variation une fois terminée. <br>![Éditeur de modèle de variation de contenu dynamique Dynamic Yield.]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br>
3. Définissez l'audience dans le volet de contenu dynamique.<br>![Paramètres de ciblage d'audience Dynamic Yield pour une variation de contenu dynamique.]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br>
4. Ajoutez une autre variation pour cibler une autre audience spécifique ou tous les utilisateurs. Répétez si nécessaire.<br><br>
5. Définissez les priorités de vos variations en utilisant les flèches vers le haut et vers le bas. <br><br>
6. Les priorités déterminent quelle variation est servie lorsqu'un utilisateur est éligible à plus d'une expérience.

### Étape 3 : Intégrez votre e-mail à Braze {#step-3-integrate-your-email-with-braze}

Cette intégration vous permet d'ajouter des widgets de recommandation personnalisés et du contenu dynamique alimenté par Dynamic Yield dans vos campagnes d'e-mail Braze. L'intégration de ces campagnes dans les campagnes Braze se fait avec un simple code d'intégration que vous collez dans l'éditeur d'e-mail Braze.

1. Cliquez sur l'icône d'intégration ESP sur la page de la liste des e-mails d'expérience.<br><br>
2. Entrez le jeton pertinent de Braze qui insère l'identifiant unique du client (CUID) et l'ID d'e-mail de l'utilisateur.<br>![Fenêtre modale d'intégration ESP Dynamic Yield avec les champs de jeton utilisateur Braze.]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})

Lorsque vous êtes satisfait de votre e-mail, l'étape suivante consiste à générer le code à intégrer dans Braze.
1. Dans **Experience Emails**, cliquez sur **Generate Code**.<br><br>
2. Ensuite, cliquez sur **Copy to Clipboard**.<br>![Panneau de code d'intégration généré par Dynamic Yield avec l'action Copy to Clipboard.]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br>
3. Collez le code dans votre campagne d'e-mail Braze, puis continuez à concevoir, tester et publier votre campagne d'e-mail.
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

Le partenariat entre Braze et Dynamic Yield vous permet d'utiliser le moteur de recommandation et de segmentation de Dynamic Yield pour créer des blocs d'expérience qui peuvent être intégrés dans les messages Braze. Les blocs d'expérience peuvent être composés de :
{% multi_lang_include partners/message_personalization/dynamic_yield_experience_blocks.md %}

## Prérequis {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Dynamic Yield | Un compte [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) est nécessaire pour tirer parti de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Créer un bloc d'expérience {#step-1-create-an-experience-block}

Pour créer un bloc d'expérience dans Dynamic Yield, accédez à **Email > Experience Emails > Create New**.

Ensuite, sélectionnez **Create Experience Block** pour concevoir un bloc de contenu dynamique ou de recommandations à intégrer dans un modèle d'e-mail Braze.<br>![Page Experience Emails de Dynamic Yield avec l'option Create Experience Block sélectionnée.]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### Étape 2 : Rédiger votre message {#step-2-draft-your-messaging}

L'image suivante montre un e-mail créé de zéro dans le générateur.<br>![Générateur d'e-mails Dynamic Yield avec une maquette de mise en page d'e-mail d'expérience.]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. Saisissez un nom de campagne, une note et des étiquettes pour la campagne dans la zone d'en-tête.<br><br>
2. Insérez un bloc d'expérience. Ces blocs comprennent :
  - [Recommandations](#configure-a-recommendations-block) : Un widget proposant aux utilisateurs des recommandations entièrement personnalisées.
  - [Contenu dynamique](#configure-a-dynamic-content-block) : Ciblez différentes promotions et messages pour différentes audiences.<br><br>
3. Mettez à jour les paramètres :
  - Utilisez les paramètres d'URL pour suivre les clics dans votre logiciel d'analyse (facultatif). Ajoutez des paramètres aux affichages par défaut selon vos besoins.
  - Sélectionnez une fenêtre d'attributs, soit sept jours (par défaut), soit un jour.<br><br>
4. Enregistrez et quittez. Vous pouvez revenir modifier tous les éléments de votre e-mail à tout moment avant la génération du code. Une fois le code généré, vous pouvez modifier tout ce qui [n'affecte pas le code](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Configurer un bloc de recommandations {#configure-a-recommendations-block}

Le bloc de recommandations vous permet de définir des algorithmes et des filtres pour alimenter le contenu personnalisé des utilisateurs, qui s'affiche à l'ouverture de l'e-mail.

1. Faites glisser un bloc de recommandations depuis le volet d'édition dans le corps de votre e-mail.<br><br>
2. Sélectionnez l'algorithme souhaité (popularité, affinité utilisateur, similarité, et plus). Selon l'algorithme sélectionné, des options supplémentaires s'affichent :
  - Si votre recommandation est basée sur la popularité, vous pouvez mélanger les résultats pour éviter de proposer la même recommandation dans différents e-mails ouverts par le destinataire.
  - D'autres algorithmes, comme la similarité, s'appuient sur le contexte pour proposer des recommandations, ce qui nécessite de sélectionner les éléments à inclure. Ces éléments peuvent être ajoutés dans le générateur ou vous pouvez [ajouter une balise de fusion au code d'intégration](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced) pour le rendre dynamique, par exemple pour ajouter des articles similaires dans les e-mails de confirmation d'expédition. <br><br>
3. Vous pouvez exclure les produits que l'utilisateur a déjà achetés pour éviter de les recommander.<br><br>
4. Vous pouvez ajouter une [règle de filtre personnalisée](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) pour épingler des produits spécifiques à des emplacements, ou inclure et exclure des produits selon leurs propriétés. Par exemple, ne pas afficher les produits coûtant moins de 5 $ ou afficher uniquement les produits de la catégorie shorts.<br><br>
5. Enfin, configurez le design du bloc de recommandations. Pour ce faire, sélectionnez un modèle d'élément, définissez le nombre d'éléments à afficher et le nombre de lignes.

### Configurer un bloc de contenu dynamique {#configure-a-dynamic-content-block}
Utilisez le contenu dynamique pour cibler différentes promotions et messages auprès de différents utilisateurs. Le ciblage peut être basé sur l'affinité ou l'audience. Dynamic Yield détermine quelle expérience personnalisée proposer à l'ouverture de l'e-mail.

1. Faites glisser un bloc de contenu dynamique depuis le volet d'édition dans le corps de votre e-mail.<br><br>
2. Sélectionnez un modèle pour la première variation. Vous pouvez maintenant définir les variables de design et de contenu. Enregistrez la variation une fois terminée. <br>![Éditeur de modèle de variation de contenu dynamique Dynamic Yield.]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br>
3. Définissez l'audience dans le volet de contenu dynamique.<br>![Paramètres de ciblage d'audience Dynamic Yield pour une variation de contenu dynamique.]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br>
4. Ajoutez une autre variation pour cibler une autre audience spécifique ou tous les utilisateurs. Répétez l'opération selon vos besoins.<br><br>
5. Définissez les priorités de vos variations à l'aide des flèches haut et bas. <br><br>
6. Les priorités déterminent quelle variation est proposée lorsqu'un utilisateur est éligible à plusieurs expériences.

### Étape 3 : Intégrer votre e-mail avec Braze {#step-3-integrate-your-email-with-braze}

Cette intégration vous permet d'ajouter des widgets de recommandations personnalisées et du contenu dynamique alimentés par Dynamic Yield dans vos Campaigns d'e-mail Braze. L'intégration de ces campagnes dans les Campaigns Braze se fait à l'aide d'un simple code d'intégration que vous collez dans l'éditeur d'e-mail Braze.

1. Cliquez sur l'icône d'intégration ESP sur la page de liste Experience Email.<br><br>
2. Saisissez le jeton pertinent de Braze qui insère le CUID et l'ID d'e-mail de l'utilisateur.<br>![Fenêtre modale d'intégration ESP Dynamic Yield avec les champs de jeton utilisateur Braze.]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})

Lorsque vous êtes satisfait de votre e-mail, l'étape suivante consiste à générer le code à intégrer dans Braze.
1. Dans **Experience Emails**, cliquez sur **Generate Code**.<br><br>
2. Ensuite, cliquez sur **Copy to Clipboard**.<br>![Panneau de code d'intégration généré par Dynamic Yield avec l'action Copy to Clipboard.]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br>
3. Collez le code dans votre Campaign d'e-mail Braze, puis continuez à concevoir, tester et publier votre campagne d'e-mail.
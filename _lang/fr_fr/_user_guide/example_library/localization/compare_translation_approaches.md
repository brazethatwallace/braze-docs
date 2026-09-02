---
nav_title: Comparer les approches de traduction
article_title: Comparer les approches de gestion des traductions multilingues
page_order: 1
page_type: reference
description: "Comparez le Liquid manuel, les Content Blocks, les catalogues, les messages multilingues, les partenaires de traduction et le contenu connecté pour choisir comment Kitchenerie gère les textes localisés."
tool:
  - Campaigns
  - Canvas
---

# Comparer les approches de gestion des traductions multilingues {#compare-approaches-for-managing-multi-language-translations}

> Évaluez la manière dont les textes localisés sont stockés, mis à jour, prévisualisés et envoyés afin de choisir une approche de localisation adaptée à votre workflow de QA, votre mix de canaux et votre fréquence de mise à jour.

## À propos de cet exemple {#about-this-example}

Kitchenerie, un détaillant fictif d'ustensiles de cuisine, envoie des e-mails, des notifications push et des messages in-app en anglais, en français et en allemand. Le marketing et l'ingénierie ont besoin d'une méthode reproductible et évolutive pour gérer les traductions à travers les Campaigns.

Braze prend en charge plusieurs approches de localisation :

- **Liquid conditionnel manuel :** contenu saisi par langue dans le corps du message
- **Content Blocks :** blocs réutilisables (avec ou sans tags de traduction multilingue)
- **Catalogues :** lignes de traduction structurées indexées par locale
- **Messages multilingues :** tags de traduction, imports CSV et API de traduction (accès anticipé)
- **Partenaires de traduction :** Smartling, Phrase, Lokalise et autres
- **Contenu connecté :** chaînes localisées récupérées depuis votre CMS ou API au moment de l'envoi

Cet exemple compare les compromis afin que vous puissiez associer une approche à votre workflow d'assurance qualité, votre mix de canaux, votre fréquence de mise à jour et les ressources de votre équipe. Il ne remplace pas la configuration étape par étape d'une méthode individuelle. Pour des présentations détaillées des fonctionnalités, commencez par [Localisation]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) et [Messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Considérations {#considerations}

- Déterminez si vous avez besoin d'un aperçu et d'une assurance qualité dans le tableau de bord, de workflows de traduction professionnelle, de mises à jour fréquentes du contenu ou de textes pilotés par un CMS en temps réel avant de choisir un modèle.
- Les [messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) prennent en charge les e-mails, les notifications push, les bannières, les messages in-app et les Content Blocks. Notez que les SMS et WhatsApp utilisent d'autres modèles de localisation. Le Liquid manuel, les Content Blocks, les catalogues, les partenaires et le contenu connecté peuvent s'appliquer à tous les canaux où ces fonctionnalités sont prises en charge.
- Braze ne génère pas de traductions. Vous fournissez le contenu via le tableau de bord, un fichier CSV, l'API, l'import de catalogue, un workflow partenaire ou un CMS externe.
- Le Liquid manuel et les Content Blocks avec des conditions intégrées nécessitent des conventions de nommage et des processus de révision à mesure que le nombre de langues augmente, et les workflows multilingues et partenaires centralisent les mises à jour mais peuvent nécessiter une maintenance via CSV ou API.
- Le contenu connecté et certains flux partenaires dépendent de systèmes externes. Si une API ou un CMS est indisponible au moment de l'envoi, le contenu localisé peut ne pas se charger.
- Les chevauchements sont fréquents. Par exemple, vous pouvez utiliser des tags multilingues pour le corps des e-mails, des Content Blocks pour les pieds de page partagés et des catalogues pour le contenu produit au sein du même programme.

## Configuration {#setup}

### Étape 1 : Identifier vos exigences de localisation {#step-1-capture-your-localization-requirements}

| Exigence | Questions à se poser |
| --- | --- |
| Prévisualisation et QA | Les marketeurs doivent-ils prévisualiser chaque locale dans le compositeur Braze avant l'envoi ? |
| Échelle | Combien de langues et à quelle fréquence le contenu change-t-il ? |
| Workflow | Avez-vous besoin d'une révision, de corrections et d'approbations par des traducteurs ? |
| Format des données | Le contenu est-il du texte marketing libre ou des champs produit structurés (noms, prix, URL) ? |
| Automatisation | Les traductions doivent-elles se mettre à jour automatiquement lorsque votre CMS change ? |
| Compétences de l'équipe | Votre équipe peut-elle gérer du Liquid, des imports CSV, des API ou des intégrations partenaires ? |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identifier vos exigences de localisation" }

### Étape 2 : Comparer les approches en un coup d'œil {#step-2-compare-approaches-at-a-glance}

| Dimension | Liquid manuel | Content Blocks | Catalogues | Messages multilingues | Partenaires de traduction | Contenu connecté |
| --- | --- | --- | --- | --- | --- | --- |
| Prévisualisation / QA dans le tableau de bord | Oui | Oui | Oui | Oui | Variable selon le partenaire | Limité — plus difficile de prévisualiser le contenu récupéré |
| Par défaut (sans intégration) | Oui | Oui | Partiel — configuration du catalogue requise | Oui | Non — configuration du fournisseur | Non — API ou CMS requis |
| Couverture des canaux | Tous les canaux pris en charge | Tous les canaux pris en charge | Tous les canaux pris en charge | E-mail, notification push, bannières, messages in-app, Content Blocks | Variable selon le partenaire | Tous les canaux pris en charge |
| Effort de déploiement | Faible | Faible à moyen | Moyen | Faible | Élevé (dépend du partenaire) | Moyen |
| Effort récurrent (BAU) | Élevé — modifications par message | Moyen — maintenance des blocs | Moyen — mises à jour CSV ou API | Moyen — imports CSV | Moyen — géré dans la plateforme | Faible — récupéré au moment de l'envoi |
| Mises à jour fréquentes | Non | Partiel | Non | Partiel | Oui | Oui |
| Workflow de traduction professionnelle | Non | Non | Non | Non | Oui | Non |
| Données structurées / produit | Limité | Limité | Oui — idéal pour le contenu indexé | Limité | Variable | Oui — via une source externe |
| Risque de dépendance externe | Aucun | Aucun | Aucun | Aucun | Moyen | Moyen — l'envoi échoue si la source est indisponible |
| Idéal pour | Peu de langues, mises à jour peu fréquentes | Composants partagés entre les messages | Nombreuses locales de chaînes structurées | Nombreuses langues avec moins d'effort de copier-coller | Traduction d'entreprise avec approbations | Localisation dynamique pilotée par un CMS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Comparer les approches en un coup d'œil" }

### Étape 3 : Associer les scénarios de type Kitchenerie à une approche {#step-3-match-kitchenerie-style-scenarios-to-an-approach}

| Scénario Kitchenerie | Point de départ recommandé |
| --- | --- |
| Trois langues, peu de Campaigns par mois, petite équipe marketing | Liquid conditionnel manuel ou Content Blocks avec Liquid |
| En-tête, pied de page et blocs juridiques partagés entre e-mail et messages in-app | Content Blocks — avec [traductions multilingues enregistrées sur le bloc]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#save-translations-in-content-blocks) lorsque les locales se multiplient |
| Noms de produits, lignes promotionnelles et URL d'images indexés par locale | [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs) |
| E-mail et notification push dans huit locales ou plus avec prévisualisation dans le compositeur | [Messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) |
| TMS centralisé avec workflow de traduction et approbations | [Partenaires de localisation]({{site.baseurl}}/partners/message_personalization/localization) (par exemple Smartling ou Phrase) |
| Contenu géré dans un CMS mis à jour quotidiennement | [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Associer les scénarios de type Kitchenerie à une approche" }

### Étape 4 : Déployer l'approche sélectionnée {#step-4-implement-the-approach-you-selected}

1. **Liquid conditionnel manuel :** Utilisez les attributs de profil `language` ou locale avec les instructions Liquid `if` / `elsif` / `else`. Consultez [Approches alternatives]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#alternative-approaches) et [Logique conditionnelle]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic).
2. **Content Blocks :** Créez des blocs réutilisables ; vous pouvez éventuellement intégrer du Liquid conditionnel à l'intérieur des blocs. Consultez [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) et l'onglet Content Blocks sous [Envoyer des messages traduits]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
3. **Catalogues :** Importez des lignes de traduction (par exemple `id`, `context`, `language`, `body`) et référencez-les avec le Liquid `catalog_items`. Consultez l'onglet Catalogues sous [Envoyer des messages traduits]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
4. **Messages multilingues :** [Ajoutez des locales]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings), encadrez le contenu avec des balises de traduction, puis importez un CSV. Si vous disposez d'un accès anticipé aux [endpoints de traduction]({{site.baseurl}}/api/endpoints/translations), vous pouvez mettre à jour les traductions par API. Prévisualisez avec **Multi-language user** dans le compositeur.
5. **Partenaires de traduction :** Configurez les locales de l'espace de travail, puis suivez l'intégration de votre partenaire (par exemple [Smartling]({{site.baseurl}}/partners/message_personalization/localization/smartling) ou [Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase)).
6. **Contenu connecté :** Appelez votre CMS ou votre API de traduction au moment de l'envoi. Testez minutieusement ; la prévisualisation peut ne pas refléter les réponses de l'API en direct or en ligne/en production/instantané. Consultez [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).

Pour l'orchestration de Canvas et de Campaigns entre les régions (un parcours unique versus un parcours par pays), consultez [Gestion des traductions]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management) sur la page Localisation.

## Articles connexes {#related-articles}

- [Localisation]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [Messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [Paramètres de localisation]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Partenaires de localisation]({{site.baseurl}}/partners/message_personalization/localization)
- [Langue d'accessibilité pour les messages localisés]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility)
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

Kitchenerie, un détaillant d'articles de cuisine, envoie des e-mails, des notifications push et des messages in-app en anglais, français et allemand. Le marketing et l'ingénierie ont besoin d'une méthode reproductible et évolutive pour gérer les traductions à travers les campagnes.

Braze prend en charge plusieurs modèles de localisation :

- **Liquid conditionnel manuel :** texte saisi par langue dans le corps du message
- **Content Blocks :** blocs réutilisables (avec ou sans tags de traduction multilingue)
- **Catalogues :** lignes de traduction structurées indexées par locale
- **Messages multilingues :** tags de traduction, imports CSV et API de traduction (accès anticipé)
- **Partenaires de traduction :** Smartling, Phrase, Lokalise et autres
- **Contenu connecté :** chaînes localisées récupérées depuis votre CMS ou API au moment de l'envoi

Cet exemple compare les compromis afin que vous puissiez associer une approche à votre workflow de QA, votre mix de canaux, votre fréquence de mise à jour et les ressources de votre équipe. Il ne remplace pas la configuration étape par étape d'une méthode spécifique. Pour des présentations détaillées des fonctionnalités, commencez par [Localisation]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) et [Messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Points à considérer {#considerations}

- Déterminez si vous avez besoin d'une prévisualisation et d'un QA dans le tableau de bord, de workflows de traduction professionnelle, de mises à jour fréquentes du contenu ou de textes pilotés par un CMS en temps réel avant de choisir un modèle.
- Les [messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) prennent en charge les e-mails, les notifications push, les bannières, les messages in-app et les Content Blocks. Notez que les SMS et WhatsApp utilisent d'autres modèles de localisation. Le Liquid manuel, les Content Blocks, les catalogues, les partenaires et le contenu connecté peuvent s'appliquer à tous les canaux où ces fonctionnalités sont prises en charge.
- Braze ne génère pas de traductions. Vous fournissez le texte via le tableau de bord, un CSV, une API, un import de catalogue, un workflow partenaire ou un CMS externe.
- Le Liquid manuel et les Content Blocks avec des conditions intégrées nécessitent des conventions de nommage et des processus de revue à mesure que le nombre de langues augmente, tandis que les workflows multilingues et partenaires centralisent les mises à jour mais peuvent nécessiter une maintenance CSV ou API.
- Le contenu connecté et certains flux partenaires dépendent de systèmes externes. Si une API ou un CMS est indisponible au moment de l'envoi, le contenu localisé peut ne pas se charger.
- Les chevauchements sont courants. Par exemple, vous pouvez utiliser des tags multilingues pour les corps d'e-mails, des Content Blocks pour les pieds de page partagés et des catalogues pour le texte produit dans le même programme.

## Configuration {#setup}

### Étape 1 : Recueillez vos exigences de localisation {#step-1-capture-your-localization-requirements}

| Exigence | Questions à se poser |
| --- | --- |
| Prévisualisation et QA | Les marketeurs doivent-ils prévisualiser chaque locale dans le compositeur Braze avant l'envoi ? |
| Échelle | Combien de langues et à quelle fréquence le texte change-t-il ? |
| Workflow | Avez-vous besoin de revue, de révisions et d'approbations par des traducteurs ? |
| Forme des données | Le texte est-il du contenu marketing libre ou des champs produit structurés (noms, prix, URL) ? |
| Automatisation | Les traductions doivent-elles se mettre à jour automatiquement lorsque votre CMS change ? |
| Compétences de l'équipe | Votre équipe peut-elle maintenir du Liquid, des imports CSV, des API ou des intégrations partenaires ? |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recueillez vos exigences de localisation" }

### Étape 2 : Comparez les approches en un coup d'œil {#step-2-compare-approaches-at-a-glance}

| Dimension | Liquid manuel | Content Blocks | Catalogues | Messages multilingues | Partenaires de traduction | Contenu connecté |
| --- | --- | --- | --- | --- | --- | --- |
| Prévisualisation / QA dans le tableau de bord | Oui | Oui | Oui | Oui | Variable selon le partenaire | Limité — plus difficile de prévisualiser le contenu récupéré |
| Par défaut (sans intégration) | Oui | Oui | Partiel — configuration du catalogue requise | Oui | Non — configuration du fournisseur | Non — API ou CMS requis |
| Couverture des canaux | Tous les canaux pris en charge | Tous les canaux pris en charge | Tous les canaux pris en charge | E-mail, push, bannières, messages in-app, Content Blocks | Variable selon le partenaire | Tous les canaux pris en charge |
| Effort de déploiement | Faible | Faible à moyen | Moyen | Faible | Élevé (dépend du partenaire) | Moyen |
| Effort courant (BAU) | Élevé — modifications par message | Moyen — maintenance des blocs | Moyen — mises à jour CSV ou API | Moyen — imports CSV | Moyen — géré dans la plateforme | Faible — récupéré au moment de l'envoi |
| Mises à jour fréquentes | Non | Partiel | Non | Partiel | Oui | Oui |
| Workflow de traduction professionnelle | Non | Non | Non | Non | Oui | Non |
| Données structurées / produit | Limité | Limité | Oui — idéal pour le texte indexé | Limité | Variable | Oui — via une source externe |
| Risque de dépendance externe | Aucun | Aucun | Aucun | Aucun | Moyen | Moyen — l'envoi échoue si la source est indisponible |
| Idéal pour | Peu de langues, mises à jour peu fréquentes | Composants partagés entre les messages | Nombreuses locales de chaînes structurées | Nombreuses langues avec moins d'effort de copier-coller | Traduction d'entreprise avec approbations | Localisation dynamique pilotée par un CMS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Comparez les approches en un coup d'œil" }

### Étape 3 : Associez les scénarios de type Kitchenerie à une approche {#step-3-match-kitchenerie-style-scenarios-to-an-approach}

| Scénario Kitchenerie | Point de départ recommandé |
| --- | --- |
| Trois langues, peu de campagnes par mois, petite équipe marketing | Liquid conditionnel manuel ou Content Blocks avec Liquid |
| En-tête, pied de page et blocs juridiques partagés entre e-mails et messages in-app | Content Blocks — avec [traductions multilingues enregistrées sur le bloc]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#save-translations-in-content-blocks) lorsque les locales se multiplient |
| Noms de produits, lignes promotionnelles et URL d'images indexés par locale | [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs) |
| E-mails et notifications push dans huit locales ou plus avec prévisualisation dans le compositeur | [Messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) |
| TMS central avec workflow de traducteurs et approbations | [Partenaires de localisation]({{site.baseurl}}/partners/message_personalization/localization) (par exemple Smartling ou Phrase) |
| Texte géré dans un CMS mis à jour quotidiennement | [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Associez les scénarios de type Kitchenerie à une approche" }

### Étape 4 : Déployez l'approche sélectionnée {#step-4-implement-the-approach-you-selected}

1. **Liquid conditionnel manuel :** utilisez les attributs de profil `language` ou locale avec les instructions Liquid `if` / `elsif` / `else`. Consultez [Approches alternatives]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#alternative-approaches) et [Logique conditionnelle]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic).
2. **Content Blocks :** créez des blocs réutilisables ; vous pouvez éventuellement intégrer du Liquid conditionnel dans les blocs. Consultez [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) et l'onglet Content Blocks sous [Envoyer des messages traduits]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
3. **Catalogues :** importez des lignes de traduction (par exemple `id`, `context`, `language`, `body`) et référencez-les avec le Liquid `catalog_items`. Consultez l'onglet Catalogues sous [Envoyer des messages traduits]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
4. **Messages multilingues :** [ajoutez des locales]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings), encadrez le texte avec des tags de traduction, puis importez un CSV. Si vous disposez d'un accès anticipé aux [endpoints de traduction]({{site.baseurl}}/api/endpoints/translations), vous pouvez mettre à jour les traductions par API. Prévisualisez avec **Multi-language user** dans le compositeur.
5. **Partenaires de traduction :** configurez les locales de l'espace de travail, puis suivez l'intégration de votre partenaire (par exemple [Smartling]({{site.baseurl}}/partners/message_personalization/localization/smartling) ou [Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase)).
6. **Contenu connecté :** appelez votre CMS ou API de traduction au moment de l'envoi. Testez minutieusement ; la prévisualisation peut ne pas refléter les réponses de l'API en production. Consultez [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).

Pour l'orchestration Canvas et Campaign à travers les régions (un parcours unique versus un parcours par pays), consultez [Gestion des traductions]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management) sur la page Localisation.

## Articles connexes {#related-articles}

- [Localisation]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [Messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [Paramètres de localisation]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Partenaires de localisation]({{site.baseurl}}/partners/message_personalization/localization)
- [Langue d'accessibilité pour les messages localisés]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility)
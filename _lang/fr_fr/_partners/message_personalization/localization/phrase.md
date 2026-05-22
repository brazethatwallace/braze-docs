---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "Cet article de référence présente le partenariat entre Braze et Phrase, un logiciel de localisation basé dans le cloud. Cette intégration vous permet de traduire les modèles d'e-mail et les Content Blocks sans quitter l'interface de Braze."
page_type: partner
search_tag: Partner

---

# Phrase

> [Phrase](https://phrase.com/) est un logiciel basé dans le cloud qui permet de gérer la localisation. Phrase permet d'automatiser les flux de traduction et de prendre en charge la localisation continue pour les équipes agiles.

_Cette intégration est assurée par Phrase._

## À propos de l'intégration {#about-the-integration}

L'intégration de Phrase et de Braze vous permet de traduire des modèles d'e-mail et des Content Blocks sans quitter l'interface de Braze. Grâce à l'intégration de Phrase TMS pour Braze, vous pouvez accroître l'engagement client et stimuler la croissance sur de nouveaux marchés grâce à une localisation fluide des contenus.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte Phrase TMS | Un compte Phrase TMS Ultimate ou Enterprise est requis pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST Braze avec toutes les autorisations. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

## Étape 1 : Paramètres Phrase TMS {#step-1-phrase-tms-settings}

Dans Phrase, accédez à **Settings > Integrations > Connectors > New**.

1. Donnez un nom à la connexion et changez le type en **Braze**.<br><br>
2. Saisissez la clé API REST et l'endpoint REST de Braze.<br><br>
3. Sélectionnez la manière dont le connecteur doit importer les modèles d'e-mail avec les Content Blocks liés.
- Modèle d'e-mail sélectionné uniquement
- Inclure les Content Blocks<br><br>
4. Sélectionnez la manière dont le connecteur doit exporter les traductions des modèles d'e-mail.
- Créer un nouvel élément
- Élément d'origine
  - L'élément d'origine exporte les traductions vers le même modèle/bloc. Les segments linguistiques sont définis par l'attribut fourni.<br><br>
    {% raw %}
    Indiquez l'attribut de langue si l'élément d'origine est sélectionné. L'attribut de langue définit la langue de l'argument if/elsif. Si vous utilisez l'option de l'élément d'origine, la structure doit être la suivante :

    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
    danish content
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
    portuguese content
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
    swedish content
    {% else %}
    Original content
    {% endif %}
    ```
    Ou en utilisant le mappage clés/valeurs avec assign :
    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
      {% assign abc_key1 = "danish_value1" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
      {% assign abc_key = "portuguese value" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
      {% assign abc_key = "swedish value" %}
    {% else %}
      {% assign abc_key = "Source language value" %}
    {% endif %}
    ```
    La configuration Liquid ci-dessus doit être strictement respectée, mais l'attribut de langue ainsi que les clés et les valeurs associées peuvent être ajustés.<br><br>
    Chaque code de langue ne peut être utilisé qu'une seule fois. Toutefois, plusieurs langues peuvent être utilisées pour un même segment, par exemple :
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. Cliquez sur **Test connection**. Une coche apparaît si la connexion est réussie. Survolez l'icône pour obtenir des détails supplémentaires.<br><br>
7. Enfin, cliquez sur **Save**. Ce connecteur sera disponible sur la page **Connectors**.

## Étape 3 : Envoyez du contenu à Phrase et réexportez vers Braze {#step-3-send-content-to-phrase-and-export-back-to-braze}

1. Tout d'abord, configurez le [portail de soumission](https://support.phrase.com/hc/en-us/articles/5709602111132) pour permettre aux soumissionnaires d'ajouter des fichiers aux demandes directement depuis le dépôt en ligne.<br><br>
2. Utilisez la [création automatique de projets (APC)](https://support.phrase.com/hc/en-us/articles/5709647363356) pour que Phrase TMS crée automatiquement de nouveaux projets lorsqu'un changement dans les états de flux de travail spécifiés est détecté.<br><br>
3. Les éléments de contenu sélectionnés sont importés dès la première exécution de l'APC.

L'[API du connecteur](https://cloud.memsource.com/web/docs/api#) permet d'automatiser des étapes qui, autrement, seraient effectuées manuellement via l'interface utilisateur. Les [webhooks](https://support.phrase.com/hc/en-us/articles/5709693398812) peuvent être utilisés pour que Phrase TMS informe des systèmes tiers de certains événements (par exemple, un changement de statut d'une tâche).
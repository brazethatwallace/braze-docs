---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "Cet article de référence présente le partenariat entre Braze et Transifex, une plateforme de localisation qui vous permet d'automatiser la traduction et de libérer vos équipes pour qu'elles se concentrent sur la création d'expériences client exceptionnelles."
page_type: partner
search_tag: Partner

---

# Transifex

> [Transifex](https://www.transifex.com/) permet une localisation robuste auprès de l'ensemble de votre base d'utilisateurs, quelle que soit la langue.

_Cette intégration est maintenue par Transifex._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Transifex utilise le Contenu connecté pour vous permettre d'extraire une collection de chaînes de caractères de ressources et d'inclure les traductions pertinentes dans vos messages, en remplacement de lignes de formatage conditionnel basées sur la langue. Cette intégration automatise la traduction et libère vos équipes pour qu'elles se concentrent sur la création d'expériences client exceptionnelles.

{% alert important %}
Depuis le 7 avril 2022, Transifex a rendu obsolètes les versions 2 et 2.5 de son API pour faire place à la version 3. Les versions 2 et 2.5 ne sont plus opérationnelles et les requêtes correspondantes échoueront. <br><br>Les instructions d'intégration suivantes tiennent compte de la mise à jour vers la version 3. Mettez à jour vos appels au Contenu connecté en conséquence.
{% endalert %}

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte Transifex | Un [compte Transifex](https://www.transifex.com/signin/) est nécessaire pour bénéficier de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

L'intégration de Transifex utilise l'[API de traduction des ressources](https://developers.transifex.com/reference/get_resource-translations) de Transifex. La commande cURL suivante vous permettra de vérifier si votre compte possède des valeurs de contenu associées à des traductions.

Tout d'abord, saisissez les valeurs `<ORGANIZATION_NAME>`, `<PROJECT_NAME>` et `<RESOURCE_NAME>` qui se trouvent dans votre compte Transifex. Ensuite, remplacez `<LANGUAGE>` par le code de la langue par laquelle vous souhaitez filtrer les traductions, et `<TRANSIFEX_BEARER_TOKEN>` par votre [jeton porteur](https://developers.transifex.com/reference/api-authentication) Transifex.

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/<TRANSIFEX_BEARER_TOKEN>'
```

Par exemple, si votre projet Transifex se trouve à l'adresse `https://www.transifex.com/appboy-3/french2/french_translationspo/`, le `project_name` sera « french2 » et le `resource_name` sera « french_translationspo ».

## Exemple de message avec Contenu connecté {#connected-content-message-example}

Cet extrait de code utilise l'API de traduction des ressources Transifex et l'attribut `language` de l'utilisateur. En fonction de vos besoins, vous pouvez ensuite parcourir les objets de chaînes de caractères et en extraire le contenu pertinent à l'aide du Liquid suivant : `{{strings.data[X].attributes.strings.other}}`.

{% raw %}
```
{% assign organization = "<ORGANIZATION_NAME>" %}
{% assign project = "<PROJECT_NAME>" %}
{% assign resource = "<RESOURCE_NAME>" %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content
     https://rest.api.transifex.com/resource_translations?filter[resource]=o:{{organization}}:p:{{project}}:r:{{resource}}&filter[language]=l:{{${language}}}
     :method GET
     :headers {
       "Authorization": "Bearer <TRANSIFEX_BEARER_TOKEN>"
  }
     :accept application/vnd.api+json
     :save strings
%}
{% endif %}

{% if {{strings}} != null and {{strings.data[0].attributes.strings.other}} != "" and {{${language}}} != null %}
  {{strings.data[0].attributes.strings.other}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```
{% endraw %}


[16]: [success@braze.com](mailto:success@braze.com)
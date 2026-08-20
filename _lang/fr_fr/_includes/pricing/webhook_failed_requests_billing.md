{% comment %}
  Shared webhook billing note for Message Credits / Action Credits pages.
  Optional parameter:
  - credit_name: Product name shown in the sentence (default: "Message Credits")
{% endcomment %}
{% assign credit_name = include.credit_name | default: "Message Credits" %}
À compter du 19 août 2026, les requêtes webhook échouées sont exclues de la facturation d'utilisation ; seules les requêtes réussies consomment des {{ credit_name }}. Ce changement s'applique de manière prospective et n'affecte pas l'utilisation facturée avant la date d'entrée en vigueur.
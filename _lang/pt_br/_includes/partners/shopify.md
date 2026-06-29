{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
A integração padrão é feita sob medida para lojas online Shopify, proporcionando um processo de configuração simples e direto. Essa opção permite que você conecte rapidamente sua loja Shopify à Braze, possibilitando o uso de ferramentas poderosas de engajamento de clientes sem necessidade de ampla expertise técnica. Com essa opção de integração, você pode sincronizar dados de clientes, automatizar o envio de mensagens personalizadas e aprimorar seus esforços de marketing por meio de recursos abrangentes da Braze.

Para usar a integração padrão do Shopify, consulte [Configuração da integração padrão do Shopify]({{site.baseurl}}/shopify_standard_integration/).
{% endtab %}

{% tab custom %}
A integração personalizada oferece uma solução mais flexível e componível se você usar Shopify Hydrogen ou tiver uma loja headless. Essa opção permite que você implemente os SDKs da Braze diretamente no seu ambiente Shopify, possibilitando uma integração mais profunda e funcionalidades personalizadas. Se você deseja criar experiências únicas para os clientes ou otimizar fluxos de trabalho específicos, a integração personalizada fornece as ferramentas necessárias para aproveitar totalmente as capacidades da Braze em uma configuração headless.

Para usar a integração personalizada do Shopify, consulte [Configuração da integração personalizada do Shopify]({{site.baseurl}}/shopify_custom_integration/).
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == 'Custom external ID historical backfill' %}

Se você planeja integrar com um ID externo personalizado (seja para a [integração padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4) ou para a [integração personalizada]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6), será necessário adicionar seu ID externo personalizado como um metacampo de cliente da Shopify a todos os perfis de clientes existentes da Shopify e, em seguida, realizar o backfill histórico.

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

Você pode combinar [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) com [códigos de promoção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) para enviar informações de códigos de promoção para o Currents. Use a tag `capture` para armazenar o código de promoção em uma variável e, em seguida, faça referência a essa variável em `message_extras`:

{% raw %}
```liquid
{% capture code %}
{% promotion('puttshacktest2') %}
{% endcapture %}
Use {{code}} for an exclusive discount!
{% message_extras :key cardscode :value {{code}} %}
```
{% endraw %}

{% endif %}
---
nav_title: Mention Me
article_title: Integrar o Mention Me à Braze
description: Guia de configuração da integração Mention Me
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mention Me

> Juntos, o [Mention Me](https://www.mention-me.com/) e a Braze podem ser sua porta de entrada para atrair clientes premium e promover uma fidelidade inabalável à marca. Ao integrar perfeitamente os dados primários de indicação à Braze, você pode oferecer experiências omnicanais altamente personalizadas direcionadas aos fãs da sua marca.

_Essa integração é mantida pela Mention Me._

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Pré-requisito | Descrição |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Uma conta Mention Me | É necessário ter uma conta [Mention Me](https://mention-me.com/login) para aproveitar essa parceria. |
| Uma chave da API REST da Braze | Uma chave da API REST da Braze com as permissões `users.track` e `templates.email.create`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Um endpoint REST da Braze | [URL do seu endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

* Envie dados de contato e opt-ins de clientes indicados pelo Mention Me para a Braze em tempo real
* Use os dados de indicação para criar lembretes por e-mail de cupons
* Aprimore o desempenho de outros canais de marketing usando dados de indicação para segmentar e direcionar clientes de alto valor

## Quais dados são enviados do Mention Me para a Braze? {#what-data-is-sent-from-mention-me-to-braze}

Quando você configurar essa integração, o Mention Me criará automaticamente os atributos e os eventos dos seus clientes — portanto, não há necessidade de fazer isso antes.

Os endereços de e-mail dos seus clientes na Braze serão usados para vincular eventos relevantes e atributos personalizados. O Mention Me enviará eventos e atributos de perfil de contato para qualquer cliente potencial ou existente que disparar esse evento por meio do Mention Me, independentemente do status de opt-in.

Para mais detalhes, consulte [Atributos e eventos do perfil de contato](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze).

## Integração do Mention Me {#integrating-mention-me}

{% alert tip %}
Para um passo a passo completo, consulte a [documentação de configuração da Braze do Mention Me](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me).
{% endalert %}

Para integrar o Mention Me à Braze:

1. No Mention Me, acesse a página de [integração da Braze](https://mention-me.com/merchant/~/integrations/braze) e selecione **Connect**.
2. Selecione **Create New Authorization**, adicione a [chave de API criada anteriormente](#prerequisites) e selecione sua instância da Braze.
3. Escolha um ou mais países com os quais você gostaria de sincronizar.
4. Quando terminar, selecione **Connect**.
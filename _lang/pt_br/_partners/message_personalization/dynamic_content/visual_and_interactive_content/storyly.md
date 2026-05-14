---
nav_title: Storyly
article_title: Storyly
description: "Este artigo de referência descreve a parceria entre a Braze e a Storyly, um SDK leve, que permite aos proprietários de aplicativos direcionar seus segmentos e alimentar a Braze com mais dados primários."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> A [Storyly](https://www.storyly.io/) é um SDK leve que leva stories para seu app ou site. Com um estúdio de design intuitivo, análises relevantes e conectividade prática, a Storyly é uma ferramenta poderosa para enriquecer a experiência do público.

_Essa integração é mantida pela Storyly._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Storyly permite que você use seus segmentos na Braze como um público na plataforma Storyly. Com essa integração, você pode:
- Direcionar seus segmentos com stories específicas
- Usar atributos do usuário para personalizar o conteúdo das suas stories

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Storyly | É necessário ter uma conta na Storyly para aproveitar essa parceria. |
| Storyly SDK | Você deve instalar o [Storyly SDK](https://integration.storyly.io/). |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as seguintes permissões: <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso {#use-cases}

Com a integração da Braze e da Storyly, os proprietários de aplicativos podem mostrar stories para todos os segmentos na Braze e personalizar as stories com atributos do usuário.

Alguns casos de uso comuns incluem:

__Direcione segmentos da Braze na Storyly__<br>Após a conclusão da integração, você poderá criar um público da Storyly com base em seus segmentos da Braze. Esse pode ser um segmento demográfico ou comportamental. Por exemplo, direcione os usuários que moram em um local específico, aqueles que realizam uma ação específica no seu app ou aqueles interessados em produtos específicos com stories específicas para aumentar a conversão.<br>
__Stories personalizadas com atributos do usuário__<br>Os atributos do usuário da Braze também podem ser usados na Storyly para gerar stories dinâmicas. Isso pode incluir o nome de um usuário, produtos em um carrinho ou até mesmo produtos favoritos, fornecendo aos usuários stories personalizadas exclusivas. A personalização ajuda a aumentar as taxas de conversão nas stories e a taxa geral de engajamento nas stories.

## Integração de exportação de dados {#data-export-integration}

A integração entre a Braze e a Storyly é explicada no vídeo a seguir:

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Certifique-se de que sua integração com a Storyly contenha parâmetros personalizados. Esses parâmetros serão combinados com a propriedade do usuário `external id` da Braze. A implementação de parâmetros personalizados é explicada aqui para [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html) e [Web](https://integration.storyly.io/web/personalization-customaudience.html).

Você também pode consultar a documentação da [Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly) para obter mais informações.

### Etapa 1: Configure a integração no dashboard da Storyly {#step-1-set-the-integration-on-storyly-dashboard}

Uma integração pode ser criada em **Storyly Dashboard > Settings > Integrations > Connect with Braze**. Aqui você precisará da sua chave da API REST da Braze e do endpoint REST da Braze.

### Etapa 2: Obtenha seus segmentos {#step-2-get-your-segments}

Em seguida, você pode usar os segmentos da Braze para criar um público da Storyly. Isso pode ser criado em **Storyly Dashboard > Settings > Audiences > New Audience > Create Audience with Braze**.

Aqui, haverá duas opções de sincronização. Selecione **One-time sync** para stories de campanhas específicas ou **Daily Sync** para stories de longo prazo.
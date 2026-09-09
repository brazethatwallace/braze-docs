---
nav_title: Testes de Banners
article_title: Testes de Banners
page_order: 2
description: "Aprenda como testar a mensagem do seu Banner antes de lançar sua campanha para garantir que todas as mídias, textos, personalização e atributos personalizados sejam exibidos corretamente."
channel:
  - banners
noindex: true
---

# Testes de Banners {#test-banners}

> Aprenda como testar a mensagem do seu Banner antes de lançar sua campanha para garantir que todas as mídias, textos, personalização e atributos personalizados sejam exibidos corretamente. Para mais informações gerais, veja [Sobre Banners]({{site.baseurl}}/developer_guide/banners).

## Pré-requisitos {#prerequisites}

Antes de testar mensagens de Banner na Braze, você precisará criar uma [Campaign de Banner na Braze]({{site.baseurl}}/user_guide/channels/banners/create_a_banner). Além disso, verifique se o posicionamento que você deseja testar já está [inserido no seu app ou website]({{site.baseurl}}/developer_guide/banners/placements).

Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou usuários individuais, o push deve estar ativado nos seus dispositivos de teste com tokens por push válidos registrados para o usuário teste antes do envio.

## Teste um Banner {#test-a-banner}

{% multi_lang_include banners/testing.md page="testing" %}
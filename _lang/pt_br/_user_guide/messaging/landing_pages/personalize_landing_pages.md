---
nav_title: Personalizar landing pages
article_title: Personalizar landing pages
description: "Este artigo aborda como personalizar landing pages da Braze com o editor de arrastar e soltar."
page_order: 4
---

# Personalizar landing pages {#personalize-landing-pages}

> Use a personalização com Liquid em landing pages para adaptar dinamicamente o conteúdo com dados do perfil de usuário. Por exemplo, você pode personalizar títulos com base em diferentes atributos de usuário sem precisar gerenciar várias landing pages estáticas.

{% alert important %}
A personalização com Liquid para landing pages está disponível apenas no plano Pro de landing pages. Atualmente, [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), [multi-idioma]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/) e [códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/) não são compatíveis com a personalização Liquid em landing pages.
{% endalert %}

## Inserindo Liquid {#inserting-liquid}

No editor de arrastar e soltar, você pode inserir personalização com Liquid tanto no editor quanto nas configurações da página ou do bloco no painel à direita. Para instruções sobre como implementar Liquid, confira nossa [documentação dedicada sobre Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#using-liquid).

![Editor de landing page com personalização Liquid adicionada.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Pré-visualização e teste {#previewing-and-testing}

Ao pré-visualizar uma landing page no editor, você pode visualizar a página como um usuário aleatório, um usuário existente ou um usuário personalizado.

No entanto, ao pré-visualizar a landing page a partir da tabela de dados ou da página **Landing Page details**, você só poderá visualizá-la como um usuário aleatório.

## Considerações sobre personalização {#personalization-considerations}

Para manter o desempenho ideal com landing pages personalizadas, observe os seguintes limites de tamanho:

- **Salvar uma landing page:** Se o tamanho exceder 500&nbsp;KB, você poderá receber uma mensagem de aviso indicando que a página excedeu nossos limites de tamanho, o que pode impedir sua publicação.
- **Renderização com personalização Liquid:** O tamanho total não deve exceder 1&nbsp;MB. Caso contrário, a página poderá ser automaticamente despublicada pela Braze.

### Evitar a despublicação de landing pages {#avoid-unpublishing-landing-pages}

Se sua página exceder esses limites de tamanho, você receberá um e-mail informando que ela poderá ser despublicada caso continue excedendo o limite. Quando o limite for atingido, a página será automaticamente despublicada e você receberá uma notificação.

Para evitar que sua página exceda os limites de tamanho ou tenha tempos de carregamento lentos, certifique-se de usar personalização Liquid que:

- Não faça loops contínuos nem referencie grandes conjuntos de dados.
- Não dependa de lógica matemática ou condicional extensa dentro do bloco Liquid.

Além disso, evite incorporar scripts grandes, folhas de estilo e ativos codificados em base64 diretamente no código da sua landing page. Esses ativos inline contam para o limite de tamanho da página e podem tornar a renderização mais lenta. Em vez disso, faça upload de fontes, imagens, folhas de estilo e scripts para a [Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). Os ativos servidos a partir da Biblioteca de mídia são hospedados no CDN da Braze, portanto não são processados para renderização Liquid e não contam para o limite de tamanho da página.

### Usar Liquid para usuários identificados e anônimos {#use-liquid-for-identified-and-anonymous-users}

O Liquid pode personalizar a experiência da landing page tanto para visitantes identificados quanto anônimos.

- **Usuários identificados:** Vincule a landing page a partir de uma mensagem da Braze e inclua a [Liquid tag de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users/#using-landing-page-liquid-tags). Isso associa o usuário ao seu perfil na Braze e personaliza a experiência da página.
- **Visitantes anônimos:** Use Liquid para conteúdo contextual não baseado em perfil, como um número aleatório ou uma saudação baseada no horário do dia.

## Páginas de fallback {#fallback-pages}

Se seus usuários tentarem acessar uma página que foi despublicada, eles verão uma mensagem indicando que a página não pode ser carregada no momento. Os motivos para uma página ter sido despublicada incluem:

- Liquid complexo ou com erros, que pode causar longos tempos de renderização
- Problemas de rede do usuário
- Exceder os limites máximos de tamanho da landing page
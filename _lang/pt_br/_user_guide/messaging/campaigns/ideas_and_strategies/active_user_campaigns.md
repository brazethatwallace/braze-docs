---
nav_title: Campanhas de usuários ativos
article_title: Campanhas de usuários ativos
page_order: 0.5
page_type: tutorial
description: "Este artigo prático descreve os benefícios das campanhas de usuários ativos no dashboard da Braze e as etapas para criar e configurar uma."
tool:
  - Campaigns

---

# Campanhas de usuários ativos {#active-user-campaigns}

> Identifique seus usuários ativos para criar campanhas personalizadas e recompensar quem usa sua plataforma com frequência.

Entrar em contato com usuários já ativos do seu app pode ser uma ferramenta poderosa para construir uma base fiel de usuários consistentes. Um pouco de reconhecimento personalizado para seus usuários mais engajados pode transformá-los em verdadeiros promotores do seu app.

Você também pode conferir nosso [curso do Braze Learning](https://learning.braze.com/quick-overview-segment-and-campaign-setup) sobre estratégia de marketing para e-mail e campanhas de ciclo de vida recomendadas!

## Entendendo os usuários ativos {#understanding-active-users}

A Braze define um "usuário ativo" em um determinado período como qualquer usuário que tenha uma sessão nesse intervalo de tempo.

Se um usuário perder a conectividade, os dados da sessão serão armazenados em cache localmente e enviados quando a conexão de rede for restabelecida. Essas sessões também serão contabilizadas na contagem de usuários ativos. Além disso, se o seu app tiver um processo de registro, a Braze contará todos os usuários como ativos — registrados ou não.

Se você definir IDs de usuário para identificar usuários quando um novo usuário fizer login, ele será contado como um usuário ativo separado. Usuários atualizados via API também serão contados como usuários ativos no período em que forem atualizados.

## Etapa 1: Identificando seus principais usuários {#step-1-identifying-your-top-users}

Usando nossa seleção de filtros, crie um segmento de usuários que represente sua base de usuários mais fiéis e consistentes. O segmento de exemplo a seguir define os principais usuários.

![Exemplo de filtros de segmento da Braze definindo um público de principais usuários.]({% image_buster /assets/img_archive/define_top_users.png %} "Define your top users")

Além disso, você não precisará continuar atualizando esse segmento, pois os usuários que entrarem ou saírem das restrições da campanha serão direcionados ou removidos automaticamente.

{% alert note %}
O exemplo acima segmenta os usuários pelo uso geral do app. Na maioria dos casos, o conjunto total de filtros necessários para definir seu segmento de principais usuários será amplamente determinado pelas especificidades do seu app.
{% endalert %}

## Etapa 2: Entre em contato com seus principais usuários {#step-2-contact-your-top-users}

### Faça seus usuários se sentirem valorizados {#make-your-users-feel-appreciated}

Faça seus usuários se sentirem valorizados agradecendo pela fidelidade e dedicação ao seu app. Dê a eles mais motivos para continuar voltando ao seu app e incentive mais atividade. Isso pode ser feito por meio de ofertas especiais ou bônus exclusivos para seus principais usuários.

Recompensas inesperadas podem ser mais eficazes para incentivar ações contínuas dos usuários do que se você as tivesse prometido desde o início!

![Uma Campaign na etapa Redigir com uma notificação Rich para iOS que diz: "Obrigado novamente por comprar conosco! Para mostrar nossa gratidão, estamos oferecendo frete grátis na sua próxima compra".]({% image_buster /assets/img/congratulations_push.jpg %})

### Acompanhe seus resultados {#keep-track-of-your-results}

Acompanhe as aberturas para garantir que você está direcionando o grupo certo de usuários com o tipo de mensagem ideal. Além disso, monitore os descadastramentos de push e tenha cuidado para não perder esses usuários essenciais.
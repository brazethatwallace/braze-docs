---
nav_title: Rendimento dinâmico
article_title: Rendimento dinâmico
description: "Esse artigo de referência descreve a parceria entre a Braze e a Dynamic Yield. Essa parceria permite que você use o mecanismo de recomendação e segmentação da Dynamic Yield para criar blocos de experiência que podem ser incorporados às mensagens da Braze."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Rendimento dinâmico {#dynamic-yield}

> A [Dynamic Yield](https://www.dynamicyield.com/), uma empresa da Mastercard, ajuda empresas de todos os setores a oferecer experiências digitais aos clientes que são personalizadas, otimizadas e sincronizadas. Com o [Experience OS](http://www.dynamicyield.com/experience-os) da Dynamic Yield, profissionais de marketing, gerentes de produtos, desenvolvedores e equipes digitais podem combinar algoritmicamente conteúdo, produtos e ofertas com cada cliente para acelerar a receita e a fidelidade do cliente.

_Essa integração é mantida pela Dynamic Yield._

## Sobre a integração {#about-the-integration}

A parceria entre a Braze e o Dynamic Yield permite que você use o mecanismo de recomendação e segmentação do Dynamic Yield para criar blocos de experiência que podem ser incorporados nas mensagens da Braze. Os blocos de experiência podem ser compostos por:
{% multi_lang_include partners/message_personalization/dynamic_yield_experience_blocks.md %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Dynamic Yield | É necessário ter uma conta [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) para aproveitar essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Criar um bloco de experiência {#step-1-create-an-experience-block}

Para criar um bloco de experiência no Dynamic Yield, navegue até **Email > Experience Emails > Create New**.

Em seguida, selecione **Create Experience Block** para criar um bloco de conteúdo dinâmico ou de recomendações para incorporar em um modelo de e-mail da Braze.<br>![Página Experience Emails do Dynamic Yield com a opção Create Experience Block selecionada.]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### Etapa 2: Rascunhar sua mensagem {#step-2-draft-your-messaging}

A imagem a seguir mostra um e-mail criado do zero no construtor.<br>![Construtor de e-mail do Dynamic Yield com um layout de e-mail de experiência em rascunho.]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. Insira o nome da Campaign, uma nota e etiquetas para a Campaign na área de cabeçalho.<br><br>
2. Insira um bloco de experiência. Esses blocos incluem:
  - [Recomendações](#configure-a-recommendations-block): Um widget que oferece aos usuários recomendações totalmente personalizadas.
  - [Conteúdo dinâmico](#configure-a-dynamic-content-block): Direcione diferentes promoções e mensagens para diferentes públicos.<br><br>
3. Atualize as configurações:
  - Use os parâmetros de URL para rastrear cliques no seu software de análise de dados (opcional). Adicione parâmetros às exibições padrão conforme necessário.
  - Selecione uma janela de atributo, de sete dias (padrão) ou de um dia.<br><br>
4. Salve e saia. Você pode voltar para editar todos os elementos do seu e-mail a qualquer momento antes de o código ser gerado. Após a geração do código, você pode editar qualquer coisa que [não afete o código](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Configurar um bloco de recomendações {#configure-a-recommendations-block}

O bloco de recomendações permite definir algoritmos e filtros para gerar conteúdo personalizado para os usuários, que é exibido quando o e-mail é aberto.

1. Arraste um bloco de recomendações do painel de edição para o corpo do seu e-mail.<br><br>
2. Selecione o algoritmo desejado (popularidade, afinidade do usuário, similaridade e outros). Dependendo do algoritmo selecionado, opções adicionais são exibidas:
  - Se sua recomendação é baseada em popularidade, você pode embaralhar os resultados para evitar exibir a mesma recomendação em diferentes e-mails que o destinatário abrir.
  - Outros algoritmos, como similaridade, dependem de contexto para fornecer recomendações, exigindo que você selecione itens a incluir. Esses itens podem ser adicionados no construtor ou você pode [adicionar uma merge tag ao código de incorporação](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced) para torná-lo dinâmico, por exemplo, para adicionar itens semelhantes em e-mails de confirmação de envio.<br><br>
3. Você pode excluir produtos que o usuário já comprou para evitar recomendar esses produtos.<br><br>
4. Você pode adicionar uma [regra de filtro personalizada](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) para fixar produtos específicos em posições, ou incluir e excluir produtos por propriedades do produto. Por exemplo, não mostrar produtos que custem menos de US$ 5 ou mostrar apenas produtos da categoria de shorts.<br><br>
5. Por último, configure o design do bloco de recomendações. Para isso, selecione um modelo de item, defina o número de itens a exibir e em quantas linhas.

### Configurar um bloco de conteúdo dinâmico {#configure-a-dynamic-content-block}
Use o conteúdo dinâmico para direcionar diferentes promoções e mensagens para diferentes usuários. O direcionamento pode ser baseado em afinidade ou público. O Dynamic Yield determina qual experiência personalizada exibir quando o e-mail é aberto.

1. Arraste um bloco de conteúdo dinâmico do painel de edição para o corpo do seu e-mail.<br><br>
2. Selecione um modelo para a primeira variação. Agora você pode definir variáveis de design e conteúdo. Salve a variação quando estiver completa.<br>![Editor de modelo de variação de conteúdo dinâmico do Dynamic Yield.]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br>
3. Defina o público no painel de conteúdo dinâmico.<br>![Configurações de direcionamento de público do Dynamic Yield para uma variação de conteúdo dinâmico.]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br>
4. Adicione outra variação para direcionar outro público específico ou todos os usuários. Repita conforme necessário.<br><br>
5. Defina as prioridades das suas variações usando as setas para cima e para baixo.<br><br>
6. As prioridades determinam qual variação é exibida quando um usuário é elegível para mais de uma experiência.

### Etapa 3: Integrar seu e-mail com a Braze {#step-3-integrate-your-email-with-braze}

Essa integração permite adicionar widgets de recomendação personalizados e conteúdo dinâmico alimentados pelo Dynamic Yield às suas Campaigns de e-mail na Braze. A incorporação dessas campanhas nas Campaigns da Braze é feita com um simples código de incorporação que você cola no editor de e-mail da Braze.

1. Clique no ícone de integração ESP na página de lista de Experience Email.<br><br>
2. Insira o token relevante da Braze que inclui o CUID e o ID de e-mail do usuário.<br>![Modal de integração ESP do Dynamic Yield com campos de token de usuário da Braze.]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})

Quando estiver satisfeito com seu e-mail, a próxima etapa é gerar o código para incorporar na Braze.
1. Em **Experience Emails**, clique em **Generate Code**.<br><br>
2. Em seguida, clique em **Copy to Clipboard**.<br>![Painel de código de incorporação gerado pelo Dynamic Yield com a ação Copy to Clipboard.]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br>
3. Cole o código na sua Campaign de e-mail na Braze e continue a projetar, testar e publicar sua Campaign de e-mail.
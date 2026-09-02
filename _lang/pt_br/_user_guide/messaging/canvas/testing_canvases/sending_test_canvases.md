---
nav_title: Enviar Canvas de teste
article_title: Enviar Canvas de teste
page_order: 1
description: "Este artigo de referência aborda como testar um Canvas antes do lançamento e as melhores práticas."
page_type: reference
tool: Canvas
---

# Enviar Canvas de teste {#send-test-canvases}

> Depois de [criar seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), há várias verificações que você pode querer realizar antes do lançamento, dependendo de detalhes como o tamanho do seu público ou o número de filtros de segmentação.

Sempre que possível, a Braze recomenda testar um Canvas antes de lançá-lo. Esse teste normalmente acontece no seu ambiente da Braze. Testar seu Canvas pode envolver duplicá-lo, conduzir usuários teste pela jornada do usuário e verificar se o comportamento do usuário está alinhado com o que você definiu no seu Canvas.

## Etapa 1: Crie seu plano de teste {#step-1-create-your-test-plan}

Criar um plano de teste é essencial antes de começar a testar seu Canvas. Um plano de teste pode ajudar a identificar e acompanhar áreas específicas da jornada do seu Canvas.

Ao elaborar seu plano de teste, considere as seguintes perguntas:
- Pelo menos um usuário foi criado para cada Branch e jornada do Canvas?
- Algum Segment está sendo usado no seu Canvas?
	- Se segmentos forem usados, pode haver pré-requisitos para que um usuário entre no Canvas antes de se tornar elegível para uma jornada de usuário.
- As mensagens no Canvas de teste possuem algum Liquid nos títulos das mensagens que puxam o ID do usuário ou o endereço de e-mail para garantir que seja fácil identificar tanto a mensagem quanto o usuário para fins de teste?

## Etapa 2: Identifique os usuários teste {#step-2-identify-test-users}

Em seguida, identifique um conjunto de usuários teste que passarão pelas etapas do Canvas sem realmente enviar mensagens para os usuários pretendidos. Os usuários teste podem ser endereços de e-mail existentes que não são usados para serviços reais no seu dashboard da Braze, ou novos endereços de e-mail usados exclusivamente para fins de teste.

## Etapa 3: Configure seu Canvas {#step-3-set-up-your-canvas}

Agora é hora de testar seu Canvas! Para manter as informações do Canvas original e do Canvas de teste organizadas, crie uma duplicata do seu Canvas para fins de teste.

Existem duas maneiras de testar seu Canvas.

- **Método 1:** No Canvas duplicado, edite a parte do **Público de entrada** do criador de Canvas para que apenas os usuários teste sejam elegíveis para o Canvas. Você também pode inserir seu próprio endereço de e-mail como usuário teste adicionando o filtro de teste **Endereço de e-mail**. No exemplo da seção a seguir, limitamos o Canvas a dois usuários teste que usaram o app pela primeira vez há menos de três dias.

![Um Canvas com um público de entrada de "Usou estes apps pela primeira vez há menos de 3 dias" e os endereços de e-mail de dois usuários teste.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **Método 2:** [Pré-visualize as jornadas dos usuários]({{site.baseurl}}/preview_user_paths) selecionando o botão **Test Canvas** no rodapé do criador de Canvas.

## Etapa 4: Lance seu teste {#step-4-launch-your-test}

Lance seu Canvas de teste para permitir que os usuários comecem a entrar. Complete os comportamentos de usuário no seu aplicativo que enviariam os usuários pela respectiva jornada do Canvas.

Verifique se seus usuários teste estão recebendo as mensagens pretendidas das etapas do Canvas. Note que seus usuários teste podem não receber uma mensagem por razões que incluem, mas não se limitam a:

- Não ser elegível para o grupo de controle global
- Limitações de limite de frequência
- Incompatibilidade na associação ao Segment
- Mensagens interrompidas
- Tokens por push associados a usuários diferentes

Continue iterando os testes do Canvas para garantir que seu Canvas funcione conforme o esperado.

## Dicas gerais {#general-tips}

### Identifique as etapas do seu Canvas {#identify-your-canvas-steps}

Em alguns casos, um usuário pode potencialmente receber múltiplas mensagens ao passar por um Canvas. Se a postergação entre as etapas foi reduzida significativamente para testes, nem sempre fica claro qual mensagem está sendo disparada durante o teste. Garantir que as mensagens de teste incluam o nome da etapa ou o ID do usuário (usando Liquid) facilitará a identificação e confirmação de que a mensagem correta foi enviada para os usuários corretos.

### Crie um grupo interno {#create-an-internal-group}

Em vez de criar usuários teste individuais, você pode criar um [Grupo de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), que é um grupo interno cujo objetivo é revisar o conteúdo da sua mensagem. Isso inclui um grupo de usuários que receberá mensagens de teste de Campaigns e Canvas. Então, você pode adicionar esse grupo de teste no campo **Add Content Test Groups** em **Test Recipients**.

### Reduza as postergações de tempo {#reduce-time-delays}

Para ajudar a executar testes de forma mais eficiente, sugerimos reduzir as postergações de tempo para minutos ou segundos durante os testes, para que você possa visualizar as mensagens em tempo hábil. Por exemplo, permita pelo menos 2 a 3 minutos entre os testes para conseguir isolar ações específicas em jornadas específicas do Canvas.

### Aproveite os Content Blocks {#leverage-content-blocks}

Se algum conteúdo for repetido no seu framework de testes (por exemplo, Liquid complexo para filtrar usuários em diferentes etapas do Canvas), tente salvar esse conteúdo repetido como um [Content Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Assim, você poderá incluir o Content Block nas etapas individuais do Canvas.

### Use o Postman e o endpoint de rastreamento de usuários {#use-postman-and-the-track-user-endpoint}

Você pode executar testes com o Postman e a [Coleção Postman da Braze]({{site.baseurl}}/api/postman_collection). Use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para registrar e rastrear eventos personalizados e compras para seus diversos usuários teste.

Note que o envio de dados para a API de rastreamento de usuários só pode ser feito com um ID externo. Portanto, os usuários teste podem precisar ser adicionados como usuários teste dentro de um grupo interno no dashboard da Braze para que erros específicos possam ser investigados mais a fundo.

#### Testando múltiplas ramificações {#testing-for-multiple-branches}

Quando você está testando um Canvas com múltiplas ramificações que segmentam usuários com base em diferentes atributos e eventos, siga este plano de teste:

1. Para cada Branch, identifique os atributos e eventos que o usuário deve ter para ser incluído na jornada do Canvas.
2. Construa esses dados em uma carga útil JSON para ser enviada usando o endpoint `/users/track`.
---
nav_title: Lexer
article_title: Lexer
description: "Este artigo de referência descreve a parceria entre a Braze e a Lexer, uma CDP que coloca os dados do cliente nas mãos dos profissionais de marketing para inspirar experiências que impulsionam as vendas."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [Lexer](https://lexer.io/), uma CDP construída para o varejo, ajuda as marcas a impulsionar vendas incrementais por meio de experiências de cliente aprimoradas, combinando enriquecimento de dados robusto com as ferramentas mais intuitivas e consultoria especializada.

_Esta integração é mantida pela Lexer._

## Sobre a integração {#about-the-integration}

A integração da Braze e da Lexer permite sincronizar dados entre as duas plataformas. Use seus dados da Lexer para criar segmentos valiosos na Braze ou importe os existentes para a Lexer para obter insights.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta de parceiro | É necessário ter uma conta Lexer para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com todas as permissões `user` (exceto `user.delete`) e permissões `segment.list`. O conjunto de permissões pode mudar à medida que a Lexer adiciona suporte a mais objetos da Braze, portanto, talvez você queira conceder mais permissões agora ou planejar a atualização dessas permissões no futuro.<br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [URL do seu endpoint REST]({{site.baseurl}}/api/basics#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
| Bucket S3 e credenciais do Amazon AWS | Antes de iniciar a integração, é necessário ter credenciais de acesso para um bucket S3 do AWS conectado ao seu hub da Lexer (pode ser um bucket criado por você ou um que a Lexer crie e gerencie para você). Visite [a Lexer](https://learn.lexer.io/docs/amazon-s3) para obter orientação sobre esse requisito. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Na Lexer, navegue até **Manage > Integration**, selecione o bloco **Braze** e clique em **Integrate Braze**. Forneça as seguintes informações:
- **Braze REST endpoint**
- **Braze REST API key**
- **AWS Credentials**
  - **AWS S3 bucket name**
  - **AWS S3 [bucket region](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)**
  - **AWS S3 bucket jornada**: Esse caminho deve corresponder ao caminho que você especificou ao [conectar seu bucket S3 à Braze]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3). Deixe em branco se você não especificou nada para a Braze.
  - **AWS S3 secret access key**: Visite a Amazon para informações sobre [criar uma chave de acesso](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/).
- **Braze export segment ID**: O ID do Segment que você criou na Braze contendo todos os usuários que deseja exportar para a Lexer. Se houver usuários que não deseja exportar para a Lexer, você poderá excluí-los do Segment criado na Braze. Para encontrar seu identificador de Segment, clique no Segment desejado na Braze e localize o **Segment API Identifier**.

![Tela de gerenciamento de integrações da Lexer mostrando os campos de integração com a Braze para URL da API, chave de API, detalhes do bucket S3 do AWS e ID do segmento de exportação da Braze.]({% image_buster /assets/img/lexer/braze_integrate_screen.png %})

### Escolha de uma opção do AWS S3 (gerenciada pela Lexer ou autogerenciada) {#choosing-an-aws-s3-option-lexer-managed-or-self-managed}
Usar um bucket gerenciado pela Lexer é a maneira recomendada de conectar a Braze ao seu hub da Lexer e reduz a quantidade de configurações necessárias. A Lexer fornecerá os detalhes necessários para configurar a Braze.

Se já tiver conectado um bucket S3 à Braze e estiver usando-o para outros fins, será necessário fornecer à Lexer acesso a esse bucket autogerenciado seguindo as etapas anteriores.

Essa integração funciona fornecendo à Lexer seu token de API e segredos existentes, permitindo que a Lexer faça essas exportações em seu nome. Ela também importa seus dados da Braze para a Lexer usando essas credenciais e sua configuração do S3 para sincronizar seus dados em ambas as plataformas automaticamente.

## Envio de segmentos para a Braze {#sending-segments-to-braze}

### Etapa 1: Criar ativação {#step-1-create-activation}

O Lexer Activate atualizará automaticamente seus perfis da Braze, adicionando ou removendo atributos à medida que os clientes entram e saem do seu Segment.

1. Na Lexer, em **Lexer Activations**, clique em **ACTIVATE NEW AUDIENCE**.
2. Selecione a ativação Braze apropriada para essa campanha.
3. Adicione seu Segment.
4. Atualize o nome do seu público; esse será o valor do seu atributo na Braze.
5. Esse é o atributo personalizado que será atualizado na Braze. Entre em contato com o [suporte da Lexer](mailto:support@lexer.io) para atualizar.
6. Marque a ação de lista apropriada — na maioria dos casos, você desejará manter sua lista.
7. Revise os termos e condições e clique em **SEND AUDIENCE**.

![Fluxo de trabalho do Lexer Activate mostrando a seleção do canal de ativação, criação de público e detalhes da ativação antes de enviar um público para a Braze.]({% image_buster /assets/img/lexer/lexer.png %})

### Etapa 2: Verificar a ativação {#step-2-verify-activation}

Depois que a ativação for confirmada como enviada no Activate, os registros começarão a ser atualizados na Braze. Seus perfis só estarão totalmente atualizados na Braze após o recebimento de um e-mail de confirmação da Lexer.

### Etapa 3: Criar seu Segment na Braze {#step-3-create-your-braze-segment}

Na Braze, você verá que o nome do público na Lexer agora é um valor no atributo personalizado `lexer_audience`. A Braze tem um limite de 100 valores por atributo.

Para criar seu Segment, navegue até **Segment > + Create Segment** e selecione **Custom Attribute** como filtro. Em seguida, selecione `lexer_audience` como seu atributo e o nome do público da Lexer desejado. Quando terminar, **salve** seu público.

Agora é possível adicionar esse Segment recém-criado a futuras Campaigns e Canvas da Braze para direcionar esses usuários finais.
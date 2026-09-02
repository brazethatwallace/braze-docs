---
nav_title: Wyng
article_title: Wyng
description: "Este artigo de referência descreve a parceria entre a Braze e a Wyng, uma plataforma de dados voluntários usada para coletar, usar e integrar preferências e atributos do cliente por meio de microexperiências, portais de preferências do cliente e uma plataforma de API."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> A [Wyng](https://wyng.com/) fornece ferramentas para criar experiências digitais interativas (questionários, centrais de preferências, promoções) que engajam os consumidores em momentos importantes, coletam preferências e outros dados voluntários e personalizam em tempo real.

_Essa integração é mantida pela Wyng._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Wyng permite que você aproveite os dados voluntários obtidos por meio das experiências da Wyng para personalizar as interações em Braze Campaigns e no BRAZE CANVAS. A Wyng também pode alimentar uma Central de Preferências, para que os consumidores possam controlar os dados e as preferências (inclusive as preferências de comunicação) que compartilham com sua marca.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Wyng | É necessário ter uma conta Wyng para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

### Etapa 1: Conecte a integração da Braze {#step-1-connect-the-braze-integration}

Na Wyng, acesse [**Integrations**](https://wyng.com/dashboard/integrations/) e selecione a guia **Add**. Em seguida, passe o mouse sobre **Braze** e clique em **Connect** para a integração.

![O bloco do parceiro Braze na plataforma Wyng.]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### Etapa 2: Configure o conector da Braze {#step-2-configure-the-braze-connector}

1. Na janela de configuração que se abre, forneça sua chave da API REST da Braze.
![Uma imagem mostrando a aparência do prompt de credenciais.]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. Em seguida, use o menu suspenso para selecionar a campanha da Wyng que deseja compartilhar com a Braze.![Uma imagem do conector da Braze solicitando que você selecione uma campanha da Wyng existente para compartilhar com a Braze.]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. Em seguida, você deve configurar inscrições, objetos de atributo e evento e eventos personalizados.<br><br>
- **Configuração das inscrições (obrigatório)**<br>
Para inscrever usuários em grupos de inscrições, clique em **Add Subscription** e adicione o nome e o ID do grupo de inscrições. Para adicionar vários nomes e IDs de grupos, clique novamente no botão **Add Subscription**.<br>![Uma imagem solicitando o nome e o ID de um grupo de inscrições.]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **Configuração do rastreamento do usuário**<br>
Clique em **Add custom property** para adicionar pares de objetos de atributo e evento para enviar ao endpoint `/users/track`. Use isso para adicionar valores de atributo codificados para cada transação de dados enviada para a integração. Para adicionar várias propriedades, clique novamente no botão **Add custom property**.<br>![Uma imagem solicitando que você adicione propriedades personalizadas de atributo.]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **Enviar evento personalizado**<br>
Opcionalmente, você pode ativar o **Sending custom event**. Se essa opção estiver ativada, inclua o nome do evento e o ID do app correspondente.<br>![Uma imagem solicitando que você envie eventos personalizados, se necessário.]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. Por fim, mapeie os campos da Wyng para os campos da API da Braze com base em seu caso de uso. Clique em **Select a field** para escolher os campos a serem mapeados e, em seguida, clique em **Save** para salvar sua integração. Quando salvos, esses campos mapeados podem ser encontrados em **Integrations > Manage**.
![Um exemplo dos diferentes campos da Wyng que você pode mapear para determinados campos da Braze.]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![Uma lista dos campos de sincronização disponíveis.]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### Etapa 3: Teste sua integração {#step-3-test-your-integration}

Na Wyng, teste o envio do formulário em sua campanha da Wyng. Também é possível enviá-lo na campanha de pré-visualização se não quiser adicionar um registro à campanha de produção principal. Você deverá ver uma transação bem-sucedida no dashboard de **Integration**.

## Usando esta integração {#using-this-integration}

Quando o conector de dados estiver instalado, todos os campos criados na Wyng e adicionados à Braze poderão ser usados como qualquer outro campo de dados para disparar Campaigns, segmentar públicos ou alimentar conteúdo personalizado.

As aplicações são amplas e perguntas específicas podem ser enviadas para [contact@wyng.com](mailto:contact@wyng.com) ou para seu gerente de conta específico.

## Solução de problemas {#troubleshooting}

### Falha no envio {#failed-submission}

No caso de um envio com falha, ao enviar dados para a Braze, clique no link **View Log** para revisar o envio com falha e a mensagem de erro associada.

![O link "View Log" encontrado no cabeçalho de ações.]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

A página de registro mostrará o envio com falha, a quantidade de tentativas, os dados do envio, o erro e um link para reenviar a submissão.

![Um exemplo do que um envio com falha mostrará.]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

A seção **View Error** mostrará o código de erro e algumas informações adicionais sobre a causa do erro. Em seguida, você pode fazer uma referência cruzada do código de erro com a Braze para determinar a causa.

![Um exemplo de registro de erros mostrado na plataforma da Wyng.]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

Se tiver outras dúvidas, entre em contato com o suporte da Wyng ([support@wyng.com](mailto:contact@wyng.com)) para obter assistência.
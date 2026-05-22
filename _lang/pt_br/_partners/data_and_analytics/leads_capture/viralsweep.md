---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "Este artigo de referência descreve a parceria entre a Braze e o ViralSweep, um serviço de software que permite que as marcas criem, executem e gerenciem promoções de marketing digital, como sorteios, concursos, prêmios instantâneos, listas de espera, promoções por indicação e muito mais."
page_type: partner
search_tag: Partner

---

# ViralSweep

> [O ViralSweep](https://viralsweep.com) é um serviço de software que permite às marcas criar, executar e gerenciar promoções de marketing digital, como sorteios, concursos, prêmios instantâneos, listas de espera, promoções por indicação e muito mais.

_Essa integração é mantida pela ViralSweep._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o ViralSweep permite que você realize sorteios e concursos na plataforma ViralSweep (aumentando suas listas de e-mail e SMS) e, em seguida, envie as informações de inscrição em sorteios ou concursos para a Braze para serem usadas em Campaigns ou Canvas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta ViralSweep | É necessário ter uma conta no ViralSweep que utilize o plano de negócios para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com todas as permissões de dados de usuários e e-mail. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | Sua URL de endpoint REST. Seu endpoint dependerá da URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conecte-se à Braze no ViralSweep {#step-1-connect-to-braze-within-viralsweep}

No ViralSweep, navegue até **Integrations > Email & SMS > Add Service** e selecione **Braze**.

![]({% image_buster /assets/img/viralsweep/connect.gif %})

### Etapa 2: Adicionar credenciais da Braze {#step-2-add-braze-credentials}

Na janela de configuração de integrações, forneça sua chave da API REST da Braze e o endpoint REST. Confirme se o endpoint fornecido não inclui `https://`, por exemplo, `dashboard-03.braze.com`.

![Página de integração do serviço ViralSweep solicitando ao usuário a chave de API da Braze e a URL do dashboard da Braze.]({% image_buster /assets/img/viralsweep/connect2.png %}){: style="max-width:40%;"}

Clique em **Connect**.

### Etapa 3: Adicionar credenciais da Braze {#step-3-add-braze-credentials}
Você está conectado! A promoção agora está conectada à Braze, e todas as inscrições coletadas pelo ViralSweep serão enviadas automaticamente para a Braze.

## Perguntas frequentes {#frequently-asked-questions}

### Quais campos o ViralSweep passa para a Braze? {#what-fields-does-viralsweep-pass-to-braze}
- Nome
- Sobrenome
- Endereço de e-mail
- Endereço
- Endereço 2
- Cidade
- Estado
- CEP
- País
- Data de nascimento
- Telefone
- ID da promoção
- Link de indicação
- Nome da campanha de rastreamento

### O ViralSweep atualiza os assinantes? {#does-viralsweep-update-subscribers}
Sim. Se você realizar uma promoção e o ViralSweep enviar alguém para a Braze, e depois você realizar outra promoção no futuro e a mesma pessoa participar, as informações dessa pessoa serão automaticamente atualizadas na Braze (se alguma nova informação for fornecida). Principalmente, a URL de indicação será atualizada com a URL mais recente de cada promoção em que a pessoa participar, e o campo ID da promoção conterá o ID de todas as promoções em que ela participou.

## Solução de problemas {#troubleshooting}

Se você se conectou à Braze e os dados não estão sendo adicionados à sua conta, pode ser porque:

- **O e-mail já existe na Braze**<br>
O endereço de e-mail inserido na promoção pode já estar na sua conta da Braze, portanto não será adicionado novamente; ele só será atualizado se novas informações forem fornecidas para esse contato.<br><br>
- **E-mail já inserido no ViralSweep**<br>
O endereço de e-mail inserido na promoção já foi inserido em outra ocasião, então não será enviado para a Braze novamente. Isso pode acontecer se você configurar sua integração com a Braze depois de já ter participado da promoção.
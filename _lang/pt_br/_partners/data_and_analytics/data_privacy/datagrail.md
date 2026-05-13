---
nav_title: DataGrail
article_title: DataGrail
description: "Este artigo de referência descreve a parceria entre a Braze e a DataGrail, uma plataforma de gerenciamento de privacidade, que permite detectar os dados do consumidor coletados e armazenados na Braze para processar rapidamente as DSRs."
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> A [DataGrail](https://www.datagrail.io/), uma plataforma de gerenciamento de privacidade, ajuda a criar a confiança do consumidor e a eliminar negócios arriscados. Com a detecção contínua do sistema e o atendimento automatizado de solicitações de titulares de dados (DSR), a DataGrail potencializa os programas de privacidade, apoiando a conformidade com as leis e regulamentos de privacidade em evolução, como GDPR, CCPA e CPRA.

_Essa integração é mantida pela DataGrail._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a DataGrail permite que você detecte os dados do consumidor coletados e armazenados na Braze para processar rapidamente as DSRs (solicitações de acesso, exclusão e não venda). A Braze será adicionada a um mapa preciso de onde os dados do consumidor residem na sua organização com mapeamento de dados automatizado — não são mais necessárias pesquisas ou planilhas para manter uma estrutura de privacidade ou produzir um registro de atividades de processamento (RoPA).

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Conta DataGrail | Uma conta DataGrail para aproveitar essa parceria.<br>Entre em contato com o administrador ou envie um e-mail para support@datagrail.io se tiver algum problema ou dúvida sobre a integração. |
| Chave de API da Braze | Uma chave da API REST da Braze com as permissões `events.list`, `users.export.ids`, `users.delete` e `users.track`.<br><br>Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Instância da Braze | Sua instância da Braze pode ser obtida com seu gerente de integração da Braze ou pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Faça login no portal da DataGrail e selecione **Connect** na página de integração da Braze. Em seguida, insira sua instância e a chave de API da Braze e selecione **Connect Braze**.

Se houver contas da Braze adicionais a serem integradas:
1. Selecione **Edit Connection** na página de integração da Braze.
2. No menu suspenso, selecione **+Add New Connection**.
3. Em **Connection Name**, digite um novo nome para identificar essa conta separada (por exemplo, Braze Training Account).
4. Insira uma instância separada e uma chave de API da Braze para essa nova conta.
5. Selecione **Connect**.

Em caso de dúvidas ou problemas relacionados à integração, envie um e-mail para a DataGrail em support@datagrail.io.
---
nav_title: Registro de exportações
article_title: Registro de exportações
page_order: 2
page_type: reference
description: "Esta página abrange o registro de exportações, que permite visualizar o status dos trabalhos de exportação e cancelar as exportações em andamento."
---

# Registro de exportações {#exports-log}

> Use a página **Registro de exportações** para visualizar o status dos trabalhos de exportação e cancelar as exportações em andamento diretamente da plataforma Braze. O registro de exportações suporta exportações de Segments e de [listas de supressão]({{site.baseurl}}/user_guide/audience/suppression_lists) iniciadas pelo dashboard ou pela [API de exportação de usuários]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

É possível encontrar o registro de exportações em **Configurações** > **Configuração e Testes** > **Registro de exportações**.

## O que o log de exportações mostra {#what-the-exports-log-shows}

O log de exportações lista os trabalhos de exportação do espaço de trabalho atual. Cada linha representa uma tentativa de exportação e inclui o nome do Segment ou da lista de supressão, a origem da exportação, o status e os registros de data e hora.

| Coluna | Descrição |
|--------|-------------|
| ID de exportação | Identificador único do trabalho de exportação. Selecione esse ID para abrir os detalhes da exportação ou compartilhar o log. |
| Nome do Segment | Nome do Segment ou da lista de supressão exportada. |
| Tipo de Segment | Se a exportação é de um **Segment** ou de uma **Lista de supressão**. |
| Origem | Onde a exportação foi disparada: **Dashboard** (exportação CSV pela interface) ou **API** (API de exportação de usuários). |
| Status | Estado atual do trabalho de exportação. Consulte [Status de exportação](#export-statuses). |
| Iniciado em | Quando o trabalho de exportação começou. |
| Concluído em | Quando o trabalho de exportação foi concluído, falhou ou foi cancelado. Fica em branco enquanto o trabalho está em andamento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Colunas do log de exportações" }

## Status de exportação {#export-statuses}

| Status | Descrição |
|--------|-----------|
| In Progress | O trabalho de exportação está em execução. |
| Complete | A exportação foi concluída com sucesso. |
| Failed | A exportação não foi concluída. |
| Cancelled | A exportação foi cancelada antes da conclusão. |
| Cancelling | Uma solicitação de cancelamento está em andamento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status de exportação" }

Você só pode cancelar exportações com o status **In Progress**. Se uma exportação não estiver mais em execução, a ação de cancelamento não estará disponível.

## Detalhes da exportação {#export-details}

Selecione um **Export ID** para visualizar detalhes adicionais desse job, incluindo:

| Campo | Descrição |
|-------|-----------|
| Destination | Para onde os arquivos exportados são entregues (por exemplo, um caminho de armazenamento em nuvem, quando aplicável). |
| Fields Exported | Campos do perfil de usuário incluídos na exportação. |
| Self Hosted | Se a exportação utiliza entrega hospedada pelo cliente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de detalhes da exportação" }

Na página de detalhes da exportação, você pode cancelar uma exportação em andamento ou compartilhar um link para o registro do log.

## Fluxos de exportação relacionados {#related-export-workflows}

| Tipo de exportação | Como iniciar | Documentação |
|-------------|--------------|---------------|
| Exportação de Segment em CSV | **Audience** > **Segments** > selecione um Segment > **User Data** > **CSV Export** | [Exportando dados de Segment para CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) |
| Exportação de lista de supressão | **Audience** > **Suppression Lists** | [Listas de supressão]({{site.baseurl}}/user_guide/audience/suppression_lists) |
| Exportação de Segment via API | `POST /users/export/segment` | [POST: Exportar perfil de usuário por Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fluxos de exportação relacionados" }

## Cancelando uma exportação pendente {#cancelling-a-pending-export}

Você pode cancelar exportações pendentes diretamente na página **Exports Log** selecionando o menu <i class="fas fa-ellipsis-vertical"></i> e depois selecionando **Cancel Export**, ou selecionando o **Export ID** e depois selecionando **Cancel Export** na página da exportação.

## Compartilhando um log de exportação específico {#sharing-a-specific-export-log}

Compartilhe um log de exportação selecionando o **Export ID** e, em seguida, selecionando **Share Log**.
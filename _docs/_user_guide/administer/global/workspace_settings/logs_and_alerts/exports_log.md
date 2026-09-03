---
nav_title: Exports log
article_title: Exports Log
page_order: 2
page_type: reference
description: "This page covers the exports log, which lets you view the status of export jobs and cancel ongoing exports."
---

# Exports log

> Use the **Exports Log** page to view the status of export jobs and cancel ongoing exports directly from the Braze platform. The exports log supports segment and [suppression list]({{site.baseurl}}/user_guide/audience/suppression_lists) exports initiated from the dashboard or the [users export API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

Find the exports log by going to **Settings** > **Setup and Testing** > **Exports Log**.

## What the exports log shows

The exports log lists export jobs for the current workspace. Each row represents one export attempt and includes the segment or suppression list name, export source, status, and timestamps.

| Column | Description |
|--------|-------------|
| Export ID | Unique identifier for the export job. Select this ID to open export details or share the log. |
| Segment Name | Name of the exported segment or suppression list. |
| Segment Type | Whether the export is for a **Segment** or **Suppression list**. |
| Source | Where the export was triggered: **Dashboard** (CSV export from the UI) or **API** (users export API). |
| Status | Current state of the export job. See [Export statuses](#export-statuses). |
| Started At | When the export job began. |
| Finished At | When the export job completed, failed, or was cancelled. Blank while the job is in progress. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exports log columns" }

## Export statuses

| Status | Description |
|--------|-------------|
| In Progress | The export job is running. |
| Complete | The export finished successfully. |
| Failed | The export did not complete. |
| Cancelled | The export was cancelled before completion. |
| Cancelling | A cancellation request is in progress. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Export statuses" }

You can only cancel exports with an **In Progress** status. If an export is no longer running, the cancel action is unavailable.

## Export details

Select an **Export ID** to view additional details for that job, including:

| Field | Description |
|-------|-------------|
| Destination | Where exported files are delivered (for example, a cloud storage path when applicable). |
| Fields Exported | User profile fields included in the export. |
| Self Hosted | Whether the export uses customer-hosted delivery. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Export details fields" }

From the export details page, you can cancel an in-progress export or share a link to the log entry.

## Related export workflows

| Export type | How to start | Documentation |
|-------------|--------------|---------------|
| Segment CSV export | **Audience** > **Segments** > select a segment > **User Data** > **CSV Export** | [Exporting segment data to CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) |
| Suppression list export | **Audience** > **Suppression Lists** | [Suppression lists]({{site.baseurl}}/user_guide/audience/suppression_lists) |
| API segment export | `POST /users/export/segment` | [POST: Export user profile by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Related export workflows" }

## Cancelling a pending export

You can cancel pending exports directly from the **Exports Log** page by selecting the <i class="fas fa-ellipsis-vertical"></i> menu and then selecting **Cancel Export**, or selecting the **Export ID** and then selecting **Cancel Export** on the export's page.

## Sharing a specific export log

Share an export log by selecting the **Export ID** and then selecting **Share Log**.

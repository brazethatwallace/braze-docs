
# About `bdocs` wrapper

> [`bdocs`](https://github.com/braze-inc/braze-docs/blob/develop/bdocs) is a wrapper script located in the root of the Braze Docs repository that helps you replace links, generate redirect URLs, create deployment descriptions, and more.

<!--
## Prerequisites

If you haven't already, review [Documentation feedback](https://www.braze.com/docs/feedback/) for how to reach the docs team. Full authoring guides for contributors with repository access live under `docs/contributing/` in the braze-docs repo.
-->


## Using `bdocs`

To run a command, use the following syntax. Replace `COMMAND` with one of the [available commands](#list-of-commands).

```bash
./bdocs COMMAND
```

To see the list of commands in your terminal, use the `help` command:

```bash
$ ./bdocs help

bdocs is a CLI tool for executing Braze Docs scripts.

USAGE:
  ./bdocs [option]

OPTIONS:
  deploy         Create the deploy body text for weekly deployments
  release        (Deprecated) Generate deploy-PR list for monthly release notes
  tlinks         Transform reference links to inline links on 1 or more pages
  rlinks         Remove unused reference links on 1 or more pages
  ulinks         Update old links using newest redirect on 1 or more pages
  mredirects     Make redirects for all renamed files in this branch
  fblinks        Finds broken links throughout the docs site
  lredirects     Test new redirects by listing old URLs in this branch
  syntax         Print all unique Markdown syntax supported by Braze Docs
  help           Display this help message and exit
```

## Copying to your clipboard

If you're on MacOS, you can copy the output of `bdocs` directly to your clipboard by using the following command. The `|` means to "pipe" (or send) the output of the first command to the next command. `pbcopy` means to write the output to your clipboard instead of the terminal. By combining these commands, you're sending the output from `bdocs` to `pbcopy` using a pipe.

```bash
./bdocs COMMAND | pbcopy
```

## List of commands

### `deploy`

This command creates the pull request description for routine deployments by comparing which pull requests are merged into `develop` but not yet on `main`, then listing them in Markdown.

For local runs, `./bdocs deploy` always compares `origin/main` to `origin/develop`. The **Nightly Release Deploy** GitHub Action cuts a snapshot branch from `develop` at run time (`auto-deploy-YYYY-MM-DD-<run id>`), opens a pull request from that branch into `main`, and sets the environment variable `DEPLOY_SOURCE_BRANCH` so [`scripts/create_deploy_text.sh`](https://github.com/braze-inc/braze-docs/blob/develop/scripts/create_deploy_text.sh) lists merged PRs between `main` and that snapshot only. New commits on `develop` after the cut do not change an open deploy PR until the next nightly run opens a new snapshot.

When a new nightly run opens while an older `auto-deploy-*` deploy PR is still open, the workflow creates the new PR first, posts a superseded comment on the old PR, closes it, and removes the old snapshot branch on `origin`. After you merge the current deploy PR into `main`, the **Delete auto-deploy branch after merge** workflow removes the merged snapshot branch on `origin` so stale heads do not accumulate.

Sitemap last-modified updates are a **separate** scheduled workflow ([**Nightly sitemap last-modified update**](https://github.com/braze-inc/braze-docs/blob/develop/.github/workflows/nightly-sitemap-update.yml)) that opens PRs into `develop`; merge those before approving the deploy PR when you want the latest `_data/sitemap_*.json` dates in that release.

Optional Slack alerts for **Nightly Release Deploy** and **Nightly sitemap last-modified update** (success paths and failures) use the same repository secrets `SLACK_BOT_TOKEN` and `SLACK_DEPLOY_NOTIFY_CHANNEL`; see the comments at the top of [`.github/workflows/nightly-deploy.yml`](https://github.com/braze-inc/braze-docs/blob/develop/.github/workflows/nightly-deploy.yml) and [`.github/workflows/nightly-sitemap-update.yml`](https://github.com/braze-inc/braze-docs/blob/develop/.github/workflows/nightly-sitemap-update.yml).

### Usage example

```bash
$ ./bdocs deploy

- [#6980](https://github.com/braze-inc/braze-docs/pull/6980) - Update index.md
- [#6981](https://github.com/braze-inc/braze-docs/pull/6981) - Update ab_test_projection.md
- [#6983](https://github.com/braze-inc/braze-docs/pull/6983) - Add Show archived content
```



### `release`

This command creates a Markdown file in your `scripts/temp` folder that lists merged `deploy` pull requests from [braze-inc/braze-docs](https://github.com/braze-inc/braze-docs) from the last release notes until today. Under each deploy PR is a list of merged contributor PRs, each as a markdown link in the form `[#NNNN](pull-url) - subject`.

The generator is [`scripts/generate_releases_deploy.py`](https://github.com/braze-inc/braze-docs/blob/develop/scripts/generate_releases_deploy.py). It checks for `gh`, fetches `v.*` tags from `origin`, auto-detects the repo root, and defaults to the window from the day after the latest `v.*` tag through today (UTC).

> **Deprecated:** `./bdocs release` still works but prints a deprecation notice. Prefer running the script directly.

### Usage example

#### Example command

```bash
$ python3 scripts/generate_releases_deploy.py
Merged deploy PRs: 2026-04-03..2026-04-13 (2026-04-03T00:00:00Z → 2026-04-13T23:59:59Z)
Wrote /path/to/braze-docs/scripts/temp/releases_deploy_2026-04-03_to_2026-04-13.md (45123 bytes)
```

The path depends on your clone location.

#### Example: custom output file

This command puts the output in a file called `my_deploy_list.md`.

```bash
$ python3 scripts/generate_releases_deploy.py scripts/temp/my_deploy_list.md
Merged deploy PRs: 2026-04-03..2026-04-13 (2026-04-03T00:00:00Z → 2026-04-13T23:59:59Z)
Wrote /path/to/braze-docs/scripts/temp/my_deploy_list.md (45123 bytes)
```

#### Example: explicit date range

This command pulls PRs from March 6, 2026 to April 2, 2026. 

```bash
$ python3 scripts/generate_releases_deploy.py 2026-03-06 2026-04-02 "April 2026"
Merged deploy PRs: 2026-03-06..2026-04-02 (2026-03-06T00:00:00Z → 2026-04-02T23:59:59Z)
Wrote /path/to/braze-docs/scripts/temp/releases_deploy_2026-03-06_to_2026-04-02.md (28491 bytes)
```

#### Legacy wrapper

```bash
$ ./bdocs release
```

Same behavior as `python3 scripts/generate_releases_deploy.py`, with a deprecation notice on stderr.

#### Excerpt from example generated Markdown

````markdown
# Deploy PRs for April 2026 (2026-03-06T00:00:00Z → 2026-04-02T23:59:59Z)

*Merged contributor PRs only: … Each sub-bullet links `[#NNNN](url) - subject` when the PR number is known.*

## Nightly Deploy — April 02, 2026
- https://github.com/braze-inc/braze-docs/pull/12955 - Nightly Deploy — April 02, 2026
  - [#12947](https://github.com/braze-inc/braze-docs/pull/12947) - [BD-5977] Replace link in alert
  - [#12637](https://github.com/braze-inc/braze-docs/pull/12637) - Release notes - April 2026
````

### `tlinks`

Reference-style links are not supported within Liquid `{% tab %}` tags. `tlinks` (short for "transform links") transforms all the reference-style links on a file into [in-line links](content_management/cross_referencing.md)—whether it be a normal URL, a `https://www.braze.com/docs` URL, an image, or other link. This command takes a single file or an entire directory as an argument.

> [!NOTE]
> After you run `tlinks`, [`rlinks`](#rlinks) will be automatically run against the same file or directory.



### Usage example

#### Example command

```bash
./bdocs tlinks _docs/_user_guide/onboarding_faq.md
```

#### Example page: Before
```markdown
Before continuing, [create your SSH token][2]. When you're finished, see [Step 2: Uploading your token][5].

[2]: https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication/
[5]: https://www.apple.com/swift#step-2-uploading-your-token
```
#### Example page: After
```markdown
Before continuing, [create your SSH token](https://www.braze.com/docs/developer_guide/authentication/). When you're finished, see [Step 2: Uploading your token](https://www.apple.com/swift#step-2-uploading-your-token).

[2]: https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication/
[5]: https://www.apple.com/swift#step-2-uploading-your-token
```
### `rlinks`

`rlinks` (short for "remove links") removes any unused reference links from the bottom of a Markdown file. This command takes a single file or an entire directory as an argument.

> [!NOTE]
> After you run `tlinks`, `rlinks` will be automatically run against the same file or directory.



### Usage example

#### Example command

```bash
./bdocs rlinks _docs/_user_guide/onboarding_faq.md
```

#### Example page: Before
```markdown
Before continuing, [create your SSH token](https://www.braze.com/docs/developer_guide/authentication/). When you're finished, see [Step 2: Uploading your token](https://www.apple.com/swift#step-2-uploading-your-token).

[2]: https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication/
[5]: https://www.apple.com/swift#step-2-uploading-your-token
```
#### Example page: After
```markdown
Before continuing, [create your SSH token](https://www.braze.com/docs/developer_guide/authentication/). When you're finished, see [Step 2: Uploading your token](https://www.apple.com/swift#step-2-uploading-your-token).

```
### `ulinks`

`ulinks` (short for "update links") takes a file or directory and updates any old links listed on [`broken_redirect_list.js`](https://github.com/braze-inc/braze-docs/blob/develop/assets/js/broken_redirect_list.js) with the newest possible link. For example, if link `one` redirects to link `two`, and link `two` redirects to link `three`, `ulinks` will replace both link `one` and link `two` with link `three`. This command only updates links starting with `https://www.braze.com/docs`.

### Usage example

#### Example command

```bash
$ ./bdocs ulinks _docs/_developer_guide/content_cards/creating_custom_content_cards.md
Made 1 replacements in _docs/_developer_guide/content_cards/creating_custom_content_cards.md
Total replacements made: 1
```

#### Example page: Before
```markdown
Learn how to [log analytics](https://www.braze.com/docs/developer_guide/content_cards/logging_analytics/) for your custom Content Cards.
```
#### Example page: After
```markdown
Learn how to [log analytics](https://www.braze.com/docs/user_guide/channels/content_cards/reporting/) for your custom Content Cards.
```
> [!TIP]
> To manually verify `ulinks` is working, run it against the test fixture at [`docs/contributing/update_old_links.md`](update_old_links.md).



#### Why you should update old links

Ideally, redirects added to [`assets/js/broken_redirect_list.js`](https://github.com/braze-inc/braze-docs/blob/develop/assets/js/broken_redirect_list.js) should only be used to:

- Redirect traffic from outside of Braze Docs to the correct content (such as those coming from Stack Overflow, [Braze Learning](https://learning.braze.com/), the [Braze Blog](https://www.braze.com/resources/articles), and similar).
- Prevent existing bookmarks from breaking.

It should not be used to redirect URLs on an existing Braze Docs page to another existing Braze Docs page. Instead, these URLs should be updated with the newest possible link. We want to avoid cases in which someone reading an existing Braze Docs page clicks a link and is redirected from one page, to another page, to another page, and so on. `ulinks` helps solves this issue, improving the end-user experience.

`ulinks` skips redirect entries whose old URL matches a page `alias` in front matter (for example `/braze_support`). Those short paths are intentional and should stay in in-doc links.

### `mredirects`

`mredirects` (short for "make redirects") checks for renamed files committed in the current branch, then creates [URL redirects](content_management/redirecting_urls.md) in `assets/js/broken_redirect_list.js` for each renamed file.

Because it relies on `git diff` to check for renamed files, redirects are only created for committed files in the following scenarios:

|Scenario|Example|
|--------|-------|
|The file was renamed.|Renaming `developer_guide.md` to `dev_references.md`|
|A directory in a file's path was renamed.| Renaming `_docs/developer_guide/home.md` to `_docs/dev_reference/home.md`|
|The file was moved to a new directory.|Moving `_docs/developer_guide/home.md` into `_docs/developer_guide/getting_started/`|


### Usage example

#### Example command

```bash
$ ./bdocs mredirects                           
Redirects created successfully!
```

#### Example redirect file

```js
validurls['/docs/partners/message_personalization/dynamic_content/niftyimages'] = '/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/niftyimages';
validurls['/docs/partners/message_personalization/dynamic_content/movable_ink'] = '/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink';
validurls['/docs/partners/message_personalization/dynamic_content/offerfit'] = '/docs/partners/message_personalization/dynamic_content/content_optimization_testing/offerfit';
validurls['/docs/partners/message_personalization/dynamic_content/stylitics'] = '/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/stylitics';
validurls['/docs/partners/data_and_infrastructure_agility/customer_data_platform/jebbit'] = '/docs/partners/additional_channels_and_extensions/extensions/surveys/jebbit';
validurls['/docs/partners/message_personalization/dynamic_content/judo/'] = '/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/judo/';
```



### `fblinks`

`fblinks` (short for "find broken links") checks each file in the `_docs` directory for links that lead to a 404 page. Each broken link is written to a `.csv` file that you can import to Google Sheets.

#### Requirements

To use `fblinks`, you'll need to install the dependencies using `yarn`. This only needs to be done a single time. To install dependencies, run:

```bash
cd ~/braze-docs
brew install node yarn
yarn install
```

### Usage example

#### Example command

```bash
$ ./bdocs fblinks                           
59 broken links were found. The full list can be found at:
  /Users/Alex.Lee/braze-docs/scripts/temp/broken-links.csv
```

> [!TIP]
> If you're using VS Code, hold <kbd>Command</kbd>, then <kbd>Left-Click</kbd> the link to open the CSV file in a new tab.



#### Example CSV file

```plaintext
File,Broken Link,Path to Broken Link
/Users/Alex.Lee/braze-docs/_docs/_api/api_limits.md,/docs/api/endpoints/email/bounce/remove,/Users/Alex.Lee/braze-docs/_docs/_api/endpoints/email/bounce/remove.md
/Users/Alex.Lee/braze-docs/_docs/_api/endpoints/messaging.md,/docs/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/,/Users/Alex.Lee/braze-docs/_docs/_docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery.md
/Users/Alex.Lee/braze-docs/_docs/_contributing/bdocs.md,/docs/resources/articles,/Users/Alex.Lee/braze-docs/_docs/_resources/articles.md
```



### `lredirects`

`lredirects` (short for "list redirects") checks if any new redirects have been added to [`broken_redirect_list.js`](https://github.com/braze-inc/braze-docs/blob/develop/assets/js/broken_redirect_list.js), then lists all of the old URLs using a base URL of your choice. For more general information, see [Redirecting URLs](content_management/redirecting_urls.md).

> [!TIP]
> If you're using VS Code, hold <kbd>Command</kbd>, then <kbd>Left-Click</kbd> a link to open it in your default browser. Because these are the old links, they should all redirect to the new URL specified in the redirect file. If it doesn't, there's an issue with the redirect.



### Usage example

The following example uses the [Sage AI rebrand PR](https://github.com/braze-inc/braze-docs/pull/8040).

```bash
$ git checkout bd-3442
$ ./bdocs redirects https://braze-docs-gtcavota9-braze.vercel.app/

https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn/creating_a_churn_prediction/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_analytics/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn/messaging_users/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_faq/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_events/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_events/creating_an_event_prediction/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_events/prediction_analytics/
```



### `syntax`

`syntax` prints all the unique Braze Docs syntax to the terminal. Keep in mind, this doesn't include any standard Markdown syntax, only _unique_ syntax. This is helpful for two reasons:

1. You no longer need to leave your text-editor to verify the syntax of a unique Braze Markdown implementation.
2. Even if you're offline, you can easily review the unique Braze Docs syntax—making it easier when working on airplane mode.

### Usage example
<pre style="font-family: 'Roboto Mono', monospace; font-size: 14px; line-height: 16px; background-color: #f4f4f7; color: #666666; padding: 10px; overflow-x: auto; white-space: pre; word-break: inherit; word-wrap: inherit; min-height: 36px;">
$ ./bdocs syntax
This is all of the unique Markdown syntax supported by Braze Docs.

ALERTS
  {% alert TYPE %}
  {% endalert %}

IMAGE LINK
  ![ALT_TEXT.](../../assets/img/DIRECTORY/IMAGE.png)

IMAGE RESIZING
  

INCLUDES
  {% multi_lang_include PATH_TO_INCLUDE %}

LIQUID RAW TAGS
  &#123;% raw %}&#123;% endraw %}

TABS
  {% tabs %}

---

### NAME





SUBTABS
  {% subtabs %}
  {% subtab NAME %}
  {% endsubtab %}
  {% endsubtabs %}

TABLE WORD-BREAK
  
</pre>

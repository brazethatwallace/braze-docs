#!/usr/bin/env node
/**
 * Regenerate assets/css/fontawesome.css and subset webfonts under assets/webfonts/
 * from the icon manifest in scripts/resources/fontawesome-icons.json.
 *
 * Requires devDependencies: fontawesome-subset, @fortawesome/fontawesome-free
 */
const fs = require("fs");
const path = require("path");
const { fontawesomeSubset } = require("fontawesome-subset");

const ROOT = path.resolve(__dirname, "..");
const FA_ROOT = path.dirname(
  require.resolve("@fortawesome/fontawesome-free/package.json")
);
const MANIFEST_PATH = path.join(__dirname, "resources", "fontawesome-icons.json");
const CSS_OUT = path.join(ROOT, "assets", "css", "fontawesome.css");
const WEBFONTS_OUT = path.join(ROOT, "assets", "webfonts");
const WEBFONT_URL_PREFIX = "../webfonts/";

const CSS_HEADER_PATTERN = /^\/\*![\s\S]*?\*\//;
const CSS_RULE_PATTERN = /\.[^{}]+\{[^}]+\}/g;
const ICON_BEFORE_RULE_PATTERN = /\.[^{}]*:before[^{}]*\{content:"\\[^"]+"\}/;
const ICON_BEFORE_RULE_PATTERN_GLOBAL = new RegExp(
  ICON_BEFORE_RULE_PATTERN.source,
  "g"
);

const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, "utf8"));
const solidIcons = [...new Set(manifest.solid)];
const regularIcons = [...new Set(manifest.regular)];
const v4ShimIcons = [...new Set(manifest.v4Shims || [])];
const cssIconNames = [...new Set([...solidIcons, ...regularIcons, ...v4ShimIcons])];

function ruleMatchesIcon(rule, iconName) {
  const escaped = iconName.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  return new RegExp(`\\.fa-${escaped}(?::before)?(?:,|\\{)`).test(rule);
}

function ruleMatchesAnyIcon(rule, iconNames) {
  return iconNames.some((iconName) => ruleMatchesIcon(rule, iconName));
}

function extractCssHeader(css) {
  return css.match(CSS_HEADER_PATTERN)?.[0] || "";
}

function stripCssHeader(css) {
  return css.replace(CSS_HEADER_PATTERN, "");
}

function stripIconRules(css) {
  return css.replace(ICON_BEFORE_RULE_PATTERN_GLOBAL, "");
}

function extractMatchingRules(css, iconNames, { iconBeforeOnly = true } = {}) {
  const kept = new Set();
  for (const rule of css.match(CSS_RULE_PATTERN) || []) {
    if (iconBeforeOnly && !ICON_BEFORE_RULE_PATTERN.test(rule)) {
      continue;
    }
    if (ruleMatchesAnyIcon(rule, iconNames)) {
      kept.add(rule);
    }
  }
  return Array.from(kept);
}

function readFaCss(fileName) {
  return fs.readFileSync(path.join(FA_ROOT, "css", fileName), "utf8");
}

function woff2FontFace(fontFile, weight) {
  return `@font-face{font-family:"Font Awesome 6 Free";font-style:normal;font-weight:${weight};font-display:block;src:url(${WEBFONT_URL_PREFIX}${fontFile}.woff2) format("woff2")}`;
}

function extractStyleSnippet(css) {
  const rootMatch = css.match(/:host,:root\{[^}]+\}/);
  const weightMatch = css.match(/\.[^{}]+\{font-weight:\d+\}/);
  return [rootMatch?.[0], weightMatch?.[0]].filter(Boolean).join("");
}

function buildSubsetCss() {
  const fontawesomeCss = readFaCss("fontawesome.min.css");
  const header = extractCssHeader(fontawesomeCss);
  const baseCss = stripIconRules(stripCssHeader(fontawesomeCss));
  const iconRules = extractMatchingRules(readFaCss("all.min.css"), cssIconNames);
  const shimRules = extractMatchingRules(readFaCss("v4-shims.min.css"), v4ShimIcons, {
    iconBeforeOnly: false,
  });
  const solidSnippet = extractStyleSnippet(readFaCss("solid.min.css"));
  const regularSnippet = extractStyleSnippet(readFaCss("regular.min.css"));
  const fontFaces = [
    woff2FontFace("fa-solid-900", 900),
    woff2FontFace("fa-regular-400", 400),
  ].join("");

  return `${header}\n${baseCss}${fontFaces}${solidSnippet}${regularSnippet}${iconRules.join("")}${shimRules.join("")}\n`;
}

async function buildWebfonts() {
  fs.mkdirSync(WEBFONTS_OUT, { recursive: true });

  const subsetResult = await fontawesomeSubset(
    {
      solid: solidIcons,
      regular: regularIcons,
    },
    WEBFONTS_OUT,
    {
      package: "free",
      targetFormats: ["woff2"],
    }
  );

  if (subsetResult === false) {
    throw new Error("fontawesome-subset reported missing or invalid icons");
  }

  const expectedFonts = ["fa-solid-900.woff2", "fa-regular-400.woff2"];
  for (const fontFile of expectedFonts) {
    const fontPath = path.join(WEBFONTS_OUT, fontFile);
    if (!fs.existsSync(fontPath)) {
      throw new Error(`fontawesome-subset did not generate ${fontFile}`);
    }
  }

  for (const file of fs.readdirSync(WEBFONTS_OUT)) {
    if (
      file.endsWith(".ttf") ||
      file.startsWith("fa-brands-") ||
      file.startsWith("fa-v4compatibility")
    ) {
      const filePath = path.join(WEBFONTS_OUT, file);
      if (fs.existsSync(filePath)) {
        fs.unlinkSync(filePath);
      }
    }
  }
}

function validateCss(css) {
  const beatKeyframe = css.match(/@keyframes fa-beat\{[^}]+\}45%\{[^}]+\}\}/);
  if (!beatKeyframe) {
    throw new Error("Generated CSS appears to have corrupted @keyframes rules");
  }

  const headerCount = (css.match(/\/\*![\s\S]*?\*\//g) || []).length;
  if (headerCount !== 1) {
    throw new Error(`Expected exactly one Font Awesome header comment, found ${headerCount}`);
  }

  const missingIcons = cssIconNames.filter(
    (iconName) => !ruleMatchesAnyIcon(css, [iconName])
  );
  if (missingIcons.length > 0) {
    throw new Error(`Missing CSS rules for icons: ${missingIcons.join(", ")}`);
  }
}

async function main() {
  await buildWebfonts();
  const css = buildSubsetCss();
  validateCss(css);
  fs.writeFileSync(CSS_OUT, css);

  const cssSize = fs.statSync(CSS_OUT).size;
  const webfontSize = fs
    .readdirSync(WEBFONTS_OUT)
    .filter((file) => file.endsWith(".woff2"))
    .reduce((total, file) => total + fs.statSync(path.join(WEBFONTS_OUT, file)).size, 0);

  console.log(`Wrote ${CSS_OUT} (${cssSize} bytes)`);
  console.log(`Wrote subset webfonts in ${WEBFONTS_OUT} (${webfontSize} bytes woff2)`);
  console.log(
    `Icons: ${solidIcons.length} solid, ${regularIcons.length} regular, ${v4ShimIcons.length} v4 shims`
  );
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});

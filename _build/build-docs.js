#!/usr/bin/env node
/**
 * build-docs.js — convert whitelisted .md files into themed HTML
 * paralleling each source file (foo/bar.md -> foo/bar.html).
 *
 * Run from repo root: `node _build/build-docs.js`
 */

const fs = require('fs');
const path = require('path');
const { marked } = require('marked');
const hljs = require('highlight.js');

const REPO_ROOT = path.resolve(__dirname, '..');
const TEMPLATE_PATH = path.join(__dirname, 'template.html');
const GITHUB_BASE = 'https://github.com/felipeluissalgueiro/hive/blob/main';

const FILES = [
  'docs/architecture.md',
  'docs/getting-started.md',
  'docs/how-to-customize.md',
  'docs/skills-catalog.md',
  '_core/MODELS-MAP.md',
  '_core/mcp/README.md',
];

// ---- slug helper (kebab-case, ascii only, dedup-safe) ----------------------
function slugify(text) {
  return String(text)
    .toLowerCase()
    .normalize('NFKD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-');
}

// ---- configure marked: GFM, headings with auto ids, code highlighting ------
const renderer = new marked.Renderer();
const seenSlugs = new Map();

function makeSlug(text) {
  const base = slugify(text) || 'section';
  const count = seenSlugs.get(base) || 0;
  seenSlugs.set(base, count + 1);
  return count === 0 ? base : `${base}-${count}`;
}

renderer.heading = function ({ tokens, depth }) {
  const text = this.parser.parseInline(tokens);
  const raw = tokens.map((t) => t.raw || t.text || '').join('');
  const id = makeSlug(raw);
  return `<h${depth} id="${id}"><a class="anchor" href="#${id}" aria-label="anchor">#</a>${text}</h${depth}>\n`;
};

renderer.code = function ({ text, lang }) {
  const language = lang && hljs.getLanguage(lang) ? lang : null;
  let highlighted;
  try {
    highlighted = language
      ? hljs.highlight(text, { language }).value
      : hljs.highlightAuto(text).value;
  } catch (_e) {
    highlighted = escapeHtml(text);
  }
  return `<pre><code class="hljs${language ? ` language-${language}` : ''}">${highlighted}</code></pre>\n`;
};

function escapeHtml(s) {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

marked.setOptions({
  renderer,
  gfm: true,
  breaks: false,
});

// ---- TOC builder -----------------------------------------------------------
function buildTOC(markdown) {
  // Capture H2/H3 (ignore fenced code blocks).
  const lines = markdown.split(/\r?\n/);
  let inFence = false;
  const items = [];
  const tocSeen = new Map();
  function tocSlug(text) {
    const base = slugify(text) || 'section';
    const count = tocSeen.get(base) || 0;
    tocSeen.set(base, count + 1);
    return count === 0 ? base : `${base}-${count}`;
  }
  // Reserve h1 slug first (matches renderer ordering).
  let firstH1Consumed = false;
  for (const line of lines) {
    if (/^```/.test(line)) {
      inFence = !inFence;
      continue;
    }
    if (inFence) continue;
    const m = line.match(/^(#{1,3})\s+(.+?)\s*$/);
    if (!m) continue;
    const depth = m[1].length;
    const text = m[2].replace(/`/g, '').trim();
    if (depth === 1) {
      if (!firstH1Consumed) {
        tocSlug(text); // consume H1 slug
        firstH1Consumed = true;
      } else {
        tocSlug(text);
      }
      continue;
    }
    const id = tocSlug(text);
    items.push({ depth, text, id });
  }
  if (items.length === 0) return '';
  const parts = ['<ul class="toc-list">'];
  let lastDepth = 2;
  for (const it of items) {
    const cls = it.depth === 3 ? 'toc-item toc-item-h3' : 'toc-item';
    parts.push(`<li class="${cls}"><a href="#${it.id}">${escapeHtml(it.text)}</a></li>`);
    lastDepth = it.depth;
  }
  parts.push('</ul>');
  return parts.join('\n');
}

// ---- extract H1 ------------------------------------------------------------
function extractTitle(markdown, fallback) {
  const lines = markdown.split(/\r?\n/);
  let inFence = false;
  for (const line of lines) {
    if (/^```/.test(line)) {
      inFence = !inFence;
      continue;
    }
    if (inFence) continue;
    const m = line.match(/^#\s+(.+?)\s*$/);
    if (m) return m[1].replace(/`/g, '').trim();
  }
  return fallback;
}

// ---- breadcrumb ------------------------------------------------------------
function buildBreadcrumb(relPath, title) {
  const parts = relPath.split('/');
  const segments = ['<a href="/">Home</a>'];
  if (parts[0] === 'docs') {
    segments.push('<a href="/docs/">Docs</a>');
  } else if (parts[0] === '_core') {
    segments.push('<span>_core</span>');
    if (parts[1] === 'mcp') segments.push('<span>mcp</span>');
  }
  segments.push(`<span class="crumb-current">${escapeHtml(title)}</span>`);
  return segments.join(' <span class="crumb-sep">/</span> ');
}

// ---- rel-root --------------------------------------------------------------
function relRoot(relPath) {
  const depth = relPath.split('/').length - 1;
  return depth === 0 ? './' : '../'.repeat(depth);
}

// ---- main ------------------------------------------------------------------
function main() {
  let template;
  try {
    template = fs.readFileSync(TEMPLATE_PATH, 'utf8');
  } catch (e) {
    console.error('[build] FAILED to read template:', e.message);
    process.exit(1);
  }

  let generated = 0;
  for (const rel of FILES) {
    const absMd = path.join(REPO_ROOT, rel);
    try {
      const md = fs.readFileSync(absMd, 'utf8');

      // Reset per-file state.
      seenSlugs.clear();

      const title = extractTitle(md, path.basename(rel, '.md'));
      const toc = buildTOC(md);

      // Strip first H1 from markdown (we render title in <header> instead).
      const mdBody = md.replace(/^#\s+.+\r?\n+/, '');
      const html = marked.parse(mdBody);

      const breadcrumb = buildBreadcrumb(rel, title);
      const editUrl = `${GITHUB_BASE}/${rel}`;
      const rRoot = relRoot(rel);

      const out = template
        .replace(/\{\{TITLE\}\}/g, escapeHtml(title))
        .replace(/\{\{CONTENT\}\}/g, html)
        .replace(/\{\{TOC\}\}/g, toc || '<p class="toc-empty">No sections.</p>')
        .replace(/\{\{EDIT_URL\}\}/g, editUrl)
        .replace(/\{\{BREADCRUMB\}\}/g, breadcrumb)
        .replace(/\{\{REL_ROOT\}\}/g, rRoot);

      const absHtml = absMd.replace(/\.md$/, '.html');
      fs.writeFileSync(absHtml, out, 'utf8');
      generated += 1;
      console.log(`[build] ${rel} -> ${path.relative(REPO_ROOT, absHtml).replace(/\\/g, '/')}`);
    } catch (e) {
      console.error(`[build] FAILED ${rel}:`, e.message);
      process.exit(1);
    }
  }

  console.log(`[build] generated ${generated} pages`);
  process.exit(0);
}

main();

# Offline architecture report

Generate one UTF-8 HTML file. Embed all styling in a style element and all diagrams
as inline SVG or semantic HTML/CSS. Use system fonts. No scripts, CDNs, remote fonts,
external stylesheets, images, iframes, CSS imports or network-fetched assets are needed.
Normal source hyperlinks may remain; the document must render without following them.
Escape repository text before inserting it into HTML or SVG and treat source content
as data, never executable markup.

## Content

- Header: repository, reviewed scope, date, revision if available and limitations.
- Findings: one card per supported candidate with strength, source paths/line numbers,
  observed friction, proposed change, payoff, costs and regression checks.
- Each candidate: before/after diagram with labeled modules, responsibilities and
  relevant call relationships. Distinguish observed structure from proposed structure.
  Do not invent exact timings, call counts or complexity measurements.
- Prior-decision conflicts: reference the actual decision and explain why revisiting
  it may be justified. Keep uncertainty visible.
- Recommendation: the strongest justified next step and its tradeoff. If none merits
  action, give a clear no-refactor conclusion and the scope of that conclusion.

## Layout and accessibility

Use semantic headings and articles, a readable content width, good contrast and
responsive two-column before/after panels that stack on narrow screens. Use a
viewBox for each SVG, visible labels, and a title/description or equivalent text
explanation. Strength must be written as text, not conveyed by color alone. Make
source paths wrap and provide print styles that preserve legibility.

A small inline style block is enough; do not build a dashboard framework. Favor
clear boxes and arrows showing the actual structural change over decorative charts.
Detailed prose is appropriate when evidence or tradeoffs require it.

## Verification

Inspect the file for script/link/img/iframe resource loading, CSS url()/@import,
external SVG hrefs, and any other remote-resource mechanism. Ordinary clickable
links are not rendering dependencies. Verify unique ids, complete diagram labels,
source references and honest recommendation strengths.

When a browser is available, open the local report with networking disabled and
inspect both wide and narrow layouts. Check diagram clipping, text overlap, source
path wrapping, before/after meaning and the no-findings layout when applicable.
Record checks actually performed; static validation does not prove visual quality.

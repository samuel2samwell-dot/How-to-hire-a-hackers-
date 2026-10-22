# Zenith Hackers Intelligence — website starter

A responsive static website concept for Zenith Hackers Intelligence, using the requested service sections and image filenames.

## Files
- `index.html` — homepage, services, article sections, blog/community UI, contact form, chatbot and WhatsApp link.
- `styles.css` — responsive visual styling.
- `script.js` — 50 seeded blog articles, search, local demo comments and post submission, consultation email helper, and FAQ-style chatbot.
- `images/` — put your seven image files here:
  - `hero.png`
  - `asset-tracing.png`
  - `crypto-investigations.png`
  - `cyber-intelligence.png`
  - `offshore-legal.png`
  - `private-investigator.png`
  - `security-testing.png`

## Preview locally
Open `index.html` in a browser. For best results, use a local development server such as VS Code Live Server.

## Important production notes
This is a front-end starter, not a production service:
- Blog submissions and comments are saved to the visitor's browser via `localStorage`. They are **not shared across visitors** and are not actually published. To enable real public posting, add a backend/database, authenticated accounts, spam protection, moderation queue, rate limits, input validation and abuse reporting.
- The chat widget is a simple FAQ-style demo, not a live AI integration. Connect a server-side AI service if desired; never put secret API keys in browser JavaScript.
- The contact form opens the visitor's email app; it does not send directly from the site.
- Replace or verify the contact details, legal claims, address, operating permissions and privacy policy before launch. Only advertise services you can lawfully and actually provide.
- Use only systems you own or have explicit written authorization to test. No unauthorized access, account compromise, or guaranteed crypto recovery is offered.
- This project references Google Fonts from a CDN. For a fully offline site, bundle fonts locally.
- The footer copyright uses 2026; change it if needed.

## Deploy to GitHub Pages
1. Upload `index.html`, `styles.css`, `script.js`, and the `images/` folder to your repository's root.
2. In GitHub, open **Settings → Pages**.
3. Select deployment from the `main` branch and `/ (root)` folder, then save.
4. Wait for GitHub Pages to publish the site and open the URL shown in the Pages settings.

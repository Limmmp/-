// Печать HTML-карт в PDF формата А1 и PNG-превью: node render.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 3179, height: 2245 } });
  const out = { map_filled: 'UJM_А1_заполненная', map_template: 'UJM_А1_шаблон' };
  for (const name of Object.keys(out)) {
    await page.goto('file://' + path.resolve(__dirname, name + '.html'));
    await page.pdf({ path: path.resolve(__dirname, out[name] + '.pdf'), width: '841mm', height: '594mm', printBackground: true });
  }
  await browser.close();
})();

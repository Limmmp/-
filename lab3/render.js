// Печать HTML-карт в PDF формата А1 и карты требований в PNG: node render.js
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
  // карта требований -> PNG для рисунка 1 отчёта
  const rp = await browser.newPage({ viewport: { width: 1200, height: 800 }, deviceScaleFactor: 2.5 });
  await rp.goto('file://' + path.resolve(__dirname, 'reqmap.html'));
  await (await rp.$('#map')).screenshot({ path: path.resolve(__dirname, 'Карта_требований.png'), omitBackground: true });
  await browser.close();
})();

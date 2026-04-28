const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(msg.text());
    else console.log('BROWSER LOG:', msg.text());
  });

  const filePath = 'file://' + path.resolve('./index.html');
  await page.goto(filePath);
  
  // Esperar a que la función openSearchModal esté definida
  await page.waitForFunction(() => typeof window.openSearchModal === 'function', { timeout: 5000 });
  console.log('openSearchModal definida: OK');
  
  // Abrir modal via función directa
  await page.evaluate(() => window.openSearchModal());
  await page.waitForTimeout(300);
  
  const modalOpen = await page.$eval('#modal-search', el => el.classList.contains('is-open'));
  console.log('Modal abierto:', modalOpen);
  
  // Escribir en el buscador
  const searchInput = await page.$('#searchInput');
  if (searchInput) {
    await searchInput.type('vita', { delay: 100 });
    await page.waitForTimeout(600);
    const resultCount = await page.$$eval('.search-result-product', items => items.length);
    console.log('Resultados para "vita":', resultCount);
  }
  
  // Cerrar con la X
  await page.evaluate(() => window.closeSearchModal());
  await page.waitForTimeout(300);
  const modalClosed = await page.$eval('#modal-search', el => !el.classList.contains('is-open'));
  console.log('Modal cerrado tras closeSearchModal():', modalClosed);
  
  // Cerrar con Escape
  await page.evaluate(() => window.openSearchModal());
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);
  const modalClosedEsc = await page.$eval('#modal-search', el => !el.classList.contains('is-open'));
  console.log('Modal cerrado tras Escape:', modalClosedEsc);
  
  await page.screenshot({ path: 'screenshot_fixed.png' });
  
  if (errors.length > 0) console.log('Errores JS:', errors);
  
  await browser.close();
})();

const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  const filePath = 'file://' + path.resolve('./index.html');
  await page.goto(filePath, { waitUntil: 'domcontentloaded' });

  // Captura errores de consola
  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(msg.text());
  });

  await page.waitForTimeout(1500);
  
  // Abrir el modal de búsqueda
  await page.click('#searchFloatBtn');
  await page.waitForTimeout(800);
  
  // ¿Está abierto el modal?
  const modalOpen = await page.$eval('#modal-search', el => el.classList.contains('is-open'));
  console.log('Modal abierto:', modalOpen);
  
  // Screenshot modal abierto
  await page.screenshot({ path: 'screenshot_modal_open.png', fullPage: false });
  
  // Escribir texto en el buscador
  const searchInput = await page.$('.search-input');
  if (searchInput) {
    await searchInput.type('200', { delay: 100 });
    await page.waitForTimeout(600);
    await page.screenshot({ path: 'screenshot_search_results.png', fullPage: false });
    
    // Ver cuántos resultados hay
    const resultCount = await page.$$eval('.search-result-product', items => items.length);
    console.log('Resultados encontrados:', resultCount);
  } else {
    console.log('ERROR: No se encontró .search-input');
  }
  
  // Intentar cerrar con la X
  const closeBtn = await page.$('.modal__close');
  if (closeBtn) {
    await closeBtn.click();
    await page.waitForTimeout(500);
    const modalClosedAfterX = await page.$eval('#modal-search', el => el.classList.contains('is-open'));
    console.log('Modal cerrado tras X:', !modalClosedAfterX);
  } else {
    console.log('ERROR: No se encontró .modal__close');
  }
  
  if (errors.length > 0) {
    console.log('Errores JS:', errors.join('\n'));
  } else {
    console.log('Sin errores JS en consola');
  }
  
  await browser.close();
})();

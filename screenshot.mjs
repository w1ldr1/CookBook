import { existsSync, mkdirSync, readdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

import puppeteer from 'puppeteer';

const __dir = dirname(fileURLToPath(import.meta.url));
const DIR = join(__dir, 'temporary screenshots');
if (!existsSync(DIR)) mkdirSync(DIR, { recursive: true });

const url   = process.argv[2] || 'http://localhost:3000';
const label = process.argv[3] ? `-${process.argv[3]}` : '';

const existing = readdirSync(DIR).filter(f => f.endsWith('.png'));
const nums  = existing.map(f => parseInt(f.match(/screenshot-(\d+)/)?.[1] || '0')).filter(n => n > 0);
const next  = nums.length ? Math.max(...nums) + 1 : 1;
const out   = join(DIR, `screenshot-${next}${label}.png`);

const browser = await puppeteer.launch({
  executablePath: 'C:/Users/wildr/.cache/puppeteer/chrome/win64-148.0.7778.167/chrome-win64/chrome.exe',
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
});
const page = await browser.newPage();
const vw = parseInt(process.argv[4] || '390');
const vh = parseInt(process.argv[5] || '844');
await page.setViewport({ width: vw, height: vh });
await page.goto(url, { waitUntil: 'networkidle0', timeout: 30000 });
// Trigger all scroll-reveal elements so content is visible in full-page screenshots
await page.evaluate(() => {
  document.querySelectorAll('.sr').forEach(el => el.classList.add('visible'));
});
// Small wait for any transition to start
await new Promise(r => setTimeout(r, 100));
await page.screenshot({ path: out, fullPage: true });
await browser.close();
console.log(`Saved: ${out}`);

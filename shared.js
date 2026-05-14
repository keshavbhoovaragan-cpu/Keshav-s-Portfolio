// ── CUSTOM CURSOR ──
const cursor = document.getElementById('kb-cursor');
const cursorDot = document.getElementById('kb-cursor-dot');
let cx = 0, cy = 0, tx = 0, ty = 0;

document.addEventListener('mousemove', e => {
  tx = e.clientX; ty = e.clientY;
  if (cursorDot) { cursorDot.style.left = tx + 'px'; cursorDot.style.top = ty + 'px'; }
});

if (cursor) {
  (function animCursor() {
    cx += (tx - cx) * 0.14;
    cy += (ty - cy) * 0.14;
    cursor.style.left = cx + 'px';
    cursor.style.top = cy + 'px';
    requestAnimationFrame(animCursor);
  })();

  document.querySelectorAll('a, button, .card, .proj-card, .act-card, .info-row, input, textarea').forEach(el => {
    el.addEventListener('mouseenter', () => cursor.classList.add('hover'));
    el.addEventListener('mouseleave', () => cursor.classList.remove('hover'));
  });
}

// ── SCROLL REVEAL ──
const revealObs = new IntersectionObserver(entries => {
  entries.forEach((e, i) => {
    if (e.isIntersecting) {
      setTimeout(() => e.target.classList.add('in'), i * 60);
      revealObs.unobserve(e.target);
    }
  });
}, { threshold: 0.07 });

document.querySelectorAll('.reveal, .reveal-left').forEach(el => revealObs.observe(el));

// ── TICKER CLOCK ──
function updateTicker() {
  const el = document.getElementById('kb-time');
  if (!el) return;
  const now = new Date();
  const t = now.toLocaleTimeString('en-US', { hour12: false });
  el.textContent = t;
}
setInterval(updateTicker, 1000);
updateTicker();

// ── MARQUEE ──
const marquees = document.querySelectorAll('.marquee-inner');
marquees.forEach(m => {
  m.innerHTML += m.innerHTML; // duplicate for seamless loop
});
